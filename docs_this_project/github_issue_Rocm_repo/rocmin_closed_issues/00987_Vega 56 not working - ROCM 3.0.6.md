# Vega 56 not working - ROCM 3.0.6

- **Issue #:** 987
- **State:** closed
- **Created:** 2019-12-30T22:51:25Z
- **Updated:** 2023-12-18T15:50:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/987

Sees it:

```
*******
Agent 3
*******
  Name:                    gfx900
  Marketing Name:          Vega 10 XL/XT [Radeon RX Vega 56/64]
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
```

**However**

```
# clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3052.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform
```

```
GPU  Temp   AvgPwr   SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%
1    28.0c  32.026W  300Mhz  300Mhz  16.86%  auto  175.0W    0%   0%
2    30.0c  3.0W     852Mhz  167Mhz  11.76%  auto  165.0W    0%   0%
```

```
# lspci  | grep AMD
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev e7)
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere HDMI Audio [Radeon RX 470/480 / 570/580/590]
02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470 (rev c3)
03:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XL/XT [Radeon RX Vega 56/64] (rev c3)
04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 HDMI Audio [Radeon Vega 56/64]
```

```
# /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices

  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```
