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
outputs = model.generate(inputs, max_length=32, num_beams=4, early_stopping=True)
print(tokenizer.decode(outputs[0]))
et = time.time()
print(et - st)

# inputs = tokenizer('''def print_prime(n):
#    """
#    Print all primes between 1 and n
#    """''', return_tensors="pt", return_attention_mask=False)

# outputs = model.generate(**inputs, max_length=200)
# text = tokenizer.batch_decode(outputs)[0]
# print(text)

# from safetensors import safe_open
# from safetensors.torch import save_file

# tensors = {
#    "weight1": torch.zeros((1024, 1024)),
#    "weight2": torch.zeros((1024, 1024))
# }
# save_file(tensors, "model.safetensors")

# tensors = {}
# with safe_open("model.safetensors", framework="pt", device="cpu") as f:
#    for key in f.keys():
#        tensors[key] = f.get_tensor(key)