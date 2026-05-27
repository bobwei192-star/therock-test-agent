# No AMD GPUs specified

> **Issue #1742**
> **状态**: closed
> **创建时间**: 2022-05-20T17:22:08Z
> **更新时间**: 2024-02-02T22:43:06Z
> **关闭时间**: 2024-02-02T22:43:06Z
> **作者**: krzysztofMajchrzak-GIT
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1742

## 描述

Hi can you please help me with this? I am remotly connected to a miner rig with 12 AMD GPUs. The OS is Ubuntu 18.04.6 LTS. 

``` 
Graphics:  Card-1: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-2: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-3: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-4: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-5: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-6: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-7: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-8: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-9: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-10: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-11: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-12: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Display Server: N/A
           drivers: amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu
           tty size: 212x85 Advanced Data: N/A out of X
```

As you can see all of them have amdgpu drivers installed. After following official documentation I have managed to install every single version of rocm from 3.0 to 5.1. Everytime I had the same problem:

```
 ======================= ROCm System Management Interface =======================
WARNING: No AMD GPUs specified
================================= Concise Info =================================
GPU  Temp  AvgPwr  SCLK  MCLK  Fan  Perf  PwrCap  VRAM%  GPU%
================================================================================
============================= End of ROCm SMI Log ==============================

```
No devices were recognized. I need rocm for tensorflow AI project. But have no clue why it does not work. Please help me. If any additional information is needed please tell me what to provide. 

One more piece of info that maybe important. There is/was a cuda installed on this ubuntu. 


---

## 评论 (5 条)

### 评论 #1 — xuhuisheng (2022-05-20T17:47:05Z)

Looks like there is no ePCI3 AtomicOp supports.
You can check by `dmesg |grep kfd`.

If you find something like this, it said that your motherboard or cpu cannot support PCI atomics, so we cannot use gfx803 on ROCm.

`kfd: skipped device 1002:7300, PCI rejects atomics`

Here is the requirement : 
<https://github.com/RadeonOpenCompute/ROCm/tree/rocm-4.5.2#supported-cpus>


---

### 评论 #2 — krzysztofMajchrzak-GIT (2022-05-20T18:12:05Z)

Is there any workaround? Or this hardware is not cooparable with tensorflow at all?

---

### 评论 #3 — xuhuisheng (2022-05-20T19:56:11Z)

If it is the PCIe-AtomicsOp issue. It is said your hardware cannot support ROCm with gfx803.
Not only tf, but also all of ROCm components. The only way is upgrade your hardware, e.g. vega56/64, radeon vii, mi100, mi200, rx6800xt.

---

### 评论 #4 — abhimeda (2024-01-26T05:25:05Z)

@krzysztofMajchrzak-GIT  Hi, is your issue resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #5 — nartmada (2024-02-02T22:43:06Z)

Closing the ticket.  
@krzysztofMajchrzak-GIT, ROCm 6.0.2 supported configuration can be found at https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html.

---
