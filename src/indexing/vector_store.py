from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from typing import List
from src.models import load_embedding_model
from configs.config import EMBEDDING_MODEL_ID

def create_vector_store(docs: List[Document]) -> FAISS:
    """Creates a vector store from a list of documents using the specified embedding model."""
    try:
        embedding_model=load_embedding_model(EMBEDDING_MODEL_ID)
        vector_store= FAISS.from_documents(
            documents=docs,
            embedding=embedding_model
        )
        return vector_store
    except Exception as e:
        raise RuntimeError(f"Failed to create vector store: {e}")