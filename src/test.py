import os
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve
from sklearn.metrics import accuracy_score, precision_score, recall_score

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded with success")
    return model

def get_prediction_analysis(model, x_test, threshold):
    df_prediction = pd.DataFrame()
    df_prediction["probability_of_heart_attack_10y"] = model.predict_proba(x_test)[:, 1]
    df_prediction["heart_attack_10y"] = (df_prediction["probability_of_heart_attack_10y"] > threshold).astype(int)
    df_prediction["total_logit_z"] = model.decision_function(x_test)
    df_parameters_z = x_test * model.coef_
    df_parameters_z = df_parameters_z.add_prefix('logit_comp_')

    df_prediction = pd.concat([df_prediction.reset_index(drop=True), 
                               df_parameters_z.reset_index(drop=True)], axis=1)

    return df_prediction

def get_threshold(txt_path):
    with open(txt_path, 'r') as f:
        threshold = float(f.read())
    return threshold

def save_metrics_report(y_true, y_pred, path='src/models/metrics_report.txt'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
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
    
    print("\n" + report_content)
    print(f"Metrics saved in: {path}")

def main():
    txt_path = "src/models/threshold.txt"
    report_path = "src/models/metrics_report.txt"
    test_dataset_path = "src/data/test_dataset.csv"
    model_path = "src/models/logistic_regression_v1.pkl"

    if not os.path.exists(model_path):
        print(f"Error: model not found {model_path}.")
        return

    model = load_model(model_path)
    threshold = get_threshold(txt_path)
    test_dataset = pd.read_csv(test_dataset_path)
    
    x_test = test_dataset.drop(columns=['TenYearCHD'])
    y_test = test_dataset['TenYearCHD']

    df_prediction = get_prediction_analysis(model, x_test, threshold)
    save_metrics_report(y_test, df_prediction["heart_attack_10y"], report_path)

if __name__ == "__main__":
    main()