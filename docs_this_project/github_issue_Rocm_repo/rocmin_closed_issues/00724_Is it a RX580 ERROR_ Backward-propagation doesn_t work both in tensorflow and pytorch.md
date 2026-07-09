# Is it a RX580 ERROR? Backward-propagation doesn't work both in tensorflow and pytorch.

- **Issue #:** 724
- **State:** closed
- **Created:** 2019-03-04T14:43:36Z
- **Updated:** 2019-03-04T15:24:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/724

Recently I use tensorflow-rocm to train my model, but the result is wrong while the same code work well in another CUDA computer.

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/337

 And some guys who use pytorch-rocm meet the same problem: his code doesn't work on rx580, but works well in pytorch-rocm developer's gfx900 architecture.

https://github.com/ROCmSoftwarePlatform/pytorch/issues/342
