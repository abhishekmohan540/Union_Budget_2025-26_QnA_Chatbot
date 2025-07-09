import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

st.set_page_config(page_title="📄Union Budget 2025 RAG Q&A Bot")

st.title("📜Union Budget 2025 Q&A Chatbot")

#  Load the PDF
loader = PyPDFLoader("data/budget_speech.pdf")
pages = loader.load()

st.write(f" Loaded {len(pages)} pages from budget_speech.pdf")

#  Chunk the text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(pages)

st.write(f" Split into {len(docs)} chunks.")

#  Create embeddings + FAISS vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

st.success("Vector store created. Ready for Q&A!")

# Load our free HuggingFace LLM
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

generator = load_generator()

# Take user input
query = st.text_input("Ask a question about the Budget Speech:")

if st.button("Get Answer") and query:
    # Search similar chunks
    relevant_docs = vectorstore.similarity_search(query, k=5)
    context = " ".join([doc.page_content for doc in relevant_docs])

    st.write("### Retrieved Context")
    st.write(context)

    prompt = f"""
Context:
{context}

Question: {query}

Instruction: Provide a clear, concise answer in 2-3 sentences. Do not repeat the entire context.

Answer:
"""

    response = generator(prompt, max_new_tokens=300)
    st.write("### Answer")
    st.write(response[0]['generated_text'])
