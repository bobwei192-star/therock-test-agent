# Does ROCm 2.7.2 support APU V1000? especially V1807B?

> **Issue #890**
> **状态**: closed
> **创建时间**: 2019-09-20T08:19:03Z
> **更新时间**: 2023-12-18T16:47:58Z
> **关闭时间**: 2023-12-18T16:47:58Z
> **作者**: edward-yang-tw
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/890

## 描述

We are working with a V1807b based platform with RX Vega11 integrated GPPU. We would like to know if ROCm support this APU.

thanks!

---

## 评论 (4 条)

### 评论 #1 — tuxzz (2019-09-24T01:02:44Z)

Seems no, but you can use OpenCL instead.
From README.md
> The integrated GPUs in AMD APUs are not officially supported targets for ROCm. As described below, "Carrizo", "Bristol Ridge", and "Raven Ridge" APUs are enabled in our upstream drivers and the ROCm OpenCL runtime. However, they are not enabled in our HCC or HIP runtimes, and may not work due to motherboard or OEM hardware limitations. As such, they are not yet officially supported targets for ROCm.

---

### 评论 #2 — drkarsten (2019-10-01T14:11:26Z)

https://bruhnspace.com/en/bruhnspace-rocm-for-amd-apus/?cn-reloaded=1. 

---

### 评论 #3 — nartmada (2023-12-12T16:27:43Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #4 — nartmada (2023-12-18T16:47:58Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
