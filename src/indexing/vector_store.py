from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from typing import List
from models import load_embedding_model
from configs.config import EMBEDDING_MODEL_ID

def create_vector_store(Docs: List[Document]) -> FAISS:
    """Creates a vector store from a list of documents using the specified embedding model."""
    try:
        embedding_model=load_embedding_model(EMBEDDING_MODEL_ID)
        return FAISS.from_documents(
            documents=Docs,
            embedding=embedding_model
        )
    except Exception as e:
        raise RuntimeError(f"Failed to create vector store: {e}")