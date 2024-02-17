import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

start = time.time()
inputs = tokenizer.encode("how are you?", return_tensors="pt")
outputs = model.generate(inputs)
ans = tokenizer.decode(outputs[0])
ans = ans.replace("<pad>", "").strip()
ans = ans.replace("</s>", "").strip()
print(ans)
end = time.time()
print("Time taken: ", (end - start), "s")
