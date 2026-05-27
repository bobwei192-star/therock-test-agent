# It is weired that RDNA2 support windows while Vega not

> **Issue #2053**
> **状态**: closed
> **创建时间**: 2023-04-15T13:01:54Z
> **更新时间**: 2024-01-24T20:17:48Z
> **关闭时间**: 2024-01-24T20:17:47Z
> **作者**: xuhuisheng
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/2053

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

Please refer here: <https://github.com/RadeonOpenCompute/ROCm/blob/19c0ba11505cf504d42b2096713d761236202361/docs/release/gpu_os_support.md?plain=1#L59-L60>

It is said that using Radeon Pro Driver, RDNA2 likes RX6900xt and Rx6600  can support HIP sdk and runtime on windows, while Radeon VII is not.

As we know, the `amdhip64.dll` is installed by amdgpu driver, so the HIP sdk and runtime should avaiable for both vega10, vega20, cdna, rdna2.

The documents seems point out there is special support on RDNA2, not for other ISA.

---

## 评论 (3 条)

### 评论 #1 — Roachomg (2023-04-16T12:55:39Z)

GCN的时代结束了...(唉)
Said goodbye to GCN.(/sigh)


---

### 评论 #2 — saadrahim (2023-04-16T23:55:40Z)

The list will be update when resolving #2044. 

---

### 评论 #3 — saadrahim (2024-01-24T20:17:47Z)

Hi @xuhuisheng,
Given the General Availability of the HIP SDK on Windows, I am closing this ticket. Please reopen if you have additional questions.

---
