import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from scipy.io.wavfile import write
from transformers import AutoModelForTextToWaveform, AutoProcessor

processor = AutoProcessor.from_pretrained(
    "/workspaces/graduation_project/backend/bark-small"
)
model = AutoModelForTextToWaveform.from_pretrained(
    "/workspaces/graduation_project/backend/bark-small"
)
chat = ChatGroq(
    model_name="mixtral-8x7b-32768",
    verbose=True,
)

IMAGE = "/workspaces/graduation_project/backend/assets/Einstein.jpg"
AUDIO = "/workspaces/graduation_project/backend/assets/AUDIO.wav"


def generate_audio(response):
    """generate audio"""
    print("\tChatacter is generating the audio...")
    inputs = processor(response, return_tensors="pt")
    audio = model.generate(**inputs)
    print("\tAudio generated with Rate 24000")
    print("\tSaving audio...")
    write(AUDIO, 24000, audio.squeeze(0).numpy())


def generate_video():
    """generate video"""
    os.system(
        f"python /workspaces/graduation_project/backend/sadtalker/inference.py --source_image {IMAGE} --driven_audio {AUDIO}"
    )


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
