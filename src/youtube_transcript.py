from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url: str) -> str:
    """Extracts the video ID from a YouTube URL."""
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com/watch?v=" in url:
        return url.split("v=")[-1]  #.split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL")
    
def get_youtube_transcript(url: str) -> str:
    
    video_id= get_video_id(url)
    try:
        transcript=YouTubeTranscriptApi.get_transcript(video_id)
        transcript="\n\n".join(script['text'] for script in transcript)     # Removed timestamps and duration
        return transcript
    except Exception as e:
        return f"An error occurred: {e}"
    
if __name__ == "__main__":
    # Example usage
    url = input("Enter YouTube video URL: ")
    transcript = get_youtube_transcript(url)
    print("Transcript:")
    print(transcript)