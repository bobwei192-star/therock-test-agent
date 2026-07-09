# [Issue]: The rocblas of 6.4.0 release doesn't ship TensileLibrary files for gfx906

- **Issue #:** 4625
- **State:** open
- **Created:** 2025-04-14T19:58:34Z
- **Updated:** 2026-01-22T19:06:34Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4625

### Problem Description

Getting an error
```
rocBLAS error: Cannot read /opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary.dat: No such file or directory for GPU arch : gfx906
 List of available TensileLibrary Files : 
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx1101.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx1102.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx1200.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx1030.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx1100.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx1201.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx942.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx90a.dat"
"/opt/rocm-6.4.0/lib/rocblas/library/TensileLibrary_lazy_gfx908.dat"
```
However, Radeon VII gfx906 still listed as deprecated instead of unsupported.
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-gpus
rocm 6.3 worked fine.

### Operating System

Ubuntu 24.04

### CPU

AMD CPU

### GPU

Radeon VII

### ROCm Version

6.4.0

### ROCm Component

rocBLAS

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_