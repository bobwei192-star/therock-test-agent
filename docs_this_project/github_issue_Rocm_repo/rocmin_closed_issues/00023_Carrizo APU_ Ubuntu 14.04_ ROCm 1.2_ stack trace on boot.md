# Carrizo APU, Ubuntu 14.04, ROCm 1.2, stack trace on boot

- **Issue #:** 23
- **State:** closed
- **Created:** 2016-08-17T18:34:51Z
- **Updated:** 2016-08-22T17:55:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/23

Hello,

I updated ROCm from 1.1.1 to version 1.2 and upon reboot I get a stack trace which hangs the boot sequence.
A fresh install of Ubuntu did nothing to solve this so it should easily be reproducible, at least on a Aspire E15 with a FX-8800P processor.

I would love to be able to paste the stack trace in this thread but kern.log doesn't show anything related to the 4.4.0-kfd-compute-rocm-rel-1.2-31 kernel and would gladly follow any directions as to provide any additional information. I do have a picture of it below which hopefully will get the idea across.

Would it be possible, as a fast recovery option, to provide ROCm version 1.1 through the apt-get server ?

![img_1211](https://cloud.githubusercontent.com/assets/4035760/17748327/bf54c04c-64b0-11e6-8e87-0b633a3dac20.JPG)
