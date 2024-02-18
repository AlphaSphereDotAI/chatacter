from transformers import AutoTokenizer, AutoModelForCausalLM
import time

tokenizer = AutoTokenizer.from_pretrained("MH0386/phi-2-napoleon-bonaparte")
model = AutoModelForCausalLM.from_pretrained("MH0386/phi-2-napoleon-bonaparte")

st = time.time()
inputs = tokenizer.encode("how are you?", return_tensors="pt")
outputs = model.generate(inputs, min_length=1000, max_length=1000, num_beams=4, early_stopping=True)
print(tokenizer.decode(outputs, skip_special_tokens=True))
et = time.time()
print(et - st)
