# Load model directly
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

inputs = tokenizer.encode("how are you?", return_tensors="pt")
outputs = model.generate(inputs, max_length=32, num_beams=4, early_stopping=True)
print(tokenizer.decode(outputs[0]))
