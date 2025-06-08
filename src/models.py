from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from configs.config import EMBEDDING_MODEL_ID, CHAT_MODEL_ID, MAX_TOKENS, TEMPARATURE
from dotenv import load_dotenv
import os
load_dotenv()

def load_embedding_model(repo_id: str = EMBEDDING_MODEL_ID):
    """Load the embedding model from Hugging Face."""
    try:
        return HuggingFaceEndpointEmbeddings(
            model=repo_id,
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )
    except Exception as e:
        raise RuntimeError(f"Failed to load embedding model: {e}")

def load_chat_model(repo_id: str = CHAT_MODEL_ID):
    """Load the chat model from Hugging Face."""
    try:
        return ChatHuggingFace(llm=HuggingFaceEndpoint(
            repo_id=repo_id,
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            max_new_tokens=MAX_TOKENS,
            temperature=TEMPARATURE
        ))
    except Exception as e:
        raise RuntimeError(f"Failed to load chat model: {e}")