# Errors installing on kernel 4.17 or 4.18

> **Issue #473**
> **状态**: closed
> **创建时间**: 2018-07-27T10:03:42Z
> **更新时间**: 2021-04-05T07:57:13Z
> **关闭时间**: 2019-01-04T00:10:49Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/473

## 描述

When attempting ROCm 1.8.2 install on Ubuntu 18.04 with kernel 4.17 or 4.18 (tried both), these are the errors:
Building initial module for 4.18.0-041800rc6-generic
ERROR (dkms apport): kernel package linux-headers-4.18.0-041800rc6-generic is not supported
Error! Bad return status for module build on kernel: 4.18.0-041800rc6-generic (x86_64)
Consult /var/lib/dkms/amdgpu/1.8-192/build/make.log for more information.

/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c: In function ‘amdgpu_pmops_runtime_suspend’:
/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c:727:2: error: implicit declaration of function ‘vga_switcheroo_set_dynamic_switch’; did you mean ‘vga_switcheroo_process_delayed_switch’? [-Werror=implicit-function-declaration]
  vga_switcheroo_set_dynamic_switch(pdev, VGA_SWITCHEROO_OFF);

---

## 评论 (14 条)

### 评论 #1 — preda (2018-07-27T10:33:12Z)

Good news, it installs and works on Ubuntu 18.04 with kernel 4.15.
Good news too, in one situation I observe a 9% performance increase compared with amdgpu-pro 18.20 in similar setup.

Looking forward to being able to use ROCm with kernel 4.17.

---

### 评论 #2 — mdPlusPlus (2018-08-05T06:24:37Z)

Afaik the next supported kernel will be 4.19, but I could be wrong.

---

### 评论 #3 — PsySc0rpi0n (2018-08-12T10:32:12Z)

Same or very similar errors here on Debian 9. Tried kernel 4.9.0-7 and 4.17.0-0.bpo.1-amd64.
I'm not sure the last official kernel supported but if it was 4.15 and the next one is 4.19, it's a pretty nice time gap!

---

### 评论 #4 — PsySc0rpi0n (2018-08-16T18:58:13Z)

Is there a way to be noticed when the next kernel version is compatible with ROCm?

---

### 评论 #5 — valeriob01 (2018-08-21T10:30:54Z)

Installed ubuntu 18.04 and ROCm and rocm-opencl-dev, but opencl does not work, when running the program it terminates with this error: platform not found .


---

### 评论 #6 — PhilipDeegan (2018-08-22T14:04:39Z)

the function ```vga_switcheroo_set_dynamic_switch``` 

does not exist in kernel 4.17

---

### 评论 #7 — rumatadest (2018-09-13T15:12:39Z)

Same issue with vga_switcheroo_set_dynamic_switch on Fedora 28. 
tested with lastest standard fedora kernel :  kernel-4.18.7-200.fc28.x86_64 

cat /var/lib/dkms/amdgpu/1.9-211.el7/build/make.log

DKMS make.log for amdgpu-1.9-211.el7 for kernel 4.18.7-200.fc28.x86_64 (x86_64)
Sun Sep 16 00:33:40 MSK 2018
make: Entering directory '/usr/src/kernels/4.18.7-200.fc28.x86_64'
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/main.o
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_drv.c: In function ‘amdgpu_pmops_runtime_suspend’:
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_drv.c:768:2: error: implicit declaration of function ‘vga_switcheroo_set_dynamic_switch’; did you mean ‘vga_switcheroo_process_delayed_switch’? [-Werror=implicit-function-declaration]
  vga_switcheroo_set_dynamic_switch(pdev, VGA_SWITCHEROO_OFF);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  vga_switcheroo_process_delayed_switch
cc1: some warnings being treated as errors
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/symbols.o
make[2]: *** [scripts/Makefile.build:317: /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_drv.o] Error 1
make[1]: *** [scripts/Makefile.build:558: /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu] Error 2
make[1]: *** Waiting for unfinished jobs....
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_drm_global.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_prime.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/amdkcl.o
make: *** [Makefile:1508: _module_/var/lib/dkms/amdgpu/1.9-211.el7/build] Error 2
make: Leaving directory '/usr/src/kernels/4.18.7-200.fc28.x86_64'


