from sentence_transformers import SentenceTransformer

def load_embedding_model(model_name):
    try:
        return SentenceTransformer(model_name)
    except Exception as e:
        raise RuntimeError(f"Failed to load embedding model: {e}")
