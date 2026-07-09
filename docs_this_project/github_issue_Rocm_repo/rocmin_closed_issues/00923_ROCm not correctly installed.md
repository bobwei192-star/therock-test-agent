# ROCm not correctly installed

- **Issue #:** 923
- **State:** closed
- **Created:** 2019-10-26T13:18:01Z
- **Updated:** 2023-12-18T17:16:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/923

Hi all. First time posting. I'm new to Linux so I'm endeavoring to tackle the hail of problems I'm getting. I'm aware I may be or have been doing something wrong, or extremely dumb, so that's why I'm here. I wanted to see if ROCm was successfully installed (below you'll see what I did to do so) by running the following commands expecting my GPU to be listed, but I get the following:

```
root@slack:~# /opt/rocm/bin/rocminfo 
ROCk module is loaded
root is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
`
and (I think there's no problem with this one, although at the very bottom there's something wrong):
root@slack:~# /opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:				 2
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.2 pocl 1.3 None+Asserts, LLVM 8.0.1, SLEEF, DISTRO, POCL_DEBUG
  Platform Name:				 Portable Computing Language
  Platform Vendor:				 The pocl project
  Platform Extensions:				 cl_khr_icd
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 Portable Computing Language
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_CPU
  Vendor ID:					 6c636f70h
  Max compute units:				 2
  Max work items dimensions:			 3
    Max work items[0]:				 4096
    Max work items[1]:				 4096
    Max work items[2]:				 4096
  Max work group size:				 4096
  Preferred vector width char:			 16
  Preferred vector width short:			 16
  Preferred vector width int:			 8
  Preferred vector width long:			 4
  Preferred vector width float:			 8
  Preferred vector width double:		 4
  Native vector width char:			 16
  Native vector width short:			 16
  Native vector width int:			 8
  Native vector width long:			 4
  Native vector width float:			 8
  Native vector width double:			 4
  Max clock frequency:				 1350Mhz
  Address bits:					 64
  Max memory allocation:			 1073741824
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 128
  Max image 2D width:				 8192
  Max image 2D height:				 8192
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 16
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 No
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 1048576
  Global memory size:				 2675807232
  Constant buffer size:				 524288
  Max number of constant args:			 8
  Local memory type:				 Global
  Local memory size:				 524288
  Kernel Preferred work group size multiple:	 8
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
    Out-of-Order:				 No
    Profiling :					 Yes
  Platform ID:					 0x7f119e1a3020
  Name:						 pthread-AMD E1-6010 APU with AMD Radeon R2 Graphics
  Vendor:					 AuthenticAMD
  Device OpenCL C version:			 OpenCL C 1.2 pocl
  Driver version:				 1.3
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 pocl HSTR: pthread-x86_64-pc-linux-gnu-btver2
  Extensions:					 cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_3d_image_writes cl_khr_fp64 cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

Kernel version:
`root@slack:~# uname -r
5.2.0-kali3-amd64` 

Hoping that I did right and that it will suffice, what I did to install ROCm, since my kernel version is 5.2.0 and AMD’s `rock-dkms` package doesn't offer at the moment a kernel driver supported on kernels above 4.18, I installed the upstream kernel driver by going directly to `rocm-dev`, as explained on https://rocm.github.io/ROCmInstall.html.

What can I do or undo to solve this? I'm aiming to run a program that requires ROCm and for the moment it's performing the same as it was before installing ROCm, which means it's not been properly installed. I don't know what else I need to provide in order for you to know what to do.

Thank you. 