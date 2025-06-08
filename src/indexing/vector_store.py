from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from typing import List
from src.models import load_embedding_model
from configs.config import EMBEDDING_MODEL_ID, VECTOR_STORE_PATH
import os

def create_vector_store(docs: List[Document],video_id) -> FAISS:
    """Creates a vector store from a list of documents using the specified embedding model."""
    try:
        vector_store_path=os.path.join(VECTOR_STORE_PATH, video_id)
        if os.path.exists(vector_store_path):
            return FAISS.load_local(vector_store_path, load_embedding_model(EMBEDDING_MODEL_ID),allow_dangerous_deserialization=True)
        else:
            embedding_model=load_embedding_model(EMBEDDING_MODEL_ID)
            vector_store= FAISS.from_documents(
                documents=docs,
                embedding=embedding_model
            )
            
            if not os.path.exists(vector_store_path):
                os.makedirs(vector_store_path)
            vector_store.save_local(vector_store_path)
            return vector_store
    except Exception as e:
        raise RuntimeError(f"Failed to create vector store: {e}")