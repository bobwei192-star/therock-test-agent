# Rocm6 not working with PCIE x1 gen1

- **Issue #:** 2926
- **State:** closed
- **Created:** 2024-02-23T23:52:25Z
- **Updated:** 2024-10-09T14:22:01Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/2926

### Problem Description

Hello, 
Im trying to use llamacpp with rocm6 and hipBlas under pcie x1 gen1 without success. 
So im using at the moment Vulkan

### Operating System

"22.04.4 LTS (Jammy Jellyfish)

### CPU

Intel(R) Core(TM) i7-7700T CPU @ 2.90GHz

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.0.0

### ROCm Component

hipBLAS

### Steps to Reproduce

git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp/
make LLAMA_HIPBLAS=1
./main -m /openhermes-2.5-neural-chat-v3-3-slerp.Q8_0.gguf -p "Hi you how are you" -ngl 90 

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_