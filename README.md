# -Intelligent-Complaint-Analysis
Building a RAG-Powered Chatbot to Turn Customer Feedback into Actionable Insights

A Retrieval-Augmented Generation (RAG) Pipeline for Semantic Complaint Search

📌 Project Overview

Financial institutions receive thousands of consumer complaints every day. Hidden within these narratives are patterns, pain points, and signals that can guide better decisions—but only if the text can be searched and understood intelligently.

This project builds the foundation of a Retrieval-Augmented Generation (RAG) system by transforming raw consumer complaint narratives into a semantic search–ready vector database. The result is a clean, reproducible pipeline that prepares complaint data for downstream applications such as chatbots, question-answering systems, and analytics tools.

The work is divided into two main stages:

Exploratory Data Analysis & Preprocessing
Text Chunking, Embedding, and Vector Store Indexing

🗂 Project Structure

weel-7/
│
├── data/
│   ├── raw/                     # Original CFPB complaint dataset
│   └── processed/               # Cleaned and filtered complaint data
│
├── notebooks/
│   ├── task1_eda_preprocessing.ipynb
│   └── task2_pipeline.ipynb
│
├── src/
│   ├── config.py                # Central configuration (columns, seeds, paths)
│   ├── utils.py                 # Validation and helper utilities
│   ├── sampling.py              # Stratified sampling logic
│   ├── chunking.py              # Text chunking functions
│   ├── embeddings.py            # Embedding model loader
│   └── vector_store.py          # FAISS/ChromaDB indexing logic
│
├── vector_store/                # Persisted vector database
├── visualizations               # stores the plot visualization 
├── requirements.txt
└── README.md

This structure separates logic (src/) from execution (notebooks/), ensuring clarity, reusability, and reproducibility.


🧪 Task 1: Exploratory Data Analysis & Preprocessing

🎯 Objective
Understand the structure and quality of the CFPB complaint data and prepare it for semantic embedding.




🧩 Task 2: Text Chunking, Embedding, and Vector Store Indexing

🎯 Objective
Convert cleaned complaint narratives into a format suitable for efficient semantic search.

📊 Stratified Sampling
Created a stratified sample of 10,000–15,000 complaints.
Ensured proportional representation across all product categories.
Used a fixed random seed for reproducibility.
Sampling logic implemented in src/sampling.py.
This prevents dominant products from overshadowing smaller categories.

✂️ Text Chunking Strategy
Long complaint narratives were split into smaller, overlapping chunks to improve embedding quality.

Implemented using:

Custom chunking logic (fallback-safe)
Optional LangChain RecursiveCharacterTextSplitter
Final configuration:

chunk_size: balances semantic coherence
chunk_overlap: preserves contextual continuity
Chunking logic lives in src/chunking.py.

🧠 Embedding Model Choice
Model used: sentence-transformers/all-MiniLM-L6-v2

Why this model?

Strong semantic performance
Lightweight and fast
Well-suited for sentence-level embeddings
Widely adopted and well-documented
Embedding loading is handled in src/embeddings.py.

🗃 Vector Store Indexing
Generated embeddings for each text chunk.
Stored vectors using FAISS (or ChromaDB as a fallback).
Persisted the vector store to disk.
Each vector includes metadata, such as:

Complaint ID
Product category
Chunk index
This ensures every retrieved chunk can be traced back to its original source.

Indexing logic is implemented in src/vector_store.py.

♻️ Reproducibility & Robustness
This project was designed to be robust and reproducible:

✅ Central configuration in src/config.py
✅ Fixed random seeds for sampling
✅ Input validation with clear error messages
✅ Graceful fallbacks for missing libraries
✅ Modular design for easy extension
All modules are orchestrated from a single notebook, ensuring clarity while maintaining clean separation of concerns.

🚀 How to Run
Install dependencies:

pip install -r requirements.txt
Run notebooks :

notebooks/task2_pipeline.ipynb
The persisted vector store will be available in:

vector_store/

🌱 Future Work
Integrate a RAG chatbot interface (Gradio or Streamlit)
Add evaluation for retrieval quality
Experiment with larger embedding models
Support real-time complaint ingestion

✨ Closing Note
This project lays a strong, thoughtful foundation for intelligent complaint analysis. Each step—EDA, cleaning, sampling, chunking, embedding, and indexing—was designed with care, clarity, and purpose.