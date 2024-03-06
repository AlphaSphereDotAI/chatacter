import json

import numpy as np
import requests
import sounddevice as sd

response = requests.post(
    "http://localhost:8000/predict?query='What is the meaning of life?'"
)

json_data: json = json.loads(json.loads(response.content.decode("utf-8")))
print(json_data.keys())
audio = np.array(json_data["audio"])
rate = json_data["rate"]
response = json_data["response"]

print(f"Audio rate: {rate}")
print(f"Response: {response}")
print(audio.shape)
audio = np.squeeze(audio)
sd.play(audio, samplerate=rate)  # replace 44100 with your actual sample rate
sd.wait()
