import streamlit as st

st.title("Drake Speak - AI Video Dubbing")
st.write("Welcome to your free video dubbing web app powered by Streamlit!")

# Add your dubbing app UI and logic here
video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
if video_file is not None:
    st.video(video_file)
    if st.button("Start Dubbing"):
        st.success("Dubbing process simulated successfully!")
      
