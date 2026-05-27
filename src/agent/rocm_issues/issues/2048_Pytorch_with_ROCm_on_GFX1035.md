# Pytorch with ROCm on GFX1035?

> **Issue #2048**
> **状态**: closed
> **创建时间**: 2023-04-14T14:34:35Z
> **更新时间**: 2024-07-09T19:35:15Z
> **关闭时间**: 2024-07-09T19:28:27Z
> **作者**: Jonezia
> **标签**: application:pytorch
> **URL**: https://github.com/ROCm/ROCm/issues/2048

## 标签

- **application:pytorch** (颜色: #bfdadc)

## 描述

Hi,

I'm attempting to get Pytorch to work with ROCm on GFX1035 (AMD Ryzen 7 PRO 6850U with Radeon Graphics). I know GFX1035 is technically not supported, but it shares an instruction set with GFX1030 and others have had success building for GFX1031 and GFX1032 by setting HSA_OVERRIDE_GFX_VERSION=10.3.0.

I have ROCm setup, with rocminfo correctly displaying my GPU. Running "torch.cuda.is_available()" returns true. I am able to run sample neural networks on the CPU perfectly fine, and I have tested training on MNIST as well as inference on Resnet50. However, if I try and run the same code on the GPU it produces bizarre and incorrect results like producing labels indices that are negative and negative probabilities etc. I am able to run simple pytorch programs like sending two matrices to the gpu and multiplying them works correctly. However, with this setup even a simple neural network with one linear layer doesn't work.

Current setup:
Ubuntu 22.04.1 with kernel 5.15.0-43 generic
Python 3.9
ROCm 5.4.2 
Pytorch for ROCm 5.4.2 (bare metal)
I then run programs with HSA_OVERRIDE_GFX_VERSION=10.3.0
This is following someone's setup for GFX1032 that worked.

I have also tried Ubuntu 22.04.2 with kernel 5.17 OEM and Python3.10. This also produced wrong results on the Resnet50 too (but different), but I was even able to run a simple neural network of 2 linear layers, ReLU, and Sigmoid with this setup.

I was wondering if anybody has had any success with getting Pytorch to work with ROCm on GFX1035 and can share their setup or any help with this. I hope there is a setup that works if I can find it. 

Thanks for any help

---

## 评论 (5 条)

### 评论 #1 — FNsi (2023-04-21T12:50:39Z)

Check the data type? 
I think Fp16 or so called half are not working with gfx1035 in some circumstances

---

### 评论 #2 — Jonezia (2023-04-25T09:48:22Z)

The data type is float32

---

### 评论 #3 — hongxiayang (2023-12-04T19:12:45Z)

@Jonezia You might have PCIe atomics support issue. Can you run this test in your pytorch env:

```
python -c "import torch; x = torch.ones(1,2).cuda(); print(x); print('sum {}'.format(torch.sum(x)))"
```
Expected output is 2. If not, let me know what you see and please you check this https://github.com/pytorch/pytorch/issues/103973 for reference to understand this problem.



---

### 评论 #4 — ppanchad-amd (2024-05-10T18:54:20Z)

@Jonezia Can you please test with latest ROCm 6.1.1? If resolved, please close the ticket. Thanks!

---

### 评论 #5 — harkgill-amd (2024-07-09T19:28:27Z)

Hi @Jonezia, I will close this ticket for now. 

If you still see this issue after following the instructions on [Installing PyTorch on ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/3rd-party/pytorch-install.html), please give the suggestion by @hongxiayang a try and reopen the issue. Thanks!

---
