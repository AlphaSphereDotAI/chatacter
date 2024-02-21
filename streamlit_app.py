import streamlit as st
import time
import os
import google.generativeai as genai

genai.configure(api_key=st.secrets['GEMINI_KEY'])
model = genai.GenerativeModel(model_name="gemini-1.0-pro")
prompt = st.chat_input("What's up?")
if prompt:
    response = chat.send_message(prompt)
    st.write(response.text)
