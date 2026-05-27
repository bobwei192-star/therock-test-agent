# hsa-ext-rocr-dev is broken since ROCm 2.9

> **Issue #981**
> **状态**: closed
> **创建时间**: 2019-12-23T07:57:16Z
> **更新时间**: 2023-12-14T11:35:43Z
> **关闭时间**: 2023-12-14T11:35:42Z
> **作者**: btspce
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/981

## 描述

When hsa-ext-rocr-dev is upgraded from ROCm repo 2.10 or 3.0 for image support clinfo segfaults and so does Darktable. Last version that worked was hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm from ROCm 2.9. Downgrading to package hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm solves the issue.

ROCm 2.2 to 2.9 works
2.10 and 3.0 does not.

AMD Raven Ridge APU 2700u Fedora 31 x64

---

## 评论 (6 条)

### 评论 #1 — vsrikarunyan (2019-12-26T05:56:35Z)

Yes, looks like it. Since the update to ROCm v3, my environment is broken. Output for `rocminfo` is as below

```
ROCk module is loaded
<username> is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.0/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

```

---

### 评论 #2 — DeadEnded (2020-01-15T16:32:52Z)

Just did a fresh install on Ryzen 2400G and getting this too... anyone have an idea when it might be addressed?

---

### 评论 #3 — btspce (2020-02-29T13:41:12Z)

Still broken in ROCm 3.1

---

### 评论 #4 — btspce (2020-04-21T08:19:01Z)

Still broken in ROCm 3.3

---

### 评论 #5 — nartmada (2023-12-13T23:15:16Z)

Hi @btspce, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #6 — btspce (2023-12-14T11:35:42Z)

I don't have this laptop anymore so I can't verify if it is fixed. Closing for now.

---
