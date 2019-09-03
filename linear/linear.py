import math
import numpy as np

import torch
from torch.nn.parameter import Parameter
from .. import functional as F
from .. import init
from .module import Module


class Linear(Module):
    """
    Args: input_features_dim: int
          output_features_dim: int
          bias: bool, default: True
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.weight = np.array((kwargs[input_dim], kwargs[output_dim]))
        if kwargs[bias]:
            self.b = np.array(kwargs[output_dim])
        else:
            self.b = np.zero(kwargs[output_dim])

    def forward(self, x):
        y = x.matmul(self.weight.t())
        y += self.b

        return y

