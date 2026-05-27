# Anyone has Deep Learning benchmark for 6800XT with Rocm?

> **Issue #1786**
> **状态**: closed
> **创建时间**: 2022-08-17T19:11:16Z
> **更新时间**: 2024-12-28T19:07:26Z
> **关闭时间**: 2024-05-09T15:29:48Z
> **作者**: ffleader1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1786

## 描述

I suppose currently 6800XT is about $600, which is the price I am willing to pay. That money can net me a 3070 Ti. However, the Nvidia choice has like half the amount of VRAM, and I am kinda get bored with the CUDA lock down system anyway. On top of that, my 1080 Ti for ML training is getting older. I can feel it...

Anyway, does anyone have any data about how AMD offerings (I know Rocm right now only support Rx 6800 and above) can compete with Nvidia cards?

Any comparable data between a 6800XT and 3070 Ti in deep learning would be nice. Thank you.

---

## 评论 (17 条)

### 评论 #1 — aoolmay (2022-08-17T19:28:09Z)

If you have a toy example(cut&paste kind of deal) i could run it for you on 6800XT now and on 6950XT in couple of days, when they finish current task.

Found and running this project https://pypi.org/project/ai-benchmark/ 

---

### 评论 #2 — ffleader1 (2022-08-17T20:02:37Z)

> If you have a toy example(cut&paste kind of deal) i could run it for you on 6800XT now and on 6950XT in couple of days, when they finish current task.
> 
> Found and running this project https://pypi.org/project/ai-benchmark/

I got these if you do not mind.

`pip install pytorch-benchmark`

````
import torch  
from torchvision.models import efficientnet_b0, vit_l_16, densenet161, regnet_y_1_6gf
from pytorch_benchmark import benchmark

model = efficientnet_b0()
sample = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
results = benchmark(model, sample, num_runs=10)

model2 =  densenet161()
sample2 = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
results2 = benchmark(model2, sample2, num_runs=10)


model3 =  regnet_y_1_6gf()
sample3 = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
results3 = benchmark(model3, sample3, num_runs=10)
````

For reference, I got 3.22s/it for efficientnet_b0; 29.59s/it for densenet161; and 4.97s/it for regnet_y_1_6gf on Colab K80.

---

### 评论 #3 — aoolmay (2022-08-17T21:14:49Z)

Couldn't get any of those two benchmarks to get running. Ai-benchmark seems outdated and doesn't give reliable results. Pytorch-benchmark doesn't recognize the GPU. I cobbled together an absurdly oversize model from keras tutorial example.
`
import tensorflow as tf
from tensorflow import keras
import numpy as np

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images_scaled = train_images / 255.0
test_images_scaled = test_images / 255.0
def get_model(hidden_layers=1):
    layers = [keras.layers.Flatten(input_shape=(28, 28))]
    for i in range(hidden_layers):
        layers.append(keras.layers.Dense(1024, activation='relu'),)
    # output layer    
    layers.append(keras.layers.Dense(10, activation='sigmoid'))
    model = keras.Sequential(layers)
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model
model = get_model(hidden_layers=128)
model.summary()
model.fit(train_images_scaled, train_labels, epochs=5, batch_size=512)
`
Epoch 1/5 118/118 [==============================] - 12s 42ms/step - loss: 2.3028 - accuracy: 0.0967
Epoch 2/5 118/118 [==============================] - 5s 42ms/step - loss: 2.3027 - accuracy: 0.0991
Epoch 3/5 118/118 [==============================] - 5s 42ms/step - loss: 2.3027 - accuracy: 0.0978
Epoch 4/5 118/118 [==============================] - 5s 42ms/step - loss: 2.3026 - accuracy: 0.0987
Epoch 5/5 118/118 [==============================] - 5s 42ms/step - loss: 2.3026 - accuracy: 0.0978


---

### 评论 #4 — aoolmay (2022-08-17T21:28:54Z)

Alternatively you can also reproduce this https://github.com/aime-team/tf2-benchmarks
Run command without XLA : python tf2-benchmarks.py --model resnet50 --batch_size 128 --num_gpus 1

Step 10, Images per second: 22.5 
Step 20, Images per second: 238.8 
Step 30, Images per second: 239.3 
Step 40, Images per second: 239.1 
Step 50, Images per second: 238.9 
Step 60, Images per second: 239.1 
Step 70, Images per second: 238.9 

