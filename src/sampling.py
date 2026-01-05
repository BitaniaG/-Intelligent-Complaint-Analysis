import pandas as pd
from sklearn.model_selection import train_test_split

def stratified_sample(df, sample_size, stratify_col, random_state):
    if stratify_col not in df.columns:
        raise ValueError(f"Column '{stratify_col}' not found")

    if sample_size > len(df):
        raise ValueError("Sample size larger than dataset")

    sampled_df, _ = train_test_split(
        df,
        train_size=sample_size,
        stratify=df[stratify_col],
        random_state=random_state
    )
    return sampled_df.reset_index(drop=True)