# Building kernel module error after nvidia driver has been installed

> **Issue #756**
> **状态**: closed
> **创建时间**: 2019-04-05T06:09:01Z
> **更新时间**: 2019-04-05T15:59:48Z
> **关闭时间**: 2019-04-05T15:59:48Z
> **作者**: vvsteg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/756

## 描述

Previously ROCm 2.2 has been installed successfully on my system with Ubuntu 18.04 (4.18.0-15-generic). Now I have made an attempt to add an Nvidia GPU to the system. 

Trying to follow #626, I have uninstalled rocm-dkms and installed the nvidia driver.

Now I am trying to reinstall rocm-dkms back but I am getting the following error:

```
Building initial module for 4.18.0-15-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms.0.crash'
Error! Bad return status for module build on kernel: 4.18.0-15-generic (x86_64)
Consult /var/lib/dkms/amdgpu/2.2-31/build/make.log for more information.
```

And ```/var/lib/dkms/amdgpu/2.2-31/build/make.log``` contains the following

```
make: Entering directory '/usr/src/linux-headers-4.18.0-15-generic'
Makefile:970: "Cannot use CONFIG_STACK_VALIDATION=y, please install libelf-dev, libelf-devel or elfutils-libelf-devel"
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/lib/chash.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_device.o
/var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_fence.c:84:1: warning: ‘_kcl_fence_default_wait’ defined but not used [-Wunused-function]
 _kcl_fence_default_wait(struct fence *fence, bool intr, signed long timeout)
 ^~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_memory.c:29:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.2-31/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.2-31/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:292:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  LD [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/lib/amdchash.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_object.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_lock.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_connectors.o
  LD [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_bo_manager.o
/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_device.c: In function ‘amdgpu_device_get_min_pci_speed_width’:
/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_device.c:3653:15: error: implicit declaration of function ‘pcie_get_speed_cap’; did you mean ‘kcl_pcie_get_speed_cap’? [-Werror=implicit-function-declaration]
   cur_speed = pcie_get_speed_cap(pdev);
               ^~~~~~~~~~~~~~~~~~
               kcl_pcie_get_speed_cap
/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_device.c:3654:15: error: implicit declaration of function ‘pcie_get_width_cap’; did you mean ‘kcl_pcie_get_width_cap’? [-Werror=implicit-function-declaration]
   cur_width = pcie_get_width_cap(pdev);
               ^~~~~~~~~~~~~~~~~~
               kcl_pcie_get_width_cap
  LD [M]  /var/lib/dkms/amdgpu/2.2-31/build/scheduler/amd-sched.o
/var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_object.c:60:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.2-31/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.2-31/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:292:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_cs.o
/var/lib/dkms/amdgpu/2.2-31/build/ttm/ttm_agp_backend.c:33:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.2-31/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.2-31/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:292:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_ttm.c:2383:12: warning: ‘ttm_pl_tt’ defined but not used [-Wunused-variable]
 static int ttm_pl_tt = TTM_PL_TT;
            ^~~~~~~~~
/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_ttm.c:2382:12: warning: ‘ttm_pl_vram’ defined but not used [-Wunused-variable]
 static int ttm_pl_vram = TTM_PL_VRAM;
            ^~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_bios.o
cc1: some warnings being treated as errors
scripts/Makefile.build:325: recipe for target '/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_device.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_device.o] Error 1
make[2]: *** Waiting for unfinished jobs....
  CC [M]  /var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu/amdgpu_benchmark.o
  LD [M]  /var/lib/dkms/amdgpu/2.2-31/build/ttm/amdttm.o
scripts/Makefile.build:581: recipe for target '/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/2.2-31/build/amd/amdgpu] Error 2
Makefile:1534: recipe for target '_module_/var/lib/dkms/amdgpu/2.2-31/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/2.2-31/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.18.0-15-generic'
```

I would really appreciate any hints or suggestions how to proceed...



---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2019-04-05T13:23:42Z)

It appears that, along the way or simultaneous to adding your other GPU, you updated your kernel to 4.18. ROCm 2.2 is not supported on kernel 4.18. See #731 

---

### 评论 #2 — vvsteg (2019-04-05T15:59:43Z)

Thank you! It was my inaccuracy. Now both cards work.

---