GPU was run on both tests how i always run it, fixed overclock at 2725 MHz, -100mV undervolt, power cap at 332W.

Run command with XLA enabled : python tf2-benchmarks.py --model resnet50 --xla --batch_size 128 --num_gpus 1
Step 10, Images per second: 45.0 
Step 20, Images per second: 272.1 
Step 30, Images per second: 271.9 
Step 40, Images per second: 272.7 
Step 50, Images per second: 271.9 

---

### 评论 #5 — viralbitcraft (2022-08-17T23:38:28Z)

1070ti with lower batch size for comparison

```
python tf2-benchmarks.py --model resnet50 --batch_size 64 --num_gpus 1


2022-08-18 01:31:49.044639: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6674 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1070 Ti, pci bus id: 0000:08:00.0, compute capability: 6
Step 10, Images per second: 42.6 
Step 20, Images per second: 136.3 
Step 30, Images per second: 137.6 
Step 40, Images per second: 138.2 
Step 50, Images per second: 137.8 
Step 60, Images per second: 136.3 
Step 70, Images per second: 137.5 
```
```
python tf2-benchmarks.py --model resnet50 --xla --batch_size 64 --num_gpus 1
2022-08-18 01:34:48.036046: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6695 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1070 Ti, pci bus id: 0000:08:00.0, compute capability: 6.1
Step 10, Images per second: 25.9 
Step 20, Images per second: 161.4 
Step 30, Images per second: 161.4 
Step 40, Images per second: 162.0 
Step 50, Images per second: 161.6 
Step 60, Images per second: 161.9 
Step 70, Images per second: 161.3 
Step 80, Images per second: 161.1 
```

---

### 评论 #6 — viralbitcraft (2022-08-17T23:52:30Z)

Can I ask you to run resnet152 with appropriate batch size?
```
python tf2-benchmarks.py --model resnet152 --batch_size 16 --num_gpus 1
2022-08-18 01:46:16.206230: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6621 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1070 Ti, pci bus id: 0000:08:00.0, compute capability: 6.1
Step 10, Images per second: 12.3 
Step 20, Images per second: 50.8 
Step 30, Images per second: 51.1 
Step 40, Images per second: 50.9 
Step 50, Images per second: 51.4 
Step 60, Images per second: 50.4 
Step 70, Images per second: 51.1 
Step 80, Images per second: 49.9 
Step 90, Images per second: 48.6 

python tf2-benchmarks.py --model resnet152 --batch_size 16 --xla --num_gpus 1
2022-08-18 01:50:12.427213: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6742 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1070 Ti, pci bus id: 0000:08:00.0, compute capability: 6.1
Step 10, Images per second: 3.8 
Step 20, Images per second: 57.8 
Step 30, Images per second: 57.6 
Step 40, Images per second: 57.8 
Step 50, Images per second: 57.7 
Step 60, Images per second: 57.6 
Step 70, Images per second: 57.6 
Step 80, Images per second: 57.7 
Step 90, Images per second: 57.6 
Step 100, Images per second: 57.6 

```
Thank you!

---

### 评论 #7 — aoolmay (2022-08-18T00:01:03Z)

@virus-junior Started another job on the 6800XT, will do when it's free.

---

### 评论 #8 — ffleader1 (2022-08-18T00:53:22Z)

Thank you both. Awesome information.
So I take it that, with my 1080 Ti, I can get is around 50% performance uplift. A little bit lower than I prefer, but I guess I will take that. 

One small question though. Does the 6800 XT ever come into compatibility issue?

---

### 评论 #9 — aoolmay (2022-08-18T06:04:28Z)

python tf2-benchmarks.py --model resnet152 --batch_size 64 --num_gpus 1
Step 10, Images per second: 35.3 
Step 20, Images per second: 113.8 
Step 30, Images per second: 113.7 
Step 40, Images per second: 114.2 
Step 50, Images per second: 113.5 
Step 60, Images per second: 113.9 
Step 70, Images per second: 114.1 

python tf2-benchmarks.py --model resnet152 --batch_size 64 --xla --num_gpus 1
Step 10, Images per second: 9.4                                                                                                                                                                                                                                                           
Step 20, Images per second: 117.7                                                                                                                                                                                                                                                         
Step 30, Images per second: 117.8                                                                                                                                                                                                                                                         
Step 40, Images per second: 117.1 
Step 50, Images per second: 117.7 
Step 60, Images per second: 117.1 
Step 70, Images per second: 117.8

