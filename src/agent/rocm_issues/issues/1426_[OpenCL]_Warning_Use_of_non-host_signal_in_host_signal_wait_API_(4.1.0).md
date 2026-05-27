# [OpenCL] Warning: Use of non-host signal in host signal wait API (4.1.0)

> **Issue #1426**
> **状态**: closed
> **创建时间**: 2021-03-24T20:06:53Z
> **更新时间**: 2021-03-25T11:14:37Z
> **关闭时间**: 2021-03-25T11:14:37Z
> **作者**: ivanmlerner
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1426

## 描述

Hello, after the update to 4.1.0 I am getting a lot of this warning when running opencl applications:

`Warning: (!g_use_interrupt_wait || isIPC()) && "Use of non-host signal in host signal wait API." in virtual hsa_signal_value_t rocr::core::BusyWaitSignal::WaitRelaxed(hsa_signal_condition_t, hsa_signal_value_t, uint64_t, hsa_wait_state_t), <<private builds directory>>/hsa-rocr/src/ROCR-Runtime-rocm-4.1.0/src/core/runtime/default_signal.cpp:87`

It looks like it is making reference to the directory it was built from.

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-03-25T02:45:50Z)

Thanks @ivanmlerner for reaching out.
Can you please share your config like OS, Asic and all details of ROCm and also exact steps to reproduce the problem.
Thank you.

---

### 评论 #2 — ivanmlerner (2021-03-25T02:56:08Z)

Hello, I am running Arch Linux with a Ryzen 3600X and an RX5500XT GPU. I know they are not supported, so if it has anything to do with that I am sorry for the trouble.
I am using amdgpu with rocm-opencl-runtime and rocm-smi installed from the AUR and packaged [here](https://github.com/rocm-arch/rocm-arch).
I'll get more information and post them here.

---

### 评论 #3 — ROCmSupport (2021-03-25T11:14:37Z)

Hi @ivanmlerner 
I am not able to reproduce this here locally. I can not comment on arch linux, as we are not supporting it.
Thank you.

---
