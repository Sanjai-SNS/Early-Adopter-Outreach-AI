# chains/rag_chain.py

from langchain_community.tools.duckduckgo_search import DuckDuckGoSearchRun
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

def run_rag_chain(query: str):
    # Step 1: Live Search from DuckDuckGo
    search = DuckDuckGoSearchRun()
    results = search.run(query)

    # Step 2: Convert to Document
    documents = [Document(page_content=results)]

    # Step 3: Split into chunks
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Step 4: Embed and store in FAISS
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_documents(texts, embeddings)

    # Step 5: Retrieve top documents
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    retrieved_docs = retriever.get_relevant_documents(query)

    # Step 6: Return retrieved chunks
    return [doc.page_content for doc in retrieved_docs]
