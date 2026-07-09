# [Issue]: [Strix Halo / 8060S] librocdxg fails to map Dedicated VRAM in WSL2; ROCm pool size is limited by .wslconfig memory setting

- **Issue #:** 6022
- **State:** closed
- **Created:** 2026-03-07T15:59:42Z
- **Updated:** 2026-05-02T15:23:54Z
- **Labels:** status: fix submitted
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6022

### Problem Description

## Env

### Windows11
```
(Get-WmiObject Win32_OperatingSystem).Version
10.0.26200

(Get-WmiObject win32_Processor).Name
AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

(Get-WmiObject win32_VideoController).Name
AMD Radeon(TM) 8060S Graphics
```

### WSL2
```
$ echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
OS:
NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"

$ echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
CPU:
model name      : AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

$ echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
GPU:
Load librocdxg.so successully!
Load all DTIF APIs OK!
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Name:                    gfx1151
  Marketing Name:          AMD Radeon(TM) 8060S Graphics
Unload librocdxg.so successully!
      Name:                    amdgcn-amd-amdhsa--gfx1151
      Name:                    amdgcn-amd-amdhsa--gfx11-generic
```

### ROCm

Version: /opt/rocm-7.2.0

### librocdxg

https://github.com/ROCm/librocdxg.git
commit: 4880c78da9f1f400d0c1a985afb72e7f3ea05161 ( Date:   Mon Feb 9 15:45:39 2026 +0800 )

### python3 -m torch.utils.collect_env
```
PyTorch version: 2.9.1+rocm7.2.0.git7e1940d4
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 7.2.26015-fc0010cf6a

OS: Ubuntu 24.04.3 LTS (x86_64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
Clang version: Could not collect
CMake version: version 3.28.3
Libc version: glibc-2.39

Python version: 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-6.6.114.1-microsoft-standard-WSL2-x86_64-with-glibc2.39
Is CUDA available: True
CUDA runtime version: Could not collect
CUDA_MODULE_LOADING set to:
GPU models and configuration: AMD Radeon(TM) 8060S Graphics (gfx1151)
Nvidia driver version: Could not collect
cuDNN version: Could not collect
Is XPU available: False
HIP runtime version: 7.2.26015
MIOpen runtime version: 3.5.1
Is XNNPACK available: True

Versions of relevant libraries:
[pip3] numpy==2.4.2
[pip3] torch==2.9.1+rocm7.2.0.lw.git7e1940d4
[pip3] torchaudio==2.9.0+rocm7.2.0.gite3c6ee2b
[pip3] torchvision==0.24.0+rocm7.2.0.gitb919bd0c
[pip3] triton==3.5.1+rocm7.2.0.gita272dfa8
[conda] Could not collect
```

### BIOS
- **BIOS UMA Settings:** `Dedicated Graphics Memory` (UMA FB Size) set to **96GB**

## Problem Description
On the **Strix Halo (8060S)** platform, `librocdxg` appears to fail to recognize or map the **Dedicated GPU Memory (Local Segment)** in the WSL2 environment. Instead, the ROCm memory pool size is strictly tied to the system memory allocated to the WSL2 VM via the `.wslconfig` file.

This prevents the GPU from utilizing its full 96GB UMA potential for large-scale AI workloads (e.g., LLM inference) within WSL2, despite the hardware being fully capable in native Windows.

## Observed Evidence

### 1. Native Windows vs. WSL2 Discrepancy
- **Native Windows:** Running `ollama` (qwen3.5:27b) in native Windows successfully utilizes **41.5GB** of the **96GB Dedicated VRAM** (monitored via AMD Software: Adrenalin Edition).
- **WSL2 Mapping:** In WSL2, `rocminfo` reports a `Pool Size` that exactly matches the `memory` limit defined in `.wslconfig`. 

### 2. `.wslconfig` Correlation Test
The ROCm pool size scales with the VM's assigned RAM rather than the BIOS UMA setting:
- When `.wslconfig` is default (~16GB), `rocminfo` reports: `Pool 1 Size: 16187412 (0xf70014) KB`.
- When `.wslconfig` is set to `memory=24GB`, `rocminfo` reports: `Pool 1 Size: 24604680 (0x1777008) KB`.

### 3. Performance & Stability Issues
When a PyTorch script requests memory near the `.wslconfig` limit (e.g., 14GB allocation in a 16GB VM), the following occurs:
- Windows Task Manager shows **Shared GPU Memory** usage spiking to 14.6/15.8 GB.
- CPU temperature rises to **85°C** due to heavy memory paging/swapping overhead.
- The process hangs, while the **96GB Dedicated GPU Memory** remains completely idle (0.6GB used).

### 4. IOMMU Status
`rocminfo` reports `IOMMU Support: None` in WSL2, even though IOMMU and SVM are enabled in the BIOS.

## Reproduction Steps
1. Set BIOS UMA FB Size to 96GB.
2. Install ROCm with `librocdxg` in WSL2 Ubuntu 24.04.
3. Run `rocminfo` and compare `Pool 1 Size` with the memory limit in `.wslconfig`.
4. Run a PyTorch script to allocate memory exceeding the WSL2 RAM limit but within the 96GB UMA limit.
5. Observe that the allocation triggers system paging or fails, instead of using the Dedicated VRAM.