@ffleader1 Always fresh install for new ROCm version and never had compatibility issues, but i only do OpenCL and ML. Once you configure the software stack, freeze your kernel and ROCm versions.

---

### 评论 #10 — ffleader1 (2022-08-22T19:57:08Z)

> > If you have a toy example(cut&paste kind of deal) i could run it for you on 6800XT now and on 6950XT in couple of days, when they finish current task.
> > Found and running this project https://pypi.org/project/ai-benchmark/
> 
> I got these if you do not mind.
> 
> `pip install pytorch-benchmark`
> 
> ```
> import torch  
> from torchvision.models import efficientnet_b0, vit_l_16, densenet161, regnet_y_1_6gf
> from pytorch_benchmark import benchmark
> 
> model = efficientnet_b0()
> sample = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
> results = benchmark(model, sample, num_runs=10)
> 
> model2 =  densenet161()
> sample2 = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
> results2 = benchmark(model2, sample2, num_runs=10)
> 
> 
> model3 =  regnet_y_1_6gf()
> sample3 = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
> results3 = benchmark(model3, sample3, num_runs=10)
> ```
> 
> For reference, I got 3.22s/it for efficientnet_b0; 29.59s/it for densenet161; and 4.97s/it for regnet_y_1_6gf on Colab K80.

I bought a Biostar Rx 6800, and for that benchmark, here is what I got for batchsize 64(same batch size as for Colab K80, used for future reference):
- efficientnet_b0: 1.30s/it
- densenet_161: 7.09s/it
- regnet_y_1_6gf: 1.76s/it 

---

### 评论 #11 — ffleader1 (2022-08-23T17:50:47Z)

> Alternatively you can also reproduce this https://github.com/aime-team/tf2-benchmarks Run command without XLA : python tf2-benchmarks.py --model resnet50 --batch_size 128 --num_gpus 1
> 
> Step 10, Images per second: 22.5 Step 20, Images per second: 238.8 Step 30, Images per second: 239.3 Step 40, Images per second: 239.1 Step 50, Images per second: 238.9 Step 60, Images per second: 239.1 Step 70, Images per second: 238.9
> 
> GPU was run on both tests how i always run it, fixed overclock at 2725 MHz, -100mV undervolt, power cap at 332W.
> 
> Run command with XLA enabled : python tf2-benchmarks.py --model resnet50 --xla --batch_size 128 --num_gpus 1 Step 10, Images per second: 45.0 Step 20, Images per second: 272.1 Step 30, Images per second: 271.9 Step 40, Images per second: 272.7 Step 50, Images per second: 271.9

Do I need to do anything to enable xla on tensorflow, because right now, running with xla on my machine yields this error: ````bitcode module not found at ./open.bc````

---

### 评论 #12 — YumingChang02 (2022-10-21T13:51:04Z)

