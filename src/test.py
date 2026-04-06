import pickle
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import accuracy_score, precision_score, recall_score

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("model loaded with sucess")
    return model

def get_prediction_analysis(model, x_test):
    df_prediction = pd.DataFrame()
    df_prediction["probability_of_heart_attack_10y"] = model.predict(x_test)
    df_prediction["heart_attack_10y"] = (df_prediction["probability_of_heart_attack_10y"] > 0.5).astype(int)
    df_prediction.insert(2, "total_logit_z", model.predict(x_test, linear=True))
    df_parameters_z = x_test.multiply(model.params)
    df_parameters_z = df_parameters_z.add_prefix('logit_comp_')

    df_prediction = pd.concat([df_prediction, df_parameters_z], axis=1)

    return df_prediction

def save_metrics_report(y_true, y_pred, path='src/models/metrics_report.txt'):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    report_content = (
        f"--- Model Evaluation ---\n"
        f"Recall: {recall:.4f}\n"
        f"Accuracy: {accuracy:.4f}\n"
        f"Precision: {precision:.4f}\n"
    )
    with open(path, 'w') as f:
        f.write(report_content)
    
    print(f"Metrics saved in: {path}")


def main():
    report_path = "src/models/metrics_report.txt"
    test_dataset_path = "src/data/test_dataset.csv"
    model_path = "src/models/logistic_regression_v1.pkl"

    model = load_model(model_path)
    test_dataset = pd.read_csv(test_dataset_path)
    x_test = test_dataset.drop(columns=['TenYearCHD'])
    y_test = test_dataset['TenYearCHD']

    df_prediction = get_prediction_analysis(model, x_test)
    save_metrics_report(y_test, df_prediction["heart_attack_10y"], report_path)

if __name__ == "__main__":
    main()