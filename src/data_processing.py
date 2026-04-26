import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Placeholder (we will expand in Phase 1)
    df = df.drop_duplicates()
    return df