> > > If you have a toy example(cut&paste kind of deal) i could run it for you on 6800XT now and on 6950XT in couple of days, when they finish current task.
> > > Found and running this project https://pypi.org/project/ai-benchmark/
> > 
> > 
> > I got these if you do not mind.
> > `pip install pytorch-benchmark`
> > ```
> > import torch  
> > from torchvision.models import efficientnet_b0, vit_l_16, densenet161, regnet_y_1_6gf
> > from pytorch_benchmark import benchmark
> > 
> > model = efficientnet_b0()
> > sample = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
> > results = benchmark(model, sample, num_runs=10)
> > 
> > model2 =  densenet161()
> > sample2 = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
> > results2 = benchmark(model2, sample2, num_runs=10)
> > 
> > 
> > model3 =  regnet_y_1_6gf()
> > sample3 = torch.randn(64, 3, 224, 224)  # (B, C, H, W)
> > results3 = benchmark(model3, sample3, num_runs=10)
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > For reference, I got 3.22s/it for efficientnet_b0; 29.59s/it for densenet161; and 4.97s/it for regnet_y_1_6gf on Colab K80.
> 
> I bought a Biostar Rx 6800, and for that benchmark, here is what I got for batchsize 64(same batch size as for Colab K80, used for future reference):
> 
>     * efficientnet_b0: 1.30s/it
> 
>     * densenet_161: 7.09s/it
> 
>     * regnet_y_1_6gf: 1.76s/it

I ran the python script with rocm/pytorch latest, setting globally HSA_OVERRIDE_GFX_VERSION=10.3.0 on msi rx6500xt
Measuring inference for batch_size=64  [00:06<00:00,  1.50it/s]
Measuring inference for batch_size=64  [00:32<00:00,  3.22s/it]
Measuring inference for batch_size=64  [00:07<00:00,  1.32it/s]
( My findings are RDNA2 with pytorch have really long initials, running the attached script now goes through a "warmup" session, which may improve average time significantly. This makes me thinking of buying a bunch of rx6600 ( Non XT )s for machine learning farm? )
[ 1950x + 16G 2666 RAM*4 ] 

---

### 评论 #13 — Rabcor (2024-04-17T07:10:22Z)

I don't think that card even supports rocm 
![image](https://github.com/ROCm/ROCm/assets/5684325/cbd4e0f8-91a6-454f-b857-5cc0518c5a80)

I mean either it does not, or the official docs are wrong.

---

### 评论 #14 — ppanchad-amd (2024-05-09T15:29:48Z)

@ffleader1 This GPU is not supported with the latest ROCm 6.1.0. Thanks!

---

### 评论 #15 — Rabcor (2024-05-10T06:27:21Z)

I think u shuold maybe be able to use ROCR though.

---

### 评论 #16 — toel1234 (2024-06-02T21:13:26Z)

I have the RX 6800 XT and ROCm 6.0.0 is running smoothly.

---

### 评论 #17 — rzalawad (2024-12-28T19:07:25Z)

@aoolmay
Hello, thank you for posting the benchmarks. Any chance you could run the following on your 6800xt?
It is a pytorch only script to train a dummy transformer network. I believe this will give useful data because
1. I can run on a 3090 and share the results with amp and without and with different precision modes and share the data
2. We will see how well ROCm integrates with newer layers such as SelfAttention, etc which have different bottlenecks compared to Conv layers in ResNet architectures.

<summary>

<details>

```python
import torch
import time
from torch import nn
from torch.optim import Adam
from torch.nn.functional import cross_entropy
from torch.amp import GradScaler, autocast


# Define a simple Transformer model
class SimpleTransformer(nn.Module):
    def __init__(
        self, vocab_size=5000, embed_dim=768, nhead=12, num_layers=12, dim_feedforward=3072
    ):
        super(SimpleTransformer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.transformer = nn.Transformer(
            d_model=embed_dim,
            nhead=nhead,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dim_feedforward=dim_feedforward,
        )
        self.fc = nn.Linear(embed_dim, vocab_size)

    def forward(self, src, tgt):
        src = self.embedding(src)
        tgt = self.embedding(tgt)
        output = self.transformer(src, tgt)
        return self.fc(output)


# Check for GPU
device = torch.device(
    "cuda" if torch.cuda.is_available() else "rocm" if torch.backends.mps.is_available() else "cpu"
)
print(f"Using device: {device}")

# User-specified precision
precision = "mixed"  # Change to "fp32" for full precision

# Hyperparameters
vocab_size = 5000
embed_dim = 768
seq_length = 1024
batch_size = 2

# Initialize model, optimizer, and data
model = SimpleTransformer(vocab_size, embed_dim).to(device)
optimizer = Adam(model.parameters(), lr=1e-3)
scaler = torch.cuda.amp.GradScaler() if precision == "mixed" and device.type == "cuda" else None

src = torch.randint(0, vocab_size, (seq_length, batch_size)).to(device)  # Fake source sequence
tgt = torch.randint(0, vocab_size, (seq_length, batch_size)).to(device)  # Fake target sequence
tgt_labels = torch.randint(0, vocab_size, (seq_length, batch_size)).to(device)  # Fake target labels

# Training loop for 100 steps
start_time = time.time()
model.train()
for step in range(100):
    optimizer.zero_grad()
    if precision == "mixed" and device.type == "cuda":
        with autocast(device_type="cuda"):
            output = model(src, tgt)
            loss = cross_entropy(output.view(-1, vocab_size), tgt_labels.view(-1))
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
    else:  # Full precision (fp32)
        output = model(src, tgt)
        loss = cross_entropy(output.view(-1, vocab_size), tgt_labels.view(-1))
        loss.backward()
        optimizer.step()

    if (step + 1) % 10 == 0:
        print(f"Step {step + 1}: Loss = {loss.item():.4f}")
end_time = time.time()

# Print training time
print(f"Training time for 100 steps: {end_time - start_time:.2f} seconds")

```

</details>

</summary>


---
