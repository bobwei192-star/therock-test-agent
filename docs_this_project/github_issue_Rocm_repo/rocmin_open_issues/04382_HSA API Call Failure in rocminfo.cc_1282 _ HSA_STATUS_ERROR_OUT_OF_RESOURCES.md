# HSA API Call Failure in rocminfo.cc:1282 – HSA_STATUS_ERROR_OUT_OF_RESOURCES

- **Issue #:** 4382
- **State:** open
- **Created:** 2025-02-16T03:10:02Z
- **Updated:** 2026-04-04T23:28:07Z
- **Labels:** Under Investigation, AMD Radeon RX 7900XTX, ROCm 6.3.2
- **URL:** https://github.com/ROCm/ROCm/issues/4382

### Problem Description

![Image](https://github.com/user-attachments/assets/d24749c8-d98d-4e56-95c2-a836d5cb6976)

Error after fresh install of Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-131-generic x86_64). 

AMD installer runs fine, runtime error during post install steps, specifically when running `rocminfo`:
```
$ amdgpu-install --usecase=dkms,rocm,rocmdev,rocmdevtools,lrt,openclsdk,hip,hiplibsdk,openmpsdk,mllib,mlsdk,asan --install-recommends --install-suggests
Hit:1 http://us.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://us.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:3 http://us.archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:4 https://download.docker.com/linux/ubuntu jammy InRelease                                                                                  
Hit:5 https://repo.radeon.com/amdgpu/6.3.2/ubuntu jammy InRelease                                                                               
Hit:6 https://repo.radeon.com/rocm/apt/6.3.2 jammy InRelease                                                              
Hit:7 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                          
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
linux-headers-5.15.0-131-generic is already the newest version (5.15.0-131.141).
amdgpu-dkms is already the newest version (1:6.10.5.60302-2109964.22.04).
rocm is already the newest version (6.3.2.60302-66~22.04).
rocm-asan is already the newest version (6.3.2.60302-66~22.04).
rocm-dev is already the newest version (6.3.2.60302-66~22.04).
rocm-developer-tools is already the newest version (6.3.2.60302-66~22.04).
rocm-hip-runtime is already the newest version (6.3.2.60302-66~22.04).
rocm-hip-sdk is already the newest version (6.3.2.60302-66~22.04).
rocm-language-runtime is already the newest version (6.3.2.60302-66~22.04).
rocm-ml-libraries is already the newest version (6.3.2.60302-66~22.04).
rocm-ml-sdk is already the newest version (6.3.2.60302-66~22.04).
rocm-opencl-sdk is already the newest version (6.3.2.60302-66~22.04).
rocm-openmp-sdk is already the newest version (6.3.2.60302-66~22.04).
rocm-utils is already the newest version (6.3.2.60302-66~22.04).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

$ rocminfo
$ clinfo
ROCk module version 6.10.5 is loaded
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1282
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3635.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```

### Operating System

Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-131-generic x86_64)

### CPU

11th Gen Intel(R) Core(TM) i9-11900K @ 3.50GHz

### GPU

Radeon RX 7900 XTX

### ROCm Version

6.3.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

`$ /opt/rocm/bin/rocminfo --support`
ROCk module version 6.10.5 is loaded
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1282
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

### Additional Information

_No response_