# [Question] hipDeviceProp' major/minor for AMD GPUs

- **Issue #:** 1907
- **State:** closed
- **Created:** 2023-02-13T20:07:39Z
- **Updated:** 2024-03-31T14:09:40Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/1907

Hi, 

I have 2 GPUs: GTX 1650 (Nvidia, Turing arch) and RX 5500 XT (AMD, gfx1012) + rocm 4.5.0.

If i start the program with Nvidia GPU and populate hipDeviceProp_t, i get major & minor compute capability = 7 and 5 accordingly (in total -> 7.5), and that's completely [fine](https://forums.developer.nvidia.com/t/cuda-enabled-geforce-1650/81010#:~:text=The%20GTX%201650%20is%20based,able%20to%20run%20those%20frameworks.).

if start the same program with Radeon, i get 10 & 1 -> 10.1. 

What do the values of major/minor attributes in hipDeviceProp_t mean for AMD GPUs? 

`RX 5500 XT has compute capability of about 10.1`?
