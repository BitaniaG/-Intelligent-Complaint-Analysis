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

week-7/
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
├── requirements.txt
└── README.md
└── .gitignore 
└──visualizations/               # stores plot visualizations 
This structure separates logic (src/) from execution (notebooks/), ensuring clarity, reusability, and reproducibility.

🧪 Task 1: Exploratory Data Analysis & Preprocessing
🎯 Objective

Understand the structure, quality, and limitations of the CFPB complaint dataset and prepare clean, high-quality textual data suitable for semantic embedding and downstream RAG tasks.

🔍 Key Steps
Dataset Loading (Memory-Safe)

Due to the large size of the CFPB dataset, the data was processed using chunk-based loading to avoid memory exhaustion.

Column names were first discovered by loading only the file header.

Small row samples were loaded to safely inspect data values and quality without loading the full dataset into memory.

Initial EDA

Inspected available product categories using sampled data.

Verified the column containing consumer complaint narratives.

Analyzed the presence and absence of complaint narratives to confirm data usability.

Identified common data quality issues such as redacted values and boilerplate phrases.

Narrative Length Analysis

Calculated word counts on sampled narratives to assess text length distribution.

Confirmed the existence of:

Very short narratives with low informational value.

Very long narratives that would require chunking for effective embedding.

These findings directly informed chunking decisions in Task 2.

Filtering

Retained complaints mapped to the five business-relevant financial product categories defined in the challenge.

Removed records with missing or empty complaint narratives.

Filtering was performed incrementally during chunked reads to ensure scalability.

Text Cleaning & Normalization

Normalized redacted patterns (e.g., XXXX → <REDACTED>) to reduce meaningless token repetition.

Converted all text to lowercase for consistency.

Removed common boilerplate complaint phrases that add no semantic value.

Removed non-informative special characters while preserving meaningful tokens.

Normalized whitespace to ensure clean, uniform text.

Performed manual sanity checks to ensure semantic meaning was preserved.

📦 Output

The final cleaned and filtered dataset produced in Task 1 is saved as:
data/processed/filtered_complaints.csv

This dataset serves as the single source of truth for downstream sampling, chunking, embedding, and vector indexing tasks in the RAG pipeline.

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

Run notebooks:
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