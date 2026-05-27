#  Installation fails under SUSE Linux Enterprise Server 15

> **Issue #1999**
> **状态**: closed
> **创建时间**: 2023-03-29T12:13:56Z
> **更新时间**: 2024-03-09T01:49:11Z
> **关闭时间**: 2024-03-09T01:49:11Z
> **作者**: MathiasMagnus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1999

## 描述

On a fresh install of SUSE Linux Enterprise Server 15 SP4, I get the following error after registering the appropriate repos and trying to install:
```
mate@MATTY-GA402RK:~> sudo zypper install amdgpu-dkms rocm-hip-libraries
Loading repository data...
Reading installed packages...
Resolving package dependencies...
2 Problems:
Problem: nothing provides 'gcc' needed by the to be installed amdgpu-dkms-1:5.18.13.50400-1510348.noarch
Problem: nothing provides 'libLLVM7 >= 7.0.1' needed by the to be installed rocblas-2.46.0.50400-sles153.72.x86_64

Problem: nothing provides 'gcc' needed by the to be installed amdgpu-dkms-1:5.18.13.50400-1510348.noarch
 Solution 1: do not install amdgpu-dkms-1:5.18.13.50400-1510348.noarch
 Solution 2: break amdgpu-dkms-1:5.18.13.50400-1510348.noarch by ignoring some of its dependencies
```
