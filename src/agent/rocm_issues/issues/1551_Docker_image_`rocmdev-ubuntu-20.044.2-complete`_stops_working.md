# Docker image `rocm/dev-ubuntu-20.04:4.2-complete` stops working

> **Issue #1551**
> **状态**: closed
> **创建时间**: 2021-08-07T18:05:20Z
> **更新时间**: 2021-08-16T05:38:16Z
> **关闭时间**: 2021-08-16T05:38:16Z
> **作者**: syifan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1551

## 描述

I have been using the docker image `rocm/dev-ubuntu-20.04:4.2-complete` as my development and testing environment. However, it stopped working after when 4.3 is released. To recreate the error, one can simply run `apt update` in the docker image and the following error will appear. 

```
W: GPG error: https://repo.radeon.com/rocm/apt/4.2 ubuntu InRelease: The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
E: The repository 'https://repo.radeon.com/rocm/apt/4.2 ubuntu InRelease' is not signed.
```

Here is the error in my testing environment. 

https://gitlab.com/akita/rhipo/-/jobs/1485844044#L52

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-08-09T06:35:42Z)

Hi @syifan 
Thanks for reaching out.
There are 2 problems I identified.

> 
> 
> I have been using the docker image `rocm/dev-ubuntu-20.04:4.2-complete` as my development and testing environment. However, it stopped working after when 4.3 is released. 
1. I am not sure how it stopped working after 4.3 released.
The environment that you are using is a docker and I do not think ROCm 4.3 is going to affect the docker.
Can you please elaborate the problem here.
**I, personally, pulled rocm/dev-ubuntu-20.04:4.2-complete on top of ROCm 4.3 on my machine and able to run the things.**


> 
> ```
> W: GPG error: https://repo.radeon.com/rocm/apt/4.2 ubuntu InRelease: The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
> E: The repository 'https://repo.radeon.com/rocm/apt/4.2 ubuntu InRelease' is not signed.
2. GPG key is old one here. the latest/updated key available at https://repo.radeon.com/rocm/rocm.gpg.key
I am also able to see the same issue but gpg key needs to be updated to the latest.

**Overall I recommend you to use the latest rocm 4.3 docker: `rocm/dev-ubuntu-20.04:4.3-complete`**
It has the latest GPG key and so all updates work perfect.

Hope this helps.
Thank you.

---

### 评论 #2 — syifan (2021-08-09T14:27:32Z)

Thanks for the answer. Yes, the error is caused by the GPG key update. When 4.3 is released, the GPG key used in the 4.2 docker image stops working. 

A bigger question is why the GPG key should change. We work on a project that is very sensitive to the compiler. ROCm made a big change in the compiler as the HSACO header is no longer provided by the OpenCL compiler. We have spent a lot of effort migrating to 4.2. However, we do not really have the bandwidth to update our tool for each ROCm version. Updating the GPG Key on the ROCm side breaks down users' toolchains. 

I know this is way beyond what can be solved by a Github issue. But may I give a suggestion? Is it possible to have a clear definition about the support duration of each version? Or as an alternative, is that possible to have a long-term support version for ROCm? With that, users who need stable versions can stay in one version for a longer time. 

Please feel free the close the issue. We can try to migrate to 4.3 and see if our system can still work. 

---

### 评论 #3 — ROCmSupport (2021-08-11T09:35:22Z)

Thanks for the point.
Let me gather little more information on this and will share an update soon.

---

### 评论 #4 — ROCmSupport (2021-08-16T05:05:24Z)

Hi @syifan 
I got an update on the GPG key.
Actually this is not a process breakage, this is the process flow.

The old GPG key is going to be expired by August 1st and so we renewed it, little before, on July 29. This is regardless of ROCm version.
For the dockers created before July 29th, as the key expired, users/all need to re-import (update) the key:
_wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -_

For the docker, which is created after July 29th, e.g. ROCm 4.3, no need to import of new key as it already has the new key.

Hope this helps.
Thank you.


---
