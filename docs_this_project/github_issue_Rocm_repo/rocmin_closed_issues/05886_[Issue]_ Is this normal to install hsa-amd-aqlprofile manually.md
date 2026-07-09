# [Issue]: Is this normal to install hsa-amd-aqlprofile manually

- **Issue #:** 5886
- **State:** closed
- **Created:** 2026-01-22T18:59:30Z
- **Updated:** 2026-02-20T20:20:49Z
- **Labels:** status: fix submitted
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5886

### Problem Description

I usually install rocm as
```
apt install rocm-hip-sdk rocm-openmp-sdk amd-smi-lib rocprofiler-sdk
```
However, to get the profiler fully functional, I have to manually install `hsa-amd-aqlprofile`.
is this additional step expected?

### Operating System

24.04.3 LTS (Noble Numbat)

### CPU

AMD EPYC 7282 16-Core Processor

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.3-7.2

### ROCm Component

rocprofiler

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_