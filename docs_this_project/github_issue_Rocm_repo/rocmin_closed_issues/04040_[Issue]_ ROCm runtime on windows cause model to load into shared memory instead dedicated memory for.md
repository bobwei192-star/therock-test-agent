# [Issue]: ROCm runtime on windows cause model to load into shared memory instead dedicated memory for N31

- **Issue #:** 4040
- **State:** closed
- **Created:** 2024-11-19T16:06:05Z
- **Updated:** 2024-11-28T21:13:35Z
- **Labels:** Under Investigation, ROCm 6.1.0, 7900xtx
- **URL:** https://github.com/ROCm/ROCm/issues/4040

### Problem Description

https://github.com/ggerganov/llama.cpp/discussions/9960#discussioncomment-11141805

https://github.com/ggerganov/llama.cpp/issues/9964


### Operating System

Windows11

### CPU

7950X3D

### GPU

7900XTX

### ROCm Version

ROCm 6.1.0

### ROCm Component

ROCR-Runtime

### Steps to Reproduce

llama.cpp Windows/ROCm builds are broken. Using shared GPU memory instead of dedicated
https://github.com/ggerganov/llama.cpp/issues/9964
workaround:

 latest ROCm runtime (1.1.13). Switching to Vulkan or 1.1.10 runtime works.
