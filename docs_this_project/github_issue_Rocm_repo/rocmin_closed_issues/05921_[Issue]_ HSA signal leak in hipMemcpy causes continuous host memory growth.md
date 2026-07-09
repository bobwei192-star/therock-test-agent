# [Issue]: HSA signal leak in hipMemcpy causes continuous host memory growth

- **Issue #:** 5921
- **State:** closed
- **Created:** 2026-02-02T09:43:44Z
- **Updated:** 2026-02-03T20:54:02Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5921

### Problem Description

# [Bug]: HSA signal leak in hipMemcpy causes continuous host memory growth

## Description

Possible source for the issue https://github.com/ROCm/ROCm/issues/5915 which affects OpenCL and Hip/Sycl applications.

Host CPU memory (RSS) grows continuously during HIP memory copy operations due to HSA signals not being properly destroyed. The leak rate is approximately 2 HSA signals per `hipMemcpy` call, leading to ~300 MB leaked per 1000 iterations with 16 MB buffers.

This affects all applications using HIP for GPU compute, including GROMACS (SYCL/HIP), and other HPC workloads.

## Environment

- **OS:** AlmaLinux 9.7 (kernel 5.14.0-611.9.1.el9_7.x86_64)
- **GPU:** AMD Instinct MI210 / MI250X (gfx90a)
- **ROCm:** 7.1.1 and 7.2.0 (both affected)
- **Driver:** amdgpu-dkms 6.16.6 / 6.16.13

## Steps to Reproduce

### Minimal Reproducer

```cpp
// hip_memory_leak_test.cpp
// Compile: hipcc -O2 -o hip_memory_leak_test hip_memory_leak_test.cpp

#include <hip/hip_runtime.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

long get_rss_kb() {
    std::ifstream stat("/proc/self/status");
    std::string line;
    while (std::getline(stat, line)) {
        if (line.substr(0, 6) == "VmRSS:") {
            std::istringstream iss(line.substr(6));
            long rss; iss >> rss;
            return rss;
        }
    }
    return 0;
}

int main() {
    const size_t buffer_size = 16 * 1024 * 1024; // 16 MB
    const int iterations = 1000;

    std::vector<float> h_data(buffer_size / sizeof(float), 1.0f);
    void* d_ptr;
    hipMalloc(&d_ptr, buffer_size);

    long initial_rss = get_rss_kb();
    std::cout << "Initial RSS: " << initial_rss << " KB" << std::endl;

    for (int i = 0; i < iterations; i++) {
        hipMemcpy(d_ptr, h_data.data(), buffer_size, hipMemcpyHostToDevice);
        hipMemcpy(h_data.data(), d_ptr, buffer_size, hipMemcpyDeviceToHost);

        if ((i + 1) % 100 == 0) {
            long rss = get_rss_kb();
            std::cout << "Iteration " << (i + 1) << ": RSS = " << rss
                      << " KB (+" << (rss - initial_rss) << " KB)" << std::endl;
        }
    }

    hipFree(d_ptr);

    long final_rss = get_rss_kb();
    std::cout << "Final RSS: " << final_rss << " KB" << std::endl;
    std::cout << "Total leaked: " << (final_rss - initial_rss) << " KB" << std::endl;

    return 0;
}
```

### Run

```bash
hipcc -O2 -o hip_memory_leak_test hip_memory_leak_test.cpp
./hip_memory_leak_test
```

### Expected Output (no leak)

```
Initial RSS: ~40000 KB
Iteration 100: RSS = ~40000 KB (+0 KB)
...
Final RSS: ~40000 KB
Total leaked: 0 KB
```

### Actual Output (leak)

```
Initial RSS: 43424 KB
Iteration 100: RSS = 112000 KB (+68576 KB)
Iteration 200: RSS = 181000 KB (+137576 KB)
...
Iteration 1000: RSS = 388000 KB (+344576 KB)
Total leaked: 344576 KB (336 MB)
```

## Root Cause Analysis

Using `rocprofv3 --hsa-core-trace --hsa-amd-trace`, we identified the leak is in **HSA signal management**:

| HSA Operation | Count (50 iterations) |
|---------------|----------------------|
| `hsa_amd_signal_create` | 133 |
| `hsa_signal_create` | 14 |
| `hsa_signal_destroy` | 38 |
| **Signals leaked** | **109** (~2.2 per hipMemcpy) |
| `hsa_amd_memory_pool_allocate` | 4 |
| `hsa_amd_memory_pool_free` | 1 |
| **Pool allocations leaked** | **3** |

Each `hipMemcpy` creates HSA signals for synchronization that are not being destroyed. Over extended workloads, this causes continuous memory growth.

## Additional Findings

### Operations that leak:

| Test | Description | Leak (1000 iter) |
|------|-------------|------------------|
| hipMemcpy H2D+D2H | Memory transfers | +336 MB |
| Kernel launch (default stream) | Using null stream | +61 MB |
| Kernel launch (multiple streams) | 4 streams round-robin | +180 MB |
| hipMemcpyAsync | Async transfers | +331 MB |

### Operations that DON'T leak:

| Test | Description | Leak |
|------|-------------|------|
| hipMalloc/hipFree only | No data transfer | +0 KB |
| Kernel launch (single explicit stream) | Persistent stream | +0 KB |

### Partial workaround:

Setting `HSA_ENABLE_SDMA=0` reduces the leak by ~45% (336 MB → 183 MB), suggesting the SDMA path creates more signals than the shader copy path.

```bash
HSA_ENABLE_SDMA=0 ./hip_memory_leak_test
```

## Impact

- **GROMACS** and other HPC applications experience memory exhaustion on long-running jobs
- Leak rate observed in real workloads: ~70-90 GB/hour with ROCm 7.1.x, ~5-9 GB/hour with ROCm 7.2.0
- Jobs that should run for days fail within hours due to OOM

## Workarounds

1. **`HSA_ENABLE_SDMA=0`** - Reduces leak by ~45%
2. **Use single explicit HIP stream** - Avoids kernel dispatch leak (but doesn't fix hipMemcpy leak)
3. **Use stock in-kernel amdgpu driver with ROCm 6.1.3** - No leak observed (not practical for MI200 series)

## System Information

```
$ hipcc --version
HIP version: 7.2.0

$ rocminfo | grep -E "Name:|Marketing"
  Name:                    AMD EPYC 7452 32-Core Processor
  Marketing Name:          AMD Instinct MI210

$ cat /opt/rocm/.info/version
7.2.0
```

for more details see referenced report

## Attachments

Full reproducer with multiple test modes and job scripts available at:
- Reproducer covers: hipMalloc/Free, hipMemcpy, kernel launches, hipHostMalloc, hipMallocManaged, async operations
- Includes memory monitoring and rocprofv3 trace analysis scripts

### Operating System

AlmaLinux 9.7

### CPU

 AMD EPYC 7452 32-Core Processor

### GPU

MI210

### ROCm Version

7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

see referenced issue

### Additional Information

_No response_