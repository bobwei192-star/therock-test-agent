# `hipMemcpy` from device to host stuck on device 1

> **Issue #2418**
> **状态**: closed
> **创建时间**: 2023-08-29T21:49:58Z
> **更新时间**: 2023-09-04T15:39:44Z
> **关闭时间**: 2023-09-04T15:39:44Z
> **作者**: MasterJH5574
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2418

## 描述

## Description

Our workstation has two Radeon RX 7900 XTX cards. Today we tried the following code stuck on the `hipMemcpy` line at the end.

```c++
#include <hip/hip_runtime.h>

#include <cstdlib>
#include <iostream>
#include <vector>

constexpr int error_exit_code = -1;

/// \brief Checks if the provided error code is \p hipSuccess and if not,
/// prints an error message to the standard error output and terminates the program
/// with an error code.
#define HIP_CHECK(condition)                                                                \
    {                                                                                       \
        const hipError_t error = condition;                                                 \
        if(error != hipSuccess)                                                             \
        {                                                                                   \
            std::cerr << "An error encountered: \"" << hipGetErrorString(error) << "\" at " \
                      << __FILE__ << ':' << __LINE__ << std::endl;                          \
            std::exit(error_exit_code);                                                     \
        }                                                                                   \
    }

int main(const int argc, const char** argv)
{
    int                dev_id = 1;      // <==== use device id 1
    float*             d_a{};
    std::vector<float> h_a(10);
    HIP_CHECK(hipSetDevice(dev_id));

    HIP_CHECK(hipMalloc(&d_a, 10 * sizeof(float)));

    std::cout << "start to copy from device to host\n";
    HIP_CHECK(hipMemcpy(h_a.data(), d_a, sizeof(float) * 10, hipMemcpyDeviceToHost));    //  <==== stuck here
    std::cout << "finish copying from device to host\n";
    return 0;
}
```

The code simply allocates memory on GPU 1, and copies the memory content back to host, and it gets stuck on `hipMemcpy`.

NOTE: If we use GPU 0 by setting `dev_id` to 0, the code works perfectly and does not get stuck on `hipMemcpy`. **It only gets stuck for GPU 1.** Using env variable `ROCR_VISIBLE_DEVICES=1` and make `dev_id = 0` does not resolve the issue.

We further test the official matrix multiplication examples at https://github.com/amd/rocm-examples/blob/develop/HIP-Basic/matrix_multiplication/main.hip. If we don’t change anything, the program happen for GPU 0 and work smoothly. When we change to use GPU 1 by either `hipSetDevice(1)` or `ROCR_VISIBLE_DEVICES=1`, the program gets stuck. So we suppose there might be some internal issue of ROCm when it comes with multiple GPUs.

------

## Workstation Environment

* CPU: AMD Ryzen 9 7950X
* GPU: 2 x AMD Radeon RX 7900 XTX
* OS: Ubuntu 22.04
* ROCm Driver: ROCm 5.6 (installed following https://docs.amd.com/en/docs-5.6.0/deploy/linux/installer/install.html)
