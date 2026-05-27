# A zillion errors while installing ROCm 3.0.6 on Vega 10

> **Issue #1037**
> **状态**: closed
> **创建时间**: 2020-03-08T02:10:04Z
> **更新时间**: 2021-04-19T12:46:52Z
> **关闭时间**: 2021-04-19T12:46:52Z
> **作者**: gauravjain14
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1037

## 描述

I am following the instructions listed at https://github.com/RadeonOpenCompute/ROCm/tree/roc-3.0.0#Ubuntu to install ROCm 3.0.6 on Ubuntu 16.04 with Kernel 4.13.0-26 and it has been nothing but a **nightmare**.

First, following the steps doesn't complete successfully as the installation errors out on not being able to locate hcc, and thus hip-hcc fails and the installation aborts. To get pass that I separately installed hcc and then reinstalled rocm-dkms. 

Then when I run `/opt/rocm/bin/rocminfo`, it gives the following error:
```
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.0/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

I thought this might be something related to the issue at https://github.com/RadeonOpenCompute/ROCm/pull/1005/files and added myself to **render** groups, to no avail. 

Things don't stop there. I thought just trying to do `hipcc square.hipref.cpp` might work. But no, things are broken to an extent that it might be easier changing the machine than installing the rocm stack. Trying to build the **square app**, gives the error `hip_runtime.h: file not found`, which is nothing but illogical because when I do` /opt/rocm/bin/hipconfig` --full, I can see what the include paths are and I can very well see `/opt/rocm/hip/include` where the `hip_runtime.h` is located at. 

It has been simply annoying when they should have simply been `sudo apt-get install rocm-dkms`

---

## 评论 (4 条)

### 评论 #1 — emoon (2020-03-13T14:00:02Z)

I don't think kernel 4.x is supported on 18.04 with ROCm 3.x

https://github.com/RadeonOpenCompute/ROCm/tree/roc-3.0.0#supported-operating-systems

`• Ubuntu 16.04.6(Kernel 4.15) and 18.04.3(Kernel 5.0)`



---

### 评论 #2 — gauravjain14 (2020-03-13T18:50:57Z)

I have edited the issue. It's 16.04 and not 18.04 I am running on. 

---

### 评论 #3 — emoon (2020-03-14T07:16:01Z)

@gauravjain14 I'm not sure if it make any different but the requirement states `4.15` kernel and your seems to be `4.13`

---

### 评论 #4 — ROCmSupport (2021-04-19T12:46:51Z)

This issue is fixed and no more observed with the latest ROCm 4.1.
Recommend to try with the same.
Thank you.

---
