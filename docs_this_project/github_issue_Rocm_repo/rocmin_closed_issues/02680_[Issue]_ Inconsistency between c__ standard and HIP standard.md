# [Issue]: Inconsistency between c++ standard and HIP standard

- **Issue #:** 2680
- **State:** closed
- **Created:** 2023-11-29T01:52:21Z
- **Updated:** 2024-12-10T15:22:43Z
- **Labels:** Verified Issue, 5.7.0, 5.7.1, 5.7.x, 5.6.x, 5.5.x
- **URL:** https://github.com/ROCm/ROCm/issues/2680

### Problem Description

In ROCm releases 5.5.x, 5.6.x, and 5.7.x, the Clang language standard default is c++17. However, this is inconsistent with the HIP/CUDA default language, c++14, and may have unexpected side effects. The issue initially appeared in the ROCm 5.5 release. The issue has been fixed on https://llvm.org/ (refer to https://reviews.llvm.org/D155539), which bumps the HIP/CUDA standard language default to c++17.
 
This issue will be fixed in a future release.
 
Users can specify the language standard using the `-std=<value>` compiler option as a workaround.

### Operating System

N/A

### CPU

N/A

### GPU

N/A

### ROCm Version

5.5.x, 5.6.x, 5.7.x

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### Output of /opt/rocm/bin/rocminfo --support

N/A