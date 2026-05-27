# amdkfd driver not loaded

> **Issue #444**
> **状态**: closed
> **创建时间**: 2018-06-27T09:06:21Z
> **更新时间**: 2018-06-27T11:11:00Z
> **关闭时间**: 2018-06-27T11:11:00Z
> **作者**: vertering
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/444

## 描述

Hi,

Using a  fresh install of Ubuntu 16.04 on a Dell Latitude e6540 with a HD Radeon 8790M. Installation goes fine, but running /opt/rocm/bin/rocminfo returns the famous 

> hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

So I started troubleshooting. /opt/rocm/opencl/bin/x86_64/clinfo produces

> Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.2 LINUX
  Platform Name:				 Intel(R) OpenCL
  Platform Vendor:				 Intel(R) Corporation
  Platform Extensions:				 cl_khr_icd cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_depth_images cl_khr_3d_image_writes cl_intel_exec_by_local_thread cl_khr_spir cl_khr_fp64 


>  Platform Name:				 Intel(R) OpenCL
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_CPU
  Vendor ID:					 8086h
  Max compute units:				 8
  Max work items dimensions:			 3
    Max work items[0]:				 8192
    Max work items[1]:				 8192
    Max work items[2]:				 8192
  Max work group size:				 8192
  Preferred vector width char:			 1
  Preferred vector width short:			 1
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 32
  Native vector width short:			 16
  Native vector width int:			 8
  Native vector width long:			 4
  Native vector width float:			 8
  Native vector width double:			 4
  Max clock frequency:				 2700Mhz
  Address bits:					 64
  Max memory allocation:			 4180098048
  Image support:				 Yes
  Max number of images read arguments:		 480
  Max number of images write arguments:		 480
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 480
  Max size of kernel argument:			 3840
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 No
    Round to +ve and infinity:			 No
    IEEE754-2008 fused multiply-add:		 No
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 262144
  Global memory size:				 16720392192
  Constant buffer size:				 131072
  Max number of constant args:			 480
  Local memory type:				 Global
  Local memory size:				 32768
  Kernel Preferred work group size multiple:	 128
  Error correction support:			 0
  Unified memory for Host and Device:		 1
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 Yes
  Queue on Host properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x166b950
  Name:						 Intel(R) Core(TM) i7-4800MQ CPU @ 2.70GHz
  Vendor:					 Intel(R) Corporation
  Device OpenCL C version:			 OpenCL C 1.2 
  Driver version:				 1.2.0.25
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 (Build 25)
  Extensions:					 cl_khr_icd cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_depth_images cl_khr_3d_image_writes cl_intel_exec_by_local_thread cl_khr_spir cl_khr_fp64 

dmesg | grep amdgpu produces:

>[    0.922697] [drm] amdgpu kernel modesetting enabled.
[    0.926624] amdgpu 0000:01:00.0: enabling device (0000 -> 0003)
[    0.926736] amdgpu 0000:01:00.0: SI support provided by radeon.
[    0.926737] amdgpu 0000:01:00.0: Use radeon.si_support=0 amdgpu.si_support=1 to override.

lsmod | grep kfd produces:

> amdkfd                188416  1
amd_iommu_v2           20480  1 amdkfd

dmesg | grep amdkfd however doesn't yield any results. So it seems the driver is not correctly loaded?  How can I fix this? 




---

## 评论 (1 条)

### 评论 #1 — gstoner (2018-06-27T11:11:00Z)

This is operator error since this GPU is not supported by ROCm it needs to be a GFX8. or GFX9 based GPU.   

---
