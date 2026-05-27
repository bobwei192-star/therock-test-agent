# Ubuntu 19.10 issue compiling rock-dkms driver

> **Issue #969**
> **状态**: closed
> **创建时间**: 2019-12-17T06:56:10Z
> **更新时间**: 2023-12-14T00:03:32Z
> **关闭时间**: 2023-12-14T00:03:32Z
> **作者**: dfontenot
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/969

## 描述

I'm running into an issue when I install the rocm-dkms driver as specified on [this page](https://rocm.github.io/install.html#using-debian-based-rocm-with-upstream-kernel-drivers). The failure is written out to /var/crash/rock-dkms.0.crash

Here is the contents of the file:

```
ProblemType: Package
DKMSBuildLog:
 DKMS make.log for amdgpu-2.10-14 for kernel 5.3.0-24-generic (x86_64)
 Mon 16 Dec 2019 10:02:09 PM PST
 make: Entering directory '/usr/src/linux-headers-5.3.0-24-generic'
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_drm.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/main.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/symbols.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_fence.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_fence_array.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_kthread.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_io.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/sched_fence.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/sched_main.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_reservation.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_memory.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_tt.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_mn.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_device_cgroup.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_workqueue.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_mm.o
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.c:189:84: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
   189 |  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed", _kcl_pcie_link_speed);
       |                                                                                    ^~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.c:3:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_common.h:22:63: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
    22 | static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
       |                                                         ~~~~~~^~~~~~~
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_perf_event.o
 /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_memory.c:29: warning: "pr_fmt" redefined
    29 | #define pr_fmt(fmt) "[TTM] " fmt
       | 
 In file included from ./include/linux/kernel.h:15,
                  from ./include/linux/list.h:9,
                  from ./include/linux/wait.h:7,
                  from ./include/linux/dma-fence.h:17,
                  from /var/lib/dkms/amdgpu/2.10-14/build/include/kcl/kcl_fence.h:12,
                  from /var/lib/dkms/amdgpu/2.10-14/build/ttm/backport/backport.h:5,
                  from <command-line>:
 ./include/linux/printk.h:288: note: this is the location of the previous definition
   288 | #define pr_fmt(fmt) fmt
       | 
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_drm.c: In function ‘drm_crtc_force_disable_all’:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_drm.c:23:10: error: implicit declaration of function ‘drm_crtc_force_disable’; did you mean ‘drm_crtc_force_disable_all’? [-Werror=implicit-function-declaration]
    23 |    ret = drm_crtc_force_disable(crtc);
       |          ^~~~~~~~~~~~~~~~~~~~~~
       |          drm_crtc_force_disable_all
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo_util.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/sched_entity.o
 cc1: some warnings being treated as errors
 make[2]: *** [scripts/Makefile.build:288: /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_drm.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_kms.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_atombios.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/atombios_crtc.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo_vm.o
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c: In function ‘amdgpu_pmops_runtime_suspend’:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c:1224:2: error: implicit declaration of function ‘drm_kms_helper_poll_disable’ [-Werror=implicit-function-declaration]
  1224 |  drm_kms_helper_poll_disable(drm_dev);
       |  ^~~~~~~~~~~~~~~~~~~~~~~~~~~
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl] Error 2
 make[1]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_module.o
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c: In function ‘amdgpu_pmops_runtime_resume’:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c:1263:2: error: implicit declaration of function ‘drm_kms_helper_poll_enable’ [-Werror=implicit-function-declaration]
  1263 |  drm_kms_helper_poll_enable(drm_dev);
       |  ^~~~~~~~~~~~~~~~~~~~~~~~~~
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_execbuf_util.o
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c: At top level:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c:1432:21: error: ‘DRIVER_IRQ_SHARED’ undeclared here (not in a function)
  1432 |   DRIVER_HAVE_IRQ | DRIVER_IRQ_SHARED | DRIVER_GEM |
       |                     ^~~~~~~~~~~~~~~~~
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c:1449:26: error: initialization of ‘bool (*)(struct drm_device *, unsigned int,  int *, ktime_t *, bool)’ {aka ‘_Bool (*)(struct drm_device *, unsigned int,  int *, long long int *, _Bool)’} from incompatible pointer type ‘int (*)(struct drm_device *, unsigned int,  int *, struct timeval *, unsigned int)’ [-Werror=incompatible-pointer-types]
  1449 |  .get_vblank_timestamp = kcl_amdgpu_get_vblank_timestamp_kms,
       |                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c:1449:26: note: (near initialization for ‘kms_driver.get_vblank_timestamp’)
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c:1450:26: error: initialization of ‘bool (*)(struct drm_device *, unsigned int,  bool,  int *, int *, ktime_t *, ktime_t *, const struct drm_display_mode *)’ {aka ‘_Bool (*)(struct drm_device *, unsigned int,  _Bool,  int *, int *, long long int *, long long int *, const struct drm_display_mode *)’} from incompatible pointer type ‘int (*)(struct drm_device *, unsigned int,  unsigned int,  int *, int *, ktime_t *, ktime_t *, const struct drm_display_mode *)’ {aka ‘int (*)(struct drm_device *, unsigned int,  unsigned int,  int *, int *, long long int *, long long int *, const struct drm_display_mode *)’} [-Werror=incompatible-pointer-types]
  1450 |  .get_scanout_position = kcl_amdgpu_get_crtc_scanout_position,
       |                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.c:1450:26: note: (near initialization for ‘kms_driver.get_scanout_position’)
 cc1: some warnings being treated as errors
 make[2]: *** [scripts/Makefile.build:290: /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_page_alloc.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo_manager.o
   LD [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/amd-sched.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_page_alloc_dma.o
   CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_agp_backend.o
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.c: In function ‘amdgpu_switcheroo_set_state’:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.c:1063:3: error: implicit declaration of function ‘drm_kms_helper_poll_enable’ [-Werror=implicit-function-declaration]
  1063 |   drm_kms_helper_poll_enable(dev);
       |   ^~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.c:1066:3: error: implicit declaration of function ‘drm_kms_helper_poll_disable’ [-Werror=implicit-function-declaration]
  1066 |   drm_kms_helper_poll_disable(dev);
       |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.c: In function ‘amdgpu_device_resume’:
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.c:3202:3: error: implicit declaration of function ‘drm_helper_hpd_irq_event’; did you mean ‘drm_fb_helper_hotplug_event’? [-Werror=implicit-function-declaration]
  3202 |   drm_helper_hpd_irq_event(dev);
       |   ^~~~~~~~~~~~~~~~~~~~~~~~
       |   drm_fb_helper_hotplug_event
 /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.c:3204:3: error: implicit declaration of function ‘drm_kms_helper_hotplug_event’; did you mean ‘drm_fb_helper_hotplug_event’? [-Werror=implicit-function-declaration]
  3204 |   drm_kms_helper_hotplug_event(dev);
       |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
       |   drm_fb_helper_hotplug_event
 /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_agp_backend.c:33: warning: "pr_fmt" redefined
    33 | #define pr_fmt(fmt) "[TTM] " fmt
       | 
 In file included from ./include/linux/kernel.h:15,
                  from ./include/linux/list.h:9,
                  from ./include/linux/wait.h:7,
                  from ./include/linux/dma-fence.h:17,
                  from /var/lib/dkms/amdgpu/2.10-14/build/include/kcl/kcl_fence.h:12,
                  from /var/lib/dkms/amdgpu/2.10-14/build/ttm/backport/backport.h:5,
                  from <command-line>:
 ./include/linux/printk.h:288: note: this is the location of the previous definition
   288 | #define pr_fmt(fmt) fmt
       | 
   LD [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/amdttm.o
 cc1: some warnings being treated as errors
 make[2]: *** [scripts/Makefile.build:288: /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.o] Error 1
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu] Error 2
 make: *** [Makefile:1655: _module_/var/lib/dkms/amdgpu/2.10-14/build] Error 2
 make: Leaving directory '/usr/src/linux-headers-5.3.0-24-generic'
DKMSKernelVersion: 5.3.0-24-generic
Date: Mon Dec 16 22:02:12 2019
DuplicateSignature: dkms:rock-dkms:2.10-14:/var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_drm.c:23:10: error: implicit declaration of function ‘drm_crtc_force_disable’; did you mean ‘drm_crtc_force_disable_all’? [-Werror=implicit-function-declaration]
Package: rock-dkms 2.10-14
PackageVersion: 2.10-14
SourcePackage: rock-dkms
Title: rock-dkms 2.10-14: amdgpu kernel module failed to build
```
Would appreciate any help in working through this driver installation issue.

