# Failure to set tba address. error -1

- **Issue #:** 959
- **State:** closed
- **Created:** 2019-12-07T11:16:38Z
- **Updated:** 2023-12-18T16:05:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/959

Linux kernel version: Git tag v5.4, with known required configures turned on
ROCm version: 2.10 (repo)
Device: Ryzen 7 2700U with Vegas 10

```
$ ./clinfo
Number of platforms:                             2
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3019.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 1.1 Mesa 19.2.6
  Platform Name:                                 Clover
  Platform Vendor:                               Mesa
  Platform Extensions:                           cl_khr_icd


  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

```

```
$ ./rocminfo
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-2.10/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
After running rocminfo dmesg shows:

```
# dmesg
...
[   71.181067] Failure to set tba address. error -1.
...
```