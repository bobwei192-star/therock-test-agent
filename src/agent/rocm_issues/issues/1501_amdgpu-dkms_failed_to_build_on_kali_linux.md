# amdgpu-dkms failed to build on kali linux

> **Issue #1501**
> **状态**: closed
> **创建时间**: 2021-06-23T14:16:18Z
> **更新时间**: 2021-06-24T04:26:14Z
> **关闭时间**: 2021-06-24T04:26:14Z
> **作者**: TxMat
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1501

## 描述

Hello,
I tried to install the ROCm on my system recently but it appears that the installer is constantly failing the build.
I tried to find solutions online but i seems nobody had this issue on Kali.

the fix often proposed for Ubuntu is to downgrade with

`sudo apt-get install linux-image-5.4.0-42-generic linux-modules-5.4.0-42-generic linux-modules-extra-5.4.0-42-generic linux-headers-5.4.0-42-generic
`

but this is'nt available on Kali.

At first i thought the GCC version was an issue (in the log there is a waring) but nobody seems to have that issue as well so i'm just lost and i came here to find some help.

here is the apt trace

```
------------------------------
Deleting module version: 5.9.20.104-1247438
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-5.9.20.104-1247438 DKMS files...
Building for 5.10.0-kali8-amd64
Building for architecture amd64
Building initial module for 5.10.0-kali8-amd64
Error! Bad return status for module build on kernel: 5.10.0-kali8-amd64 (amd64)
Consult /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/make.log for more information.
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

and here is the log file

```
DKMS make.log for amdgpu-5.9.20.104-1247438 for kernel 5.10.0-kali8-amd64 (amd64)
mer. 23 juin 2021 16:03:56 CEST
make : on entre dans le répertoire « /usr/src/linux-headers-5.10.0-kali8-amd64 »
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/Makefile:26: "Local GCC version 100202 does not match kernel compiler GCC version 100201"
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/Makefile:27: "This may cause unexpected and hard-to-isolate compiler-related issues"
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_common.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/dma-buf/dma-resv.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_backlight.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_ioctl.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_range_manager.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_perf_event.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_resource.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_seq_file.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_suspend.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_memory.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_sched.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_reservation.o
  LD [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_cache.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_auth.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_fb.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_fbmem.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_print.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_fence.o
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_fence.c:30:1: warning: ‘dma_fence_test_signaled_any’ defined but not used [-Wunused-function]
   30 | dma_fence_test_signaled_any(struct dma_fence **fences, uint32_t count,
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_connector.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_atomic_helper.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_modes.o
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c: In function ‘amdgpu_connector_update_scratch_regs’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c:235:6: warning: unused variable ‘i’ [-Wunused-variable]
  235 |  int i;
      |      ^
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c: In function ‘amdgpu_connector_find_encoder’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c:258:6: warning: unused variable ‘i’ [-Wunused-variable]
  258 |  int i;
      |      ^
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c: In function ‘amdgpu_connector_best_single_encoder’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c:373:6: warning: unused variable ‘i’ [-Wunused-variable]
  373 |  int i;
      |      ^
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_time.o
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c: In function ‘amdgpu_connector_dvi_detect’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c:1121:7: warning: unused variable ‘i’ [-Wunused-variable]
 1121 |   int i;
      |       ^
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c: In function ‘amdgpu_connector_dvi_encoder’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c:1177:6: warning: unused variable ‘i’ [-Wunused-variable]
 1177 |  int i;
      |      ^
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c: In function ‘amdgpu_connector_encoder_get_dp_bridge_encoder_id’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c:1341:6: warning: unused variable ‘i’ [-Wunused-variable]
 1341 |  int i;
      |      ^
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c: In function ‘amdgpu_connector_encoder_is_hbr2’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_connectors.c:1366:6: warning: unused variable ‘i’ [-Wunused-variable]
 1366 |  int i;
      |      ^
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_ftrace.o
  LD [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/ttm/amdttm.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_acpi_table.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/kcl_drm_hdcp.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_cs.o
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c: In function ‘amdgpu_ssg_init’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c:2498:18: error: ‘struct dev_pagemap’ has no member named ‘res’; did you mean ‘ref’?
 2498 |  adev->ssg.pgmap.res.start = res.start;
      |                  ^~~
      |                  ref
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c:2499:18: error: ‘struct dev_pagemap’ has no member named ‘res’; did you mean ‘ref’?
 2499 |  adev->ssg.pgmap.res.end = res.end;
      |                  ^~~
      |                  ref
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c:2500:18: error: ‘struct dev_pagemap’ has no member named ‘res’; did you mean ‘ref’?
 2500 |  adev->ssg.pgmap.res.name = res.name;
      |                  ^~~
      |                  ref
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c: In function ‘amdgpu_ttm_debugfs_init’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c:3265:6: warning: unused variable ‘r’ [-Wunused-variable]
 3265 |  int r;
      |      ^
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c: In function ‘amdgpu_ttm_domain_start’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c:844:6: warning: this statement may fall through [-Wimplicit-fallthrough=]
  844 |   if (adev->direct_gma.dgma_bo)
      |      ^
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.c:846:2: note: here
  846 |  case AMDGPU_PL_DGMA_IMPORT:
      |  ^~~~
make[3]: *** [/usr/src/linux-headers-5.10.0-kali8-common/scripts/Makefile.build:284 : /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_ttm.o] Erreur 1
make[3]: *** Attente des tâches non terminées....
  LD [M]  /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdkcl/amdkcl.o
In file included from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/backport/backport.h:6,
                 from <command-line>:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.c: In function ‘amdgpu_display_get_fb_info’:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.c:995:44: warning: passing argument 1 of ‘drm_gem_fb_get_obj’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  995 |  rbo = gem_to_amdgpu_bo(drm_gem_fb_get_obj(&amdgpu_fb->base, 0));
      |                                            ^~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/kernel.h:852:26: note: in definition of macro ‘container_of’
  852 |  void *__mptr = (void *)(ptr);     \
      |                          ^~~
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.c:995:8: note: in expansion of macro ‘gem_to_amdgpu_bo’
  995 |  rbo = gem_to_amdgpu_bo(drm_gem_fb_get_obj(&amdgpu_fb->base, 0));
      |        ^~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/include/kcl/header/drm/drm_gem_framebuffer_helper.h:6,
                 from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/backport/include/kcl/kcl_amdgpu_drm_gem_framebuffer_helper.h:4,
                 from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/backport/backport.h:71,
                 from <command-line>:
/usr/src/linux-headers-5.10.0-kali8-common/include/drm/drm_gem_framebuffer_helper.h:18:67: note: expected ‘struct drm_framebuffer *’ but argument is of type ‘const struct drm_framebuffer *’
   18 | struct drm_gem_object *drm_gem_fb_get_obj(struct drm_framebuffer *fb,
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~
In file included from <command-line>:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.c:995:44: warning: passing argument 1 of ‘drm_gem_fb_get_obj’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  995 |  rbo = gem_to_amdgpu_bo(drm_gem_fb_get_obj(&amdgpu_fb->base, 0));
      |                                            ^~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/compiler_types.h:295:9: note: in definition of macro ‘__compiletime_assert’
  295 |   if (!(condition))     \
      |         ^~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/compiler_types.h:315:2: note: in expansion of macro ‘_compiletime_assert’
  315 |  _compiletime_assert(condition, msg, __compiletime_assert_, __COUNTER__)
      |  ^~~~~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/build_bug.h:39:37: note: in expansion of macro ‘compiletime_assert’
   39 | #define BUILD_BUG_ON_MSG(cond, msg) compiletime_assert(!(cond), msg)
      |                                     ^~~~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/kernel.h:853:2: note: in expansion of macro ‘BUILD_BUG_ON_MSG’
  853 |  BUILD_BUG_ON_MSG(!__same_type(*(ptr), ((type *)0)->member) && \
      |  ^~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/kernel.h:853:20: note: in expansion of macro ‘__same_type’
  853 |  BUILD_BUG_ON_MSG(!__same_type(*(ptr), ((type *)0)->member) && \
      |                    ^~~~~~~~~~~
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_gem.h:34:32: note: in expansion of macro ‘container_of’
   34 | #define gem_to_amdgpu_bo(gobj) container_of((gobj), struct amdgpu_bo, tbo.base)
      |                                ^~~~~~~~~~~~
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.c:995:8: note: in expansion of macro ‘gem_to_amdgpu_bo’
  995 |  rbo = gem_to_amdgpu_bo(drm_gem_fb_get_obj(&amdgpu_fb->base, 0));
      |        ^~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/include/kcl/header/drm/drm_gem_framebuffer_helper.h:6,
                 from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/backport/include/kcl/kcl_amdgpu_drm_gem_framebuffer_helper.h:4,
                 from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/backport/backport.h:71,
                 from <command-line>:
/usr/src/linux-headers-5.10.0-kali8-common/include/drm/drm_gem_framebuffer_helper.h:18:67: note: expected ‘struct drm_framebuffer *’ but argument is of type ‘const struct drm_framebuffer *’
   18 | struct drm_gem_object *drm_gem_fb_get_obj(struct drm_framebuffer *fb,
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~
In file included from <command-line>:
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.c:995:44: warning: passing argument 1 of ‘drm_gem_fb_get_obj’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  995 |  rbo = gem_to_amdgpu_bo(drm_gem_fb_get_obj(&amdgpu_fb->base, 0));
      |                                            ^~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/compiler_types.h:295:9: note: in definition of macro ‘__compiletime_assert’
  295 |   if (!(condition))     \
      |         ^~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/compiler_types.h:315:2: note: in expansion of macro ‘_compiletime_assert’
  315 |  _compiletime_assert(condition, msg, __compiletime_assert_, __COUNTER__)
      |  ^~~~~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/build_bug.h:39:37: note: in expansion of macro ‘compiletime_assert’
   39 | #define BUILD_BUG_ON_MSG(cond, msg) compiletime_assert(!(cond), msg)
      |                                     ^~~~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/kernel.h:853:2: note: in expansion of macro ‘BUILD_BUG_ON_MSG’
  853 |  BUILD_BUG_ON_MSG(!__same_type(*(ptr), ((type *)0)->member) && \
      |  ^~~~~~~~~~~~~~~~
/usr/src/linux-headers-5.10.0-kali8-common/include/linux/kernel.h:854:6: note: in expansion of macro ‘__same_type’
  854 |     !__same_type(*(ptr), void),   \
      |      ^~~~~~~~~~~
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_gem.h:34:32: note: in expansion of macro ‘container_of’
   34 | #define gem_to_amdgpu_bo(gobj) container_of((gobj), struct amdgpu_bo, tbo.base)
      |                                ^~~~~~~~~~~~
/var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu/amdgpu_display.c:995:8: note: in expansion of macro ‘gem_to_amdgpu_bo’
  995 |  rbo = gem_to_amdgpu_bo(drm_gem_fb_get_obj(&amdgpu_fb->base, 0));
      |        ^~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/include/kcl/header/drm/drm_gem_framebuffer_helper.h:6,
                 from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/backport/include/kcl/kcl_amdgpu_drm_gem_framebuffer_helper.h:4,
                 from /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/backport/backport.h:71,
                 from <command-line>:
/usr/src/linux-headers-5.10.0-kali8-common/include/drm/drm_gem_framebuffer_helper.h:18:67: note: expected ‘struct drm_framebuffer *’ but argument is of type ‘const struct drm_framebuffer *’
   18 | struct drm_gem_object *drm_gem_fb_get_obj(struct drm_framebuffer *fb,
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~
make[2]: *** [/usr/src/linux-headers-5.10.0-kali8-common/scripts/Makefile.build:501 : /var/lib/dkms/amdgpu/5.9.20.104-1247438/build/amd/amdgpu] Erreur 2
make[1]: *** [/usr/src/linux-headers-5.10.0-kali8-common/Makefile:1845 : /var/lib/dkms/amdgpu/5.9.20.104-1247438/build] Erreur 2
make: *** [/usr/src/linux-headers-5.10.0-kali8-common/Makefile:185 : __sub-make] Erreur 2
make : on quitte le répertoire « /usr/src/linux-headers-5.10.0-kali8-amd64 »
```

Have a nice day.
TXMat


---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-06-24T04:26:14Z)

Thanks @TxMat for reaching out.
We do not support Kali linux officially and so can not comment.
Thank you.

---
