# Is the RX 590 compatible with WSL2?

- **Issue #:** 1249
- **State:** closed
- **Created:** 2020-09-29T09:19:37Z
- **Updated:** 2025-04-12T20:18:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/1249

```
Environment:
Windows 10 Home (Version 2004)
Sapphire RX 590 (Driver 20.9.1)
Ryzen 5 2600

WSL2 Ubuntu 20.04 (kernel: 5.4.51-microsoft-standard-WSL2+)
````

I followed [this link](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu) to install it, but I get an error.

```
$ /opt/rocm/bin/rocminfo
ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
Failed to get user name to check for video group membership
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

~~clinfo doesn't seem to be a problem.~~
No error in clinfo, but it does not seem to recognize the GPU.
```
$ /opt/rocm/opencl/bin/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3186.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               0
```