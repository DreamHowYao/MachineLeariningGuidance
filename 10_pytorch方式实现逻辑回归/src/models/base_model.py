import torch
import torch.nn as nn
from torch.nn.functional import sigmoid

class LrModel(nn.Module):
    def __init__(self, input_dim, out_features ,device=torch.device('cpu')):
        super(LrModel, self).__init__()
        self.device = device
        self.linear = nn.Linear(in_features=input_dim,out_features=out_features)

    def forward(self, x):
        return sigmoid(self.linear(x))
