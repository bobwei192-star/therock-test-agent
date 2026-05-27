# rocm-smi (rocm v2.3) error

> **Issue #777**
> **状态**: closed
> **创建时间**: 2019-04-19T01:18:08Z
> **更新时间**: 2019-06-07T12:14:40Z
> **关闭时间**: 2019-06-07T12:14:40Z
> **作者**: WannaBeOCer
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/777

## 描述

Was working fine with ROCm v2.2, manually setting the power target to 300w also works fine.

> Traceback (most recent call last):
>   File "/opt/rocm/bin/rocm-smi", line 1910, in <module>
>     setPowerOverDrive(deviceList, args.setpoweroverdrive, args.autorespond)
>   File "/opt/rocm/bin/rocm-smi", line 1396, in setPowerOverDrive
>     power_cap_path = getFilePath(device, 'power1_cap')
>   File "/opt/rocm/bin/rocm-smi", line 130, in getFilePath
>     pathDict = valuePaths[key]
> KeyError: 'power1_cap'

---

## 评论 (3 条)

### 评论 #1 — kentrussell (2019-05-09T20:00:18Z)

I fixed this internally but missed the 2.4 fix. All you have to do is edit the SMI and change "power1_cap" to "power_cap" on line 1396. It'll be in 2.5, but that doesn't help right now.

---

### 评论 #2 — WannaBeOCer (2019-05-10T01:20:56Z)

> I fixed this internally but missed the 2.4 fix. All you have to do is edit the SMI and change "power1_cap" to "power_cap" on line 1396. It'll be in 2.5, but that doesn't help right now.

Thank you! 

---

### 评论 #3 — kentrussell (2019-06-07T12:14:40Z)

This is fixed in 2.5

---
