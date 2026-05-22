import os
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DOC_DIR = "./docs" 
DB_DIR = "./chroma_db"

def ingest_documents():
    print("Loading Markdown document...")
    file_path = os.path.join(DOC_DIR, "DMR_Manual.md")
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}. Please ensure your manual is there.")
        return

    # Read the raw text
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_document = f.read()

    # 1. Macro-Chunking: Split only on Chapter and Section to keep subsections glued together
    headers_to_split_on = [
        ("#", "Chapter"),
        ("##", "Section"),
    ]

    # 2. Split natively by Markdown headers, keeping headers in the text
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False
    )
    chunks = markdown_splitter.split_text(markdown_document)
    print(f"Split into {len(chunks)} context-aware Markdown chunks.")

    # 3. Create offline embeddings and Vector DB
    print("Downloading/Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

    print("Creating local vector database...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    print(f"Success! Ingested into {DB_DIR}")

if __name__ == "__main__":
    ingest_documents()