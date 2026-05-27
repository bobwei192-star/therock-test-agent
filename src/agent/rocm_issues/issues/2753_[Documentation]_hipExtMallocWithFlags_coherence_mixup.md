# [Documentation] hipExtMallocWithFlags coherence mixup

> **Issue #2753**
> **状态**: closed
> **创建时间**: 2023-12-19T18:14:46Z
> **更新时间**: 2024-01-18T16:32:02Z
> **关闭时间**: 2024-01-18T16:32:01Z
> **作者**: gilbertlee-amd
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/2753

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

https://rocm.docs.amd.com/en/latest/conceptual/gpu-memory.html#coherence

There appear to be a number of typos in this section.

The hipHostMallocDefault flag should be hipDeviceMallocDefault and have coarse-grained coherence.
The coherence for hipDeviceMallocFinegrained should be fine-grained.

