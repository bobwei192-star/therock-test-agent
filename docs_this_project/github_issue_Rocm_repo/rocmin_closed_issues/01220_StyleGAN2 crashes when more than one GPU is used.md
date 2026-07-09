# StyleGAN2 crashes when more than one GPU is used

- **Issue #:** 1220
- **State:** closed
- **Created:** 2020-09-16T03:35:07Z
- **Updated:** 2021-05-20T08:38:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/1220

CPU:Ryzen 1700
GPU: 2xVega 56
kernel: 5.4.0-47-generic #51-Ubuntu
ubuntu: 20.04
rocm: 3.7-20

StyleGAN2 repository
https://github.com/NVlabs/stylegan2

when it tries to do a second time of the .run method it throws this error at https://github.com/NVlabs/stylegan2/blob/master/training/training_loop.py#L299, without any kind of python error.

```
:0:rocdevice.cpp            :2159: 12230237400 us: Device::callbackQueue aborting with status: 0x29
Aborted (core dumped)
```
and adjusting the mini-batch to 8 making the round have len(round)=1, throws this:

```
Memory access fault by GPU node-1 (Agent handle: 0x55cf3f329fa0) on address 0x8000000000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```
this algorithm is used as the backbone for generation/translation/editing of other repositories so is kind of bad not being able to train it with multi-GPU

https://github.com/l4rz/practical-aspects-of-stylegan2-training, replacing all the `impl=cuda` with `impl=ref`, makes StyleGAN2 work, but again without being able to use multiGPU, in this case with a Radeon Pro Duo 2x4Gb.
