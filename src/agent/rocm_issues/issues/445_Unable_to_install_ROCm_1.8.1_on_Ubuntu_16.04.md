# Unable to install ROCm 1.8.1 on Ubuntu 16.04

> **Issue #445**
> **状态**: closed
> **创建时间**: 2018-06-27T14:11:36Z
> **更新时间**: 2018-08-24T00:35:59Z
> **关闭时间**: 2018-08-24T00:35:59Z
> **作者**: nishagandhi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/445

## 描述

Hi, I have been following instructions to install ROCm 1.8.1 (from https://rocm.github.io/ROCmInstall.html), all the instructions prior to **sudo apt-get install rocm-dkms**  were executed successfully. However, its unable to locate the package rocm-dkms :  

Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package rocm-dkms


---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-07-07T15:06:29Z)

Can you look at see what Linux kernel your running 4.15 ?? 

---

### 评论 #2 — min0ru (2018-07-22T12:35:45Z)

Are you sure that you added rocm deb repository?

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
sudo apt update



---
