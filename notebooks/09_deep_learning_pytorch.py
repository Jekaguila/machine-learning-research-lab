import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(10,20),
    nn.ReLU(),
    nn.Linear(20,1)
)
