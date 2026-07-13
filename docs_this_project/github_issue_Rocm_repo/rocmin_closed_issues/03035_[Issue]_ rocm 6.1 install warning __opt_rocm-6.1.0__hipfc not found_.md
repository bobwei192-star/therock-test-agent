# [Issue]: rocm 6.1 install warning "/opt/rocm-6.1.0//hipfc not found"

- **Issue #:** 3035
- **State:** closed
- **Created:** 2024-04-17T19:29:14Z
- **Updated:** 2024-12-11T02:31:59Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon VII
- **URL:** https://github.com/ROCm/ROCm/issues/3035

### Problem Description

```
$ sudo apt install rocm-hip-sdk6.1.0 rocm-openmp-sdk6.1.0
...
Setting up hipblas-dev6.1.0 (2.1.0.60100-82~20.04) ...
Setting up hipsparse6.1.0 (3.0.1.60100-82~20.04) ...
Setting up hipsparse-dev6.1.0 (3.0.1.60100-82~20.04) ...
Setting up rocalution6.1.0 (3.1.1.60100-82~20.04) ...
Setting up rccl-dev6.1.0 (2.18.6.60100-82~20.04) ...
Setting up hipsolver6.1.0 (2.1.0.60100-82~20.04) ...
Setting up hipblaslt6.1.0 (0.7.0.60100-82~20.04) ...
Setting up hipsparselt6.1.0 (0.1.0.60100-82~20.04) ...
Setting up rocalution-dev6.1.0 (3.1.1.60100-82~20.04) ...
Setting up hipsolver-dev6.1.0 (2.1.0.60100-82~20.04) ...
Setting up rocm-hip-libraries6.1.0 (6.1.0.60100-82~20.04) ...
Setting up hipsparselt-dev6.1.0 (0.1.0.60100-82~20.04) ...
Setting up hipblaslt-dev6.1.0 (0.7.0.60100-82~20.04) ...
Setting up rocm-hip-sdk6.1.0 (6.1.0.60100-82~20.04) ...
/opt/rocm-6.1.0//hipfc not found, but that is OK
```
Noticed the last line warning about `/opt/rocm-6.1.0//hipfc`. It is actually at `/opt/rocm-6.1.0/bin/hipfc`

### Operating System

ubuntu 20.04.6 LTS

### CPU

AMD EPYC 7282 16-Core Processor

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_