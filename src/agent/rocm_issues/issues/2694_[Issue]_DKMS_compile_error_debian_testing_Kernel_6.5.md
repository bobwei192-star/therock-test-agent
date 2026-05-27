# [Issue]:  DKMS compile error debian testing Kernel 6.5

> **Issue #2694**
> **状态**: closed
> **创建时间**: 2023-12-06T21:42:24Z
> **更新时间**: 2024-06-19T17:17:54Z
> **关闭时间**: 2024-06-19T17:17:54Z
> **作者**: ithuis
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2694

## 描述

### Problem Description

i am trying to install drivers via

amdgpu-install --no-32 


then i get the compile error 

DKMS make.log for amdgpu-6.2.4-1646729.22.04 for kernel 6.5.0-5-amd64 (amd64)
wo  6 dec 2023 22:36:56 CET
make: Map '/usr/src/linux-headers-6.5.0-5-amd64' wordt binnengegaan
/var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/Makefile:52: *** dma_resv->seq is missing. exit....  Gestopt.
make[1]: *** [/usr/src/linux-headers-6.5.0-5-common/Makefile:2059: /var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build] Fout 2
make: *** [/usr/src/linux-headers-6.5.0-5-common/Makefile:246: __sub-make] Fout 2
make: Map '/usr/src/linux-headers-6.5.0-5-amd64' wordt verlaten


### Operating System

Debian testing

### CPU

AMD Ryzen 7 PRO 7840U w/ Radeon 780M Graphics

### GPU

AMD Ryzen 7 PRO 7840U w/ Radeon 780M Graphics

### ROCm Version

5.7.0

### ROCm Component

_No response_

### Steps to Reproduce

amdgp-install --no-32

### Output of /opt/rocm/bin/rocminfo --support

ROCk module is NOT loaded, possibly no GPU devices
