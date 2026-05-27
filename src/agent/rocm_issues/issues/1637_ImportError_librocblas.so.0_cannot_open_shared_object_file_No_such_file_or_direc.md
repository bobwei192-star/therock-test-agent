#  ImportError: librocblas.so.0: cannot open shared object file: No such file or directory

> **Issue #1637**
> **状态**: closed
> **创建时间**: 2021-12-12T19:58:35Z
> **更新时间**: 2021-12-20T11:55:13Z
> **关闭时间**: 2021-12-20T09:26:47Z
> **作者**: Jourdelune
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1637

## 描述

Hello, I get this error when I want to use tenserflow rocm
`    from tensorflow.python._pywrap_tensorflow_internal import *
ImportError: librccl.so.1: cannot open shared object file: No such file or directory
`

but I don't have this file in `opt/rocm/lib`

```
cmake                          libhipblas.so           libhip_hcc.so        libhiprtc.so        libmcwamp_hsa.so  librocblas.so.0         librocfft-device.so.0        librocfft.so.0        librocr_debug_agent64.so
libclang_rt.builtins-x86_64.a  libhipblas.so.0         libhip_hcc_static.a  libmcwamp_atomic.a  libmcwamp.so      librocblas.so.2.2.11.0  librocfft-device.so.0.9.4.0  librocfft.so.0.9.4.0
libhc_am.so                    libhipblas.so.0.12.6.0  libhiprand.so        libmcwamp_cpu.so    librocblas.so     librocfft-device.so     librocfft.so                 librocrand.so
```

And when I try to install rocm-libs I get this error

```
sudo apt install rocm-libs
[sudo] password for server: 
Sorry, try again.
[sudo] password for server: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-libs is already the newest version (2.6.22).
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
2 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] Y
Setting up rock-dkms (2.6-22) ...
Removing old amdgpu-2.6-22 DKMS files...

------------------------------
Deleting module version: 2.6-22
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-2.6-22 DKMS files...
Building for 5.4.0-91-generic
Building for architecture x86_64
Building initial module for 5.4.0-91-generic
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: aclocal --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /usr/bin/autoconf --force
autoreconf: running: /usr/bin/autoheader --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms.0.crash'
Error! Bad return status for module build on kernel: 5.4.0-91-generic (x86_64)
Consult /var/lib/dkms/amdgpu/2.6-22/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
No apport report written because the error message indicates its a followup error from a previous failure.
                                                                                                          dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

here are the contents of `/var/crash/rock-dkms.0.crash`

```
ProblemType: Package
DKMSBuildLog:
 DKMS make.log for amdgpu-2.6-22 for kernel 5.4.0-91-generic (x86_64)
 Sun 12 Dec 2021 07:45:54 PM UTC
 make: Entering directory '/usr/src/linux-headers-5.4.0-91-generic'
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_drm.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/main.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/symbols.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/sched_main.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_memory.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_drv.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_device.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_tt.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/ttm/backport/backport.h:7,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_memory.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/sched_fence.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/../include/../backport/backport.h:11,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_drv.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/sched_entity.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/../include/../backport/backport.h:11,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_device.o] Error 1
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu] Error 2
 make[1]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_fence.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/ttm/backport/backport.h:7,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_tt.o] Error 1
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.6-22/build/ttm] Error 2
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_fence_array.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_kthread.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_io.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_reservation.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_reservation.c:33:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_reservation.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   LD [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/amd-sched.o
 /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
 /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.c:199:83: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
   199 |  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed",_kcl_pcie_link_speed_stub);
       |                                                                                   ^~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.c:3:
 /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_common.h:22:63: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
    22 | static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
       |                                                         ~~~~~~^~~~~~~
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl] Error 2
 make: *** [Makefile:1762: /var/lib/dkms/amdgpu/2.6-22/build] Error 2
 make: Leaving directory '/usr/src/linux-headers-5.4.0-91-generic'
