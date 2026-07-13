# [Issue]: GPU benchmark via PyTorch shows 9060XT is slower than 6600

- **Issue #:** 5079
- **State:** closed
- **Created:** 2025-07-22T06:48:58Z
- **Updated:** 2025-07-22T07:17:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/5079

### Problem Description

I have 2 GPUs, a 9060XT 16GB and a 6600 8GB. I am using this code to try to benchmark the performance for each GPU.

```

import os
import torch
import time
from tqdm import tqdm

os.environ['HSA_OVERRIDE_GFX_VERSION_1'] = '12.0.0'
os.environ['HSA_OVERRIDE_GFX_VERSION_2'] = '10.3.0'

def benchmark_gpu(device_id, num_tests=5):
    
    device = torch.device(f'cuda:{device_id}')
    print(f"\nBenchmarking {torch.cuda.get_device_name(device)}...")
    print(f"Running {num_tests} tests per matrix size...")
    
    sizes = [256, 512, 1024, 2048, 4096]
    
    
    x = torch.randn(1024, 1024, device=device)
    y = torch.randn(1024, 1024, device=device)
    _ = x @ y
    
    for size in sizes:
        start = time.time()
        
        for _ in range(num_tests):
            a = torch.randn(size, size, device=device)
            b = torch.randn(size, size, device=device)
            
            torch.cuda.synchronize()
            
            _ = a @ b
            torch.cuda.synchronize()
            
        duration = (time.time() - start)*1000
        
        avg_time = duration/num_tests
        
        print(f"Size {size}x{size}: {avg_time:.2f} ms")

def runner(gpu_id, num_tests=5):
    print("\nPyTorch GPU Selector & Benchmark")
    print(f"PyTorch version: {torch.__version__}")
    print(f"ROCm available: {torch.cuda.is_available()}")
    
    if gpu_id is not None:
        benchmark_gpu(gpu_id, num_tests)

runner(0, num_tests=100)
print("\n\n")
runner(1, num_tests=100)

```
This is the output I get

```
PyTorch GPU Selector & Benchmark
PyTorch version: 2.9.0.dev20250716+rocm6.4
ROCm available: True

Benchmarking AMD Radeon RX 9060 XT...
Running 100 tests per matrix size...
Size 256x256: 0.14 ms
Size 512x512: 0.26 ms
Size 1024x1024: 0.41 ms
Size 2048x2048: 2.39 ms
Size 4096x4096: 17.82 ms




PyTorch GPU Selector & Benchmark
PyTorch version: 2.9.0.dev20250716+rocm6.4
ROCm available: True

Benchmarking AMD Radeon RX 6600...
Running 100 tests per matrix size...
Size 256x256: 0.02 ms
Size 512x512: 0.02 ms
Size 1024x1024: 0.02 ms
Size 2048x2048: 0.02 ms
Size 4096x4096: 0.02 ms
```


I understand that since my display is connected to the 9060XT, there can be performance drops but I have tried connecting my display to the 6600 too, but the values are mostly the same. Is there any issue with my GPU or is there any fault in the code that makes it look like that the 9060XT is slower than the 6600?

Also my motherboard is a B650M Aorus Pro AX from Gigabyte. I have a PCIE x16 and a PCIE x4 channel. The 9060XT is connected to the x16 and the 6600 is connected to the x4. I don't know if these could be a motherboard problem, but just in case.

### Operating System

Ubunut 24.04

### CPU

AMD Ryzen 5600z

### GPU

9060XT 16GB and 6600 8GB

### ROCm Version

ROCM 6.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_