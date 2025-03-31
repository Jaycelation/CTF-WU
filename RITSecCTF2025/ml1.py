import torch
import json

# Load state_dict
state_dict = torch.load("eldorian_artifact.pth", map_location="cpu")

for key, value in state_dict.items():
    if isinstance(value, torch.Tensor):
        try:
            text = "".join([chr(int(v)) for v in value.flatten().tolist() if 32 <= v <= 126])
            print(f"Decoded text from {key}: {text}")
        except:
            pass