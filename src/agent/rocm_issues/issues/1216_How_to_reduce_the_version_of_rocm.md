# How to reduce the version of rocm

> **Issue #1216**
> **状态**: closed
> **创建时间**: 2020-09-11T09:25:29Z
> **更新时间**: 2020-12-16T05:49:28Z
> **关闭时间**: 2020-12-16T04:44:35Z
> **作者**: JLxiaocaiji
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/1216

## 标签

- **Question** (颜色: #cc317c)

## 描述

hi，my graphics card is Vega56. I have installed the latest version of Rocm. Before that, it helped me a lot. Now I have a new task. The required environment is pytorch1.4.0+torchvision0.5. The latest version of rocm does not support cuda. Option, what should I do?

---

## 评论 (5 条)

### 评论 #1 — xuhuisheng (2020-09-11T09:48:03Z)

We could use specific version of rocm, e.g. http://repo.radeon.com/rocm/apt/3.5.1/

---

### 评论 #2 — JLxiaocaiji (2020-09-11T10:59:13Z)

ohhhhh,thank you very much.

---

### 评论 #3 — JLxiaocaiji (2020-09-12T08:02:41Z)

I tried the method you gave, but it didn't work. I saw that the official document mentions that multiple versions can be installed starting from V3.3, but I hope the official can take care of stupid people like me, because I have tried many methods without success.LOL

---

### 评论 #4 — YifeiLu-1 (2020-09-15T19:02:48Z)

https://github.com/RadeonOpenCompute/ROCm/issues/284#issuecomment-539095892
Maybe try nuke the rocm 3.7 installation and install the old one according to this comment?

---

### 评论 #5 — ROCmSupport (2020-12-16T04:44:34Z)

Hi @JLxiaocaiji 
Thanks for reaching out.
You can install ROCm in 2 different ways.
1. Single rocm --> Map the repo as _http://repo.radeon.com/rocm/apt/3.5.1/_ and **sudo apt install rocm-dkms** 
2. Multi rocm --> Can install multiple rocm versions side by side. For ex: installing rocm 3.9 and 3.10 can be done in the way like --> Map the repo of 3.9 as http://repo.radeon.com/rocm/apt/3.9/ and **sudo apt install rock-dkms rock-dkms-firmware rocm-dev3.9.0** --> Map the repo of 3.10 as http://repo.radeon.com/rocm/apt/3.10/ and **sudo apt install rocm-dev3.9.0**
Like wise you can install many versions.
Hope this helps.
Thank you.


---
