# Remove hardcoded kernel version in ROCm. 

> **Issue #1221**
> **状态**: closed
> **创建时间**: 2020-09-17T21:48:35Z
> **更新时间**: 2021-01-06T13:53:31Z
> **关闭时间**: 2021-01-06T13:51:39Z
> **作者**: sameershende
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1221

## 描述

While compiling ROCm for Ubuntu 20.04 I see a couple of places where the kernel version has been hardcoded. It may be better for a script to detect the kernel version and inject it in these places. Specifically, 3.6.0 is assumed in:

1. ROCK-Kernel-Driver/include/config/kernel.release 
2. ROCK-Kernel-Driver/include/config/auto.conf.cmd

files. 

---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2020-12-16T05:41:35Z)

Thanks @sameershende for reaching out.
I will reach respective component owner on this.
Thank you.

---

### 评论 #2 — kentrussell (2020-12-16T11:51:28Z)

These are generated during the package creation for each release. Is there a problem with the values? he 3.6.0 references the ROCm 3.6.0 release, not kernel 3.6. If there is something that is going wrong with that value, we can bring it up with the Packaging team

---

### 评论 #3 — ROCmSupport (2021-01-05T10:05:56Z)

Hi @sameershende 
Request you to respond asap so that we can do something.
Thank you.

---

### 评论 #4 — sameershende (2021-01-05T16:46:19Z)

I can't find kernel.release and auto.conf.cmd files in the current repo, so it is difficult to check the values with the current release. I just checked my notes and the value that was hardcoded was not 3.6.0 - it was 5.6.0. Clearly, it couldn't have been a ROCm release id. It was an OS kernel version number that was just hardcoded in these two files (auto.conf.cmd and kernel.release). For Ubuntu 20.04, I had to modify it manually to 5.4.0-42-generic. And the variable that was assigned this value was KERNEL_VERSION. If a high level script to build ROCm on multiple platforms (including ppc64le) is created, it would have to detect this version from the output of uname and inject it into these files. But since these files are not used for the build,  perhaps this issue has been resolved. 

---

### 评论 #5 — kentrussell (2021-01-06T13:51:39Z)

I cannot find the files in any ROCm version of this repo. Regardless, since the issue is not present in 4.0 (or as far back as 3.6), we will close this

Also note that the 3.6-4.0 releases are based on the 5.6 kernel base (which you can confirm in git log) which is likely where these values were obtained from. 

---
