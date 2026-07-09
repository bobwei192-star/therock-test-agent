# Problem installing rocm-dkms on different Linux distributes and PCs. 

- **Issue #:** 902
- **State:** closed
- **Created:** 2019-10-05T05:58:21Z
- **Updated:** 2019-10-06T08:45:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/902

Greetings.
I have unsuccessfully tried to install ROCm on different Linux distributives (Ubuntu 16.04, 18.04, CentOS 7.4, 7.6, 7.7). 
My PC hardware is AMD RX580, FX8300, Asus m5a99x Evo, 16gb ddr3.
Notebook: Dell 7375 (Ryzen 2500U, Vega8, 32gb ddr4).
I have tried using both rocm-dkms packages and using upstream kernel driver (uname –r shows, that kernel did not change after installation), that both led to the same error.
On versions 2.2, 2.3, 2.5 error is:

```
pavlo@pavlo-desktop:~$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
pavlo@pavlo-desktop:~$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104
```

On versions 2.7.2, 2.8 error is:

```
pavlo@pavlo-desktop:~$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2973.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
pavlo@pavlo-desktop:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
pavlo is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.8@2/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

```

I`ve used a tutorial from https://rocm.github.io/ROCmInstall.html.
Thank you for your help.
