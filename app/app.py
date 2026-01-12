import sys
from pathlib import Path
import streamlit as st

# Add project root to path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from src.retrieval.retriever import ComplaintRetriever
from src.generation.generator import ComplaintGenerator
from src.rag.rag_pipeline import ComplaintRAGPipeline

# Initialize RAG Pipeline
@st.cache_resource
def load_rag_pipeline():
    retriever = ComplaintRetriever(
        index_path="vector_db/faiss_index",
        metadata_path="vector_db/faiss_index_meta.pkl"
    )
    generator = ComplaintGenerator()
    return ComplaintRAGPipeline(retriever, generator)

rag = load_rag_pipeline()

# Build the UI
st.title("📊 CrediTrust Complaint Insight Assistant")

st.write(
    "Ask questions about customer complaints and receive evidence-backed insights."
)

question = st.text_input(
    "Enter your question:",
    placeholder="Why are customers unhappy with credit cards?"
)

if st.button("Analyze"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer, sources = rag.answer(question, top_k=5)

        st.subheader("🔍 Answer")
        st.write(answer)

        st.subheader("📌 Source Complaints")
        for s in sources:
            st.markdown(
                f"- **Product:** {s['product']} | **Complaint ID:** {s['complaint_id']}"
            )
