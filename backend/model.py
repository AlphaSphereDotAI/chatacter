import os

import pandas as pd
from huggingface_hub import snapshot_download
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from scipy.io.wavfile import write
from transformers import AutoModelForTextToWaveform, AutoProcessor

CONFIG = pd.read_json("/workspaces/graduation_project/config.json")


def check_and_download_model(model_path, repo_id):
    if not os.path.exists(model_path):
        print("Model not found. Downloading...")
        snapshot_download(repo_id=repo_id, local_dir=model_path)
    else:
        print("Model exists.")


check_and_download_model(CONFIG["model"]["text_to_voice"], "suno/bark-small")
processor = AutoProcessor.from_pretrained(CONFIG["model"]["text_to_voice"])
model = AutoModelForTextToWaveform.from_pretrained(CONFIG["model"]["text_to_voice"])
chat = ChatGroq(model_name="mixtral-8x7b-32768", verbose=True)


def generate_audio(response):
    """generate audio"""
    print("\tChatacter is generating the audio...")
    inputs = processor(response, return_tensors="pt")
    audio = model.generate(**inputs)
    print("\tAudio generated with Rate 24000")
    print("\tSaving audio...")
    write(CONFIG["assets"]["audio"], 24000, audio.squeeze(0).numpy())


def generate_video():
    """generate video"""
    # os.system(
    #     f"python /workspaces/graduation_project/backend/sadtalker/inference.py --source_image {CONFIG['image']} --driven_audio {CONFIG['audio']}"
    # )


def get_response(query):
    """get response function"""
    print("1 / 2")
    print(f"Sending {query} to Chatacter...")
    print("Thinking...")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Ack as Napoleon Bonaparte. Answer in one statement."),
            ("human", "{text}"),
        ]
    )
    chain = prompt | chat
    response = chain.invoke({"text": query})
    print("2 / 2")
    generate_audio(response.content)
    print(f"Here is the response: {response.content}")
    generate_video()
    return response.content
