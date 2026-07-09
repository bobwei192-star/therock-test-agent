# [Issue]: ROCm 6.2.2 couldn't query GPU power and temperature monitor

- **Issue #:** 4268
- **State:** closed
- **Created:** 2025-01-17T18:52:21Z
- **Updated:** 2025-04-10T17:25:02Z
- **Labels:** Under Investigation, ROCm 6.2.2
- **URL:** https://github.com/ROCm/ROCm/issues/4268

### Problem Description

On the system below using ROCm 6.2.2, rocm-smi couldn't query one GPU's Temp and Power. Rebooting the node fixed the issue.
**My questions are:**
1) How does this monitor query error affect the GPU functionality?
2) What's the root cause of this monitor query error?

Ubuntu 22.04.5 LTS
ROCm version: 6.2.2-116
Hardware: MI300
```
$ rocm-smi
 
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
Expected integer value from monitor, but got ""
=============================================== ROCm System Management Interface ===============================================
========================================================= Concise Info =========================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK     MCLK     Fan  Perf  PwrCap       VRAM%  GPU%
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)
================================================================================================================================
0       2     0x74b5,   65402  56.0°C      321.0W    NPS1, N/A, 0        2074Mhz  1300Mhz  0%   auto  750.0W       90%    58%
1       3     0x74b5,   27175  54.0°C      322.0W    NPS1, N/A, 0        2077Mhz  1300Mhz  0%   auto  750.0W       90%    84%
2       4     0x74b5,   16561  53.0°C      308.0W    NPS1, N/A, 0        2084Mhz  1300Mhz  0%   auto  750.0W       90%    97%
3       5     0x74b5,   54764  51.0°C      311.0W    NPS1, N/A, 0        2083Mhz  1300Mhz  0%   auto  750.0W       90%    78%
4       6     0x74b5,   10760  38.0°C      136.0W    NPS1, N/A, 0        132Mhz   900Mhz   0%   auto  750.0W       0%     0%
5       7     0x74b5,   48981  39.0°C      136.0W    NPS1, N/A, 0        131Mhz   900Mhz   0%   auto  750.0W       0%     0%
6       8     0x74b5,   32548  37.0°C      137.0W    NPS1, N/A, 0        132Mhz   900Mhz   0%   auto  750.0W       0%     0%
7       9     0x74b5,   60025  N/A         N/A       NPS1, N/A, 0        None     None     0%   auto  Unsupported  0%     0%
================================================================================================================================
===================================================== End of ROCm SMI Log ======================================================

```

### Operating System

Ubuntu 22.04.5 LTS

### CPU

Intel Xeon

### GPU

AMD MI300x

### ROCm Version

ROCm 6.2.2

### ROCm Component

ROCm

### Steps to Reproduce

not sure how this occurred.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_