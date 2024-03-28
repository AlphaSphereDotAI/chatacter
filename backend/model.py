from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from scipy.io.wavfile import write
from transformers import pipeline

pipe = pipeline(
    "text-to-speech",
    model="suno/bark-small",
    device=0,
)
chat = ChatGroq(
    model_name="mixtral-8x7b-32768",
    verbose=True,
)


def generate_audio(response):
    """generate audio"""
    print("\tChatacter is generating the audio...")
    audio = pipe(response)
    print(f"\tAudio generated with Rate {audio['sampling_rate']}")
    print("\tSaving audio...")
    audio_data = audio["audio"]
    sample_rate = audio["sampling_rate"]
    write("./assets/demo.wav", sample_rate, audio_data.T)


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
    return response.content
