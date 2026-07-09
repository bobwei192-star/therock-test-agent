# [Issue]: RuntimeError: HIP error: invalid device function

- **Issue #:** 5668
- **State:** closed
- **Created:** 2025-11-14T11:11:23Z
- **Updated:** 2025-12-01T16:34:38Z
- **Labels:** Documentation, status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5668

### Problem Description

RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

### Operating System

Ubuntu 24

### CPU

AMD radeon AI max+395

### GPU

product: Strix Halo [Radeon Graphics / Radeon 8050S Graphics / Radeon 8060S Graphics]

### ROCm Version

ROCk module version 6.16.6 is loaded

### ROCm Component

_No response_

### Steps to Reproduce

RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.


### Additional Information

**1.system is ubuntu**
**2.rocminfo**
rocminfo
ROCk module version 6.16.6 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES
**3.rocm-smi**
ROCM-SMI version: 3.0.0+03a4530
ROCM-SMI-LIB version: 7.5.0
**4.pytorch version**
torch                    2.4.1+rocm6.0
torch-complex            0.4.4
torchaudio               2.4.1+rocm6.0
torchvision              0.19.1+rocm6.0