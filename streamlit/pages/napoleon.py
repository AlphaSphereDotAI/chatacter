import json

import requests

import streamlit as st

st.set_page_config(
    page_title="Chat with Napoleon Bonaparte",
    page_icon="😀",
    layout="wide",
)


def request_prediction(query: str):
    response = requests.post(
        f"https://8000-01hqrk1qr2p3w6cc5np0wk0ys5.cloudspaces.litng.ai/predict?query='{query}'"
    )
    download_audio = requests.get(
        "https://8000-01hqrk1qr2p3w6cc5np0wk0ys5.cloudspaces.litng.ai/download"
    )
    audio = download_audio.content
    response = json.loads(response.content.decode("utf-8"))
    return response, audio


st.title("😎 Chat with Napoleon Bonaparte")
query = st.chat_input("Type your message here")

if query is not None:
    message = st.chat_message("human")
    response, audio = request_prediction(query)
    message.write(response)
    st.audio(audio, format="audio/wav")
