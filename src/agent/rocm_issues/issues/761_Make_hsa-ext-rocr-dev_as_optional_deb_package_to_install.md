# Make hsa-ext-rocr-dev as optional deb package to install

> **Issue #761**
> **状态**: closed
> **创建时间**: 2019-04-12T13:44:13Z
> **更新时间**: 2021-11-15T07:50:42Z
> **关闭时间**: 2021-11-15T07:50:42Z
> **作者**: elukey
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/761

## 描述

Hi everybody,

thanks a lot for all the efforts to keep this suite as open as possible to the community. I have read in several places (https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/33, https://github.com/RadeonOpenCompute/ROCm/issues/267#issuecomment-422172140) that the only remaining package not open source is `hsa-ext-rocr-dev`, that IIUC, should be optional. The main issue is that in several rocm deb packages it is listed as dependency:
```
apt-cache rdepends hsa-ext-rocr-dev
hsa-ext-rocr-dev
Reverse Depends:
  hsa-rocr-dev
  rocm-dev
  hcc
```

It would be extremely useful if that dependency was removed, so whoever wants to stick with open-source only could deploy rocm without having to mess with dependencies to remove `hsa-ext-rocr-dev`. A quick update of the documentation would resolve any doubt from whoever wants to keep closed sources binaries.

Thanks in advance!

Luca

---

## 评论 (16 条)

### 评论 #1 — elukey (2019-04-16T07:35:30Z)

Any comment? :)

---

### 评论 #2 — elukey (2019-04-23T14:38:51Z)

Re-iterating the question, maybe this time I'll have more luck :)

---

### 评论 #3 — elukey (2019-05-07T15:39:12Z)

I'd love to get a comment on this, even "we don't know", please :)

---

### 评论 #4 — elukey (2019-05-10T13:28:25Z)

@jlgreathouse sorry to ping you directly, but would you know how can I follow up on this? I am a fan of ROCm, we'd love at Wikimedia to use a fully open source solution for GPUs but this use case is kinda blocking us. I am available to work on a solution if needed! Thanks in advance..

---

### 评论 #5 — elukey (2019-05-17T08:26:56Z)

This could be interesting, even though only for hcc:

https://github.com/RadeonOpenCompute/Experimental_ROC/blob/34c7766472436e729b74d0e2af4748d58d30d931/distro_install_scripts/shared_files/patches/hcc_open_build.patch



---

### 评论 #6 — elukey (2019-05-28T08:33:33Z)

Gently pinging again :)

---

### 评论 #7 — elukey (2019-07-08T14:09:36Z)

Another ping before giving up..

---

### 评论 #8 — pramenku (2019-07-08T18:57:44Z)

Hi elukey
Thanks for reporting.
We will see how we can do or what's the best solution and come back. Not promising anything for now.
Please stay tuned. 

Thanks.


---

### 评论 #9 — elukey (2019-07-09T05:56:25Z)

@pramenku thanks a lot!

---

### 评论 #10 — pramenku (2019-07-25T20:30:24Z)

Hi elukey,
It looks like in near future, these dependency things will be removed.
When and how, will be known later. Please stay tuned. 
Thanks


---

### 评论 #11 — elukey (2019-11-07T15:28:45Z)

Any news??

---

### 评论 #12 — pramenku (2019-11-07T15:33:52Z)

Sorry. Work is in progress but no exact date as of today. It's not straight forward so taking time. 
Thanks for getting the update.

---

### 评论 #13 — elukey (2021-11-15T06:57:42Z)

Any news?

---

### 评论 #14 — pramenku (2021-11-15T07:24:35Z)

Hi @elukey 
 hsa-ext-rocr-dev is no more part of rocm packages and entire runtime is now part of hsa-rocr and hsa-rocr-dev.
 You can use our latest release ROCm4.5
 
 You can refer for package info : https://rocmdocs.amd.com/en/latest/Installation_Guide/Software-Stack-for-AMD-GPU.html
 
You can close this issue if you get the answer.

---

### 评论 #15 — elukey (2021-11-15T07:40:06Z)

@pramenku Hi! Thanks a lot for the update. IIUC the content of `hsa-ext-rocr-dev` is not a problem anymore, so ROCm doesn't need to install anymore binary-only packages (all open source). If this is true, great result, you folks are great!

---

### 评论 #16 — pramenku (2021-11-15T07:47:29Z)

Thanks @elukey for nice comment. :)  Your understanding is correct.
Keep using ROCm and enjoy it.  :) You can close this issue.  :)

---
