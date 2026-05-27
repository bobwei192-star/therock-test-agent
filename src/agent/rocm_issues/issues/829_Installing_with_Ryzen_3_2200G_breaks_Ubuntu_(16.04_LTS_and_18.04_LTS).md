# Installing with Ryzen 3 2200G breaks Ubuntu (16.04 LTS and 18.04 LTS)

> **Issue #829**
> **状态**: closed
> **创建时间**: 2019-06-26T10:23:52Z
> **更新时间**: 2023-12-21T14:35:10Z
> **关闭时间**: 2023-12-21T14:35:09Z
> **作者**: manhofer
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/829

## 描述

Hi

I tried to install ROCm today on a machine equipped with a Ryzen 3 2200G. The operating system is a freshly installed Ubuntu 16.04 LTS (also tried with 18.04 LTS).

I followed all instructions, and after installing
`rocm-dkms`
and subsequent rebooting, Ubuntu does not start anymore. It goes past the initial bios screen, then the monitor turns black and nothing happens. There still is a signal coming to the monitor, since it does not turn off, but all I see is black.

I could not manage to fix the problem, only re-installing Ubuntu helped.

If I run `/opt/rocm/bin/rocminfo` after the install, it gives me some weird error and refers to a directory `home/jenkins/...`, even though there is no such user on the system.

If I run `/opt/rocm/opencl/bin/x86_64/clinfo`, I get an error 1001 (Could not get device IDs...).

Any ideas why this could be happening?



---

## 评论 (4 条)

### 评论 #1 — calvintam236 (2019-07-08T22:01:22Z)

I think it is caused by failure on installing module on kernel. ROCm often has problems with the latest version of kernel. Which kernel are you using after installation?

---

### 评论 #2 — manhofer (2019-07-09T12:14:31Z)

I think I used a 4.15.x or something like that (don't have the system here to look up the specific version).

I have now managed to get OpenCL support working using the official amdgpu-pro driver (18.50), which works fine so far. So no more need for ROCm at the moment.

---

### 评论 #3 — tasso (2023-12-18T22:19:58Z)

Is this still reproducible?  If not, can we please close the issue?  Thanks!

---

### 评论 #4 — tasso (2023-12-21T14:35:09Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---
