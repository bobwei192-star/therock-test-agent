# Can't install rock/rocm on Linux kernel 5.13.0-27-generic

> **Issue #1658**
> **状态**: closed
> **创建时间**: 2022-01-19T22:05:20Z
> **更新时间**: 2022-02-21T08:32:41Z
> **关闭时间**: 2022-02-21T08:32:41Z
> **作者**: bpickrel
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1658

## 描述

I just tried to install rocm on a brand new computer with freshly installed OS (Ubuntu 20.04.3), and encountered repeated failures including the the following:

```bpickrel@home-tower:~$ sudo apt-get install amdgpu-dkms
Reading package lists... Done
Building dependency tree
Reading state information... Done
amdgpu-dkms is already the newest version (1:5.11.32.40502-1350682).
0 upgraded, 0 newly installed, 0 to remove and 4 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] Y
Setting up amdgpu-dkms (1:5.11.32.40502-1350682) ...
Removing old amdgpu-5.11.32-1350682 DKMS files...

------------------------------
Deleting module version: 5.11.32-1350682
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-5.11.32-1350682 DKMS files...
Building for 5.13.0-27-generic
Building for architecture x86_64
Building initial module for 5.13.0-27-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms.0.crash'
Error! Bad return status for module build on kernel: 5.13.0-27-generic (x86_64)
Consult /var/lib/dkms/amdgpu/5.11.32-1350682/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```


The installation process for ver 4.5 apparently does not support the default linux kernel 5.13.0-27-generic.  (Apparently the previous version rocm 4.3 does not have this issue.)




---

## 评论 (14 条)

### 评论 #1 — ramcherukuri (2022-01-19T22:25:58Z)

From 4.5 installation steps changed for DKMS, here you can find the details. 
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#installer-script-method 

---

### 评论 #2 — srinivamd (2022-01-19T22:29:37Z)


> The installation process for ver 4.5 apparently does not support the default linux kernel 5.13.0-27-generic. (Apparently the previous version rocm 4.3 does not have this issue.)

Yes, Ubuntu 20.04 updated HWE kernel to 5.13 which will be supported in the next ROCm release. 

---

### 评论 #3 — bpickrel (2022-01-19T22:49:56Z)

