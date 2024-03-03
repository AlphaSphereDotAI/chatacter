import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from transformers import pipeline

pipe = pipeline(
    "text-to-speech",
    model="suno/bark",
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
    # audio = pipe(response.content)
    # print(audio["audio"])
    print("Here is the response:")
    print(response.content)
    data = {
        # "audio": audio["audio"].tolist(),
        # "rate": audio["sampling_rate"],
        "response": response.content,
    }
    return json.dumps(data)
