# PyTorch Docker container does not run

> **Issue #1155**
> **状态**: closed
> **创建时间**: 2020-06-21T02:54:39Z
> **更新时间**: 2020-06-22T14:59:34Z
> **关闭时间**: 2020-06-22T14:51:18Z
> **作者**: devksingh4
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1155

## 描述

Hello, 
After following these instructions: 
[https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#recommended-install-using-published-pytorch-rocm-docker-image](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#recommended-install-using-published-pytorch-rocm-docker-image), I run `PYTORCH_TEST_WITH_ROCM=1 python test/run_test.py --verbose` and get `No module named torch`. This is running in the Docker container. 

System: 
AMD Ryzen 5 1600AF
AMD RX 580 8GB 
Ubuntu 18.04.4 LTS - Kernel 5.3.0-59
`rocminfo` shows `ROCk module is loaded`, GPU is shown as Agent 2.


---

## 评论 (3 条)

### 评论 #1 — rkothako (2020-06-22T06:48:47Z)

Hi @devksingh4 
Please try with PYTORCH_TEST_WITH_ROCM=1 **python3.6** test/run_test.py --verbose

---

### 评论 #2 — devksingh4 (2020-06-22T14:51:18Z)

That does work! Jupyter Lab doesn't launch in this environment, but I suspect that's another issue, I'll file another bug. 

The documentation should be changed to reflect this, no? 

---

### 评论 #3 — Rmalavally (2020-06-22T14:59:34Z)

The AMD ROCm documentation is updated to reflect this correction at:

https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#building-pytorch-for-rocm

Thank you for reaching out.

---