---

### 评论 #8 — ernestoriv7 (2018-09-20T13:35:07Z)

@rumatadest 

Could you please let me know the steps that you followed to installed rocm in fedora 28? I'm planning to use that distro due to hardware compatibility.

---

### 评论 #9 — rumatadest (2018-09-20T14:46:02Z)

I used "Net install" version Fedora 28.  Fedora-Server-netinst-x86_64-28-1.1.iso
1. Standatd instalation with minumum componets. Only base system and "developmet tools". Without GUI
2. Update to lastest package with yum update.  It will install kernel 4.18.x instead 4.16
3. Next steps from this wiki : https://github.com/RadeonOpenCompute/ROCm#centosrhel-7-both-74-and-75-support
i think that devtoolset-7 is not needed. fedora 28 used gcc 8 from box.
4. add ROCm rpm repo
5. try to install rocm-dkms
6. instalation fail (((




---

### 评论 #10 — ernestoriv7 (2018-09-20T15:05:20Z)

> I used "Net install" version Fedora 28. Fedora-Server-netinst-x86_64-28-1.1.iso
> 
> 1. Standatd instalation with minumum componets. Only base system and "developmet tools". Without GUI
> 2. Update to lastest package with yum update.  It will install kernel 4.18.x instead 4.16
> 3. Next steps from this wiki : https://github.com/RadeonOpenCompute/ROCm#centosrhel-7-both-74-and-75-support
>    i think that devtoolset-7 is not needed. fedora 28 used gcc 8 from box.
> 4. add ROCm rpm repo
> 5. try to install rocm-dkms
> 6. instalation fail (((

Great, thanks. From what I see the ROCm github installation instructions, rocm-dkms is not needed for newer kernels, only the other packages. You can check the details over here.

https://github.com/RadeonOpenCompute/ROCm

Also this link shows the packages that should be installed to install rocm withoud dkms.

https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/open-source-amd-linux/1047471-amd-rocm-1-9-available-with-vega-20-support-plus-upstream-kernel-compatibility/page2

I will try to do that on fedora 28 and let you know.

Thanks again



---

### 评论 #11 — preda (2019-01-04T00:10:49Z)

Closing because ROCm 2.0 can now be installed both on Ubuntu 18.04 and 18.10.

---

### 评论 #12 — jlgreathouse (2019-01-04T00:15:28Z)

@preda it looks like you and I are both combing through old issues. I was just about to post here. :) Thanks for going through these old issues and cleaning up the solved ones.

If y'all are interested in installing ROCm 1.9.2 or 2.0 (and future versions) on Ubuntu 18.10, Fedora 28, Fedora 29, etc. that using new kernels such as 4.17 or 4.18, you might want to check out our new [Experimental ROC](https://github.com/RadeonOpenCompute/Experimental_ROC) project. This includes scripts that will install ROCm on these systems for you. preda is already aware of these, but I'm putting the link here in case someone else finds this issue through an internet search.

In addition, we have written new documentation to describe the tradeoffs between our `rock-dkms` module and the upstream kernel driver in 4.17 and above. See [this section](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#rocm-support-in-upstream-linux-kernels) for more information and [this section](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#using-debian-based-rocm-with-upstream-kernel-drivers) for some more information about installing using an upstream kernel.

---

### 评论 #13 — randall-coding (2021-04-05T04:30:32Z)

I'm getting this error on Ubuntu 18.04, kernel 4.15, but the other user said 4.15 should work?  Any recommendations?  I'm installing using this package https://www.amd.com/en/support/kb/release-notes/rn-prorad-lin-18-20

` error: implicit declaration of function ‘vga_switcheroo_set_dynamic_switch’; did you mean ‘vga_switcheroo_process_delayed_switch’`

---

### 评论 #14 — ROCmSupport (2021-04-05T07:57:13Z)

Hi @Randall-Coding 
4.15 kernel is very old, recommend to use 5.4 or bigger one.
Thank you.

---
