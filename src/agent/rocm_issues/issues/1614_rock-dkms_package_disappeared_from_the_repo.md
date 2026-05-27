# rock-dkms package disappeared from the repo

> **Issue #1614**
> **状态**: closed
> **创建时间**: 2021-11-05T09:23:28Z
> **更新时间**: 2022-04-24T12:44:56Z
> **关闭时间**: 2021-11-10T12:29:36Z
> **作者**: MathiasMagnus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1614

## 描述

Hi! I wanted to install ROCm recently on some cluster machines but install fails due to a missing package.
```
$ sudo apt-add-repository 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main'
...
$ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-dkms : Depends: rock-dkms but it is not installable
E: Unable to correct problems, you have held broken packages.
$ apt search rocm-dkms
Sorting... Done
Full Text Search... Done
rocm-dkms/Ubuntu 4.5.0.40500-56 amd64
  Radeon Open Compute (ROCm) Runtime software stack

$ apt search rock-dkms
Sorting... Done
Full Text Search... Done
```
Browsing through `https://repo.radeon.com/rocm/apt/` I saw that neither the `debian` (latest?) nor `4.5` folders have the `rock-dkms` package in them. `4.3.1` does. I installed the runtime in a docker container just Yesterday and it worked.

---

## 评论 (8 条)

### 评论 #1 — ex-rzr (2021-11-05T10:47:54Z)

I seems that they are replaced with `amdgpu-dkms` and `amdgpu-dkms-firmware`. At least that what the new install script (`sudo amdgpu-install --usecase=hiplibsdk,rocm`) installs.

---

### 评论 #2 — dkgaraujo (2021-11-08T11:23:43Z)

Also facing the same issue as original poster, using Ubuntu 20.04.3 LTS.

---

### 评论 #3 — ROCmSupport (2021-11-10T12:29:36Z)

Hi @MathiasMagnus 
Thanks for reaching out.
Installation procedure got changed from ROCm 4.5 and request to follow the new steps documented @ [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html](url)
There will not be rock-dkms anymore and its replaced by amdgpu-dkms.
Thank you.

---

### 评论 #4 — erkinalp (2021-11-18T20:12:56Z)

@ROCmSupport your link is formatted incorrectly

---

### 评论 #5 — ROCmSupport (2021-11-22T07:28:40Z)

Hi @erkinalp,
Link is correct only. But request to copy the address and paste in browser window instead of clicking directly.
Thank you.

---

### 评论 #6 — ki9us (2021-12-22T22:41:34Z)

I've been googling for a while and still can't figure out how to install rocm on a stock ubuntu machine.  

These packages don't exist:  

```
$ sudo apt install amdgpu-dkms amdgpu-dkms-firmware
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package amdgpu-dkms
E: Unable to locate package amdgpu-dkms-firmware
```

There's no information in [the docs](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu) on how to install `rock-dkms` or get past this error.  

Why was this closed?  There's no solution.  

---

### 评论 #7 — ROCmSupport (2021-12-23T05:41:12Z)

rock-dkms is no more now and its amdgpu-dkms now.
Request to follow the installation procedure @ https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#rocm-installation-guide-v4-5

Thank you.

---

### 评论 #8 — Two-Worlds (2022-04-24T12:44:56Z)

We get that, but fails as signature has now expired.

---
