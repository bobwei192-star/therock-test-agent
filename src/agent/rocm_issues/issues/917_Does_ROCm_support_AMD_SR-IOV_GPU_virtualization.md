# Does ROCm support AMD SR-IOV GPU virtualization

> **Issue #917**
> **状态**: closed
> **创建时间**: 2019-10-22T09:43:54Z
> **更新时间**: 2023-12-15T07:22:29Z
> **关闭时间**: 2023-12-15T07:22:28Z
> **作者**: zhangyy91
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/917

## 描述

Hi, Guys, I am new to ROCm and GPU virtualization. I wonder if ROCm supports to run in a virtual machine with SR-IOV virtual GPUs.

---

## 评论 (3 条)

### 评论 #1 — heero-yuy (2019-12-24T06:24:33Z)

Hi,
ROCm didn't support the Virtual GPU usage, instead that have Docker can play a role under Host with mutliple GPU on same Host.

if need seperate Virtual Machine, maybe Linux KVM can use, but just only computing feature, there's no function related VDI usage on ROCm, thanks! 


---

### 评论 #2 — nartmada (2023-12-12T23:45:48Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #3 — zhangyy91 (2023-12-15T07:22:28Z)

@nartmada Thanks for your reply and I will close this issue.

---
