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

🧠 Task 3: Retrieval-Augmented Generation (RAG) Core Logic & Evaluation
🎯 Objective

The goal of Task 3 is to transform the preprocessed and embedded CFPB complaint data into an intelligent question-answering system using a Retrieval-Augmented Generation (RAG) architecture. This task connects semantic retrieval with controlled language generation to enable grounded, evidence-based answers to natural-language business questions.

🏗️ RAG Architecture Overview

The RAG system is composed of three modular components:

Retriever

Generator

RAG Pipeline (Orchestration Layer)

Each component is implemented as a reusable Python module under the src/ directory to ensure maintainability and clarity.

🔍 Retriever Implementation

The retriever embeds user queries using the same sentence-transformer model used during indexing (all-MiniLM-L6-v2).

It performs similarity search against a persisted FAISS vector store.

The retriever returns the top-k most relevant complaint text chunks along with their metadata (product category and complaint ID).

This ensures semantic consistency between indexed data and incoming queries.

🧾 Prompt Engineering & Generator

A structured prompt template instructs the language model to:

Act as a financial analyst assistant

Use only the retrieved complaint context

Avoid hallucination or unsupported claims

The generator combines the user query and retrieved complaint chunks into a single prompt and sends it to the language model.

The generated response is concise, grounded in evidence, and focused on identifying recurring patterns rather than summarizing individual complaints.

🔁 RAG Pipeline Module

The RAG pipeline integrates the retriever and generator into a single callable interface.

Given a user question, the pipeline:

Retrieves relevant complaint chunks

Constructs a grounded prompt

Generates a final response

Returns both the answer and source metadata

This modular design allows easy reuse across evaluation notebooks and the interactive UI.

🧪 Qualitative Evaluation

To evaluate the effectiveness of the RAG system, 8 representative business questions were tested using a dedicated evaluation notebook:

Examples include:

Why are customers unhappy with credit cards?

What recurring issues do customers report about money transfers?

Are personal loan complaints mostly about interest rates or repayment?

What complaints suggest potential regulatory or compliance risks?

Evaluation focused on:

Relevance of retrieved context

Faithfulness of answers to complaint data

Ability to synthesize patterns across multiple complaints

The system consistently produced grounded, complaint-backed responses, meeting the qualitative evaluation requirements of the task.

💬 Task 4: Interactive Chat Interface (Streamlit)
🎯 Objective

Task 4 exposes the RAG system through a user-friendly web interface, enabling non-technical stakeholders to interact with complaint data using natural language.

🖥️ Application Overview

The interface is implemented using Streamlit

Entry point: app/app.py

The app connects directly to the persisted FAISS vector store and RAG pipeline

🎛️ UI Features

The application includes:

A text input field for user questions

An “Ask” button to submit queries

A clearly formatted answer section

Transparent display of source complaint metadata (product category and complaint ID)

A clean and intuitive layout suitable for non-technical users

This design prioritizes usability, explainability, and trust.

▶️ Running the Application
streamlit run app/app.py


Once launched, the app is accessible at:

http://localhost:8501

✅ Outcome

The interactive interface successfully demonstrates how a RAG-powered system can transform raw complaint data into actionable organizational intelligence, supporting faster decision-making and improved insight discovery.