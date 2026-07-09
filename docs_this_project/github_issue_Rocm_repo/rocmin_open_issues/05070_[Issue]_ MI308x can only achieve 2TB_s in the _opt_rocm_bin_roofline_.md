# [Issue]: MI308x can only achieve 2TB/s in the /opt/rocm/bin/roofline*

- **Issue #:** 5070
- **State:** open
- **Created:** 2025-07-21T01:43:44Z
- **Updated:** 2025-07-23T01:53:39Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5070

### Problem Description

We tests our HPC program, which computing density is 0.5/1.0 FLOPS/Byte in double/single precision, the speed of it is limited by the memory bandwidth of HBM. 
For the MI308x, which we have tried three different rocm, 2 different operating system, it always shows 2TB/s in the /opt/rocm/bin/roofline* tests. For the MI300x, it gives 4.2TB/s, the memory bandwidth should not decrease from MI300x to MI308x. 
The speed of our program runs on MI300x is like 3 times faster than MI308x. I doubt it caused by the rocm is not very fit the MI308x, or it has some bugs for MI308x. 

### Operating System

Ubuntu 22.04.5 LTS and Rocky-9.5

### CPU

AMD EPYC 9654

### GPU

AMD instinct MI308x

### ROCm Version

Rocm-7.0.0, Rocm-6.4.1, Rocm-6.3.3

### ROCm Component

HIPCC

### Steps to Reproduce

<img width="973" height="627" alt="Image" src="https://github.com/user-attachments/assets/5bea4566-0f74-422f-bdac-82a056413b08" />

<img width="992" height="595" alt="Image" src="https://github.com/user-attachments/assets/c207403c-aecf-4806-9b0f-d1037f7c2677" />

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_