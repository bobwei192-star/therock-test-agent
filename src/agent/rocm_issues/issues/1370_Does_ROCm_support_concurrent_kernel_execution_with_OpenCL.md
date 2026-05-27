# Does ROCm support concurrent kernel execution with OpenCL?

> **Issue #1370**
> **状态**: closed
> **创建时间**: 2021-02-04T07:41:28Z
> **更新时间**: 2021-02-09T07:30:53Z
> **关闭时间**: 2021-02-09T07:30:53Z
> **作者**: WyldeCat
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1370

## 描述

Let's suppose there are multiple command queues with single device.
If multiple cl_kernel with very small global work item size are enqueued to each queues, are they executed concurrently?

I'm using RX 5700 XT, ubuntu 20.04 and ROCm 3.10.0.

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-02-04T08:57:38Z)

Hi @WyldeCat 
Thanks for reaching out.
Yes, ROCm supports concurrent kernel execution with OpenCL but I feel not with all hardware.
I will get more information on supported hardware.

But I can not comment on RX5700 XT as we are not officially supporting them right now.

---

### 评论 #2 — WyldeCat (2021-02-05T02:19:35Z)

Thanks @ROCmSupport 
please let me know if RX6900 xt supports concurrent kernel execution.

---

### 评论 #3 — ROCmSupport (2021-02-05T04:46:29Z)

Hi @WyldeCat 
Got an update from OpenCL developer in below way.

_I think all ASICs supported by ROCM support concurrent execution. As long as there's no barrier to mandate a wait, cp would run kernels concurrently as long as hw resources are available._

Regarding RX6900, we are not supporting this hardware right now and so can not talk on this.

---

### 评论 #4 — ROCmSupport (2021-02-05T06:23:51Z)

Please let me know if you need any more information, otherwise I am going to close this issue.
Thank you.

---
