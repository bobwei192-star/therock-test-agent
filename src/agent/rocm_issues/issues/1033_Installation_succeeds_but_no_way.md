# Installation succeeds but no way

> **Issue #1033**
> **状态**: closed
> **创建时间**: 2020-03-01T13:57:11Z
> **更新时间**: 2020-12-01T19:16:39Z
> **关闭时间**: 2020-12-01T18:25:46Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1033

## 描述

# apt upgrade
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
4 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
Setting up linux-headers-4.19.0-8-amd64 (4.19.98-1) ...
/etc/kernel/header_postinst.d/dkms:
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/2.7-27/source/dkms.conf does not exist.
run-parts: /etc/kernel/header_postinst.d/dkms exited with return code 4
Failed to process /etc/kernel/header_postinst.d at /var/lib/dpkg/info/linux-headers-4.19.0-8-amd64.postinst line 11.
dpkg: error processing package linux-headers-4.19.0-8-amd64 (--configure):
 installed linux-headers-4.19.0-8-amd64 package post-installation script subprocess returned error exit status 1
Setting up linux-image-4.19.0-8-amd64 (4.19.98-1) ...
/etc/kernel/postinst.d/dkms:
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/2.7-27/source/dkms.conf does not exist.
run-parts: /etc/kernel/postinst.d/dkms exited with return code 4
dpkg: error processing package linux-image-4.19.0-8-amd64 (--configure):
 installed linux-image-4.19.0-8-amd64 package post-installation script subprocess returned error exit status 1
dpkg: dependency problems prevent configuration of linux-headers-amd64:
 linux-headers-amd64 depends on linux-headers-4.19.0-8-amd64; however:
  Package linux-headers-4.19.0-8-amd64 is not configured yet.

