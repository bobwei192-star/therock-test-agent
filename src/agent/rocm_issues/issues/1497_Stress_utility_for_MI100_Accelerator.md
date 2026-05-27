# Stress utility for MI100 Accelerator

> **Issue #1497**
> **状态**: closed
> **创建时间**: 2021-06-21T13:13:27Z
> **更新时间**: 2021-06-23T08:06:11Z
> **关闭时间**: 2021-06-23T08:06:11Z
> **作者**: question12345
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1497

## 描述

Hello 

Is there any utility I can use on centos 7.9 to stress test a MI100 accelerator?

thanks


---

## 评论 (3 条)

### 评论 #1 — preda (2021-06-22T10:52:50Z)

you could try gpuowl https://github.com/preda/gpuowl


---

### 评论 #2 — ROCmSupport (2021-06-23T05:16:05Z)

Thanks @question12345 for reaching us.
Let me take a look.

---

### 评论 #3 — ROCmSupport (2021-06-23T07:32:47Z)

I recommend to use/run using rocm-validation-suite and pick **rvs stress tests**.
Steps to do:
1. Install rocm using **sudo apt install rocm-dkms**
2. Install rvs(rocm-validation-suite) using **sudo apt install rvs**
3. cd /opt/rocm/rvs && sudo cp -rf /opt/rocm/rvs/testscripts/* /opt/rocm/rvs/
4. Run the script, for examples, take stress module: **sudo ./rvs-stress-long.sh**

Hope this helps.
Thank you.



---
