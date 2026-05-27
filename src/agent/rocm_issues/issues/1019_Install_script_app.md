# Install script / app ?

> **Issue #1019**
> **状态**: closed
> **创建时间**: 2020-02-22T22:28:06Z
> **更新时间**: 2021-04-20T07:20:16Z
> **关闭时间**: 2021-04-19T12:52:45Z
> **作者**: ScarFez
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1019

## 描述

Is there any app or install script for any Linux distribution that can install the current version of ROCm in the correct order ?

If so, please en light me; which Distro and version and where it can be obtained


---

## 评论 (3 条)

### 评论 #1 — valeriob01 (2020-02-23T05:14:44Z)

This is for a minimal ROCm installation for Debian:

```
apt update
apt dist-upgrade
apt install libnuma-dev
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | tee /etc/apt/sources.list.d/rocm.list
apt update
apt install rock-dkms rocm-opencl rocm-opencl-dev rocm-smi
echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | tee /etc/udev/rules.d/70-kfd.rules
/usr/sbin/usermod -a -G video root
echo 'ADD_EXTRA_GROUPS=1' | tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | tee -a /etc/adduser.conf
echo 'export LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:$$LD_LIBRARY_PATH' | tee -a /etc/profile.d/rocm.sh
echo 'export PATH=$$PATH:/bin:/sbin:/usr/bin:/usr/sbin:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64' | tee -a /etc/profile.d/rocm.sh
```

---

### 评论 #2 — valeriob01 (2020-02-23T05:17:09Z)

> This is for a minimal ROCm installation for Debian:
> 
> ```
> apt update
> apt dist-upgrade
> apt install libnuma-dev
> wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | apt-key add -
> echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | tee /etc/apt/sources.list.d/rocm.list
> apt update
> apt install rock-dkms rocm-opencl rocm-opencl-dev rocm-smi
> echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | tee /etc/udev/rules.d/70-kfd.rules
> /usr/sbin/usermod -a -G video root
> echo 'ADD_EXTRA_GROUPS=1' | tee -a /etc/adduser.conf
> echo 'EXTRA_GROUPS=video' | tee -a /etc/adduser.conf
> echo 'export LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:$$LD_LIBRARY_PATH' | tee -a /etc/profile.d/rocm.sh
> echo 'export PATH=$$PATH:/bin:/sbin:/usr/bin:/usr/sbin:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64' | tee -a /etc/profile.d/rocm.sh
> ```

however ROCm 3.0 will not work, substitute 'apt/debian' with the previous ROCm version 'apt/...'


---

### 评论 #3 — ROCmSupport (2021-04-19T12:52:45Z)

Hi @ScarFez 
Thanks for reaching out.
There will not be any install script.
Installation of rocm on a clean system can be done by "sudo apt install rocm-dkms" and other meta packages like rocm-libs etc.
Thank you.

---
