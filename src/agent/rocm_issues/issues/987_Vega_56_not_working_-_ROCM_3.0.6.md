# Vega 56 not working - ROCM 3.0.6

> **Issue #987**
> **状态**: closed
> **创建时间**: 2019-12-30T22:51:25Z
> **更新时间**: 2023-12-18T15:50:37Z
> **关闭时间**: 2023-12-18T15:50:37Z
> **作者**: tgwaste
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/987

## 描述

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


---

## 评论 (10 条)

### 评论 #1 — preda (2020-01-02T09:53:59Z)

#977

---

### 评论 #2 — derekwin (2020-01-16T01:23:12Z)

I got the same error when I install on ubuntu19，and my gpu is  RX580.

---

### 评论 #3 — tgwaste (2020-01-16T02:02:24Z)

I decided to just use 18.04 and the standard drivers.
Get them and then just do:

[Download Drivers](https://www.amd.com/en/support/graphics/radeon-rx-vega-series/radeon-rx-vega-series/radeon-rx-vega-56)

```
sudo apt-get install --install-recommends linux-generic-hwe-18.04
sudo dpkg --add-architecture i386
tar -xvf amdgpu-pro-19.50-967956-ubuntu-18.04.tar.xz
cd /root/amdgpu-pro-19.50-967956-ubuntu-18.04
./amdgpu-pro-install -y --opencl=legacy,pal
apt-get -y install ocl-icd-opencl-dev clinfo libpci-dev
```

Super simple.  Both my Vegas work perfectly now.


---

### 评论 #4 — derekwin (2020-01-16T02:33:19Z)

> I decided to just use 18.04 and the standard drivers.
> Get them and then just do:
> 
> ```
> sudo apt-get install --install-recommends linux-generic-hwe-18.04
> sudo dpkg --add-architecture i386
> tar -xvf amdgpu-pro-19.30.tar.xz
> cd /root/amdgpu-pro-19.30-934563-ubuntu-18.04
> ./amdgpu-pro-install -y --opencl=legacy,pal
> apt-get -y install ocl-icd-opencl-dev clinfo libpci-dev
> ```
> 
> Super simple. Both my Vegas work perfectly now.

Thank you .

---

### 评论 #5 — markkdev (2020-01-25T08:36:34Z)

@tgwaste is this something you do after installing rocm-dkms ? I'm just starting out and I keep running into issues with multi gpu use. Running a vega 64 and rx580. Thanks

---

### 评论 #6 — tgwaste (2020-01-25T16:33:56Z)

No, you cant have both together.  Start with a fresh system then do the steps I posted.  Obviously you need to go to AMD site and download the drivers.  This **amdgpu-pro-19.30.tar.xz** is just for reference. I'll update my post with the download link.



---

### 评论 #7 — markkdev (2020-01-26T02:18:49Z)

@tgwaste appreciate that. So is rocm not even needed for tensorflow training on AMD? I was under the impression that that's what gave AMD GPUs the capability.



---

### 评论 #8 — jcdutton (2020-01-29T12:07:08Z)

FIX (Workaround) AVAILABLE:  As per: https://github.com/RadeonOpenCompute/ROCm/issues/977

My PC has 2 RAM chips. 16GB per chip. Previously both chips were on node0. As per the motherboard manual for installing 2 chips.
If I move the RAM so that 1 chip is on node0 and the other chip is on node1.
clinfo now detects my GPU.
So, my advice for the people seeing this problem is to re-arrange the RAM chips into different slots.
This bug still needs fixing though. Or at least a more useful error message so the user knows they need to move RAM chips about.
This problem is only a problem on CPUs that have more than one node.
I have a Threadripper 1950X which has two nodes. node0 and node1
Example:
ls /sys/devices/system/node/node0
If it includes "memory0" to "memoryNNN"  it is good RAM layout.
If there are no "memory" entries, the RAM is NOT GOOD layout.
ls /sys/devices/system/node/node1
If it includes "memoryXXX" to "memoryNNN"  it is good RAM layout.
If there are no "memory" entries, the RAM is NOT GOOD layout.

You need at least some memory entries on each node0 and node1

---

### 评论 #9 — nartmada (2023-12-13T23:32:38Z)

Hi @tgwaste, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #10 — nartmada (2023-12-18T15:50:37Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
