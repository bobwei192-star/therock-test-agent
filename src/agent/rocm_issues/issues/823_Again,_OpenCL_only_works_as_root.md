# Again, OpenCL only works as root

> **Issue #823**
> **状态**: closed
> **创建时间**: 2019-06-18T04:24:08Z
> **更新时间**: 2019-08-05T11:17:50Z
> **关闭时间**: 2019-08-05T11:17:50Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/823

## 描述

A program running as regular user does not start. Error:

ocl.getPlatformIDs returned error=-1001 and 0 platforms

but it starts when run as root.


---

## 评论 (9 条)

### 评论 #1 — vastech73 (2019-06-18T05:15:48Z)

Valerie,
can you pls let us know what application were you running ?
Moreover, Could you retry installing rocm/OpenCL and check ?


---

### 评论 #2 — valeriob01 (2019-06-18T05:26:29Z)

First, my name is Valerio.
Second, ROCm already installed.
Application: https://github.com/preda/gpuowl


---

### 评论 #3 — vastech73 (2019-06-18T05:54:29Z)

Valerio,
We will come back to you post checking this internally.
Vasu

---

### 评论 #4 — valeriob01 (2019-06-18T05:57:15Z)

Thanks.


---

### 评论 #5 — valeriob01 (2019-06-19T07:13:05Z)

This is a real problem with some batch systems that do not allow jobs to run as root.


---

### 评论 #6 — vastech73 (2019-06-19T10:50:39Z)

Valerio,
Did you add the user to video group by issuing this command : “sudo usermod -a -G video  $LOGNAME” 
Pls confirm. We have checked internally without adding the user to this group and we see the same issue that has been raised.
Thanks,
Vasu

---

### 评论 #7 — valeriob01 (2019-06-19T11:10:16Z)

Yes, I have added all users to the video group. I would not post this issue if it was so simple to resolve.


---

### 评论 #8 — valeriob01 (2019-06-23T04:59:29Z)

I have found how to resolve the issue partially.
The file /etc/OpenCL/vendors/amdocl64.icd has owner root and group root. Assigning this ownership to a regular user makes that user able to run OpenCL applications.


---

### 评论 #9 — valeriob01 (2019-08-05T11:17:50Z)

I am closing this issue because after a full month there is no feedback. Will reopen new issue if needed.

---
