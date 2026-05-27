# Corrupted display

> **Issue #115**
> **状态**: closed
> **创建时间**: 2017-05-04T00:26:23Z
> **更新时间**: 2017-10-17T14:13:12Z
> **关闭时间**: 2017-10-17T14:13:12Z
> **作者**: grmat
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/115

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

After following the installation instructions with binaries from the repo, I can't use the graphical desktop anymore.

The screen is corrupted and shows content that was shown **before rebooting** (see picture below) like visited websites.

GPU: Hawaii (R9 290X)
OS: Ubuntu 16.04

I can then switch to a virtual terminal, build and run the vector sample without problems.

![corrupted-screen](https://cloud.githubusercontent.com/assets/12658837/25686663/50544672-3070-11e7-839e-7a2a99fa4cc8.jpg)


---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-07-02T17:45:47Z)

Can you try ROCm 1.6 here are new install instructions 
https://rocm.github.io/ROCmInstall.html

---

### 评论 #2 — grmat (2017-07-10T21:05:29Z)

@gstoner freshly installed Ubuntu 16.04 + ROCm 1.6, the problem remains.

Just read that Michael from Phoronix is affected by the same problem:

> when trying ROCm 1.6 with the Radeon R9 290 I was just hitting corrupted screen output when booting the system

https://www.phoronix.com/scan.php?page=article&item=amd-rocm16-nvidia&num=1

---

### 评论 #3 — gstoner (2017-07-26T13:49:53Z)

Please check with ROCm 1.6.1 

---

### 评论 #4 — gstoner (2017-10-17T14:13:12Z)

There are big changes coming AMDGPU driver in how they are handling display in Linux Kernel 4.15, this is not ROCm compute driver issue. 

---
