# Problems installing ROCm on Ubuntu Server

- **Issue #:** 1152
- **State:** closed
- **Created:** 2020-06-17T09:31:45Z
- **Updated:** 2020-06-19T09:11:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/1152

## issue
I have tried installing ROCm on Ubuntu server(16.04 LTS/18.04 LTS) but it cannot recognize GPU devices properly,
since ROCm and tools do not work properly.

## To reproduce
 * Making platform with Ubuntu server(16.04 or 18.04).
 * Installing ROCm as it is shown on ROCm documents.
 * Running rocminfo and clinfo

If you have installed ROCm properly, you may see hardware infos, but I have encountered these errors.

(rocminfo)
```
$ /opt/rocm-3.5.0/bin/rocminfo 
ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
johndoe is member of video group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

(clinfo)
```
$ /opt/rocm-3.5.0/opencl/bin/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3137.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0

```

(rocm-smi)
```
$ /opt/rocm-3.5.0/bin/rocm-smi 
Unable to get devices, /sys/class/drm is empty or missing
ERROR: No DRM devices available. Exiting
```

And I could not find /dev/dri/* and /dev/kfd/* ,too.


 

