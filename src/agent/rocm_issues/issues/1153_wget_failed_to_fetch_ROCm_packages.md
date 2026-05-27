# wget failed to fetch ROCm packages

> **Issue #1153**
> **状态**: closed
> **创建时间**: 2020-06-17T16:36:56Z
> **更新时间**: 2020-06-17T18:00:18Z
> **关闭时间**: 2020-06-17T18:00:17Z
> **作者**: etonkan91
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1153

## 描述

Hi, 

I have been trying to install rocm-kernel using the apt command on Ubuntu following the Quick Start Guide in https://rocmdocs.amd.com/en/latest/ROCm_Virtualization_Containers/quickstart.html. 

However, whenever I run the get command, the command seems to be stuck. So, I went to ping packages.amd.com and I notice there are no outputs. When I ping the same address on a Windows PC, I got "Request timed out." I am wondering if the quick start guide is out of date or if the link to the packages has changed. Would someone please advise? Thanks in advance.

The wget command I ran is: wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -

Also, I am not sure if this is the correct location for reporting an AMD site failure for ROCm. Please redirect me to the correct site if this is not relevant to ROCm.

---

## 评论 (3 条)

### 评论 #1 — Rmalavally (2020-06-17T16:44:49Z)

Thank you for checking with us. We will review the documentation for technical accuracy and get back to you. 
Please don't hesitate to reach out if you have any other questions or concerns.

AMD ROCm Documentation Team

---

### 评论 #2 — Rmalavally (2020-06-17T17:04:03Z)

Please refer our updated installation instructions at the following link and let us know if you are still experiencing issues with AMD ROCm installation.

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#

---

### 评论 #3 — etonkan91 (2020-06-17T18:00:17Z)

Thanks! I am able to install ROCm with the new link.

---
