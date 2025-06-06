from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from langchain_huggingface import HuggingFaceEndpoint
from configs.config import EMBEDDING_MODEL_ID, CHAT_MODEL_ID
from dotenv import load_dotenv
import os
load_dotenv()

def load_embedding_model(repo_id: str = EMBEDDING_MODEL_ID):
    """Load the embedding model from Hugging Face."""
    try:
        return HuggingFaceEndpointEmbeddings(
            repo_id=repo_id,
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )
    except Exception as e:
        raise RuntimeError(f"Failed to load embedding model: {e}")

def load_chat_model(repo_id: str = CHAT_MODEL_ID):
    """Load the chat model from Hugging Face."""
    try:
        return HuggingFaceEndpoint(
            repo_id=repo_id,
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )
    except Exception as e:
        raise RuntimeError(f"Failed to load chat model: {e}")