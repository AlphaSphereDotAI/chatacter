# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

inputs = tokenizer.encode("how are you?", return_tensors="pt")
outputs = model.generate(inputs, max_length=32, num_beams=4, early_stopping=True)
print(tokenizer.decode(outputs[0]))
