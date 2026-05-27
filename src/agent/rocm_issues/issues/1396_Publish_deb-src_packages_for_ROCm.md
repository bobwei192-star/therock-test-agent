# Publish deb-src packages for ROCm

> **Issue #1396**
> **状态**: closed
> **创建时间**: 2021-03-01T11:29:00Z
> **更新时间**: 2021-03-22T07:14:58Z
> **关闭时间**: 2021-03-22T04:05:53Z
> **作者**: klausman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1396

## 描述

As per the subject. Currently, only the binary debs are available.

In cases like [issue 1236](https://github.com/RadeonOpenCompute/ROCm/issues/1236), working around dependencies that are not available (and not strictly required), it would be much easier to take a deb-src, tweak what is needed and then build one's own packages from that, rather than having to take apart a binary package or forcing installation and breaking the dependency tree.

---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-03-01T11:39:52Z)

Thanks @klausman for reaching out.
I will check this for you and get back asap.

---

### 评论 #2 — ROCmSupport (2021-03-22T04:05:53Z)

Hi @klausman 
I got an update for you.

We only support Ubuntu 18.04 and 20.4 officially. This python3.8 is one of the reason we cannot support 16.04 because it does not have python3.8. Supporting other OS/versions are expensive in the sense that development teams need to come up with different package dependency list, and we need to have that environment to develop and test. Even though Debian is very close to Ubuntu, they still have minor difference in package versions, etc. so we cannot support. 

We can't provide deb-src package as of now which depends on every component team. Some packages have non-open source code. We do have all the source code (for open source packages) available on https://github.com/RadeonOpenCompute/ROCm . Even with the source code, it will be very difficult for user to build the package themselves (set the correct environment and get all the dependencies). We have a task to open source our build instruction but that still need some time (pass all the legal procedures).

Just to solve your issue for now, it will be much much easier to break down the binary package and modify the dependency manually than to build it from source code. We recommend to follow the workaround given in issue #1236, but this is not officially supported method.

Hope it clarifies.
Thank you.


---

### 评论 #3 — xuhuisheng (2021-03-22T06:54:39Z)

@ROCmSupport 
I think there is only one close-source component - hsa-amd-aqlprofile. But even I didn't install it, ROCm can run properly.
Does ROCm have a plan to open-source it? 

---

### 评论 #4 — elukey (2021-03-22T06:59:47Z)

@ROCmSupport if possible there should be a clear list of non open source packages that are optional, the power of ROCm is being open source and some clarity would really be great :)

---

### 评论 #5 — ROCmSupport (2021-03-22T07:14:58Z)

Agree with you @elukey.
But we can't provide deb-src package as of now which depends on every component team, which needs some discussion and plans.
Anyway, let me talk to our BU team for their inputs.
Thank you.


---
