import os
import time

import google.generativeai as genai
import pandas as pd
import streamlit as st

genai.configure(api_key="")

# import pprint
# for model in genai.list_models():
#     pprint.pprint(model)

model = genai.GenerativeModel(model_name="gemini-1.0-pro")
chat = model.start_chat(history=[])
prompt = st.chat_input("What's up?")
if prompt:
    response = chat.send_message(prompt)
    st.write(response.text)

# Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0, 'Loading...')
# for i in range(100):
#     latest_iteration.text(f"Iteration {i+1}")
#     bar.progress(i + 1)
#     time.sleep(0.1)

video_file = open(
    "D:/OneDrive - Cairo University - Students/Development/graduation_project/AI/SadTalker/examples/ref_video/WDA_KatieHill_000.mp4",
    "rb",
)
video_bytes = video_file.read()
# st.video(video_bytes)
