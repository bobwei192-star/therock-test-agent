# Memory Leak with PyTorch in ROCM 2.9

- **Issue #:** 984
- **State:** closed
- **Created:** 2019-12-26T15:00:18Z
- **Updated:** 2023-12-18T15:52:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/984

Hi,

I have been running some experiments on my Vega 10 GPU and I have found that while I am running a model fully in GPU it starts eating slowly the CPU memory until there is no memory left. I simplified my code as much as possible to help you reproduce it. I've tried exactly the same code in a p2.xlarge instance in AWS with Pytorch and the CPU memory usage is perfectly constant while training.

If you run it, you will see that after 30 epochs it will have consumed about 5-10 GB of CPU memory. When training bigger models this effect is more remarkable...

I am using Pytorch inside Docker, using **rocm/pytorch:rocm2.9_ubuntu16.04_py3.6_pytorch** as a base.

Any help will be appreciated :D

```
import numpy as np
from torch import nn
import torch

BATCH_SIZE = 128
TIME_STEPS = 1000
FEATURES = 10
FORECAST_HORIZON = 15

# Model delfinition

class Encoder(nn.Module):
    def __init__(self, n_num_time_feats):
        super().__init__()
        self.rnn_encoder = nn.LSTM(input_size=n_num_time_feats, hidden_size=128)

    def forward(self, x_num_time):
        _, state = self.rnn_encoder(x_num_time)
        return state

class Decoder(nn.Module):
    def __init__(self, n_forecast_timesteps):
        super().__init__()
        self.h = nn.Linear(in_features=256, out_features=n_forecast_timesteps)

    def forward(self, state):
        batch_size = 128
        context_thought = torch.cat(state, -1).squeeze()
        output = self.h(context_thought).t()
        return output

def torch_rmse(actual, forecast):
    residuals = actual - forecast
    rmse = torch.sqrt(torch.mean((residuals) ** 2))
    return rmse

enc = Encoder(FEATURES).cuda()
dec = Decoder(FORECAST_HORIZON).cuda()
optimizer = torch.optim.Adam(params=list(enc.parameters()) + list(dec.parameters()))

for epoch in range(0, 30):  # Epochs loop
    print("Epoch: ", epoch)
    for i in range(2000):  # Batches loop
        data = np.random.randn(TIME_STEPS, BATCH_SIZE, FEATURES).astype(np.float32)
        target = np.random.randn(FORECAST_HORIZON, BATCH_SIZE).astype(np.float32)
        data = torch.from_numpy(data).cuda()
        target = torch.from_numpy(target).cuda()

        optimizer.zero_grad()
        output = dec(enc(data))
        loss = torch_rmse(target, output)
        loss.backward()
        optimizer.step()
```

Edit: I tried with the version 3.0 of ROCM and the problem is still there. 