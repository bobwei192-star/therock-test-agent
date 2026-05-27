# OpenCL alongside ROCm?

> **Issue #12**
> **状态**: closed
> **创建时间**: 2016-05-18T08:14:54Z
> **更新时间**: 2016-05-19T19:26:44Z
> **关闭时间**: 2016-05-19T14:18:46Z
> **作者**: psteinb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/12

## 描述

Hi - I was wondering how to have OpenCL available on a rocm enabled kernel with ubuntu 14.04.4. I followed the installation instructions in this repo and installed the opencl icd through `ocl-icd-opencl-dev` but clinfo just prints:

```
$ clinfo
I: ICD loader reports no usable platforms
```

whereas lspci correctly reports the GPU(s):

```
$ lspci -v |grep "VGA controller"
02:00.0 VGA compatible controller: NVIDIA Corporation GF119 [NVS 310] (rev a1) (prog-if 00 [VGA controller])
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca) (prog-if 00 [VGA controller])
```

but rocm-smi also chokes a bit:

```
$ sudo /opt/rocm/bin/rocm-smi -a


===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]          : Temperature: 38.0c
GPU[1]          : Unable to display temperature
============================================================================
============================================================================
GPU[0]          : GPU Clock Level: 0 (300Mhz)
GPU[0]          : GPU Memory Clock Level: 0 (500Mhz)
GPU[1]          : PowerPlay not enabled - Cannot display clocks
============================================================================
============================================================================
GPU[0]          : Fan Level: 48 (18.82)%
GPU[1]          : PowerPlay not enabled - Cannot display fan speed
============================================================================
============================================================================
GPU[0]          : Current PowerPlay Level: auto
GPU[1]          : PowerPlay not enabled - Cannot display Performance Level
============================================================================
============================================================================
GPU[0]          : Supported GPU clock frequencies on GPU0
GPU[0]          : 0: 300Mhz *
GPU[0]          : 1: 508Mhz 
GPU[0]          : 2: 717Mhz 
GPU[0]          : 3: 874Mhz 
GPU[0]          : 4: 911Mhz 
GPU[0]          : 5: 944Mhz 
GPU[0]          : 6: 974Mhz 
GPU[0]          : 7: 1000Mhz 
GPU[0]          : 
GPU[0]          : Supported GPU Memory clock frequencies on GPU0
GPU[0]          : 0: 500Mhz *
GPU[0]          : 
GPU[1]          : PowerPlay not enabled - Cannot display clocks
============================================================================
===================          End of ROCm SMI Log         ===================
```

Any hint would be appreciated.
P


---

## 评论 (3 条)

### 评论 #1 — psteinb (2016-05-19T11:41:02Z)

I just had another unsuccessful stab at it, I installed the AMDAPPSDK 3.0 for 64bit Linux. I exported PATH and LD_LIBRARY_PATH according to the contents of `/opt/AMDAPPSDK-3.0`. The shipped clinfo gave similar results to the above:

```
$ clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

I suspect the driver to be the problem, should I try to install AMD GPU Pro? Will that work with a ROCm system?


---

### 评论 #2 — jedwards-AMD (2016-05-19T14:18:46Z)

OpenCL is not supported on the ROCm stack using the AMDAPPSDK of any version.

The OpenCL library provided in the AMDAPPSDK 3.0 is not compatible with the ROCm drivers. You need the Catalyst drivers to be installed for OpenCL to work. In fact, the OpenCL runtime libraries that support Catalyst are provided when the Catalyst drivers are installed; the versions provided in the AMDAPPSDK 3.0 are stub libraries that can only be used to link applications.


---

### 评论 #3 — psteinb (2016-05-19T19:26:44Z)

Thanks for setting this clear.


---
