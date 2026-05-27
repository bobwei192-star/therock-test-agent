# How to Share GPU Memories?

> **Issue #721**
> **状态**: closed
> **创建时间**: 2019-02-28T16:11:20Z
> **更新时间**: 2019-03-08T20:05:19Z
> **关闭时间**: 2019-03-08T20:05:19Z
> **作者**: ali-masoudi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/721

## 描述

Hi Guys
I have 2 x RX580 each 8GB, on Ubuntu 16.04
I want to know is it possible two share memories between 2 GPUs and gain 16GB Memory?
How about computing power?
I am using Tensorflow-rocm
 

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-03-08T20:05:19Z)

If you are asking specifically about how to use >1 GPU in tensorflow, I recommend asking this question in the [ROCm TensorFlow issue tracker](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues).

If you are more generally asking if you can allocate memory on one GPU and access it from another -- at this time I do not believe this is possible in the general case (though you can do P2P transfers between the devices).

There's also little to no benefit to doing so even if you could. You would still need to go over your limited PCIe bus to go between the cards. In this case, you're probably better off putting your data on the host (e.g. in OpenCL using the `CL_MEM_USE_HOST_PTR` or `CL_MEM_ALLOC_HOST_PTR` flags). You can allocate more data in host memory than can fit in your GPU's memory. This is perfectly legal in ROCm and I just tested it on multiple of my own GPUs.

---
