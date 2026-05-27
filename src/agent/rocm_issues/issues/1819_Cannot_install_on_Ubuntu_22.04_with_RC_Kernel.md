# Cannot install on Ubuntu 22.04 with RC Kernel.

> **Issue #1819**
> **状态**: closed
> **创建时间**: 2022-10-01T23:22:31Z
> **更新时间**: 2024-02-08T16:37:00Z
> **关闭时间**: 2024-02-08T16:37:00Z
> **作者**: Chase-san
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1819

## 描述

I get an error with `amdgpu-dkms` when trying to install with the linux RC kernel.

```
Hit:1 http://deb.debian.org/debian experimental InRelease
Hit:2 http://ca.archive.ubuntu.com/ubuntu jammy InRelease                                                                                                                                          
Hit:3 https://repo.steampowered.com/steam stable InRelease                                                                                                                                         
Get:4 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]                                                                                                           
Hit:5 https://repo.radeon.com/amdgpu/5.3/ubuntu jammy InRelease                                                                                                                      
Hit:6 https://repo.radeon.com/rocm/apt/5.3 jammy InRelease                                                                              
Get:7 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]                                                               
Get:8 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease [99.8 kB]                                               
Hit:9 https://ppa.launchpadcontent.net/cappelikan/ppa/ubuntu jammy InRelease                                                  
Hit:10 https://ppa.launchpadcontent.net/ubuntucinnamonremix/all/ubuntu jammy InRelease       
Fetched 324 kB in 1s (361 kB/s)                            
Reading package lists... Done
W: http://deb.debian.org/debian/dists/experimental/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
amdgpu-dkms is already the newest version (1:5.18.2.22.40.50300-1483871.22.04).
amdgpu-lib is already the newest version (1:5.3.50300-1483871.22.04).
linux-headers-6.0.0-rc7-amd64 is already the newest version (6.0~rc7-1~exp1).
rocm-hip-runtime is already the newest version (5.3.0.50300-63~22.04).
rocm-opencl-runtime is already the newest version (5.3.0.50300-63~22.04).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Setting up amdgpu-dkms (1:5.18.2.22.40.50300-1483871.22.04) ...
Removing old amdgpu-5.18.2.22.40-1483871.22.04 DKMS files...
Deleting module amdgpu-5.18.2.22.40-1483871.22.04 completely from the DKMS tree.
Loading new amdgpu-5.18.2.22.40-1483871.22.04 DKMS files...
Building for 6.0.0-rc7-amd64
Building for architecture x86_64
Building initial module for 6.0.0-rc7-amd64
ERROR (dkms apport): kernel package linux-headers-6.0.0-rc7-amd64 is not supported
Error! Bad return status for module build on kernel: 6.0.0-rc7-amd64 (x86_64)
Consult /var/lib/dkms/amdgpu/5.18.2.22.40-1483871.22.04/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

The RC kernel is the only one that supports bluetooth on the ASUS X670E board I am using.

---

## 评论 (5 条)

### 评论 #1 — xuhuisheng (2022-10-02T00:18:03Z)

It is said that support ubuntu-22.04.1 with kernel-5.15 and OEM 5.17. So it cannot support kernel-6.0.0-rc7.

<https://docs.amd.com/bundle/ROCm-Release-Notes-v5.3/page/About_This_Document.html#d2e37>

Since ubuntu LTS will change linux kernel version in its lifecycle. We'd better not focus on the version of ubuntu but version of kernel.

Thats means amdgpu-dkms may break on the next point version of ubuntu LTS, if you cannot fix kernel compilation issue, like me. Please remember which version of kernel can run properly with related amdgpu-dkms, and at least hold one related version of kernel on the PC.

---

Emm~, kernel-6.0.0-rc7 must use latest codes, so it is possible the upstream amdgpu codes in 6.0.0-rc7 just equals with latest version of seperated admgpu codes.

You can have a try upstream amdgpu with 6.0.0-rc7.  just install ROCm without dkms.

`sudo amdgpu-install --usecase=rocm --no-dkms`

---

### 评论 #2 — ghost (2022-10-06T16:25:01Z)

Try 
https://techviewleo.com/install-linux-kernel-6-on-ubuntu/

---

### 评论 #3 — Chase-san (2022-10-08T02:52:31Z)

@nenericamarius it was not an issue installing the kernel hah. That went fine, but yes I realize that kernel 6.0 already has recent drivers.

---

### 评论 #4 — dchmelik (2022-11-18T12:29:27Z)

I have same problem on 22.04 Ubuntu-based with just the default (generic, lowlatency) kernels: please update the bug report title to make clear if it's a more general problem (however it might just be when using 'opencl=rocr,legacy', and not when not using 'legacy', which still means it's quite broken for people without excessive display/video/graphics cards).

---

### 评论 #5 — nartmada (2024-02-02T22:52:44Z)

Hi @Chase-san, please check latest ROCm 6.0.2 to see if your issue still exists.  Please close the ticket if your issue has been fixed.  Thanks.

---
