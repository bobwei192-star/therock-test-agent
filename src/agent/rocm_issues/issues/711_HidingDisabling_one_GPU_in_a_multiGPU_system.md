# Hiding/Disabling one GPU in a multiGPU system

> **Issue #711**
> **状态**: closed
> **创建时间**: 2019-02-17T23:17:26Z
> **更新时间**: 2019-02-19T15:27:52Z
> **关闭时间**: 2019-02-19T15:27:52Z
> **作者**: SandboChang
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/711

## 标签

- **Question** (颜色: #cc317c)

## 描述

Background: ubuntu 18.04, ROCm 2.1
GPUs: Vega FE*2, Radeon VII*1

Would there be a way to hide one GPU in the system?
I am trying to run some tests with the GPUs, but many of the benchmark scripts do not allow selecting a particular GPU device. Thus if I can hide the GPU from the software it will be very helpful.

With Nvidia's card, it seems like this can be done by "CUDA_VISIBLE_DEVICES" to hide a GPU from a test. Would there be a similar feature in ROCm?

---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2019-02-18T16:47:39Z)

We make this avaialble as a language-level feature rather than a ROCm-wide feature. So depending on the programming language your benchmark uses, you will need to set a different environment variable:

- OpenCL: [GPU_DEVICE_ORDINAL](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-2.1.0/runtime/utils/flags.hpp#L43) is a comma-separated list of the devices you would like to be visible to your OpenCL-using application.
- HIP: [HIP_VISIBLE_DEVICES](https://github.com/ROCm-Developer-Tools/HIP/blob/roc-2.1.0/src/hip_hcc.cpp#L1255) is a comma-separated list of devices you would like to be visible to your HIP-using application.
- HCC: [HCC_DEFAULT_GPU](https://github.com/RadeonOpenCompute/hcc/blob/roc-2.1.0/lib/hsa/mcwamp_hsa.cpp#L3772) can be used to automatically change which GPU HCC will use for GPU offload.

---

### 评论 #2 — SandboChang (2019-02-19T02:22:18Z)

> We make this avaialble as a language-level feature rather than a ROCm-wide feature. So depending on the programming language your benchmark uses, you will need to set a different environment variable:
> 
> * OpenCL: [GPU_DEVICE_ORDINAL](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-2.1.0/runtime/utils/flags.hpp#L43) is a comma-separated list of the devices you would like to be visible to your OpenCL-using application.
> * HIP: [HIP_VISIBLE_DEVICES](https://github.com/ROCm-Developer-Tools/HIP/blob/roc-2.1.0/src/hip_hcc.cpp#L1255) is a comma-separated list of devices you would like to be visible to your HIP-using application.
> * HCC: [HCC_DEFAULT_GPU](https://github.com/RadeonOpenCompute/hcc/blob/roc-2.1.0/lib/hsa/mcwamp_hsa.cpp#L3772) can be used to automatically change which GPU HCC will use for GPU offload.

Thanks a lot for your detailed reply. I should have been more specific, I am trying to run some benchmarks which were provided here:
https://github.com/tensorflow/benchmarks/tree/master/scripts/tf_cnn_benchmarks

So it is using Tensorflow with ROCm. In this case, I am not sure if it falls into the category of OpenCL/HIP/HCC. Appreciated if you can let me know.

---

### 评论 #3 — jlgreathouse (2019-02-19T14:55:08Z)

[AMD's TensorFlow implementation](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues) uses the HIP language runtime, so you should probably use `HIP_VISIBLE_DEVICES`.

---

### 评论 #4 — SandboChang (2019-02-19T15:25:32Z)

Thanks, by adding this line HIP_VISIBLE_DEVICES=2 in front of python3 ....benchmark...., I was able to run it on the desired GPU.

---
