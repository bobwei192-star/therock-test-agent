# [Issue]: Shared memory is forced with llama.cpp llama-server --mlock

- **Issue #:** 4903
- **State:** closed
- **Created:** 2025-06-08T22:27:48Z
- **Updated:** 2026-03-08T08:37:02Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/4903

### Problem Description

```
llama-server.exe  -m "C:\Users\musclez\Downloads\llama-b5603-bin-win-hip-radeon-x64\Qwen3-Embedding-8B-Q8_0.gguf"  -a qwen3 -b 1024 -ub 1024 -c 1024 -fa --no-mmap -ngl 999 --embeddings --pooling mean --no-webui -sm none --mlock -mg 0
```

--mlock is supposed to lock it to VRAM on windows, but even with it active and low VRAM usage, it offloads to the shared/system memory.

![Image](https://github.com/user-attachments/assets/2d75b9ca-0f01-4887-a8ca-6e89ef19708e)

![Image](https://github.com/user-attachments/assets/09ee4b3d-3f22-4eca-b958-85c18a73918f)

![Image](https://github.com/user-attachments/assets/4c1073e8-bd42-4173-8cd1-6dcf7294befd)

https://github.com/ggml-org/llama.cpp/issues/9964

### Operating System

Windows 11

### CPU

7800x3D

### GPU

7900XT

### ROCm Version

ROCm 6.2

### ROCm Component

hipBLAS

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_