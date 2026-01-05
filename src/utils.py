import numpy as np
def validate_dataframe(df, required_columns):
    missing = [c for c in required_columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

def stack_embeddings(embeddings_list):
    return np.vstack(embeddings_list).astype("float32")
