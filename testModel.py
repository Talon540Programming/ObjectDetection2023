import torch

file = './yolov5/runs/train/exp/weights/best.pt'
model = torch.jit.load(file)

with torch.no_grad():
    