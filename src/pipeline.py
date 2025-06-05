from indexing.youtube_transcript import get_youtube_transcript
from indexing.chunking import split_text_into_chunks
from indexing.vector_store import create_vector_store
from models import load_embedding_model, load_chat_model
from configs import config
from typing import List
from langchain.schema import Document

def main_pipeline(yt_video_url: str,query:str):
    # Indexing step
    transcript = get_youtube_transcript(yt_video_url)
    if isinstance(transcript, str) and "An error occurred" in transcript:
        print(transcript)
        return
    chuncks= split_text_into_chunks(transcript, chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
    vector_store=create_vector_store(chuncks)
    print(vector_store.get(include=["metadatas", "documents", "ids"])[0])
    
if __name__ == "__main__":
    yt_video_url = input("Enter YouTube video URL: ")
    query = input("Enter your query: ")
    main(yt_video_url, query)