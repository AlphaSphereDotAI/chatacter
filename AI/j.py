from safetensors import safe_open
from safetensors.torch import save_file
import torch

# tensors = {"weight1": torch.zeros((1024, 1024)), "weight2": torch.zeros((1024, 1024))}
# save_file(tensors, "model.safetensors")

tensors = {}
with safe_open("C:/Users/moham/.cache/huggingface/hub/models--microsoft--phi-2/snapshots/b10c3eba545ad279e7208ee3a5d644566f001670/model-00001-of-00002.safetensors", framework="pt", device="cpu") as f:
    for key in f.keys():
        tensors[key] = f.get_tensor(key)
        print(tensors[key])

