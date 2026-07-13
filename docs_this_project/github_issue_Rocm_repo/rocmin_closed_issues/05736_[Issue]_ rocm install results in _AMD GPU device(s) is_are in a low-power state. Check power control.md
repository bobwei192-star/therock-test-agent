# [Issue]: rocm install results in "AMD GPU device(s) is/are in a low-power state. Check power control/runtime_status"

- **Issue #:** 5736
- **State:** closed
- **Created:** 2025-12-03T19:40:05Z
- **Updated:** 2026-02-20T14:57:01Z
- **Labels:** status: assessed
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5736

### Problem Description

customer (Altair, **Jonathan Mozo <[jmozo@altair.com](mailto:jmozo@altair.com)>** ) is failing to install rocm and GPU driver. sees various errors:

"when I run sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)”, I get the following. 
 

E:Unable to locate package linux-modules-extra-5.18.2-mi300-build-140423-**ubuntu-22.04**
E: Couldn't find any package by glob 'linux-modules-extra-5.18.2-mi300-build-140423-ubuntu-22.04'

"
then customer was able to move forward a bit and ended up with 

rocm-smi
ERROR:root:Driver not initialized (amdgpu not found in modules)

then customer tried to reinstall rocm and ended up with 

I saw 7.1 was released so I just tried that version and same result when running rocm-smi.

mozo@us-midc-mi300a:/etc/modprobe.d$ rocm-smi


WARNING: No AMD GPUs specified
WARNING: AMD GPU device(s) is/are in a low-power state. Check power control/runtime_status

===================================== ROCm System Management Interface =====================================
=============================================== Concise Info ===============================================
Device  Node  IDs           Temp    Power  Partitions          SCLK  MCLK  Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,  GUID)  (Edge)  (Avg)  (Mem, Compute, ID)                                              
============================================================================================================
============================================================================================================
=========================================== End of ROCm SMI Log ============================================
jmozo@us-midc-mi300a:/etc/modprobe.d$ 







### Operating System

Ubuntu 22.04

### CPU

NA

### GPU

NA

### ROCm Version

7

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_