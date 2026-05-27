# OpenCL ICD?

> **Issue #1369**
> **状态**: closed
> **创建时间**: 2021-01-25T23:20:59Z
> **更新时间**: 2021-02-05T05:21:29Z
> **关闭时间**: 2021-02-05T05:21:29Z
> **作者**: yaxxie
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1369

## 描述

Does the ROCM distributions provide an OpenCL ICD file? If so, which component is it bundled with?
If not, is it possible to produce/provide one?

---

## 评论 (10 条)

### 评论 #1 — xuhuisheng (2021-01-25T23:50:25Z)

I am not familiar with OpenCL. Maybe this is what you look for.
https://github.com/RadeonOpenCompute/ROCm/blob/master/default.xml#L30

---

### 评论 #2 — ROCmSupport (2021-01-27T12:09:25Z)

Thanks @yaxxie for reaching us.
Hope you got the answer from previous comments.
Please let me know if you need more information.
Thank you.


---

### 评论 #3 — seesturm (2021-01-27T12:52:09Z)

Not exactly sure what the issue reporter is asking but I'd say the ICD (Installable Client Driver) is in file _/opt/rocm-4.0.0/opencl/lib/libamdocl64.so_ which is part of the _rocm-opencl_ package.

---

### 评论 #4 — yaxxie (2021-01-27T17:06:39Z)

I took a look at what some .icd files contain it seems to just contain an SO name -- what I was trying to get at was if the distribution could automatically set this up upon installation so that use doesn't need to put a .icd file containing the so-name into /etc/OpenCL/vendors/ (I'm also not sure how mine appears to work correctly because I didn't put the rocm installation on library path but it seems like openCL apps are automatically finding the rocm openCL)

---

### 评论 #5 — ROCmSupport (2021-02-01T06:03:08Z)

Hi @yaxxie 
I did not get your point completely.
In my case, when I install ROCm or OpenCL/ROCm, icd file will be mapped/created automatically as part of installation under /etc/OpenCL/vendors and things work perfect.
I never set anything manually and the things happened automatically for me.
Hope its clear.
Please let me know if you need more information. Else you/I can close this issue.
Thank you.

---

### 评论 #6 — yaxxie (2021-02-01T11:48:05Z)

Thanks if it is meant to be created automatically then I guess I'll just try yo figure out why that didn't happen in my case

---

### 评论 #7 — ROCmSupport (2021-02-01T13:56:02Z)

Yes, it meant to be created automatically.
Request to try on a fresh OS once and you will come to know.

Thank you.

---

### 评论 #8 — ROCmSupport (2021-02-04T05:46:55Z)

Hi @yaxxie 
Hope your issue is resolved, request you to close this ticket.
Thank you.

---

### 评论 #9 — yaxxie (2021-02-04T11:02:33Z)

I had this issue.

Another user mentioned same issue in another thread.

https://github.com/RadeonOpenCompute/ROCm/issues/567#issuecomment-756179833

Workaround is easy, so you can close at your discretion. 

---

### 评论 #10 — ROCmSupport (2021-02-05T05:21:29Z)

Thanks @yaxxie 
I am closing this as per the information shared by us.

---
