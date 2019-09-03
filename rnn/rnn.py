import torch
import torch.nn as nn

class RNN(Module):
    '''
    input: batch_size * sequence_len * embedding_dim
    h_0: hidden_dim

    output: batch_size * sequence_len * output_dim
    '''
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.U = nn.Linear(kwargs[hidden_dim], kwargs[hidden_dim])
        self.W = nn.Linear(kwargs[embedding_dim], kwargs[hidden_dim])
        self.b = torch.Tensor(kwargs[hidden_dim])

        self.V = nn.Linear(kwargs[hidden_dim], kwargs[output_dim])

    def forward(self, x, h_0):
        # for simple , input x: sequence_len * embedding_dim
        y = []
        for i in range(kwargs[sequence_len]):
            h = nn.ReLU(self.U(h) + self.W(x[i]) + self.b)
            y.append(self.V(h))

        return torch.Tensor(y)

