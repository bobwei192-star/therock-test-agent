# rocm-smi fails to set profile

> **Issue #1089**
> **状态**: closed
> **创建时间**: 2020-04-24T18:17:42Z
> **更新时间**: 2021-03-17T06:57:35Z
> **关闭时间**: 2021-03-17T06:55:56Z
> **作者**: btspce
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1089

## 描述

System: Raven Ridge 2700u
rocm-smi from ROCm 2.2 works.

$ sudo /opt/rocm-3.3.0/bin/rocm-smi --setprofile 3


========================ROCm System Management Interface========================
Traceback (most recent call last):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 2995, in <module>
    setProfile(deviceList, args.setprofile)
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 2434, in setProfile
    if writeProfileSysfs(device, profile):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 677, in writeProfileSysfs
    if not verifySetProfile(device, value):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 583, in verifySetProfile
    maxProfileLevel = getMaxLevel(device, 'profile')
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 856, in getMaxLevel
    return int(levels.splitlines()[-1][0])
ValueError: invalid literal for int() with base 10: ' '

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-03-17T06:49:18Z)

Thanks @btspce for reaching out.
I will check this for you asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-03-17T06:55:56Z)

Hi @btspce 
I have verified with the latest ROCm 4.0 and found that issue is not observed anymore.
Request you to try with the same.

**_taccuser@taccuser-X399-DESIGNARE-EX:/opt$ /opt/rocm-4.0.0/bin/rocm-smi --setprofile 3

======================= ROCm System Management Interface =======================
============================== Set Power Profile ===============================
GPU[0]          : Successfully set profile to: POWER SAVING
================================================================================
============================= End of ROCm SMI Log ==============================_**

Thank you.

---
