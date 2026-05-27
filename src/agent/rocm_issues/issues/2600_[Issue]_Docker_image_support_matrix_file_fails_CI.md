# [Issue]: Docker image support matrix file fails CI

> **Issue #2600**
> **状态**: closed
> **创建时间**: 2023-10-23T17:18:29Z
> **更新时间**: 2024-01-28T15:50:47Z
> **关闭时间**: 2024-01-28T15:50:46Z
> **作者**: danpetreamd
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2600

## 负责人

- danpetreamd

## 描述

### Problem Description

Run rst-lint /home/runner/work/ROCm/ROCm
ERROR [/home/runner/work/ROCm/ROCm/docs/release/docker_image_support_matrix.rst:8](https://github.com/RadeonOpenCompute/ROCm/blob/ce82a047bf98db3c5e71ab98df0c94c784e00440/docs/release/docker_image_support_matrix.rst?plain=1#L8) Unknown directive type "tab-set".
Error: Process completed with exit code 2.



### Operating System

N/A - this is a documentation only issue.

### CPU

N/A - this is a documentation only issue.

### GPU

N/A - this is a documentation only issue.

### ROCm Version

5.7.x

### ROCm Component

_No response_

### Steps to Reproduce

Any docs PR will fail with the above error.

### Output of /opt/rocm/bin/rocminfo --support

N/A - this is a documentation only issue.
