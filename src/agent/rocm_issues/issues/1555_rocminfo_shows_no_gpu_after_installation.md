# rocminfo shows "no gpu" after installation

> **Issue #1555**
> **状态**: closed
> **创建时间**: 2021-08-16T12:50:30Z
> **更新时间**: 2024-01-08T06:42:52Z
> **关闭时间**: 2021-11-25T10:44:56Z
> **作者**: kineticz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1555

## 描述

```
azureuser@gvme7b1132637:~$ /opt/rocm/bin/rocminfo
ROCk module is NOT loaded, possibly no GPU devices
azureuser@gvme7b1132637:~$ /opt/rocm/opencl/bin/clinfo
Number of platforms:				1
  Platform Profile:				FULL_PROFILE
  Platform Version:				OpenCL 2.0 AMD-APP (3305.0)
  Platform Name:				AMD Accelerated Parallel Processing
  Platform Vendor:				Advanced Micro Devices, Inc.
  Platform Extensions:				cl_khr_icd cl_amd_event_callback 


  Platform Name:				AMD Accelerated Parallel Processing
Number of devices:				0
```

Strange thing is that opencl seems available. 
The installation and tests were done on a NV4as_v4 VM with Instinct MI25 GPU. 
ROCM version: 4.3 (Installed according to https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html)
OS version: Ubuntu 20.04.2

---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2021-08-16T14:04:06Z)

Thanks @kindlychung for reaching out.
Can you please share the exact steps to reproduce the problem.
Thank you.

---

### 评论 #2 — Nishant-Pall (2021-08-19T10:57:28Z)

I have the same problem as well, I believe @kindlychung installed ROCm according to the installation guide. I'm getting exactly the same results even though I believe my GPU chip is of type 'polaris 12'. The steps I followed were exactly as mentioned in the guide and the commands ```/opt/rocm/bin/rocminfo``` gave the results as they got. 

OS Version: Ubuntu 20.04
Kernel: 5.11.0-27-generic

Edit: I just read kernel requirements and I believe it wouldn't work on kernels beyond version 5.8

---

### 评论 #3 — ROCmSupport (2021-08-23T05:46:55Z)

Hi @Nishant-Pall 
Polaris12 is NOT a supported card and so things will not work on them, which I can say that a different issue from the titled one.

Hi @kindlychung 
Please help us with the exact steps you followed from start, so that we will understand better and tries to provide resolution.
Thank you.

---

### 评论 #4 — mdberryh (2021-08-24T03:54:16Z)

I have the exact same problem, and I have the Radeon Pro 6600

`uname -a
Linux  5.11.0-27-generic #29~20.04.1-Ubuntu SMP Wed Aug 11 15:58:17 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
`
[SYSTEM_NAME_or_ISSUEID.rocm_techsupport.log](https://github.com/RadeonOpenCompute/ROCm/files/7036355/SYSTEM_NAME_or_ISSUEID.rocm_techsupport.log)



---

### 评论 #5 — ROCmSupport (2021-08-24T05:12:15Z)

Hi @mdberryh 
ROCm does not support Navi10 cards and so things do not work on these cards as expected.
Please track supported hardware section @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support
Thank you.

---

### 评论 #6 — mdberryh (2021-08-24T12:28:07Z)

@ROCmSupport  Thanks for your quick assistance! I was hoping to use AMD GPUs for neural networks, so I thought I'd give it a try. I am pretty confused with the differences between Rocm and AMD Pro drivers. Reading different frameworks both are mentioned and both use openCL. I'll see what I can do with the AMD Pro drivers for linux.

---

### 评论 #7 — ROCmSupport (2021-11-16T10:03:03Z)

Hi @kindlychung
As mentioned before, can you please help me with the exact steps you followed from starting, so that we can debug the problem in a better way.
And also I recommend you to verify onc with the latest ROCm 4.5 and update.
Thank you.

---

### 评论 #8 — ROCmSupport (2021-11-25T10:44:56Z)

Hi @kindlychung 
Issue is not reproducible with ROCm 4.5. Request to verify with the same.
Thank you.

---

### 评论 #9 — elhewaty (2024-01-08T06:42:52Z)

@ROCmSupport do you support `Topaz XT [Radeon R7 M260/M265 / M340/M360 / M440/M445 / 530/535 / 620/625 Mobile]`

---
