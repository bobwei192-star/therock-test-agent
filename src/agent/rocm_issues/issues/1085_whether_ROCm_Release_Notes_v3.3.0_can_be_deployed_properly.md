#  whether ROCm Release Notes v3.3.0 can be deployed properly

> **Issue #1085**
> **状态**: closed
> **创建时间**: 2020-04-21T02:14:20Z
> **更新时间**: 2021-03-17T07:06:10Z
> **关闭时间**: 2021-03-17T07:06:10Z
> **作者**: jackyin68
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1085

## 描述

Whether AMD ROCm Release Notes v3.3.0 can be deployed in Ubuntu 18.04..04?
Very confused, cost a lot of time, HSA_STATUS_ERROR_OUT_OF_RESOURCES cannot be resolved.
Kindly person can give the answer or give up?

---

## 评论 (11 条)

### 评论 #1 — MatPoliquin (2020-04-22T00:20:12Z)

I got the same problem You can role back to 3.1.1 by setting the rocm repo to:
`http://repo.radeon.com/rocm/apt/3.1.1/`
reinstall and reboot


---

### 评论 #2 — jackyin68 (2020-04-22T02:30:41Z)

thanks,ubuntu 18.04 Or ubuntu 18.03

---

### 评论 #3 — MatPoliquin (2020-04-22T13:58:19Z)

@jackyin68 I use Ubuntu 19.10

---

### 评论 #4 — jackyin68 (2020-04-23T01:32:30Z)

Great, I try again.  many compositions have been tried but failed. 

---

### 评论 #5 — jackyin68 (2020-04-23T01:35:20Z)

@MatPoliquin do your system work well?

---

### 评论 #6 — MatPoliquin (2020-04-23T09:23:42Z)

@jackyin68 Ubuntu 19.10 with rocm 3.1.1 on a RX580 works ok

---

### 评论 #7 — emerth (2020-04-25T17:32:52Z)

Check if your user account has R/W on /dev/kfd, and /dev/dri/*.
If not, change the account's group memberships or the file permissions to allow R/W and try again.
Note your udev subsystem probably resets the permissions on reboot. For udev, see udev documentation.

---

### 评论 #8 — jackyin68 (2020-04-28T11:16:34Z)

Rx550 does not work

---

### 评论 #9 — mochouaaaaa (2020-05-11T01:38:36Z)

The rx580 video card on Ubuntu 18.04 starts the training interface. The mouse can't click any event, and the training time is 60 times less than that of CPU. Have you ever encountered similar problems?

---

### 评论 #10 — ROCmSupport (2021-03-17T07:05:48Z)

Thanks @jackyin68 for reaching out.
I will take a look at this request.

---

### 评论 #11 — ROCmSupport (2021-03-17T07:06:10Z)

Hi @jackyin68 
As this issue is related to 3.3 and as we do not see any issues with ROCm 4.0 and 4.0 supports Ubuntu 20.04.1/18.04.5, I will close this issue.
Feel free to open a new issue if any.
Thank you.

---
