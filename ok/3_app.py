import streamlit as st
import os
from rag_pipeline import setup_rag, format_docs

st.set_page_config(page_title="DMR Fault Analysis Bot", layout="wide")
st.title("📻 Offline DMR Diagnostic Assistant")
st.markdown("Powered by Phi-3 & ChromaDB (100% Offline)")

@st.cache_resource
def load_system():
    if not os.path.exists("./chroma_db"):
        st.error("Database not found! Please run 'python 1_ingest_data.py' first.")
        st.stop()
    return setup_rag()

# Load the RAG system
with st.spinner("Initializing offline models..."):
    retriever, rag_chain = load_system()

query = st.text_input("Enter fault symptom, error code, or technical query:")

if st.button("Analyze"):
    if query:
        with st.spinner("Searching manuals..."):
            # Step 1: Fetch the documents quickly
            docs = retriever.invoke(query)
            context_text = format_docs(docs)
            
        st.write("### Diagnostic Output")
        
        # OPTIMIZATION 4: Real-time Streaming
        # This writes the response to the screen word-by-word as it generates.
        response_stream = rag_chain.stream({"context": context_text, "question": query})
        st.write_stream(response_stream)
        
        st.write("### Source References (Ground Truth)")
        for i, doc in enumerate(docs):
            print(f"\n--- CHUNK {i+1} ---\n{doc.page_content}")
            with st.expander(f"Reference Document Context {i+1}"):
                st.write(doc.page_content)