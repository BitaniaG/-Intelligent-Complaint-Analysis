import faiss
import numpy as np
import os
import pickle

def create_faiss_index(embeddings, metadata, save_path):
    if len(embeddings) == 0:
        raise ValueError("No embeddings provided")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    faiss.write_index(index, save_path)

    with open(save_path + "_meta.pkl", "wb") as f:
        pickle.dump(metadata, f)

    return index