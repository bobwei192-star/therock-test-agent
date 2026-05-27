# Unable to locate package rocm, but can install rocm-opencl

> **Issue #311**
> **状态**: closed
> **创建时间**: 2018-01-24T13:57:52Z
> **更新时间**: 2018-08-24T00:57:50Z
> **关闭时间**: 2018-08-24T00:57:50Z
> **作者**: RaymonSHan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/311

## 描述

I add deb, updata & upgrade, following https://rocm.github.io/install.html 
but 

raymon@raymonR7: ~ $ sudo apt-get install rocm-opencl
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-opencl is already the newest version (1.2.0-2017121952).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
raymon@raymonR7:~$ 

raymon@raymonR7: ~ $ sudo apt-get install rocm
[sudo] password for raymon: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package rocm









---

## 评论 (6 条)

### 评论 #1 — gstoner (2018-01-24T14:42:57Z)

What Distro and which version are you working on.   Also is this being installed on AMDGPUpro driver or you following the install instruction for installing the ROCm driver.   Since the package here are for the ROCm driver 

---

### 评论 #2 — gstoner (2018-01-24T14:43:59Z)

Normally you do sudo apt-get install rocm rocm-opencl-dev at the same time when you do install. 

---

### 评论 #3 — RaymonSHan (2018-01-24T16:34:18Z)

ub16.04.3
I have uninstalled AMDGPU driver, and installed ROCm drvier.

the things happed in this way.
after deb & update, 
sudo apt-get install rocm                         .... it is OK
sudo apt-get install rocm-opencl            ....E: Unable to locate package rocm-opencl

but when i tab the command apt-get remove rocm,    the rocm-opencl is list, while rocm is not
so i
sudo apt-get remove rocm                          ....E: Unable to locate package rocm
sudo apt-get remove rocm-opencl             .... it work , removed

reboot, deb and update again following rocm.github.io/install.html
sudo apt-get install rocm                         ....E: Unable to locate package rocm
sudo apt-get install rocm-opencl            ... it is OK.

i do not know the struct of deb server, but i can install any packet list in
http://repo.radeon.com/rocm/apt/debian/pool/main/r/
but there are not rocm

---

### 评论 #4 — RaymonSHan (2018-01-29T12:02:25Z)

Maybe it is not the right way, but i almost finish it in following way.

following wiki of rocm , install rocm_dkms and rocm_opencl.  then install AMDGPU-pro. 
i know, it is not the right way, but my hipconfig report hcc & my opencl program is OK after this.

now the only thing left is i meet 'error while loading shared libraries: libCXLActivityLogger.so: cannot open shared object file: No such file or directory"

i found that file in rocm repo, the only thing is which path should i place it.
THANKS

---

### 评论 #5 — ArlasJ (2018-01-31T10:27:11Z)

Hey RaymonSHan,

I got the same error. Can you help me please with that?
libCXLActivityLogger.so

---

### 评论 #6 — gstoner (2018-03-02T23:07:21Z)

@RaymonSHan  Can you try the beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2  It support 4.13 Linux kernel 

---
