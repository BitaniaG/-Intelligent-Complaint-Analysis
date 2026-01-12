import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


class ComplaintRetriever:
    """
    Handles semantic retrieval from a FAISS vector store.
    """

    def __init__(self, index_path, metadata_path, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        # Load FAISS index
        self.index = faiss.read_index(index_path)

        # Load metadata
        with open(metadata_path, "rb") as f:
            self.metadata = pickle.load(f)

        # Load embedding model (same as used in Task 2)
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query, top_k=5):
        """
        Convert query to embedding and retrieve top-k similar chunks.
        """
        query_embedding = self.model.encode(query).astype("float32").reshape(1, -1)

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results
