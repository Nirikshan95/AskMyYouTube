import streamlit as st
from src.pipeline import main_pipeline

st.title('AskMyTouTube')
st.write('This is a simple app to ask questions about YouTube videos.')

yt_video_url = st.text_input("Enter YouTube video URL:")
query= st.text_input("Enter your query:")
if st.button('Submit'):
    if yt_video_url and query:
        result = main_pipeline(yt_video_url, query)
        if isinstance(result, str):
            st.error(result)
        else:
            st.write("Results:")
            st.write(result)
    else:
        st.warning("Please enter both YouTube video URL and your query.")