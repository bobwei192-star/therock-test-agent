# Darktable stopped working after recent update

> **Issue #846**
> **状态**: closed
> **创建时间**: 2019-07-16T08:31:47Z
> **更新时间**: 2019-10-24T02:23:43Z
> **关闭时间**: 2019-10-24T02:23:43Z
> **作者**: Aceler
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/846

## 描述

Ubuntu 19.04, rocm from PPA. After recent update near 10-11 of july, darktable can't start with opencl enabled.

Console output and Backtrace:
[Console output.txt](https://github.com/RadeonOpenCompute/ROCm/files/3396058/Console.output.txt)
[darktable_bt_W0XY4Z.txt](https://github.com/RadeonOpenCompute/ROCm/files/3396059/darktable_bt_W0XY4Z.txt)

I use upstream kernel driver from kernel 5.0.0, but I also tried rocm driver with kernel 4.15 with the same outcome.

---

## 评论 (4 条)

### 评论 #1 — sarunasb (2019-07-23T14:36:34Z)

Confirmed, darktable 2.6, Linux 5.2.0-050200rc6-generic.

[darktable_bt_MDKM5Z.txt](https://github.com/RadeonOpenCompute/ROCm/files/3422569/darktable_bt_MDKM5Z.txt)


---

### 评论 #2 — pramenku (2019-07-28T07:55:33Z)

Please expect fix in ROCm2.7

---

### 评论 #3 — dahabakuk (2019-08-17T05:15:49Z)

updated to RCOm2.7 today on debian buster and darktable works again! thanks guys

---

### 评论 #4 — pramenku (2019-08-17T05:39:37Z)

Thanks for the update and good to know.
Please close this issue.

---
