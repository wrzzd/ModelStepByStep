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
        super(
