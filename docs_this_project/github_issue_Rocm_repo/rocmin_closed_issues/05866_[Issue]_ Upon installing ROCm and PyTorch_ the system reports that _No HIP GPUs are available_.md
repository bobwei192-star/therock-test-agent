# [Issue]: Upon installing ROCm and PyTorch, the system reports that 'No HIP GPUs are available'.

- **Issue #:** 5866
- **State:** closed
- **Created:** 2026-01-18T03:39:29Z
- **Updated:** 2026-01-22T15:00:01Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5866

### Problem Description

I attempted to install ROCm on Ubuntu 22.04 (WSL2). However, PyTorch fails to detect any available GPU after the installation. My GPU is a Radeon RX 7900 XTX, so theoretically, this shouldn't be an issue.

<img width="1115" height="628" alt="Image" src="https://github.com/user-attachments/assets/89b0c63b-e2e5-4d14-8f08-37953cc4b57a" />[](url)

### Operating System

Ubuntu 22.04 (WSL2)

### CPU

AMD Ryzen 7 7700 8-Core Processor

### GPU

AMD Radeon RX 7900 XTX 

### ROCm Version

6.4.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_