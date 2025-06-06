from src.indexing.youtube_transcript import get_youtube_transcript,transcript_exception_msg
from src.indexing.chunking import split_text_into_chunks
from src.indexing.vector_store import create_vector_store
from src.models import load_embedding_model, load_chat_model
from configs import config

def main_pipeline(yt_video_url: str,query:str):
    # Indexing step
    transcript = get_youtube_transcript(yt_video_url)
    if isinstance(transcript, str) and transcript_exception_msg in transcript:
        print(transcript)
        return transcript_exception_msg
    else:
        chuncks= split_text_into_chunks(transcript, chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
        if not isinstance(chuncks, list):
            print(chuncks)
            return chuncks
        print(f'chuck 1: \n\n {chuncks[0]}')
        vector_store=create_vector_store(chuncks)
        return vector_store.get(include=["metadatas", "documents", "ids"])[0]
    
if __name__ == "__main__":
    yt_video_url = input("Enter YouTube video URL: ")
    query = input("Enter your query: ")
    main_pipeline(yt_video_url, query)