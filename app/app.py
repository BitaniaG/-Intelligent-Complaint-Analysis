import sys
from pathlib import Path
import streamlit as st

# --------------------------------------------------
# Make project root importable so `src/` works
# --------------------------------------------------
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

# --------------------------------------------------
# Import RAG components
# --------------------------------------------------
from src.retrieval.retriever import ComplaintRetriever
from src.generation.generator import ComplaintGenerator
from src.rag.rag_pipeline import ComplaintRAGPipeline

# --------------------------------------------------
# Load RAG pipeline once (cached for performance)
# --------------------------------------------------
@st.cache_resource
def load_rag_pipeline():
    """
    Loads the retriever, generator, and RAG pipeline.
    Cached so it does not reload on every UI interaction.
    """
    retriever = ComplaintRetriever(
        index_path="vector_db/faiss_index",
        metadata_path="vector_db/faiss_index_meta.pkl"
    )
    generator = ComplaintGenerator()
    return ComplaintRAGPipeline(retriever, generator)

rag = load_rag_pipeline()

# --------------------------------------------------
# Initialize session state (needed for Clear button)
# --------------------------------------------------
if "question" not in st.session_state:
    st.session_state.question = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "sources" not in st.session_state:
    st.session_state.sources = []

# --------------------------------------------------
# Build the UI
# --------------------------------------------------
st.title("📊 CrediTrust Complaint Insight Assistant")

st.write(
    "Ask questions about customer complaints and receive evidence-backed insights."
)

# Text input bound to session state
st.session_state.question = st.text_input(
    "Enter your question:",
    value=st.session_state.question,
    placeholder="Why are customers unhappy with credit cards?"
)

# Layout buttons side by side
col1, col2 = st.columns(2)

with col1:
    analyze_clicked = st.button("Analyze")

with col2:
    clear_clicked = st.button("Clear")

# --------------------------------------------------
# Handle Analyze action
# --------------------------------------------------
if analyze_clicked:
    if st.session_state.question.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer, sources = rag.answer(
            st.session_state.question,
            top_k=5
        )
        st.session_state.answer = answer
        st.session_state.sources = sources

# --------------------------------------------------
# Handle Clear / Reset action
# --------------------------------------------------
if clear_clicked:
    st.session_state.question = ""
    st.session_state.answer = ""
    st.session_state.sources = []

# --------------------------------------------------
# Display Answer and Sources (if available)
# --------------------------------------------------
if st.session_state.answer:
    st.subheader("🔍 Answer")
    st.write(st.session_state.answer)

    st.subheader("📌 Source Complaints")
    for s in st.session_state.sources:
        st.markdown(
            f"- **Product:** {s['product']} | **Complaint ID:** {s['complaint_id']}"
        )
