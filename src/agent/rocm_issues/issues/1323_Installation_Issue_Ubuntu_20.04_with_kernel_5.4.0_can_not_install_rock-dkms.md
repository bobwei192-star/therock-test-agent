# Installation Issue: Ubuntu 20.04 with kernel 5.4.0 can not install rock-dkms

> **Issue #1323**
> **状态**: closed
> **创建时间**: 2020-12-08T12:31:16Z
> **更新时间**: 2021-03-11T06:48:08Z
> **关闭时间**: 2020-12-11T04:37:17Z
> **作者**: dasfinux
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1323

## 描述

I run install rocm-dkms, then got the fellowing message:

Loading new amdgpu-3.10-27 DKMS files...
Building for 5.4.0-56-generic
Building for architecture x86_64
Building initial module for 5.4.0-56-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms.0.cra
sh'
Error! Bad return status for module build on kernel: 5.4.0-56-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.10-27/build/make.log for more information.

And information in  /var/lib/dkms/amdgpu/3.10-27/build/make.log:

DKMS make.log for amdgpu-3.10-27 for kernel 5.4.0-56-generic (x86_64)
2020年 12月 08日 星期二 20:17:04 CST
make: 进入目录“/usr/src/linux-headers-5.4.0-56-generic”
/var/lib/dkms/amdgpu/3.10-27/build/Makefile:20: "Local GCC version 90303 does not match kernel compiler GCC version 90300"
/var/lib/dkms/amdgpu/3.10-27/build/Makefile:21: "This may cause unexpected and hard-to-isolate compiler-related issues"
  AR      /var/lib/dkms/amdgpu/3.10-27/build/built-in.a
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_memory.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_ioctl.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_cache.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_perf_event.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_kms.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_fence.c:30:1: warning: ‘dma_fence_test_signaled_any’ defined but not used [-Wunused-function]
   30 | dma_fence_test_signaled_any(struct dma_fence **fences, uint32_t count,
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_suspend.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_seq_file.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_connector.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.c:103:84: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  103 |  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed", _kcl_pcie_link_speed_stub);
      |                                                                                    ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.c:4:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_common.h:12:63: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
   12 | static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
      |                                                         ~~~~~~^~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_backlight.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_atomic_helper.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_fb.o
  LD [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_modeset_lock.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_modes.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_time.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/dma-buf/dma-resv.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fence.o
  LD [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_benchmark.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_test.o
  LD [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/amdttm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_afmt.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_trace_points.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fb.c: In function ‘amdgpufb_create’:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fb.c:252:14: warning: assignment discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  252 |  info->fbops = &amdgpufb_ops;
      |              ^
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_i2c.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.c: In function ‘amdgpu_read_platform_bios’:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.c:200:9: error: implicit declaration of function ‘pci_platform_rom’ [-Werror=implicit-function-declaration]
  200 |  bios = pci_platform_rom(adev->pdev, &size);
      |         ^~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.c:200:7: warning: assignment to ‘uint8_t *’ {aka ‘unsigned char *’} from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
  200 |  bios = pci_platform_rom(adev->pdev, &size);
      |       ^
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_dma_buf.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ib.o
cc1: some warnings being treated as errors
make[2]: *** [scripts/Makefile.build:275：/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.o] 错误 1
make[2]: *** 正在等待未完成的任务....
make[1]: *** [scripts/Makefile.build:522：/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu] 错误 2
make: *** [Makefile:1757：/var/lib/dkms/amdgpu/3.10-27/build] 错误 2
make: 离开目录“/usr/src/linux-headers-5.4.0-56-generic”



---

## 评论 (8 条)

### 评论 #1 — ROCmSupport (2020-12-08T12:58:58Z)

Thanks @dasfinux for reaching out.
We are ready with the fix and it will be pushed soon.

Actually its duplicate of #1315 

---

### 评论 #2 — ROCmSupport (2020-12-11T04:37:10Z)

Hi All,
Fix for 5.4.0-56 is ready and pushed too. Updated Documentation accordingly.
Request to try the new packages.

**_Note: AMD ROCm v3.10 fails to install on Ubuntu kernel v5.4.0-56. To resolve the installation issue, new packages for 'rock-dkms' and 'rock-dkms-firmware' are created and replaced. It is recommended to perform a clean and fresh installation with the new packages._**

Thank you.

---

### 评论 #3 — PierrickMonchoix (2021-01-30T10:31:43Z)

Hi! 
I have the same error as dasfinux.

I have just tried to install Rocm 4.0.0.40000-23 (following steps in the Rocm Website) with this version of Ubuntu:

~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.2 LTS
Release:	20.04
Codename:	focal

I have this error:   ( and the same log as dasfinux )

Loading new amdgpu-4.0-23 DKMS files...
Building for 5.8.0-41-generic
Building for architecture x86_64
Building initial module for 5.8.0-41-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms-firmware.0.crash'
Error! Bad return status for module build on kernel: 5.8.0-41-generic (x86_64)
Consult /var/lib/dkms/amdgpu/4.0-23/build/make.log for more information.
...
E: Sub-process /usr/bin/dpkg returned an error code (1)

May someone help me please.
(I'm new to Linux)

---

### 评论 #4 — seesturm (2021-01-30T11:19:21Z)

Hi @PierrickMonchoix . I have no relation with AMD and am only a user of ROCm. 
**My View**
* You dont have the same error as dasfinux. dasfinux had kernel 5.4 while you have kernel 5.8.
* At the time of issue creation the 5.4 kernel version was 5.4.0-56. ROCm 4.0 contains fixes for enabling dkms (kernel module) build on 5.4.0-56. Probably also all following updates of 5.4 do work too. (Currently it is 5.4.0-65)
* Release notes for ROCm claim Ubuntu 20.04.1 support. You have 20.04.2. AMD deciding for limiting support to 20.04.1 is rather unfortunate since default ubuntu desktop installation is already for 20.04.2
* I've seen indications that AMD is working on support for kernel 5.8 in one of the upcoming ROCm releases. When this comes ROCm will probably get compatible with 20.04.2. There was no timeline given though.

**Hints**
* https://ubuntu.com/download/server still gives option to download 20.04.1. (Don't know for how long). Nevertheless this is the server installation and you probably want desktop. You might succeed to "convert" 20.04.1 from server to destop by means of installing "ubuntu-desktop" package after server version installation.
* You might have luck by means of uninstalling kernel 5.8 and using the "original" 5.4 kernel. The new kernel is "pulled" via [HWE](https://wiki.ubuntu.com/Kernel/LTSEnablementStack) kernel while original kernel uses normal generic package.

I didn't try it out, but to my best knowledge the procedure changing from HWE to normal kernel is
```sh
# Install 20.04.1 kernel
sudo apt install linux-generic
# Remove HWE kernel (20.04.2)
sudo apt remove ^linux-.*hwe-20.04$
sudo apt remove 5.8.0-..-generic$
```
Please note that executing these steps has the risk that you end up with no bootable kernel. If that happens you probably need to reinstall ubuntu.

---

### 评论 #5 — PierrickMonchoix (2021-01-30T12:28:01Z)

Hi @seesturm !

Thank you so much for responding that quickly.

In fact, I'm in 5.8 kernel:
~$ uname --all
Linux pierrick-Nitro-AN515-52 5.8.0-41-generic #46~20.04.1-Ubuntu SMP Mon Jan 18 17:52:23 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

Indeed, I want to stay in a desktop version. 
Moreover, as I'm new to Linux, I prefer not to downgrade my Ubuntu version ( if possible ).

Someone talk me about Docker in order to use the 20.04.1 Ubuntu version, do you think it is a good idea for using Rocm?

----------

More info about my GPU if you need:
~$ sudo lshw -C display
[sudo] Mot de passe de pierrick : 
  *-display                 
       description: VGA compatible controller
       produit: GP107M [GeForce GTX 1050 Ti Mobile]








---

### 评论 #6 — seesturm (2021-01-30T12:36:30Z)

Hi @PierrickMonchoix 
While the set of AMD GPUs supported by ROCm is already quite small there is zero chance that ROCm will support NVidia GPU.

(Note: This statement is technically not 100% correct since "ROCm/HIP" allows usage of CUDA backend. But I guess you want to use ROCm differently).

---

### 评论 #7 — PierrickMonchoix (2021-01-30T15:05:33Z)

Ok thank your for warning me.

As a student, my purpose is to train on Rocm for an internship in April (they use OpenCL with Rocm as I understand).
But now you told me that, I think I will just use OpenCL with CUDA.

Thank you so much for all @seesturm !

---

### 评论 #8 — xuhuisheng (2021-03-11T06:48:08Z)

You could install linux-5.4 and uninstall linux-5.8 manually. Reboot and re-install rocm-dkms.

Like this:

```
sudo apt install linux-modules-extra-5.4.0-64-generic linux-headers-5.4.0-64-generic

sudo apt remove linux-modules-extra-5.8.0-44-generic linux-headers-5.8.0-44-generic

```

---
