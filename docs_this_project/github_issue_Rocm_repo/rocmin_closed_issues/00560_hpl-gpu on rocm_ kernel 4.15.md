# hpl-gpu on rocm, kernel 4.15

- **Issue #:** 560
- **State:** closed
- **Created:** 2018-09-27T10:44:10Z
- **Updated:** 2018-09-27T16:04:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/560

Hello!
I am trying to run hpl-gpu (https://github.com/davidrohr/hpl-gpu/wiki) on rocm (v 1.9-211) on 4.15.3 linux kernel.  But it says "No CPU OpenCL device found for mapping buffers". I have Intel Xeon E5 v3 series CPU and instinct-mi25 GPU, rocm v1.9-211, rocm-opencl v1.2.0-2018090737
clinfo shows only AMD GPU device, no CPU devices. 
Please, help me to solve the problem