DKMSKernelVersion: 5.4.0-91-generic
Date: Sun Dec 12 19:45:57 2021
Package: rock-dkms 2.6-22
PackageVersion: 2.6-22
SourcePackage: rock-dkms
Title: rock-dkms 2.6-22: amdgpu kernel module failed to build
```

Here is my configuration:
- kernel: 5.4.0-91-generic
- cpu: Intel(R) Core(TM) i5-9600K CPU @ 3.70GHz
- gpu: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
- os: Ubuntu 20.04.3 LTS


---

## 评论 (9 条)

### 评论 #1 — martinezhermes (2021-12-13T14:25:02Z)

Hey, I have a config very similar to yours (we don't have the same cpu), I had that issue before `ImportError: librocblas.so.0: cannot open shared object file`, I solved it by rolling back to ROCm 4.1.
The latest verstion (4.5) is very buggy in this setup, it think it has to do with the linux kernel. ROCm 4.1 works as expected.

---

### 评论 #2 — Jourdelune (2021-12-13T17:07:39Z)

Okay, I'll try this version!

---

### 评论 #3 — Jourdelune (2021-12-13T20:40:55Z)

It does not work, the installation is done well but the files `/opt/rocm/bin/rocminfo`
`/opt/rocm/opencl/bin/clinfo` does not exist and if I install earlier versions like crom-3, I get this error with clinfo: `ERROR: clGetPlatformIDs(-1001)`

---

### 评论 #4 — martinezhermes (2021-12-14T09:02:07Z)

> It does not work, the installation is done well but the files `/opt/rocm/bin/rocminfo`
> `/opt/rocm/opencl/bin/clinfo` does not exist and if I install earlier versions like crom-3, I get this error with clinfo: `ERROR: clGetPlatformIDs(-1001)`

have you checked yourself that the folder /opt/rocm-4.1.0/bin/ contains clinfo? if so then remove rocm inside /opt/ and ln -s to 4.1.0. BTW I've updated to 4.2.0 now in order to use PyTorch from pip

also, `Ach9#2154` I'm based in Paris

---

### 评论 #5 — Jourdelune (2021-12-14T09:47:57Z)

I have checked at the maint, otherwise I have done your manipulation and now rocm contains clinfo but not the rest, yet when I install rocm it does not send an error

---

### 评论 #6 — Jourdelune (2021-12-14T09:50:58Z)

if I install rocm with amdgpu, it also sends no error:
```
 sudo amdgpu-install --usecase=rocm
Reading package lists... Done
Building dependency tree
Reading state information... Done
linux-headers-5.4.0-91-generic is already the newest version (5.4.0-91.102).
linux-modules-extra-5.4.0-91-generic is already the newest version (5.4.0-91.102).
amdgpu-dkms is already the newest version (1:5.11.32.40501-1337797).
rocm-dev is already the newest version (4.5.0.40500-56).
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
````
but how can I use it with tenserflow if it looks for a specific file?

---

### 评论 #7 — Jourdelune (2021-12-14T10:16:09Z)

I redid an installation with amdgpu and now I have 2 rocm folders, and if I do rocm-smi, it works. I guess I have to do `sudo apt install rocm-libs miopen-hip rccl` and then I can run tenserflow. However I still don't have these 2 files 
`/opt/rocm/bin/rocminfo`
`/opt/rocm/opencl/bin/clinfo`

---

### 评论 #8 — ROCmSupport (2021-12-20T09:26:47Z)

Hi @Jourdelune 
Thanks for reaching out.
I certainly understood the problem.
As ROCm does not support gfx8 anymore, we can not help you on this.
Request to try on officially supported cards and reach us for official help, we are here to help you.
Thank you.

---

### 评论 #9 — Jourdelune (2021-12-20T11:55:13Z)

Ok, is there any way to use these graphics cards with tenserflow to speed up the process? It's a shame to have 3 graphics cards that are useless...

---
