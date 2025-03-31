import pickle

with open("resnet18.pth", "rb") as f:
    data = pickle.load(f, encoding="bytes", fix_imports=False)
    print(data)