---

## 评论 (10 条)

### 评论 #1 — pqyptixa (2019-12-26T01:47:38Z)

I get a similar error log, though not exactly the same, when trying to install rocm-dkms 3.0 in Ubuntu 18.04:

```
Configurando rock-dkms (3.0-6) ...
Loading new amdgpu-3.0-6 DKMS files...
Building for 5.3.0-24-generic
Building for architecture x86_64
Building initial module for 5.3.0-24-generic
Error! Bad return status for module build on kernel: 5.3.0-24-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.0-6/build/make.log for more information.
```
make.log contains this:
```
DKMS make.log for amdgpu-3.0-6 for kernel 5.3.0-24-generic (x86_64)
mié dic 25 22:39:44 -03 2019
make: se entra en el directorio '/usr/src/linux-headers-5.3.0-24-generic'
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_drm_cache.o
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_fence.c:29:1: warning: ‘dma_fence_test_signaled_any’ defined but not used [-Wunused-function]
   29 | dma_fence_test_signaled_any(struct dma_fence **fences, uint32_t count,
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_reservation.o
In file included from /var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../include/../backport/backport.h:7,
                 from <command-line>:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../backport/include/kcl/kcl_amdgpu.h: In function ‘kcl_amdgpu_get_vblank_timestamp_kms’:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../backport/include/kcl/kcl_amdgpu.h:99:9: error: implicit declaration of function ‘amdgpu_get_vblank_timestamp_kms’; did you mean ‘kcl_amdgpu_get_vblank_timestamp_kms’? [-Werror=implicit-function-declaration]
   99 |  return amdgpu_get_vblank_timestamp_kms(dev, pipe, max_error, vblank_time, flags);
      |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |         kcl_amdgpu_get_vblank_timestamp_kms
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.c: At top level:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.c:1471:26: error: initialization of ‘bool (*)(struct drm_device *, unsigned int,  int *, ktime_t *, bool)’ {aka ‘_Bool (*)(struct drm_device *, unsigned int,  int *, long long int *, _Bool)’} from incompatible pointer type ‘int (*)(struct drm_device *, unsigned int,  int *, struct timeval *, unsigned int)’ [-Werror=incompatible-pointer-types]
 1471 |  .get_vblank_timestamp = kcl_amdgpu_get_vblank_timestamp_kms,
      |                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.c:1471:26: note: (near initialization for ‘kms_driver.get_vblank_timestamp’)
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.c:1472:26: error: initialization of ‘bool (*)(struct drm_device *, unsigned int,  bool,  int *, int *, ktime_t *, ktime_t *, const struct drm_display_mode *)’ {aka ‘_Bool (*)(struct drm_device *, unsigned int,  _Bool,  int *, int *, long long int *, long long int *, const struct drm_display_mode *)’} from incompatible pointer type ‘int (*)(struct drm_device *, unsigned int,  unsigned int,  int *, int *, ktime_t *, ktime_t *, const struct drm_display_mode *)’ {aka ‘int (*)(struct drm_device *, unsigned int,  unsigned int,  int *, int *, long long int *, long long int *, const struct drm_display_mode *)’} [-Werror=incompatible-pointer-types]
 1472 |  .get_scanout_position = kcl_amdgpu_get_crtc_scanout_position,
      |                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.c:1472:26: note: (near initialization for ‘kms_driver.get_scanout_position’)
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/scheduler/sched_entity.o
cc1: some warnings being treated as errors
scripts/Makefile.build:288: recipe for target '/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_drv.o] Error 1
make[2]: *** Se espera a que terminen otras tareas....
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_pci.o
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_reservation.c: In function ‘amdkcl_reservation_init’:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_reservation.c:58:10: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-array-qualifiers]
   58 |          &_kcl_reservation_seqcount_string_stub);
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_reservation.c:32:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_common.h:23:63: note: expected ‘void *’ but argument is of type ‘const char (*)[21]’
   23 | static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
      |                                                         ~~~~~~^~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_suspend.o
In file included from /var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../include/../backport/backport.h:7,
                 from <command-line>:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../backport/include/kcl/kcl_amdgpu.h: In function ‘kcl_amdgpu_get_vblank_timestamp_kms’:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../backport/include/kcl/kcl_amdgpu.h:99:9: error: implicit declaration of function ‘amdgpu_get_vblank_timestamp_kms’; did you mean ‘kcl_amdgpu_get_vblank_timestamp_kms’? [-Werror=implicit-function-declaration]
   99 |  return amdgpu_get_vblank_timestamp_kms(dev, pipe, max_error, vblank_time, flags);
      |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |         kcl_amdgpu_get_vblank_timestamp_kms
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_perf_event.o
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_pci.c:189:84: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  189 |  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed", _kcl_pcie_link_speed_stub);
      |                                                                                    ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_pci.c:3:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_common.h:23:63: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
   23 | static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
      |                                                         ~~~~~~^~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_bo_vm.o
In file included from /var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../include/../backport/backport.h:7,
                 from <command-line>:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../backport/include/kcl/kcl_amdgpu.h: In function ‘kcl_amdgpu_get_vblank_timestamp_kms’:
/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/../backport/include/kcl/kcl_amdgpu.h:99:9: error: implicit declaration of function ‘amdgpu_get_vblank_timestamp_kms’; did you mean ‘kcl_amdgpu_get_vblank_timestamp_kms’? [-Werror=implicit-function-declaration]
   99 |  return amdgpu_get_vblank_timestamp_kms(dev, pipe, max_error, vblank_time, flags);
      |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |         kcl_amdgpu_get_vblank_timestamp_kms
  LD [M]  /var/lib/dkms/amdgpu/3.0-6/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_page_alloc.o
/var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_bo.o: warning: objtool: ttm_bo_del_from_lru()+0xe3: unreachable instruction
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_page_alloc_dma.o
cc1: some warnings being treated as errors
scripts/Makefile.build:288: recipe for target '/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_kms.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_kms.o] Error 1
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/reservation.o
cc1: some warnings being treated as errors
scripts/Makefile.build:288: recipe for target '/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_device.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu/amdgpu_device.o] Error 1
scripts/Makefile.build:519: recipe for target '/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/3.0-6/build/amd/amdgpu] Error 2
make[1]: *** Se espera a que terminen otras tareas....
  LD [M]  /var/lib/dkms/amdgpu/3.0-6/build/amd/amdkcl/amdkcl.o
  LD [M]  /var/lib/dkms/amdgpu/3.0-6/build/ttm/amdttm.o
Makefile:1655: recipe for target '_module_/var/lib/dkms/amdgpu/3.0-6/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/3.0-6/build] Error 2
make: se sale del directorio '/usr/src/linux-headers-5.3.0-24-generic'
```

