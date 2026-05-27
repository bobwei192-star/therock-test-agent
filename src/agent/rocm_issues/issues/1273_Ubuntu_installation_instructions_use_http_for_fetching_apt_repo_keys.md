# Ubuntu installation instructions use http for fetching apt repo keys

> **Issue #1273**
> **状态**: closed
> **创建时间**: 2020-10-31T23:18:32Z
> **更新时间**: 2020-12-11T05:29:41Z
> **关闭时间**: 2020-12-11T05:29:41Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1273

## 描述

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#installing-a-rocm-package-from-a-debian-repository

uses http, instead of https in the install instruction for fetching apt repo keys.

This is unsecure.

Please use https. From my test the server already serves files on https, so just update of the documentation (links and example how to use it), should be updated and it should work.



---

## 评论 (4 条)

### 评论 #1 — rkothako (2020-11-03T05:19:09Z)

@baryluk, Thanks for the ticket logged.
We are working on it and will share an update asap.

---

### 评论 #2 — cgmb (2020-11-03T20:25:39Z)

Note that this problem appears in multiple places within the docs:
```
cgmb@localhost:~/ws$ git clone https://github.com/RadeonOpenCompute/ROCm_Documentation.git
cgmb@localhost:~/ws$ cd ROCm_Documentation/
cgmb@localhost:~/ws/ROCm_Documentation$ git grep 'http[^s].*gpg.key'
Deep_learning/Deep-learning.rst:   wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
Installation_Guide/Installation-Guide.rst:* Old Key: http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key
Installation_Guide/Installation-Guide.rst:* New Key: http://repo.radeon.com/rocm/rocm.gpg.key 
Installation_Guide/Quick Start Installation Guide.rst:    wget -q -O - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
Installation_Guide/ROCk-kernel.rst: wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
ROCm_API_References/Thrust.rst: $ wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
ROCm_Libraries/dep-lib.rst:  wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
ROCm_Libraries/dep-lib.rst:  wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
ROCm_Libraries/dep-lib.rst:  wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
ROCm_Tools/hcFFT.rst:  wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
ROCm_Tools/hcRNG.rst:  wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
ROCm_Tools/hipeigen.rst:  wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
```

---

### 评论 #3 — rkothako (2020-11-04T08:03:05Z)

Hi @cgmb , we are working on changing in all possible places.
I will share an update soon.

---

### 评论 #4 — ROCmSupport (2020-12-11T05:29:41Z)

Updates are done now.
Its mapped to https now.
Thank you.

---
