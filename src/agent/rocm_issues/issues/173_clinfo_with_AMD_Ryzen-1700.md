# clinfo with AMD Ryzen-1700 

> **Issue #173**
> **状态**: closed
> **创建时间**: 2017-07-29T06:24:34Z
> **更新时间**: 2017-07-29T08:38:05Z
> **关闭时间**: 2017-07-29T08:38:05Z
> **作者**: skn123
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/173

## 描述

a.) Installed Ubuntu 16.04.2 LTS vanilla
b.) Installed rocm as described on the webpage
c.) Rebooted.
d.) GPU is being detected correctly !!!
e.) CPU is not showing up????!!!!!

What needs to be done to solve this problem?

Configuration:
AMD RYZEN 1700
AMD Radeon RX460

Output from clinfo
``Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (2450.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Device 67ef
  Device Topology:				 PCI[ B#34, D#0, F#0 ]
  Max compute units:				 14
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1250Mhz
  Address bits:					 64
  Max memory allocation:			 3221225472
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26607
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 4294967296
  Constant buffer size:				 3221225472
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 3221225472
  Max global variable preferred total size:	 4294967296
  Max read/write image args:			 64
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7f731067b598
  Name:						 gfx803
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 1.1 (HSA,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 
``

---

## 评论 (4 条)

### 评论 #1 — ekondis (2017-07-29T07:13:47Z)

That's normal. Currently there is not a CPU OpenCL runtime.

---

### 评论 #2 — skn123 (2017-07-29T07:30:06Z)

I noticed this behavior when I had to install OpenCL runtime for Intel + NVidia. Is there something I can do to enable OpenCL runtime for CPU also? It does say on the webpage that AMD Ryzen is supported

---

### 评论 #3 — ekondis (2017-07-29T07:53:46Z)

Ryzen is supported from the point of view that it allows GPUs to work under ROCm.
If you want a CPU OpenCL runtime you should additionally install a third party one (e.g. POCL).

---

### 评论 #4 — skn123 (2017-07-29T08:18:19Z)

yup what i did after i saw your first post. you can close this thread

---