dpkg: error processing package linux-headers-amd64 (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of linux-image-amd64:
 linux-image-amd64 depends on linux-image-4.19.0-8-amd64; however:
  Package linux-image-4.19.0-8-amd64 is not configured yet.

dpkg: error processing package linux-image-amd64 (--configure):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 linux-headers-4.19.0-8-amd64
 linux-image-4.19.0-8-amd64
 linux-headers-amd64
 linux-image-amd64
E: Sub-process /usr/bin/dpkg returned an error code (1)


---

## 评论 (16 条)

### 评论 #1 — valeriob01 (2020-03-01T16:18:41Z)

this didn't work and I had to reinstall the system, removing rocm failed.


---

### 评论 #2 — valeriob01 (2020-03-01T16:51:54Z)

Reinstalled the system. Reinstalled ROCm.



---

### 评论 #3 — rkothako (2020-03-02T04:32:55Z)

@valeriob01 
Can I know the Ubuntu version you are using?
ROCm 3.1 supports Ubuntu 16.04.6 with 4.15 kernels and Ubuntu 18.04.3 with Ubuntu 5.3 kernels.
There is no guarantee that ROCm works for any other kernel like 4.19. 

---

### 评论 #4 — valeriob01 (2020-03-02T06:11:57Z)

> @valeriob01
> Can I know the Ubuntu version you are using?
> ROCm 3.1 supports Ubuntu 16.04.6 with 4.15 kernels and Ubuntu 18.04.3 with Ubuntu 5.3 kernels.
> There is no guarantee that ROCm works for any other kernel like 4.19.

Not using Ubuntu, I am using Debian 10.1 with kernel 4.19.0-8, I wrote an installation script that works on Debian.

---

### 评论 #5 — rkothako (2020-03-02T07:21:04Z)

Debian OS is not an officially supported OS for ROCm as per https://github.com/RadeonOpenCompute/ROCm --> Supported Operating Systems section

---

### 评论 #6 — valeriob01 (2020-03-02T08:07:44Z)

> Debian OS is not an officially supported OS for ROCm as per https://github.com/RadeonOpenCompute/ROCm --> Supported Operating Systems section

AND ?

I have run ROCm on Debian since version 1.9



---

### 评论 #7 — rkothako (2020-03-02T08:16:20Z)

OK. It might or might not work as we do not support officially.
I recommend to go ahead with working version.

---

### 评论 #8 — valeriob01 (2020-03-02T08:22:07Z)

> OK. It might or might not work as we do not support officially.
> I recommend to go ahead with working version.

But let me say it, it is unfortunate that you don't support Debian. As I recall it Ubuntu is a _derivative_ of Debian. So you might as well support Debian.


---

### 评论 #9 — preda (2020-03-02T10:36:08Z)

It would be nice to expand the official or not-so-offical list of setups on which ROCm works. For example, I've been running ROCm for years on Linux kernels that were not on the "supported" list, and it did work. Right now I'm running ROCm 3.1 on Linux kernel 5.6, before that ROCm 2.10 on Linux kernel 5.6, 5.5, 5.4.

I guess it comes down to whether AMD can afford to do more extensive validation on a wider range of OSs / kernels for each release. The benefit would be that newcomers would be more likely to find their setup of choice as "supported" and thus enticed to try ROCm with confidence.


---

### 评论 #10 — bcllcb (2020-03-07T14:17:39Z)

>  For example, I've been running ROCm for years on Linux kernels that were not on the "supported" list, and it did work. Right now I'm running ROCm 3.1 on Linux kernel 5.6, before that ROCm 2.10 on Linux kernel 5.6, 5.5, 5.4.
> 
Can you tell us how to install without errors using debian? I test with 4.19 and 5.4 without success.
Thanks



---

### 评论 #11 — valeriob01 (2020-03-07T14:33:54Z)

> > For example, I've been running ROCm for years on Linux kernels that were not on the "supported" list, and it did work. Right now I'm running ROCm 3.1 on Linux kernel 5.6, before that ROCm 2.10 on Linux kernel 5.6, 5.5, 5.4.
> 
> Can you tell us how to install without errors using debian? I test with 4.19 and 5.4 without success.
> Thanks

https://github.com/valeriob01/Mersenne-gpu-computing-node/blob/master/install-rocm.Makefile


---

### 评论 #12 — valeriob01 (2020-03-07T14:45:45Z)

> > > For example, I've been running ROCm for years on Linux kernels that were not on the "supported" list, and it did work. Right now I'm running ROCm 3.1 on Linux kernel 5.6, before that ROCm 2.10 on Linux kernel 5.6, 5.5, 5.4.
> > 
> > 
> > Can you tell us how to install without errors using debian? I test with 4.19 and 5.4 without success.
> > Thanks
> 
> https://github.com/valeriob01/Mersenne-gpu-computing-node/blob/master/install-rocm.Makefile

you can substitute the /debian/ part with /2.10/ to get ver. 2.10


---

### 评论 #13 — bcllcb (2020-03-08T19:56:59Z)

> > > > For example, I've been running ROCm for years on Linux kernels that were not on the "supported" list, and it did work. Right now I'm running ROCm 3.1 on Linux kernel 5.6, before that ROCm 2.10 on Linux kernel 5.6, 5.5, 5.4.
> > > 
> > > 
> > > Can you tell us how to install without errors using debian? I test with 4.19 and 5.4 without success.
> > > Thanks
> > 
> > 
> > https://github.com/valeriob01/Mersenne-gpu-computing-node/blob/master/install-rocm.Makefile
> 
> you can substitute the /debian/ part with /2.10/ to get ver. 2.10

Thanks alot. Using debian 4.19.0-6-amd64 kernel is perfect.

---

### 评论 #14 — valeriob01 (2020-03-14T07:33:27Z)

Second attempt. Installation of ROCm 3.1.1 succeeds but program unable to find devices.
clGetDeviceID fails


---

### 评论 #15 — jlgreathouse (2020-12-01T18:25:46Z)

I'm sorry to hear that you had these issues at the time -- hopefully things are working a little better now. If you run into further problems with installing ROCm, please submit another issue. However, as noted in some of the responses, the ROCm team can only offer support on a limited number of operating systems and versions.

---

### 评论 #16 — valeriob01 (2020-12-01T19:16:39Z)

I had to adopt Ubuntu, since then the issue is solved. It is unfortunate that in order to be productive I had to change OS to solve the issue, seen that Ubuntu is a derivative of Debian. I expected Debian to get better support from AMD.


---
