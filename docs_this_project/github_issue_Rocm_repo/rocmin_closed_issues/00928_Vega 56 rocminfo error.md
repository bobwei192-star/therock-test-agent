# Vega 56 rocminfo error

- **Issue #:** 928
- **State:** closed
- **Created:** 2019-11-03T11:14:29Z
- **Updated:** 2022-01-28T06:30:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/928

Hi, 

I just installed ROCm following the repo readme on an ubuntu 18.04 install. One I run rocminfo I get the following error:

`ROCk module is loaded
jugu is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.`

And trying to run clinfo I get the following:

`Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)`

Even though the error is about the device ID I can see the GPU on rocm-smi.

Any info on how to debug the issue? I'm on Ubuntu 18.04, fresh install and updated, upstream kernel, Vega 65, ryzen 1400 and gigabyte aorus wifi