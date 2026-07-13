# "AMDKFD_IOC_ACQUIRE_VM failed" on linux-4.18-rc1 with Vega 64

- **Issue #:** 438
- **State:** closed
- **Created:** 2018-06-20T02:28:05Z
- **Updated:** 2018-06-27T16:38:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/438

Tested with roc-1.8.x and master branches of ROCT-Thunk-Interface and ROCR-Runtime:

```
# uname -a
Linux localhost 4.18.0-rc1-mainline #1 SMP PREEMPT Wed Jun 6 19:43:20 CEST 2018 x86_64 GNU/Linux

# lspci | grep VGA
08:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XT [Radeon RX Vega 64] (rev c1)

# HSAKMT_DEBUG_LEVEL=7 rocminfo 
acquiring VM for 86f3 using 5
AMDKFD_IOC_ACQUIRE_VM failed
hsa api call failure at line 896, file: /home/narthorn/dev/rocm/rocminfo/rocminfo.cc. Call returned 4104
```
It looks like /dev/kfd is successfully opened, but this ioctl fails with EINVAL during hsa initialization.