Why do the instructions at [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#confirm-you-have-a-supported-linux-distribution-version](url) not make that clear? The  ["System Requirements"](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#confirm-you-have-a-supported-linux-distribution-version) paragraph states that Ubuntu 20.04.3 is supported.

---

### 评论 #4 — Weaverzhu (2022-01-23T08:40:49Z)

```c
In file included from /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:34:
 /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_topology.h:229:11: error: conflicting types for ‘amd_iommu_pc_get_max_banks’
   229 | extern u8 amd_iommu_pc_get_max_banks(u16 devid);
       |           ^~~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:31:
 ./include/linux/amd-iommu.h:201:4: note: previous declaration of ‘amd_iommu_pc_get_max_banks’ was here
   201 | u8 amd_iommu_pc_get_max_banks(unsigned int idx);
       |    ^~~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:34:
 /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_topology.h:230:11: error: conflicting types for ‘amd_iommu_pc_get_max_counters’
   230 | extern u8 amd_iommu_pc_get_max_counters(u16 devid);
       |           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:31:
 ./include/linux/amd-iommu.h:202:4: note: previous declaration of ‘amd_iommu_pc_get_max_counters’ was here
   202 | u8 amd_iommu_pc_get_max_counters(unsigned int idx);
       |    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:347:11: error: conflicting types for ‘amd_iommu_pc_get_max_banks’
   347 | extern u8 amd_iommu_pc_get_max_banks(u16 devid);
       |           ^~~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:31:
 ./include/linux/amd-iommu.h:201:4: note: previous declaration of ‘amd_iommu_pc_get_max_banks’ was here
   201 | u8 amd_iommu_pc_get_max_banks(unsigned int idx);
       |    ^~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:348:11: error: conflicting types for ‘amd_iommu_pc_get_max_counters’
   348 | extern u8 amd_iommu_pc_get_max_counters(u16 devid);
       |           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.c:31:
 ./include/linux/amd-iommu.h:202:4: note: previous declaration of ‘amd_iommu_pc_get_max_counters’ was here
   202 | u8 amd_iommu_pc_get_max_counters(unsigned int idx);
       |    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 make[2]: *** [scripts/Makefile.build:281: /var/lib/dkms/amdgpu/5.11.32-1350682/build/amd/amdgpu/../amdkfd/kfd_iommu.o] Error 1
```

looks like it's triggered by a compliation error.


---

### 评论 #5 — ptd006 (2022-01-28T22:35:06Z)

Same issue on a freshly upgrade'd (to 5.13.0-27) Ubuntu 20.04.1.

---

### 评论 #6 — bpickrel (2022-01-28T23:20:08Z)

A couple of other bits of info:  Ubuntu version 20 changed kernel versions from 11 to 13 this past August, which may have been the genesis of this error; but whichever kernel is still designated Ubuntu version 20.04.3; 

I was finally able to install (not build) ROCm by using the contents of the Docker file at [RadeonOpenCompute](https://github.com/RadeonOpenCompute/ROCm-docker/blob/master/dev/Dockerfile-ubuntu-20.04-complete) as a guide.  Most of the commands need to have "sudo" prefixed in order to run them from the command line.

---

### 评论 #7 — jrbyrnes (2022-01-28T23:44:01Z)

I ran into this issue on a fresh upgrade to (5.13.0-27) on Ubuntu release
as well. To resolve, I rolled back the kernel to 5.11 with the HWE tools.

Rollback, download (linux-headers-5.11.0-46-generic,
linux-image-5.11.0-46-generic, linux-modules-5.11.0-46-generic,
linux-modules-extra-5.11.0-46-generic, linux-tools-5.11.0-46-generic,
linux-hwe-5.11-tools-common) from here
<https://packages.ubuntu.com/source/focal-updates/linux-hwe-5.11>. Install
with sudo dpkg -i *.deb.

Purge 5.13

sudo apt-get autopurge 'linux-image-5.13.0-*-generic' \
'linux-image-unsigned-5.13.0-*-generic' 'linux-modules-5.13.0-*-generic' \
'linux-hwe-5.13-headers-5.13.0-*' linux-generic-hwe-20.04

After this, I was able to install ROCm using amdgpu-install and run. Also,
I was able to build from source.



On Fri, Jan 28, 2022 at 3:20 PM bpickrel ***@***.***> wrote:

> A couple of other bits of info: Ubuntu version 20 changed kernel versions
> from 11 to 13 this past August, which may have been the genesis of this
> error; but whichever kernel is still designated Ubuntu version 20.04.3;
>
> I was finally able to install (not build) ROCm by using the contents of
> the Docker file at RadeonOpenCompute
> <https://github.com/RadeonOpenCompute/ROCm-docker/blob/master/dev/Dockerfile-ubuntu-20.04-complete>
> as a guide. Most of the commands need to have "sudo" prefixed in order to
> run them from the command line.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1658#issuecomment-1024735926>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABQDYWZJEZWBZX34H7J7WADUYMQDRANCNFSM5MLDU5OQ>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


---

### 评论 #8 — Weaverzhu (2022-01-29T03:44:30Z)

My workaround is to uninstall kernel 5.13 and I found it work in 5.11.

---

### 评论 #9 — wertysas (2022-01-29T20:30:03Z)

I also had to downgrade to the 5.11 kernel which solved the problem.

---

### 评论 #10 — ROCmSupport (2022-01-31T06:25:47Z)

Hi @bpickrel and all,
Thanks for reaching out.

We are aware of the issue and team is coming up with a fix/workaround. We have an internal issue already filed for this.
As Ubuntu recently pushed a new kernel which is 5.13.0-27, this problem happened. 
Things are pretty good with 5.11 and our internal teams are proceeding with this for now.
Meanwhile I request everyone to roll back to 5.11 kernel which is an approved kernel by ROCm.
I will keep you posted. 
Thank you.


---

### 评论 #11 — ROCmSupport (2022-02-07T10:38:48Z)

Good news is that, 5.0 internal builds are ready with fix/workaround incorporated. I have verified too and things are working good.
Please stay tuned for 5.0 builds(will be released very soon) having the resolution for this issue.
Thank you.

---

### 评论 #12 — ptd006 (2022-02-07T11:10:37Z)

Great news, thanks for the update :)

I am only a lazy amateur running a rig that I update-upgrade-vacuum every 6 weeks or so.  I know occasionally all magic breaks but it'd really be great to keep up with LTS updates in future :)

---

### 评论 #13 — ptd006 (2022-02-12T16:36:29Z)

Thanks, 5.0.0.50000-49 working fine with kernel 5.13.0-28 on 20.04 LTS

---

### 评论 #14 — ROCmSupport (2022-02-21T08:32:41Z)

Thanks for the confirmation.
I am closing this thread as the fix is validated. Thank you.

---
