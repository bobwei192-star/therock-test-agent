# Training causes GPU hang after a few seconds with ROCm 2.0

- **Issue #:** 665
- **State:** closed
- **Created:** 2019-01-08T00:19:50Z
- **Updated:** 2019-01-08T02:41:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/665

When trying to train a GAN using the following Tensorflow implementation of SAGAN:
https://github.com/taki0112/Self-Attention-GAN-Tensorflow

the system locks up every time after the script has run for a few seconds.
I'm using Linux Mint 19, 4.15 kernel and a RX 470 card.

Command line used for the script:
python3 main.py --phase train --dataset celebA --gan_type hinge --batch_size=1 --img_size=128



[stderr.txt](https://github.com/RadeonOpenCompute/ROCm/files/2734745/stderr.txt)
[kernel.log](https://github.com/RadeonOpenCompute/ROCm/files/2734754/kernel.log)
