import os
import pickle
import pandas as pd
import statsmodels.api as sm
from dataCleaner import DataCleaner
from sklearn.model_selection import train_test_split

def train_model(x_train, y_train):
    model = sm.Logit(y_train, x_train).fit()
    return model

def save_model(model, path='src/models/logistic_regression_model.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved in: {path}")

def main():
    RAW_DATA = "src/data/framingham.csv"
    PROCESSED_DIR = "src/data"
    MODEL_DIR = "src/models"

    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(MODEL_DIR, exist_ok=True)

    processor = DataCleaner()
    df_raw = pd.read_csv(RAW_DATA)
    df_clean = processor.clean_data(df_raw)
    df_balanced = processor.perform_class_balancing(df_clean)
    processor.save_balanced_cvs(df_balanced)

    df_vars = df_balanced.drop(columns=['TenYearCHD'])
    df_vars_with_const= sm.add_constant(df_vars)
    df_heart_attack_10y = df_balanced['TenYearCHD']

    x_train, x_test, y_train, y_test = train_test_split(
    df_vars_with_const, df_heart_attack_10y, test_size=0.25, random_state=42)

    pd.concat([x_train, y_train], axis=1).to_csv(f"{PROCESSED_DIR}/train_dataset.csv", index=False)
    pd.concat([x_test, y_test], axis=1).to_csv(f"{PROCESSED_DIR}/test_dataset.csv", index=False)

    model = train_model(x_train, y_train)
    save_model(model, f"{MODEL_DIR}/logistic_regression_v1.pkl")

if __name__ == "__main__":
    main()