import json
import requests
import streamlit as st

API = "localhost:8000"  # "https://8000-01hqrk1qr2p3w6cc5np0wk0ys5.cloudspaces.litng.ai"

st.set_page_config(
    page_title="Chat with Napoleon Bonaparte",
    page_icon="😀",
    layout="wide",
)


def request_prediction(query: str):
    response = requests.post(
        f"{API}/predict?query='{query}'",
        timeout=1000,
    )
    download_audio = requests.get(
        f"{API}/download",
        timeout=1000,
    )
    audio = download_audio.content
    response = json.loads(response.content.decode("utf-8"))
    return response, audio


st.title("😎 Chat with Napoleon Bonaparte")
userInput = st.chat_input("Type your message here")

if userInput is not None:
    message = st.chat_message("human")
    message.write("🕒")
    response, audio = request_prediction(userInput)
    message.write(response)
    st.audio(audio, format="audio/wav")