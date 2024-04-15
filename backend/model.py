import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from sadtalker.app import download_model
from scipy.io.wavfile import write
from transformers import pipeline

pipe = pipeline(
    "text-to-speech",
    model="suno/bark-small",
)
chat = ChatGroq(
    model_name="mixtral-8x7b-32768",
    verbose=True,
)
IMAGE = "../AI/SadTalker/examples/source_image/Einstein.jpg"
AUDIO = "./assets/AUDIO.wav"
CHECKPOINT_DIR = "../AI/SadTalker/checkpoints"
RESULT_DIR = "./assets"


def generate_audio(response):
    """generate audio"""
    print("\tChatacter is generating the audio...")
    audio = pipe(response)
    print(f"\tAudio generated with Rate {audio['sampling_rate']}")
    print("\tSaving audio...")
    audio_data = audio["audio"]
    sample_rate = audio["sampling_rate"]
    write("./assets/AUDIO.wav", sample_rate, audio_data.T)


def generate_video():
    """generate video"""
    download_model("../AI/SadTalker")
    os.system(
        f"python inference.py \
            --source_image {IMAGE} \
            --driven_audio {AUDIO} \
            --checkpoint_dir {CHECKPOINT_DIR} \
            --result_dir {RESULT_DIR}"
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
