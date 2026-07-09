# GPU not working with rocm-5.2.1

- **Issue #:** 1812
- **State:** closed
- **Created:** 2022-09-23T18:21:21Z
- **Updated:** 2023-12-27T17:17:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1812

I have setup the MI 100 on ubuntu 20.04.5 with kernel version with 5.13.0-35-generic. I installed the rocm-5.2.1 version. But there was something strange which I observed.  The GPU is detected (I used rocm-smi) to check that

But there was another issue. 

1. The hip sample programs are getting compiled but when I am executing them, There GPU is not executing them. I was getting issues that the GPU was not detected. 
2. The code skips the section which has to be executed by the gpu. 

 

Hoping to hear from you soon