# Fiji device not detected, machine hangs with ROCm 1.4

- **Issue #:** 89
- **State:** closed
- **Created:** 2017-02-23T23:51:53Z
- **Updated:** 2017-02-24T02:02:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/89

System Ubuntu 16.04
Hardware: CPU AMD FX-8350, GPU: Fiji (Fury Nano)

Installed:  rocm opencl-rocm opencl-rocm-dev
Rebooted with the new kernel, after which I can't get any devices detected nor run any HIP, hsa, or OpenCL code.

* bit_extract HIP sample gives:
```
### HCC STATUS_CHECK Error: HSA_STATUS_ERROR_OUT_OF_RESOURCES (0x1008) at file:/home/scchan/code/github/hcc-roc-1.4.x/hcc/lib/hsa/mcwamp_hsa.cpp line:2728
Aborted (core dumped)
```

* stadard clinfo hangs, the one provided by rocm outputs this:
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (2300.5)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 

  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

* kern.log contains the following (after running clinfo)
```
kfd: qcm fence wait loop timeout expired
kfd: unmapping queues failed.
kfd: the cp might be in an unrecoverable state due to an unsuccessful queues preemption<4>[ 3721.447737] amdkfd: Resetting wave fronts on dev ffff8800bf91bc00
```
This is often preceded by some NetworkManager stats printout. (Occasionally the machine hangs or does not respond over the network -- maybe related, maybe not.) 