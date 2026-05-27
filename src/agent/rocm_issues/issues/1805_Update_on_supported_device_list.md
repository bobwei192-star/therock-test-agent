# Update on supported device list?

> **Issue #1805**
> **状态**: closed
> **创建时间**: 2022-09-07T01:46:38Z
> **更新时间**: 2023-10-27T16:10:49Z
> **关闭时间**: 2023-10-27T16:10:49Z
> **作者**: libeiqibns
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1805

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

The latest document on ROCm supported devices I found on AMD doc portal is this one:
https://docs.amd.com/bundle/Hardware_and_Software_Reference_Guide/page/Hardware_and_Software_Support.html

However, this document seems a little bit outdated. Some GitHub issues (such as https://github.com/RadeonOpenCompute/ROCm/issues/1803 ) claim cards that does not appear on this document can play ROCm (at least partially) as well. So I wonder if there is any update on ROCm supported device status. 

---

## 评论 (7 条)

### 评论 #1 — Rmalavally (2022-09-07T02:27:53Z)

Please refer to the ROCm Installation Guide for the latest information on supported devices. 

https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.2.3/page/Introduction_to_AMD_ROCm_Installation_Guide_for_Linux.html

Let us know if you cannot find the information you need.

ROCm Documentation Team

---

### 评论 #2 — libeiqibns (2022-09-09T07:27:14Z)

This makes me even more confused... Supported device on "Prerequisite" section on the installation guide clearly contradict with information listed on "Hardware and software support" document (https://docs.amd.com/bundle/Hardware_and_Software_Reference_Guide/page/Hardware_and_Software_Support.html). For example, RX Vega 64 and Radeon Instinct MI25 are listed as "supported" on "Hardware and software support", but does not appear on installation guide. 

By the way, I am using a AMD Radeon Pro WX 9100, which I believe has a "Navi 10" chip, to play ROCm. Neither does it appear on the installation guide.

---

### 评论 #3 — klausbu (2022-10-01T10:56:52Z)

When can we expect NAVI 22 and 23 support?

ALL current AMD notebook GPUs are NAVI 22/gfx1031 (RX 6700M and RX 6800M) or NAVI 23/gfx1032 (RX 6600M) and a lot of scientific and engineering software development (before investing in very expensive professional hardware based on a proof of concept, tests and benchmarks) and education (engineering and AI) is done on notebooks.

Is it really necessary that everybody preferring AMD hardware has to go through a partial, experimental source compilation enabled only by the enthusiast community to make it work on this widespread hardware?

I don`t get it, buy a CPU and every compiler will support it out of the box or within weeks, buy a GPU and you may have to wait for months or years or forever due to artificially imposed limitations.

---

### 评论 #4 — jmcelroy01 (2022-10-01T20:40:16Z)

Also interested in clear support for Navi 23, in particular on Linux. [Here](https://github.com/krrishnarraj/clpeak/issues/94) and [here](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/151) and [here](https://github.com/RadeonOpenCompute/ROCm/issues/1756) show my and others' ongoing efforts in making things work on OpenSUSE and other distros. 

Using `HSA_OVERRIDE_GFX_VERSION=10.3.0` and `AMD_LOG_LEVEL=4` shows that the 6700s can work with tensorflow on Tumbleweed, but there are some kinks to work out.

```
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

2022-07-28 18:40:55.942148: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

[name: "/device:CPU:0"
 device_type: "CPU"
 memory_limit: 268435456
 locality {
 }
 incarnation: 742499257225071470
 xla_global_id: -1,
 name: "/device:GPU:0"
 device_type: "GPU"
 memory_limit: 8048869376
 locality {
   bus_id: 1
   links {
     link {
       device_id: 1
       type: "StreamExecutor"
       strength: 1
     }
   }
 }
 incarnation: 11711825762745260538
 physical_device_desc: "device: 0, name: AMD Radeon RX 6700S, pci bus id: 0000:03:00.0"
 xla_global_id: 416903419,
 name: "/device:GPU:1"
 device_type: "GPU"
 memory_limit: 300941312
 locality {
   bus_id: 1
   links {
     link {
       type: "StreamExecutor"
       strength: 1
     }
   }
 }
 incarnation: 4568022636384927665
 physical_device_desc: "device: 1, name: , pci bus id: 0000:07:00.0"
 xla_global_id: 2144165316]

2022-07-28 18:40:55.945451: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
....
2022-07-28 18:40:55.945930: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /device:GPU:0 with 7676 MB memory:  -> device: 0, name: AMD Radeon RX 6700S, pci bus id: 0000:03:00.0
....
:3:rocdevice.cpp            :416 : 156258780086 us: 9631 : [tid:0x7fd0be49e440] Initializing HSA stack.
:3:comgrctx.cpp             :33  : 156258811776 us: 9631 : [tid:0x7fd0be49e440] Loading COMGR library.
:3:rocdevice.cpp            :207 : 156258811867 us: 9631 : [tid:0x7fd0be49e440] Numa selects cpu agent[0]=0x55c55077abe0(fine=0x55c550751970,coarse=0x55c54ef6a220) for gpu agent=0x55c5531ca1d0
:3:rocdevice.cpp            :1611: 156258812159 us: 9631 : [tid:0x7fd0be49e440] HMM support: 1, xnack: 0, direct host access: 0

:4:rocdevice.cpp            :1918: 156258812446 us: 9631 : [tid:0x7fd0be49e440] Allocate hsa host memory 0x7fcfb2d00000, size 0x101000
....
:3:rocdevice.cpp            :207 : 156258812959 us: 9631 : [tid:0x7fd0be49e440] Numa selects cpu agent[0]=0x55c55077abe0(fine=0x55c550751970,coarse=0x55c54ef6a220) for gpu agent=0x55c5531c6070
....
```

---

### 评论 #5 — greymogh (2022-10-31T10:02:01Z)

> Please refer to the ROCm Installation Guide for the latest information on supported devices.
> 
> https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.2.3/page/Introduction_to_AMD_ROCm_Installation_Guide_for_Linux.html
> 
> Let us know if you cannot find the information you need.
> 
> ROCm Documentation Team

Hello,

-> page not found

Thanks

---

### 评论 #6 — jmcelroy01 (2022-10-31T10:31:07Z)

[https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.2.3/page/How_to_Install_ROCm.html](https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.2.3/page/How_to_Install_ROCm.html)

Also, the [https://repo.radeon.com/amdgpu/latest/sle/15.4/main/x86_64/](https://repo.radeon.com/amdgpu/latest/sle/15.4/main/x86_64/) repo is not needed on Tumbleweed, and doesn't work anyway because of their libffi.so.7 dependency (TW is on libffi.so.8 now). libwayland, libdrm, Mesa, etc. are all in Opensuse/Packman repos. I just added the ROCm repo. No need to go through the trouble of specifying use cases, you can just install the packages you want with Yast. 

---

### 评论 #7 — samjwu (2023-10-27T16:09:37Z)

Supported GPUs list for Linux and Windows as of ROCm 5.7.1

Linux: https://rocm.docs.amd.com/en/docs-5.7.1/release/gpu_os_support.html

Windows: https://rocm.docs.amd.com/en/docs-5.7.1/release/windows_support.html

---
