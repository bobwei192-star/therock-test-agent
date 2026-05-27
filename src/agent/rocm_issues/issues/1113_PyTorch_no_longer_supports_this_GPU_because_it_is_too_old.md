# PyTorch no longer supports this GPU because it is too old.

> **Issue #1113**
> **状态**: closed
> **创建时间**: 2020-05-20T00:56:43Z
> **更新时间**: 2021-06-02T12:25:45Z
> **关闭时间**: 2021-06-02T12:25:45Z
> **作者**: piondeno
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1113

## 描述

Dear all
The environment is :
CPU : ryzen 1800x
GPU : RX570 or VEGA-56
ROCm : 3.3
Pytorch : 1.4
OS : unbuntu 18.04

Each time I run the code in Pytorch with GPU, it will show the following warning message:
/home/datakey/.local/lib/python3.7/site-packages/torch/cuda/__init__.py:87: UserWarning: 
    Found GPU0 Vega 10 XT [Radeon RX Vega 64] which is of cuda capability 3.0.
    PyTorch no longer supports this GPU because it is too old.
    The minimum cuda capability that we support is 3.5.

No matter which GPU that I used, RX570 or VEGA-56.

And the command :　
torch._C._cuda_getCompiledVersion()
Out[2]: 303

Is there any one encounter same situation as me ?
Will it affect the computing efficient of Pytorch with such situation?
Thanks


 

---

## 评论 (6 条)

### 评论 #1 — ableeker (2020-05-20T20:39:50Z)

CUDA? CUDA is an Nvidia interface that only works on Nvidia GPU's, and definitly not on AMD GPU's.

---

### 评论 #2 — Djip007 (2020-05-21T09:37:16Z)

may be have a look here for pytorch release for rocm:
https://github.com/ROCmSoftwarePlatform/pytorch

---

### 评论 #3 — piondeno (2020-05-22T09:21:48Z)

Thanks for advise
I do not find any information about this yet.
So you never encounter such warning information before?

---

### 评论 #4 — gootsing (2020-10-19T06:44:12Z)

That's because the computing capability is hard coded by AMD with 3.0, which is actually meaningless. It doesn't seem matter since I checked the runtime GPU information, it reaches 100% GPU usage when it's running with this warning information. If you look into the ROCM source, you can find the following in hip_hcc.cpp:
    // Masquerade as a 3.0-level device. This will change as more HW functions are properly
    // supported. Application code should use the arch.has* to do detailed feature detection.
    prop->major = 3;
    prop->minor = 0;
So in theory you may change this as you wish if you build ROCM of your own.

---

### 评论 #5 — ROCmSupport (2021-03-03T09:30:41Z)

Hi @piondeno 
Thanks for reaching out.
Recommend you to check with the latest ROCm 4.0 or 4.1 and with Vega64 and update asap.
So that I will move it forward.
Thank you.

---

### 评论 #6 — ROCmSupport (2021-06-02T12:25:45Z)

Closing this as there is no update/response from user for more than a month.
Feel free to open a new issue if any.
Thank you.

---
