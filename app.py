import streamlit as st
from src.pipeline import main_pipeline

st.title('AskMyTouTube')
st.write('This is a simple app to ask questions about YouTube videos.')

if not "yt_video_url" in st.session_state:
    st.session_state["yt_video_url"] = ""
if not "messages" in st.session_state:
    st.session_state["messages"] = []

yt_video_url = st.text_input("Enter YouTube video URL:")

if st.button('Submit'):
    if yt_video_url:
        st.session_state["yt_video_url"] = yt_video_url
        st.success("YouTube URL saved! Now ask your question below.")
    else:
        st.warning("Please enter YouTube video URL.")
        
query= st.chat_input("Enter your query:")
if query:
    if st.session_state["yt_video_url"]:
        with st.spinner("Processing your query..."):
            result = main_pipeline(st.session_state["yt_video_url"], query)
            st.session_state["messages"].append({"role": "user", "content": query})
            st.session_state["messages"].append({"role": "assistant", "content": result})
            if isinstance(result, str):
                st.error(result)
            else:
                st.write("Results:")
                st.write(result)
else:
    st.warning("Please enter a query.")
            
# Display chat history
if st.session_state.messages:
    st.markdown("---")
    st.subheader("Conversation History")
    for msg in st.session_state.messages:
        st.write(f"**{msg['role']}:** {msg['content']}")