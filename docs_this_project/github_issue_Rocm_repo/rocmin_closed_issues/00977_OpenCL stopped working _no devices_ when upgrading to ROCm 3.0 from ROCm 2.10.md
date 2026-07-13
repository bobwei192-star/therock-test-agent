# OpenCL stopped working "no devices" when upgrading to ROCm 3.0 from ROCm 2.10

- **Issue #:** 977
- **State:** closed
- **Created:** 2019-12-20T13:49:13Z
- **Updated:** 2021-01-29T13:17:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/977

I updated from ROCm 2.10 to ROCm 3.0, and OpenCL stopped working by reporting 0 devices.
There are no errors in dmesg.

Kernel: Linux 5.4.5 and 5.5.0-rc2 (same behavior on both), GPU RadeonVII.
rocm-smi reports correctly all the GPUs, so it seems the hardware is detected and initialized correctly:
```
~/rocm-opencl$ ~/ROC-smi/rocm-smi 
GPU  Temp   AvgPwr  SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
0    33.0c  27.0W   809Mhz  351Mhz  20.0%   auto  250.0W    0%   0%    
[etc]
```

But both /usr/bin/clinfo and /opt/rocm/opencl/bin/x86_64/clinfo report no devices:
```
/opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```
```
/usr/bin/clinfo  
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3052.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform
```

The ROCm packages that I have installed:
```
hsa-rocr-dev/Ubuntu 16.04,now 1.1.9.0-rocm-rel-3.0-6-7128d0d amd64 [installed,automatic]
hsakmt-roct/Ubuntu 16.04,now 1.0.9-298-gea01eb3 amd64 [installed,automatic]
rocm-opencl/Ubuntu 16.04,now 2.0.0-rocm-rel-3.0-6-9a4afec amd64 [installed]
```