## Expected Behavior
`librocdxg` should map the 96GB Dedicated VRAM (UMA Frame Buffer) as the primary `LOCAL_SEGMENT` for the ROCm runtime, allowing for large allocations independent of the WSL2 system memory limit.

## Additional Context
- Setting `ROCM_DEBUG_ENABLE_WDDM_ANY=1` does not change the reported pool size.
- The 8060S compute cores are functional, reaching ~30.93 TFLOPS in GEMM tests, indicating the issue is strictly related to memory segment mapping.


### Operating System

Windows 11 Professional + WSL2: Ubuntu 24.04

### CPU

AMD RYZEN AI MAX+ 395 w

### GPU

Radeon 8060S

### ROCm Version

/opt/rocm-7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information


## Test script and screenshots

### 1, Run `ollama run qwen3.5:27b` on Windows 11

Task Manager, screenshot attachment 1

<img width="836" height="356" alt="Image" src="https://github.com/user-attachments/assets/2409eb6a-3556-42f7-9bf0-55bbcd1f4c51" />

### 2, Run Python script in WSL2

`target_gb` was changed from `14` to `8`.

```
import torch
import time

def test_strix_halo_performance():
    print(f"--- Hardware & Environment Check ---")
    print(f"PyTorch Version: {torch.__version__}")
    print(f"ROCm Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Device Name: {torch.cuda.get_device_name(0)}")
    else:
        print("Error: ROCm GPU not detected by PyTorch.")
        return

    # 8060S excels at FP16/BF16 computation.
    device = torch.device("cuda")
    dtype = torch.float16 

    print(f"\n--- Phase 1: Peak Compute Test (GEMM) ---")
    # Stressing the GPU cores with large matrix multiplication
    size = 8192  
    a = torch.randn(size, size, device=device, dtype=dtype)
    b = torch.randn(size, size, device=device, dtype=dtype)
    
    # Warm-up
    for _ in range(10):
        torch.matmul(a, b)
    
    torch.cuda.synchronize()
    start = time.time()
    iters = 50
    for _ in range(iters):
        torch.matmul(a, b)
    torch.cuda.synchronize()
    end = time.time()
    
    # Calculate TFLOPS: (2 * N^3 * iterations) / time
    tflops = (2 * size**3 * iters) / (end - start) / 1e12
    print(f"Matrix Size: {size}x{size}")
    print(f"Avg Latency: {(end - start)/iters*1000:.2f} ms")
    print(f"Estimated Throughput: {tflops:.2f} TFLOPS")

    print(f"\n--- Phase 2: Memory Bandwidth Test ---")
    # Testing data movement speed within the Unified Memory
    gb_size = 4 
    elements = (gb_size * 1024**3) // 2  # float16 = 2 bytes
    x = torch.randn(elements, device=device, dtype=dtype)
    y = torch.empty_like(x)
    
    torch.cuda.synchronize()
    start = time.time()
    for _ in range(100):
        y.copy_(x)
    torch.cuda.synchronize()
    end = time.time()
    
    # Bandwidth = (Size * Iterations * 2 for Read+Write) / Time
    bandwidth = (gb_size * 100 * 2) / (end - start)
    print(f"Transfer Size: {gb_size} GB")
    print(f"Actual Bandwidth: {bandwidth:.2f} GB/s")

    print(f"\n--- Phase 3: Memory Capacity Stress Test ---")
    # Attempting to allocate a large chunk of VRAM
    # NOTE: On Strix Halo in WSL2, this often hits the .wslconfig limit instead of Dedicated VRAM.
    target_gb = 8
    print(f"Attempting to allocate {target_gb} GB of GPU memory...")
    try:
        n_elements = (target_gb * 1024**3) // 2
        dummy_tensor = torch.zeros(n_elements, device=device, dtype=dtype)
        print(f"Success! Allocated {target_gb} GB.")
        
        # Verify write stability
        dummy_tensor.fill_(1.0)
        print("Memory write verification passed.")
    except RuntimeError as e:
        print(f"Allocation Failed: {e}")
        print("\nPossible Cause: librocdxg is mapping System RAM instead of Dedicated VRAM.")

if __name__ == "__main__":
    test_strix_halo_performance()
```

Result:
```
(rocm_env) @WIN-:~$ python3 scripts/test_strix_halo_power.py
--- Hardware & Environment Check ---
PyTorch Version: 2.9.1+rocm7.2.0.git7e1940d4
Load librocdxg.so successully!
Load all DTIF APIs OK!
ROCm Available: True
Device Name: AMD Radeon(TM) 8060S Graphics

--- Phase 1: Peak Compute Test (GEMM) ---
Matrix Size: 8192x8192
Avg Latency: 33.37 ms
Estimated Throughput: 32.95 TFLOPS

--- Phase 2: Memory Bandwidth Test ---
Transfer Size: 4 GB
Actual Bandwidth: 172.05 GB/s

--- Phase 3: Memory Capacity Stress Test ---
Attempting to allocate 8 GB of GPU memory...
Killed
```

Task Manager, screenshot attachment 2

<img width="860" height="359" alt="Image" src="https://github.com/user-attachments/assets/1c36f2e7-1e41-4176-b994-67091bc4b25a" />
