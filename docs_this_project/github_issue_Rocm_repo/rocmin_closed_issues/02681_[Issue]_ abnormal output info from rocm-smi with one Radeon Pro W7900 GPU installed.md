# [Issue]: abnormal output info from rocm-smi with one Radeon Pro W7900 GPU installed

- **Issue #:** 2681
- **State:** closed
- **Created:** 2023-11-29T14:58:44Z
- **Updated:** 2024-02-02T04:36:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/2681

### Problem Description

1. Run rocm-smi
2. see the output
- unsupported info output from rocm-smi
- Why here are two GPUs info but just one Radeon Pro W7900 GPU installed

### Operating System

Ubuntu 22.04.3

### CPU

AMD Ryzen 7900

### GPU

AMD Radeon Pro W7900

### ROCm Version

5.7.1

### ROCm Component

_No response_

### Steps to Reproduce

Run rocm-smi

### Output of /opt/rocm/bin/rocminfo --support

amd@AIG-PM:~$ rocm-smi


========================= ROCm System Management Interface =========================
=================================== Concise Info ===================================
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
GPU[0]          : get_power_avg, Unexpected data received
====================================================================================
====================================================================================
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
GPU[0]          : get_power_cap, Unexpected data received
ERROR: GPU[1]   : sclk clock is unsupported
====================================================================================
GPU[1]          : get_power_cap, Not supported on the given system
GPU  Temp (DieEdge)  AvgPwr  SCLK  MCLK     Fan  Perf     PwrCap       VRAM%  GPU%
0    N/A             N/A     None  None     0%   unknown  Unsupported    0%   0%
1    42.0c           0.159W  None  3000Mhz  0%   auto     Unsupported    3%   0%
====================================================================================
=============================== End of ROCm SMI Log ================================
