# E: Unable to locate package rocm-dkms Ubuntu 18.04

- **Issue #:** 1234
- **State:** closed
- **Created:** 2020-09-22T22:57:17Z
- **Updated:** 2020-09-22T23:50:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/1234

Following these instructions and getting errors - https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu

tried updating 

sudo nano /etc/apt/sources.list.d/rocm.list 

to 

deb [arch=amd64] http://repo.radeon.com/rocm/apt/3.5.1 xenial main

That didnt help

GPU is rx470

uname -sr
Linux 4.15.0-118-generic

 dmesg | grep kfd
[    5.422782] kfd kfd: Initialized module
[    6.243361] amdgpu 0000:01:00.0: kfd not supported on this ASIC


