# Memory Leak with PyTorch in ROCM 2.9

> **Issue #984**
> **状态**: closed
> **创建时间**: 2019-12-26T15:00:18Z
> **更新时间**: 2023-12-18T15:52:28Z
> **关闭时间**: 2023-12-18T15:52:28Z
> **作者**: ivallesp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/984

## 描述

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

---

## 评论 (5 条)

### 评论 #1 — ivallesp (2020-01-08T01:27:43Z)

any help?


---

### 评论 #2 — iotamudelta (2020-01-08T03:41:09Z)

Since you observe CPU memory exhaustion, could you elaborate on your host setup? How much RAM do you installed, what OS and kernel is running on the host, can you see which process is eating up the memory (is it the python process?)?

For future reference: we are monitoring https://github.com/ROCmSoftwarePlatform/pytorch/ issues closely, so if you have future issues do not hesitate to open them there if they are observed with PyTorch like this one.

---

### 评论 #3 — iotamudelta (2020-01-09T03:25:41Z)

I've run the script for the full 30 epochs and memory consumption of the python process on host never exceeded 4.6 GB RES. I think that's good news insofar as it doesn't seem to be fundamentally broken. My environment was a ROCm 3.0 docker, recent PyTorch, Radeon VII, Ubuntu 19.10 with stock Linux 5.3 kernel (no rocm-dkms). So as noted before it'd be very important for you to share your setup so that we have a chance at figuring out what relevant difference(s) are.

---

### 评论 #4 — nartmada (2023-12-13T23:26:11Z)

Hi @ivallesp, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #5 — nartmada (2023-12-18T15:52:28Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
