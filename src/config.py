import random
import numpy as np

# Reproducibility
RANDOM_SEED = 42

# Sampling
SAMPLE_SIZE = 12000
STRATIFY_COLUMN = "Product"

# Text
TEXT_COLUMN = 'clean_text'
ID_COLUMN = 'complaint_length'

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Embeddings
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Paths
VECTOR_DB_PATH = "vector_db/faiss_index"
