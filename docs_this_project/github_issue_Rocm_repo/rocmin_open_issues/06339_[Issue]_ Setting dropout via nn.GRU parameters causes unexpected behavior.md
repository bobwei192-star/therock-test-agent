# [Issue]: Setting dropout via nn.GRU parameters causes unexpected behavior

- **Issue #:** 6339
- **State:** open
- **Created:** 2026-06-08T00:35:53Z
- **Updated:** 2026-06-30T20:17:27Z
- **Labels:** application:pytorch, status: triage, project: miopen
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6339

### Problem Description

This was tested on both pytorch 2.12.0+rocm7.2 and pytorch 2.9.1+rocm7.2.1.gitff65f5bc.
A clean conda environment using torch 2.12+rocm7.2 was created for testing.

When building a character RNN from [example code](https://github.com/ageron/handson-mlp/blob/main/14_nlp_with_rnns_and_attention.ipynb) and with reference from previous training/validation benchmarks from an nvidia GPU, I encountered unexpected behavior when dropouts are introduced via parameters into nn.GRU. 

Specifically, when I call `self.gru = nn.GRU(embed_dim, hidden_dim, num_layers=n_layers,batch_first=True, dropout=dropout)` with 2 layers and dropout set to 0.1, training stalls on an AMD GPU, whereas training runs normally on an nvidia GPU. using nn.Dropout fixes the problem, which points to a bug in how dropout is implemented in nn.GRU (and possibly other similar classes).

loss stalls at ~3.07 irrespective of all hyperparameter tuning.
When manually placing nn.dropout between layers, normal loss optimization is recovered.

**Using dropouts w/ nn.gru (2 hidden layers, dropouts = .1) (ShakespeareModel, see example code):**
batch: 50, loss:3.6340441703796387
...
batch: 2300, loss:3.0771820545196533
...
batch: 5850, loss:3.067248821258545

**Using dropouts using nn.Dropout between 2 GRU layers (ShakespeareModel2 (!!), see example code):**
batch: 50, loss:3.6074438095092773
...
batch: 2300, loss:2.439793586730957
...
batch: 5850, loss:1.8970005512237549


**In the ROCm environment, switching to 'cpu' does not fix this problem.**

**I also ran this using a free T4 GPU in colab; nn.GRU dropouts worked normally and loss optimized normally (ShakespeareModel).**
batch: 50, loss:3.6132819652557373
...
batch: 2300, loss:2.5288307666778564
...
batch: 5850, loss:2.13324236869812



Efforts were made to resolve some non-determinism in the below script. I understand there are non-deterministic factors in training. Loss using nn.GRU dropouts does not minimize normally over multiple hyperparameter settings and seeds.


Thank you.


### Operating System

Ubuntu 24.04.4 LTS (Noble Numbat)

### CPU

CPU: AMD Ryzen 7 9700X 8-Core Processor

### GPU

Radeon RX 7900 XTX                 

### ROCm Version

7.2

### ROCm Component

_No response_

### Steps to Reproduce

**Loss should fall below 3 within 2000 batches**

```
from pathlib import Path
import urllib.request
import requests
import torch
import numpy as np
from torch.utils.data import DataLoader
import torch.nn as nn

SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.use_deterministic_algorithms(True)
device = 'cuda'


# Get shakespeare training set
url = "https://homl.info/shakespeare"
response = requests.get(url)
shakespeare_text = response.text

# Create encoder and decoder
vocab = sorted(set(shakespeare_text.lower()))
char_to_id = {char: index for index, char in enumerate(vocab)}
id_to_char = {index: char for index, char in enumerate(vocab)}

def encode_text(text):
    return torch.tensor([char_to_id[char] for char in text.lower()])

def decode_text(char_ids):
    return "".join([id_to_char[char_id.item()] for char_id in char_ids])


# Create Dataset
class CharDataset(torch.utils.data.Dataset):
  def __init__(self, text, window_size):
    self.text = text
    self.encoded_text = encode_text(self.text)
    self.window_size = window_size

  def __len__(self):
    # 1 short to preserve spot for target 
    return len(self.text) - self.window_size

  def __getitem__(self, idx):
    if idx >= len(self):
      raise IndexError("index outside valid range")
    end = idx + self.window_size
    window = self.encoded_text[idx:end]
    target = self.encoded_text[idx+1:end+1]
    return window, target

# Create dataloaders
window_length = 50
batch_size = 512
train_set = CharDataset(shakespeare_text[:1_000_000], window_length)
valid_set = CharDataset(shakespeare_text[1_000_000:1_060_000], window_length)
test_set = CharDataset(shakespeare_text[1_060_000:], window_length)
train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, generator=torch.Generator().manual_seed(SEED), num_workers=0)
valid_loader = DataLoader(valid_set, batch_size=batch_size, num_workers=0)
test_loader = DataLoader(test_set, batch_size=batch_size, num_workers=0)

# Create Model
class ShakespeareModel(nn.Module):
    def __init__(self, vocab_size, n_layers=2, embed_dim=10, hidden_dim=128,
                 dropout=0.1):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.gru = nn.GRU(embed_dim, hidden_dim, num_layers=n_layers,
                          batch_first=True, dropout=dropout)
        self.output = nn.Linear(hidden_dim, vocab_size)

    def forward(self, X):
        embeddings = self.embed(X)
        outputs, _states = self.gru(embeddings)
        return self.output(outputs).permute(0, 2, 1)

model = ShakespeareModel(len(vocab)).to(device)
opt = torch.optim.Adam(model.parameters())
loss_fn = nn.CrossEntropyLoss()
model.train()
cur_batch =0
for epoch in range(3):
  for i,(xb,yb) in enumerate(train_loader):
      cur_batch +=1
      xb = xb.to(device)
      yb = yb.to(device)
      opt.zero_grad()
      out = model(xb)
      loss = loss_fn(out.reshape(-1,out.size(1)), yb.reshape(-1))
      loss.backward(); opt.step()
      if cur_batch%50==0: print(f'batch: {cur_batch}, loss:{loss.item()}'
```

Here is the second model and basic training loop using nn.Dropout:
```

class ShakespeareModel2(nn.Module):
    def __init__(self, vocab_size, n_layers=2, embed_dim=10, hidden_dim=128,
                 dropout=0.1):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.gru_1 = nn.GRU(embed_dim, hidden_dim, num_layers=1,
                          batch_first=True)
        self.dropout = nn.Dropout(dropout)
        self.gru_2 = nn.GRU(hidden_dim, hidden_dim, num_layers=1,
                          batch_first=True)
        self.output = nn.Linear(hidden_dim, vocab_size)

    def forward(self, X):
        embeddings = self.embed(X)
        outputs, _ = self.gru_1(embeddings)
        outputs = self.dropout(outputs)
        outputs, _ = self.gru_2(outputs)
        return self.output(outputs).permute(0, 2, 1)

model = ShakespeareModel2(len(vocab)).to(device)
opt = torch.optim.Adam(model.parameters())
loss_fn = nn.CrossEntropyLoss()
model.train()
cur_batch =0
for epoch in range(3):
  for i,(xb,yb) in enumerate(train_loader):
      cur_batch +=1
      xb = xb.to(device)
      yb = yb.to(device)
      opt.zero_grad()
      out = model(xb)
      loss = loss_fn(out.reshape(-1,out.size(1)), yb.reshape(-1))
      loss.backward(); opt.step()
      if cur_batch%50==0: print(f'batch: {cur_batch}, loss:{loss.item()}')
```


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_