# rocminfo shows "no gpu" after installation

- **Issue #:** 1555
- **State:** closed
- **Created:** 2021-08-16T12:50:30Z
- **Updated:** 2024-01-08T06:42:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/1555

```
azureuser@gvme7b1132637:~$ /opt/rocm/bin/rocminfo
ROCk module is NOT loaded, possibly no GPU devices
azureuser@gvme7b1132637:~$ /opt/rocm/opencl/bin/clinfo
Number of platforms:				1
  Platform Profile:				FULL_PROFILE
  Platform Version:				OpenCL 2.0 AMD-APP (3305.0)
  Platform Name:				AMD Accelerated Parallel Processing
  Platform Vendor:				Advanced Micro Devices, Inc.
  Platform Extensions:				cl_khr_icd cl_amd_event_callback 


  Platform Name:				AMD Accelerated Parallel Processing
Number of devices:				0
```

Strange thing is that opencl seems available. 
The installation and tests were done on a NV4as_v4 VM with Instinct MI25 GPU. 
ROCM version: 4.3 (Installed according to https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html)
OS version: Ubuntu 20.04.2