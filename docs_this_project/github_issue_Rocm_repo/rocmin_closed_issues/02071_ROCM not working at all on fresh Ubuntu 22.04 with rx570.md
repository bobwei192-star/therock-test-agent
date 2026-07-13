# ROCM not working at all on fresh Ubuntu 22.04 with rx570

- **Issue #:** 2071
- **State:** closed
- **Created:** 2023-04-21T15:55:44Z
- **Updated:** 2023-04-22T03:30:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/2071

Hi! I spent multiple days in trying to install ROCm on my Mint 21, based on Ubuntu 22, but got zero result.

I tried to install different versions with different ways; tried to install even ROCm 4.3.1, which should work on my GPU, but no; with dkms and without; downgraded kernels min to 5.14.0. It was no success for me to install ROCm 3.5.1, because it not building, and also old kernel not loading. I tried to install legacy opencl, but it not installing.

Today I installed fresh Ubuntu 22.04 to check it is just my OS or really ROCm not working. I installed ROCm 5.4.3 and it gave me same results - just no GPU agent in rocminfo and no devices in clinfo. 

GPU: XFX rx570 8gb
Ubuntu clinfo & rocminfo output: [info.log](https://github.com/RadeonOpenCompute/ROCm/files/11297349/info.log)
