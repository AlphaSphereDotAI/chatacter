import streamlit as st
import google.generativeai as genai
from bark import SAMPLE_RATE, generate_audio, preload_models

preload_models()

genai.configure(api_key=st.secrets["GEMINI_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.0-pro")
prompt = st.chat_input("What's up?")
chat = model.start_chat(history=[])
if prompt:
    response = chat.send_message(prompt)
    audio_array = generate_audio(response.text)
    st.audio(audio_array, format="audio/wav", sample_rate=SAMPLE_RATE)
    st.write(response.text)
