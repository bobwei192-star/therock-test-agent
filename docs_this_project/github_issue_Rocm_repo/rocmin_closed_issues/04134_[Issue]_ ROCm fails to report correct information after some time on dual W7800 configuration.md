# [Issue]: ROCm fails to report correct information after some time on dual W7800 configuration

- **Issue #:** 4134
- **State:** closed
- **Created:** 2024-12-06T20:32:27Z
- **Updated:** 2025-01-16T19:21:28Z
- **Labels:** Under Investigation, ROCm 6.1.0, 2x AMD Radeon Pro W7800
- **URL:** https://github.com/ROCm/ROCm/issues/4134

### Problem Description

I am currently running a workstation with two AMD Radeon Pro W7800 cards. 

Link to motherboard: [Gigabyte TRX50-AERO-D](https://www.gigabyte.com/Motherboard/TRX50-AERO-D-rev-12)

As a reminder, the W7800 runs `gfx1100`. Upon system boot, both cards behave as expected. `rocm-smi` and `rocminfo` report the correct information, and the ROCm interface works correctly with PyTorch and other applications. 

After a seemingly arbitrary amount of time, ROCm seems to just "die" for each card. These events are independent per card, and the uptime after boot is <24hr before this occurs (I have not narrowed the time down exactly, and it does not even seem to be consistent). This occurs even if no ROCm-related program was run by the user.

I.e., I boot, wait, and then ROCm can no longer communicate with my cards. Here is what `rocm-smi` output after the "crash":

```
$ rocm-smi


Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
========================================== ROCm System Management Interface ==========================================
==================================================== Concise Info ====================================================
Device  Node  IDs              Temp    Power  Partitions          SCLK  MCLK  Fan  Perf     PwrCap       VRAM%  GPU%  
              (DID,     GUID)  (Edge)  (Avg)  (Mem, Compute, ID)                                                      
======================================================================================================================
0       2     0x745e,   49070  N/A     N/A    N/A, N/A, 0         None  None  0%   unknown  Unsupported  0%     0%    
1       1     0x745e,   8521   N/A     N/A    N/A, N/A, 0         None  None  0%   unknown  Unsupported  0%     0%    
======================================================================================================================
================================================ End of ROCm SMI Log =================================================

```

Is there any insight into what might be causing this? [This issue](https://github.com/ROCm/ROCm/issues/2681) seems related, but I am running ROCm 6.1.3.

### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen Threadripper 7960X 24-Cores

### GPU

2x AMD Radeon Pro W7800

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
$ /opt/rocm/bin/rocminfo --support
ROCk module version 6.7.0 is loaded
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1250
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

### Additional Information

_No response_