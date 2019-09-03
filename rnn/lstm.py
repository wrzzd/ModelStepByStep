import math
import numpy as np
import torch
import torch.nn as nn

class LSTM(RNNBase):
    __overloads__ = {'forward': ['forward_packed', 'forward_tensor']}

    def __init__(self, *args, **kwargs):
        super(LSTM, self).__init__('LSTM', *args, **kwargs)

        


