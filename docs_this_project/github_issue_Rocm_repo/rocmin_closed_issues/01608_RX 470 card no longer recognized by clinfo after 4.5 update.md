# RX 470 card no longer recognized by clinfo after 4.5 update

- **Issue #:** 1608
- **State:** closed
- **Created:** 2021-11-03T14:39:27Z
- **Updated:** 2022-09-17T04:29:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1608

Card was working fine with 4.3.

I uninstalled my previous version (4.3) and installed 4.5.

output from `/opt/rocm/opencl/bin/clinfo` :

```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.2 AMD-APP (3361.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```

output from `rocminfo`

```
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1143
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

output from `rocm-smi`

```
======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr   SCLK     MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
0    47.0c  23.116W  1169Mhz  300Mhz  19.22%  auto  92.0W    16%   0%    
================================================================================
============================= End of ROCm SMI Log ==============================
```