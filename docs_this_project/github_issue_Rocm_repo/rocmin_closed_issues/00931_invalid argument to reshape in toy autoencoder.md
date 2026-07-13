# invalid argument to reshape in toy autoencoder

- **Issue #:** 931
- **State:** closed
- **Created:** 2019-11-08T06:14:48Z
- **Updated:** 2019-11-13T21:00:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/931

Summary of your hardware:
CPU: Ryzen 7 1700x
GPU: Radeon RX Vega 64
Motherboard: ASRock X370 Gaming X

PCIe Information: output of lshw attached

Something is throwing up InvalidArgumentError at a random point during training.

I built a toy autoencoder using keras; at a random point during training, it dies with an error.  My code is never using tf.reshape, so presumably this is something internal.

The failure happens at a random point several epochs in; it's failed as early as the 7th epoc, and its failed after the 100th.

I have attached a minimal program that reproduces the bug, and sample output.

[random crash.py.txt](https://github.com/RadeonOpenCompute/ROCm/files/3823173/random.crash.py.txt)
[error snipped.txt](https://github.com/RadeonOpenCompute/ROCm/files/3823178/error.snipped.txt)

