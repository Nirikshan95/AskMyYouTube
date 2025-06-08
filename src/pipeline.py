from src.indexing.youtube_transcript import get_youtube_transcript,transcript_exception_msg
from src.indexing.chunking import split_text_into_chunks
from src.indexing.vector_store import create_vector_store
from src.models import load_embedding_model, load_chat_model
from src.ans_generation import generate_answer
from configs import config

def main_pipeline(yt_video_url: str,query:str):
    
    # Indexing step
    transcript,video_id = get_youtube_transcript(yt_video_url)
    if isinstance(transcript, str) and transcript_exception_msg in transcript:
        return transcript_exception_msg
    else:
        chuncks= split_text_into_chunks(transcript, chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)
        if not isinstance(chuncks, list):
            return chuncks
        vector_store=create_vector_store(chuncks,video_id)
    
    # Retrieval
    retriever=vector_store.as_retriever(search_type="mmr", search_kwargs={"k": config.RETRIEVAL_K})
    retrivered_docs=retriever.invoke(query)
    answer=generate_answer(retrivered_docs,query)
    return answer