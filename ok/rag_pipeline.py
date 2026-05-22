from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

DB_DIR = "./chroma_db"

# Helper function to join retrieved documents into readable text
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def setup_rag():
    # 1. Load the existing local vector database
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    vector_db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    # OPTIMIZATION 1: Reduced 'k' from 6 to 3. Phi-3 processes less text, making it much faster.
    retriever = vector_db.as_retriever(
        search_type="mmr", 
        search_kwargs={"k": 3, "fetch_k": 10})

    # OPTIMIZATION 2: Explicitly switch to Phi-3
    llm = Ollama(model="phi3", temperature=0.0)

    # 3. The "Synthesize & Educate" Prompt
    template = """You are a highly skilled, conversational technical expert for DMR radios. Your goal is to explain concepts clearly, deeply, and naturally, using ONLY the provided <context>.

    <rules>
    1. READ AND SYNTHESIZE: Read the <context> carefully to understand the information related to the User's Query.
    2. BE CONVERSATIONAL & EDUCATIONAL: Do not just blindly copy-paste raw text. Explain the concepts naturally, as if you were teaching a junior field technician. If they ask for a "deep dive," provide a thorough, structured explanation.
    3. RICH FORMATTING: Structure your response beautifully. Use Markdown headings (###), bold text (**bold**) for key terms, and clean bullet points to make the output highly readable and professional.
    4. NO HALLUCINATIONS: You are allowed to rephrase and summarize for readability, but you MUST NOT invent new features, facts, numbers, or steps that are not explicitly stated in the <context>.
    5. MISSING INFO: If the <context> does not contain enough information to answer the query, politely inform the user that the manual does not cover those specific details.
    </rules>

    <context>
    {context}
    </context>

    User Query: {question}

    Answer:"""

    prompt = PromptTemplate.from_template(template)

    # OPTIMIZATION 3: Return the retriever and chain separately so Streamlit can stream the text.
    rag_chain = prompt | llm | StrOutputParser()
    
    return retriever, rag_chain