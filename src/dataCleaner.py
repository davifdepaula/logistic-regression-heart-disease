import pandas as pd

class DataCleaner:

    def __init__(self):
        pass

    def clean_data(self, dataframe):
        return dataframe.dropna()

    def perform_class_balancing(self, dataframe):
        df_classe_0 = dataframe[dataframe['TenYearCHD'] == 0]
        df_classe_1 = dataframe[dataframe['TenYearCHD'] == 1]
        df_classe_0_under = df_classe_0.sample(len(df_classe_1), random_state=42)
        df_balanced = pd.concat([df_classe_0_under, df_classe_1], axis=0)
        df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)
        return df_balanced
    
    def save_balanced_cvs(self, dataframe, filepath = 'src/data/processed_dataset.csv'):
        dataframe.to_csv(filepath, index=False)