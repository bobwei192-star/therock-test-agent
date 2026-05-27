# [QUESTION] Permission for power_dpm_force_performance_level on Ubuntu 18

> **Issue #612**
> **状态**: closed
> **创建时间**: 2018-11-14T10:03:31Z
> **更新时间**: 2018-11-14T18:41:43Z
> **关闭时间**: 2018-11-14T18:41:42Z
> **作者**: vecera-vojtech
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/612

## 描述

Hello, 

I've just installed `rocm-dkms` following [instructions](https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository) on my Ubuntu 18.04.1 LTS machine (fresh install). I've tested installation with `clinfo` and `rocminfo` and every thing went well (thanks for greate guide and ROCm package). The issue came when I've tried using `hashcat` which supports ROCm OCL. Hashcat threw `/sys/bus/pci/devices/0000:03:00.0/power_dpm_force_performance_level: Permission denied`, which is non-critical error. Then I've done 
```
$ ls -al /sys/bus/pci/devices/0000\:03\:00.0/power_dpm_force_performance_level
-rw-r--r-- 1 root root 4096 lis 14 10:35 /sys/bus/pci/devices/0000:03:00.0/power_dpm_force_performance_level
```
As you can see there are rights only for root:root. Why aren't the right something like 664 and group video at least? Might it cause some security holes? Couldn't those permissions be like that by default?

I've used commands bellow to get rid of the non-critical errors.
```
$ sudo chgrp video /sys/bus/pci/devices/0000\:03\:00.0/power_dpm_force_performance_level
$ sudo chmod 664 /sys/bus/pci/devices/0000\:03\:00.0/power_dpm_force_performance_level
```

Thanks for answer and sorry for bothering with such minor thing.

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-11-14T17:27:04Z)

Hi @Azaran 

Writing to sysfs files like this is, by default, considered a privileged operation because it can affect the performance of the GPU for other users on the system. As such, we do not automatically make this available to non-administrative users. If an administrator of the system (e.g. you if you're on a single-user system) wants to allow all GPU users to be able to force high or low performance on all other GPU users, they may do so by setting such permissions. However, we don't think it's appropriate for us to make such a decision by default.

---

### 评论 #2 — vecera-vojtech (2018-11-14T18:41:42Z)

Alright, thank you for your response. I just wondered what were the exact reasons and if that was really intended. 

Closing thread.

---
