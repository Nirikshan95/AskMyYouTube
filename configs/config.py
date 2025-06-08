# Embedding model
EMBEDDING_MODEL_ID="sentence-transformers/all-MiniLM-L6-v2"

# Chat model
CHAT_MODEL_ID="deepseek-ai/DeepSeek-V3-0324"
MAX_TOKENS = 200  # Maximum tokens for the chat model
TEMPARATURE = 0.3  # Temperature for the chat model

# Indexing - chuncking
CHUNK_SIZE = 1000  # Size of each chunk in characters
CHUNK_OVERLAP = 100  # Overlap size in characters between chunks 

#indexing - vector store
VECTOR_STORE_PATH = "vector_store"  # Path to save the vector store

# Retrieval
RETRIEVAL_K = 5  # Number of chunks to retrieve for each query