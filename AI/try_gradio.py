import streamlit as st
import time
import os

st.chat_input("What's up?")

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0, 'Loading...')

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

video_file = open(
    "D:/OneDrive - Cairo University - Students/Development/graduation_project/AI/SadTalker/examples/ref_video/WDA_KatieHill_000.mp4",
    "rb",
)
video_bytes = video_file.read()
st.video(video_bytes)
