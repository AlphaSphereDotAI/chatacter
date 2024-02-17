from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

torch.set_default_device("cuda")
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/phi-2", torch_dtype="auto", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

st = time.time()
inputs = tokenizer.encode("how are you?", return_tensors="pt")
# outputs = model.generate(inputs, max_length=32, num_beams=4, early_stopping=True)
# print(tokenizer.decode(outputs[0]))
outputs = model.generate(inputs, min_length=1000, max_length=1000, num_beams=4, early_stopping=True)
text = tokenizer.batch_decode(outputs)
print(text)
et = time.time()
print(et - st)
