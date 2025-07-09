# 📜 Union Budget 2025-26 QnA Chatbot

This is a simple **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **LangChain**, and a free open LLM from Hugging Face.

Ask natural language questions about the **Union Budget 2025**, and get intelligent, context-aware answers!

---

## 🚀 **How It Works**

✅ Loads a PDF file
✅ Splits the text into overlapping chunks for semantic search  
✅ Embeds the chunks with `sentence-transformers`  
✅ Stores them in a local **FAISS vector store**  
✅ Uses a **lightweight open-source LLM**  to generate final answers based on the retrieved context

---

## 📂 **Project Structure**

1️⃣ **Clone the repo**
git clone https://github.com/your-username/your-repo.git
cd your-repo
2️⃣ **Create virtual environment (optional)**
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows
3️⃣ **Install dependencies**
pip install -r requirements.txt
4️⃣ **Run Streamlit app**
streamlit run app.py
5️⃣ **Open your browser and ask any question about the Budget Speech!**


## 📂 **Chatbot Link**

