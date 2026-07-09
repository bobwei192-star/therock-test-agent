# [Issue]: Low performance in llama.cpp mmf mul_mat_f on 9070XT

- **Issue #:** 5727
- **State:** closed
- **Created:** 2025-12-01T03:44:32Z
- **Updated:** 2025-12-12T18:10:43Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5727

### Problem Description

ROCm compiler doesn't generate the code with good enough performance for 9070XT, the performance of "MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],k_v=0,o=1)" is 3.1 tflops, I need use some weird code to force compiler to unroll more codes then the performance becomes to 4.95 tflops.

This will reduce the performance of dense model like deepseek R1 about 30%.

### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

AMD Ryzen 9 7900X3D 12-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 7.1.1

### ROCm Component

HIP

### Steps to Reproduce

llama.cpp version
```
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
git checkout ff90508
```

build command
```
cmake -S . -B build -DGGML_HIP=ON -DGPU_TARGETS=gfx1201 -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF -DGGML_HIP_ROCWMMA_FATTN=ON
cmake --build build -j
```

run command
```
./build/bin/test-backend-ops perf -o "MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],k_v=0,o=1)"
```

the original output, the performance is 3.09 tflops
```
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: AMD Radeon RX 9070 XT, gfx1201 (0x1201), VMM: no, Wave Size: 32
Testing 2 devices

Backend 1/2: ROCm0
  Device description: AMD Radeon RX 9070 XT
  Device memory: 16304 MB (16238 MB free)

  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],k_v=0,o=1):                 3317 runs -   303.79 us/run - 939.52 MFLOP/run -   3.09 TFLOPS
  Backend ROCm0: OK
Backend 2/2: CPU
  Skipping CPU backend
2/2 backends passed
OK
```

Use this attached [mmf.zip](https://github.com/user-attachments/files/23844560/mmf.zip) to replace the original one, then recompile the code and rerun the command.

The output after patch, the performance becomes to 4.94 tflops
```
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: AMD Radeon RX 9070 XT, gfx1201 (0x1201), VMM: no, Wave Size: 32
Testing 2 devices

Backend 1/2: ROCm0
  Device description: AMD Radeon RX 9070 XT
  Device memory: 16304 MB (16238 MB free)

  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],k_v=0,o=1):                 5350 runs -   190.37 us/run - 939.52 MFLOP/run -   4.94 TFLOPS
  Backend ROCm0: OK
Backend 2/2: CPU
  Skipping CPU backend
2/2 backends passed
OK
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_