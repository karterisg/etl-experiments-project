import pandas as pd
import numpy as np
import os

def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} rows.")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.dropna(how='all', inplace=True)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    string_cols = df.select_dtypes(include=['object']).columns
    df[string_cols] = df[string_cols].apply(lambda col: col.str.strip())
    print("Cleaning completed.")
    return df

def save_clean_data(df: pd.DataFrame, out_path: str):
    df.to_csv(out_path, index=False)
    print(f"Saved cleaned data: {out_path}")

if __name__ == "__main__":
    RAW_PATH = "data/raw_data.csv"
    CLEAN_PATH = "data/clean_data.csv"

    df = load_data(RAW_PATH)
    df = clean_data(df)
    save_clean_data(df, CLEAN_PATH)
