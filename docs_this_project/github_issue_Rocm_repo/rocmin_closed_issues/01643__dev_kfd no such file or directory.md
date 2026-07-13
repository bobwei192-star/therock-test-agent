# /dev/kfd no such file or directory

- **Issue #:** 1643
- **State:** closed
- **Created:** 2021-12-18T02:17:09Z
- **Updated:** 2021-12-20T11:29:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/1643

What is /dev/kfd and how do I enable it in my kernel build? 

I am running on Gentoo Linux kernel 5.15.7-gentoo with a custom build of ROCm. 

`clinfo` shows no devices detected: 

```
 # clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP.dbg (3305.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No devices found in platform [AMD Accelerated Parallel Processing?]
  clCreateContext(NULL, ...) [default]            No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.3.0
  ICD loader Profile                              OpenCL 3.0
```

And `rocminfo` says that /dev/kfd is not found: 

```
 # rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: No such file or directory
happysmash27 is member of video group
```

I have enabled all kernel settings as described by the Gentoo wiki page: https://wiki.gentoo.org/wiki/OpenCL. 

`dmesg|grep "kfd"` and `dmesg|grep "KFD"` return nothing. 

I am on an RX 480. 

What could be missing that enables /dev/kfd to exist? 