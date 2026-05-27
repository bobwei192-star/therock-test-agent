# tensorflow-rocm hangs when using GPU for graphic output

> **Issue #680**
> **状态**: closed
> **创建时间**: 2019-01-19T11:00:38Z
> **更新时间**: 2023-12-12T21:54:03Z
> **关闭时间**: 2023-12-12T21:54:03Z
> **作者**: kimia000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/680

## 描述

I installed ROCm and tensorflow-rocm on Ubuntu 18.04 according to the instruction. Everything is smooth but the python process freezes if going to another page (from terminal). For example, if checking a Chrome page over the terminal window (which needs the GPU to build a graphical output).

```
2019-01-19 10:30:29.215816: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2019-01-19 10:30:29.219253: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1530] Found device 0 with properties: 
name: Vega [Radeon RX Vega]
AMDGPU ISA: gfx900
memoryClockRate (GHz) 1.63
pciBusID 0000:43:00.0
Total memory: 7.98GiB
Free memory: 7.73GiB
2019-01-19 10:30:29.219277: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1641] Adding visible gpu devices: 0
2019-01-19 10:30:29.219296: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1051] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-01-19 10:30:29.219303: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1057]      0 
2019-01-19 10:30:29.219309: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1070] 0:   N 
2019-01-19 10:30:29.219346: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1189] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7524 MB memory) -> physical GPU (device: 0, name: Vega [Radeon RX Vega], pci bus id: 0000:43:00.0)
```
The problem is that I cannot abort the process/python script by Ctrl+C in the terminal, and the GPU remains occupied until I restart the machine. If I close the terminal and open it again,

```
terminate called after throwing an instance of 'std::runtime_error'
  what():  No device code available for function: _ZN10tensorflow7functor28FillPhiloxRandomKernelLaunchINS_6random19UniformDistributionINS2_12PhiloxRandomEfEEEEvS4_PNT_17ResultElementTypeExS6_
Aborted (core dumped)
```

Note that the issue is not about tensorflow, but the GPU driver, I think.

In any case, the key problem is that the device remains occupied and cannot be freed without a restart.

I think the issue occurs when the GPU is used for other tasks (not a computing task, just normal graphic output) while tensorflow is working.

---

## 评论 (2 条)

### 评论 #1 — tasso (2023-12-08T17:57:15Z)

Thanks for reaching out.  Is this still an issue?  if not; can we please close it?

---

### 评论 #2 — tasso (2023-12-12T21:54:03Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
