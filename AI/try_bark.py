# from bark import SAMPLE_RATE, generate_audio, preload_models
# from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# # download and load all models
# preload_models()

# # generate audio from text
# text_prompt = """
#      Hello, my name is Suno. And, uh — and I like pizza. [laughs]
#      But I also have other interests such as playing tic tac toe.
# """
# audio_array = generate_audio(text_prompt)

# # save audio to disk
# write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)

from qai_hub_models.models import llama_v2_7b_chat_quantized

# Load the model
torch_model = llama_v2_7b_chat_quantized

# Generate a response
response = torch_model.generate_response("Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe.")
print(response)