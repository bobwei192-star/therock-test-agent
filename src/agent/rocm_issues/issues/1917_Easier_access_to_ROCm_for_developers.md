# Easier access to ROCm for developers

> **Issue #1917**
> **状态**: closed
> **创建时间**: 2023-03-05T14:51:01Z
> **更新时间**: 2024-10-11T15:46:05Z
> **关闭时间**: 2024-10-11T15:46:05Z
> **作者**: laoshaw
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1917

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

I can develop with OneAPI and CUDA easily these days in cloud(for CUDA I can develop locally with my graphic card), but it's very hard or impossible to find hardware or cloud platform to run ROCm code, is there a platform for me to try out the ROCm stack? does AMD provide some cloud platform for that so people can actually write software with MI2xx now?



---

## 评论 (1 条)

### 评论 #1 — jamesxu2 (2024-10-11T15:46:05Z)

Hi @laoshaw , there are a couple of options for trying out the ROCm stack:
1. If you have an Nvidia GPU for local testing - ROCm's programming interface is called [HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/) and provides a cross-platform C++ API that allows you to run the ROCm stack on Nvidia or AMD hardware. You can see the discussion on this issue for more details: https://github.com/ROCm/HIP/issues/3582. There's also plenty of information on the [HIP FAQ](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/faq.html#is-hip-a-drop-in-replacement-for-cuda) about compiling for Nvidia devices.
2. You can purchase an AMD GPU for local testing - See our [ROCm supported devices](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-gpus)
3. You can actually run HIP programs without a GPU - There is a library called HIP-CPU that is in active development to enable a subset of the ROCm stack on a much wider range of platforms. See the [HIP-CPU introductory documentation here](https://github.com/ROCm/HIP-CPU/blob/master/docs/overview.md). 
4. AMD has its own cloud platform to run the ROCm stack with MI2XX and MI3XX devices - https://aac.amd.com/ . 

---