---

### 评论 #2 — pqyptixa (2019-12-26T13:41:17Z)

Well, according to [some random comment I found somewhere else](https://fosstodon.org/@dctrud/103315274791608145), apparently I don't need rocm-dkms to be able to use OpenCL programs, only the rocm-dev package. However, now I hit another bug...

---

### 评论 #3 — dfontenot (2019-12-26T19:25:20Z)

Yeah, I saw the mention about just installing rocm-dev on the [rocm github page](https://rocm.github.io/install.html#ubuntu-support---installing-from-a-debian-repository) (section  "Using Debian-based ROCm with upstream kernel drivers")

However, in the previous section ("Installing development packages for cross compilation") there's a not that says: "To execute ROCm enabled apps you will require a system with the full ROCm driver stack installed", which I assume means having the rocm-dkms package installed. I'm not sure what exactly is a ROCm enabled app. Would anyone be able to provide some clarity on that note?

---

### 评论 #4 — Artem-B (2020-02-20T23:54:16Z)

@pqyptixa https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/pull/87 should help with the build errors you've reported above.

---

### 评论 #5 — BloodyIron (2020-02-22T16:08:09Z)

@Artem-B any idea when that will make it to the PPA?

Or rather, how those using the PPA can leverage that adjustment you made?

---

### 评论 #6 — Artem-B (2020-02-22T16:32:47Z)

For myself, I've fixed it directly in the sources installed by the package, but that's not a good option for most people.
As for when it will make it into the package repo -- I don't know. Hopefully soon.

---

### 评论 #7 — BloodyIron (2020-02-22T16:56:08Z)

Ubuntu 19.10

So I purged all rock and rocm packages, then disabled the main repo, and enabled the 2.10 rocm repo. Installed rocm-dkms and it failed part way through. But now clinfo actually shows device info.

However, the program I care about for openCL here, DaVinci Resolve, keeps getting "stuck" at "Loading Waveform Monitor". And I'm not sure if it will ever finish laoding.

I've rebooted, and same effect.

I'm going to try this again with 2.9, as I think I got further with that previously on 19.10, but I am not 100% sure. Either way, 3.0 is completely non-functional for me, despite being on a supported kernel (5.3).

Really would be great to have at least minimal operational ability in the 6 Month Ubuntu releases, instead of having to stay ONLY on the 2yr LTS releases. There's many many improvements to gaming, and other things, in each 6 Month release cycle, which is why I'm not on 18.04 today.

I can understand that the LTS versions of Ubuntu should experience the best stability, but I'm okay with a "beta" or "unsupported, but works" version of rocm for the 6 Month release versions of Ubuntu. Just so I can actually use openCL with AMDGPU instead of needing AMDGPU-PRO.

Gaming is a real thing on Linux, it is growing, and these release cycles need to act like it.

---

### 评论 #8 — BloodyIron (2020-02-22T17:05:39Z)

So I purged all rock and rocm packages from 2.10, switched to 2.9 repo, and installed the package "rocm-opencl" and now DaVinci Resolve is actually launching! I appear to have a working openCL setup now (time will tell if this is true).

FYI,

* Ubuntu 19.10
* AMD RX580
* 5.3.0-40-generic #32-Ubuntu SMP Fri Jan 31

If you're unfamiliar with how to enable the earliier repos, this is the active line of my relevant aptitude list file:

deb [arch=amd64] http://repo.radeon.com/rocm/apt/2.9.0/ xenial main

---

### 评论 #9 — keryell (2022-04-05T20:57:57Z)

I guess this can be closed since this OS is no longer supported for 2 years now.

---

### 评论 #10 — nartmada (2023-12-13T23:06:09Z)

Hi @dfontenot, please close the ticket if this is no longer an issue.  Thanks.

---
