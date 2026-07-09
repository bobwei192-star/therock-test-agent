# Laptop can't use ROCm1.9.

- **Issue #:** 554
- **State:** closed
- **Created:** 2018-09-21T15:21:37Z
- **Updated:** 2018-09-30T00:35:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/554

model:OMEN by HP 15-ax211TX
CPU:i5 7300HQ
GPU:RX460
System:Ubuntu 18.04
kernel:4.15.0-20-generic
$ rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104

$ /opt/rocm/opencl/bin/x86_64/clinfo 
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

$ rocm-smi -p
====================    ROCm System Management Interface    ====================
GPU[0] 		: Cannot get Performance Level: Performance Level not supported
GPU[1] 		: Current PowerPlay Level: off
====================           End of ROCm SMI Log          ====================

$ rocm-smi -d1 -P
====================    ROCm System Management Interface    ====================
GPU[1] 		: WARNING: Empty SysFS value: power
GPU[1] 		: Cannot get GPU power Consumption: Average GPU Power not supported
====================           End of ROCm SMI Log          ====================
