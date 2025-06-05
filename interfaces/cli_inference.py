from src.pipeline import main_pipeline

def main():
    yt_video_url = input("Enter YouTube video URL: ")
    query = input("Enter your query: ")
    main_pipeline(yt_video_url, query)

if __name__ == "__main__":
    main()