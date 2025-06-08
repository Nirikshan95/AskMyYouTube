from youtube_transcript_api import YouTubeTranscriptApi

transcript_exception_msg="An error occurred: \n\n Try again [ sometimes it's failed to fetch transcript or video/video captions are not available ]\n\n Please check the video URL or try another one."

def get_video_id(url: str) -> str:
    """Extracts the video ID from a YouTube URL."""
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com/watch?v=" in url:
        return url.split("v=")[-1]  #.split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL")
    
def get_youtube_transcript(url: str):
    
    video_id= get_video_id(url)
    try:
        transcript=YouTubeTranscriptApi.get_transcript(video_id)
        transcript="\n\n".join(script['text'] for script in transcript)     # Removed timestamps and duration
        return transcript,video_id
    except Exception :
        return transcript_exception_msg,None