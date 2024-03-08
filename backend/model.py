from fastapi.responses import FileResponse
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


def get_response(query):
    """get response function"""
    print("1 / 2")
    print(f"Sending {query} to Chatacter...")
    print("Thinking...")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are Napoleon Bonaparte. Answer in one statement."),
            ("human", "{text}"),
        ]
    )
    chain = prompt | chat
    response = chain.invoke({"text": query})
    print("2 / 2")
    print("Chatacter is generating the audio...")
    audio = pipe(response.content)
    print(f"Audio generated with Rate {audio['sampling_rate']}")
    print("Saving audio...")
    audio_data = audio["audio"]
    sample_rate = audio["sampling_rate"]
    write("./assets/demo.wav", sample_rate, audio_data.T)
    print(f"Here is the response: {response.content}")
    return [response.content, FileResponse("./assets/demo.wav")]
