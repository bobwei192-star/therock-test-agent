# slow shutdown/reboot on 16.04 LTS

> **Issue #230**
> **状态**: closed
> **创建时间**: 2017-10-19T21:13:59Z
> **更新时间**: 2017-10-23T14:15:14Z
> **关闭时间**: 2017-10-23T14:15:14Z
> **作者**: rijujohnx
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/230

## 描述

I am using the latest version of ROCm kernel and Xubuntu 16.04.  After installing the ROCm kernel I am experiencing very slow shutdown/reboot.  It takes approximately 3-4 minutes after "reached target shutdown"

NOTE: I have 8 amd gpu's connected using amdgpu-pro driver 17.30 

---

## 评论 (2 条)

### 评论 #1 — preda (2017-10-23T07:11:45Z)

I think you're not supposed to mix ROCm with amdgpu-pro. Choose and keep only one.


---

### 评论 #2 — gstoner (2017-10-23T14:15:14Z)

Yes your mixing and matching components this is not supported 

---
