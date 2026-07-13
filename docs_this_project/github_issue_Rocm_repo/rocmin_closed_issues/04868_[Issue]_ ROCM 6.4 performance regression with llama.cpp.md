# [Issue]: ROCM 6.4 performance regression with llama.cpp

- **Issue #:** 4868
- **State:** closed
- **Created:** 2025-06-01T04:52:33Z
- **Updated:** 2025-07-14T18:42:53Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4868

### Problem Description

ROCM 6.4 inference with llama.cpp is 10x slower than ROCM 6.3 (!)
You may have to run it a few times until it becomes super slow.
There are no warnings or errors.
eg with Meta-Llama-3-8B.Q4_K_M.gguf
expected: 80 token/sec
actual: 12 token/sec

### Operating System

Ubuntu 24.04.2

### CPU

AMD Ryzen Threadripper 3970X

### GPU

2x Radeon 7900 XTX

### ROCm Version

ROCm 6.4

### ROCm Component

_No response_

### Steps to Reproduce

`llama-bench -m Meta-Llama-3-8B.Q4_K_M.gguf`

You may have to run it a few times until it becomes super slow.
Both ROCm and Vulkan llama.cpp have this issue.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_