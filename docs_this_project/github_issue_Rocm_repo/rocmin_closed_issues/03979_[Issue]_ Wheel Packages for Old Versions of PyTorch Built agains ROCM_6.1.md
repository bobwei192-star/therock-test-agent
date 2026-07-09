# [Issue]: Wheel Packages for Old Versions of PyTorch Built agains ROCM/6.1 

- **Issue #:** 3979
- **State:** closed
- **Created:** 2024-10-31T05:29:13Z
- **Updated:** 2024-11-04T01:30:12Z
- **Labels:** Under Investigation, ROCm 6.1.0, N/A
- **URL:** https://github.com/ROCm/ROCm/issues/3979

### Problem Description

Please provide wheel packages for older versions of PyTorch, e.g. 2.1, 2,2 and 2.3 which are built against more recent ROCm 6.1. 

I would like to determine if there is performance regression with new releases of PyTorch. 
This has been observed with NVIDIA as well. 
So we would like to find best versions without relying on containers.   

### Operating System

RHEL 8

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

```
$ conda create -n torch-2.1.2 python=3.10
$ conda activate torch-2.1.2
$ pip install torch==2.1.2 --index-url https://download.pytorch.org/whl/rocm6.1 
ERROR: Could not find a version that satisfies the requirement torch==2.1.2 (from versions: 2.4.0+rocm6.1, 2.4.1+rocm6.1, 2.5.0+rocm6.1, 2.5.1+rocm6.1)
ERROR: No matching distribution found for torch==2.1.2
```
So for ROCm-6.+, only recent 2.4+ releases are provided.  

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_