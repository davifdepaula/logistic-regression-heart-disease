import os
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from dataCleaner import DataCleaner
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve

def get_optimal_threshold(model, x_val, y_val):
    y_probs = model.predict_proba(x_val)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_val, y_probs)
    j_scores = tpr + (1 - fpr) - 1
    best_idx = np.argmax(j_scores)
    return thresholds[best_idx]

def train_model(x_train, y_train):
    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    model.fit(x_train, y_train)
    return model

def save_model_and_threshold(model, threshold, model_path, txt_path):
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    with open(txt_path, 'w') as f:
        f.write(str(threshold))
    
    print(f"--- Success ---")
    print(f"Model exported to: {model_path}")
    print(f"Threshold exported to: {txt_path}")
    print(f"Final Threshold Value: {threshold:.4f}")

def main():
    RAW_DATA = "src/data/framingham.csv"
    PROCESSED_DIR = "src/data"
    MODEL_DIR = "src/models"

    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(MODEL_DIR, exist_ok=True)

    processor = DataCleaner()
    df_raw = pd.read_csv(RAW_DATA)
    df_clean = processor.clean_data(df_raw)
    processor.save_cvs(df_clean)

    X = df_clean.drop(columns=['TenYearCHD'])
    y = df_clean['TenYearCHD']

    x_train, x_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    x_val, x_test, y_val, y_test = train_test_split(
        x_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
    )

    pd.concat([x_train, y_train], axis=1).to_csv(f"{PROCESSED_DIR}/train_dataset.csv", index=False)
    pd.concat([x_val, y_val], axis=1).to_csv(f"{PROCESSED_DIR}/val_dataset.csv", index=False)
    pd.concat([x_test, y_test], axis=1).to_csv(f"{PROCESSED_DIR}/test_dataset.csv", index=False)

    model = train_model(x_train, y_train)
    best_threshold = get_optimal_threshold(model, x_val, y_val)
    
    save_model_and_threshold(
        model, 
        best_threshold, 
        f"{MODEL_DIR}/logistic_regression_v1.pkl",
        f"{MODEL_DIR}/optimized_threshold.txt"
    )

if __name__ == "__main__":
    main()