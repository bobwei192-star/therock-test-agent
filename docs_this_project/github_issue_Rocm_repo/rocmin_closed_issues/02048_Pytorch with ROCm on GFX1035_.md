# Pytorch with ROCm on GFX1035?

- **Issue #:** 2048
- **State:** closed
- **Created:** 2023-04-14T14:34:35Z
- **Updated:** 2024-07-09T19:35:15Z
- **Labels:** application:pytorch
- **URL:** https://github.com/ROCm/ROCm/issues/2048

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