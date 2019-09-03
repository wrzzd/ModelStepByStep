import torch
from torch import nn
from torch.nn.parameter import Parameter

import numpy as np

class BiLinear(Module):
    def __init__(self, in1_features, in2_features, out_features, bias=True):
        super(BiLinear, self).__init__()
        self.in2_features = in2_features
        self.in1_features = in1_features
        self.out_features = out_features

        self.weight = Parameter(torch.Tensor(out_features, in1_features, in2_features))

        if bias:
            self.bias = Parameter(torch.Tensor(out_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self):


    
