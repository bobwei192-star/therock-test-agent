# Pytorch + ROCm Stuck

- **Issue #:** 2227
- **State:** closed
- **Created:** 2023-06-08T05:43:46Z
- **Updated:** 2023-10-07T16:29:23Z
- **Labels:** application:pytorch
- **URL:** https://github.com/ROCm/ROCm/issues/2227

I am trying to run Pytorch on my Provii and RX6300, the environment is:

OS: Ubuntu 20.04.6

Torch: 2.0.1 + ROCm-5.4.2

ROCm: 5.4.5

 

But when I used any operations related to GPU, like tensor.cuda(), the Provii will just stuck and RX6300 will return Segmentation Fault. That is, the pytorch with rocm did not work at all.

 

I have tried different OS (22.04) and ROCm(5.4.2), docker version torch, host version ... They all did not works... What can I try? I guess the problem may come from the driver?

 

Thanks in advance!