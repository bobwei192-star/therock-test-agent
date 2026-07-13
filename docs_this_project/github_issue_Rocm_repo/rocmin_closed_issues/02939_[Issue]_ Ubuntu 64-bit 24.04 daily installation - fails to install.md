# [Issue]: Ubuntu 64-bit 24.04 daily installation - fails to install

- **Issue #:** 2939
- **State:** closed
- **Created:** 2024-03-03T16:36:41Z
- **Updated:** 2024-08-28T18:27:29Z
- **Labels:** Feature Request, Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/2939

### Problem Description

sudo apt install amdgpu-dkms
```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
amdgpu-dkms is already the newest version (1:6.3.6.60002-1718217.22.04).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
Setting up amdgpu-dkms (1:6.3.6.60002-1718217.22.04) ...
Removing old amdgpu-6.3.6-1718217.22.04 DKMS files...
Deleting module amdgpu-6.3.6-1718217.22.04 completely from the DKMS tree.
Loading new amdgpu-6.3.6-1718217.22.04 DKMS files...
Building for 6.8.0-11-generic
Building for architecture x86_64
Building initial module for 6.8.0-11-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms.0.crash'
Error! Bad return status for module build on kernel: 6.8.0-11-generic (x86_64)
Consult /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

cat /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/make.log
```
DKMS make.log for amdgpu-6.3.6-1718217.22.04 for kernel 6.8.0-11-generic (x86_64)
Sun Mar  3 04:17:26 PM GMT 2024
make: Entering directory '/usr/src/linux-headers-6.8.0-11-generic'
warning: the compiler differs from the one used to build the kernel
  The kernel was built by: x86_64-linux-gnu-gcc-13 (Ubuntu 13.2.0-13ubuntu1) 13.2.0
  You are using:           gcc-13 (Ubuntu 13.2.0-16ubuntu1) 13.2.0
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdxcp/amdgpu_xcp_drv.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdxcp/./backport/kcl_drm_drv.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/drm_gem_ttm_helper.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_common.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/drm_buddy.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/main.c:16:12: warning: no previous prototype for ‘amdkcl_init’ [-Wmissing-prototypes]
   16 | int __init amdkcl_init(void)
      |            ^~~~~~~~~~~
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/main.c:33:13: warning: no previous prototype for ‘amdkcl_exit’ [-Wmissing-prototypes]
   33 | void __exit amdkcl_exit(void)
      |             ^~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_kernel_params.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_range_manager.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_common.c:30:6: warning: no previous prototype for ‘amdkcl_symbol_init’ [-Wmissing-prototypes]
   30 | void amdkcl_symbol_init(void)
      |      ^~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/dma-buf/dma-resv.o
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo.c:37:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h: At top level:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo_vm.c:37:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h: At top level:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_execbuf_util.c:30:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h: At top level:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
cc1: some warnings being treated as errors
cc1: some warnings being treated as errors
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/drm_gem_ttm_helper.h:10,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/drm_gem_ttm_helper.c:5:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h: At top level:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo_util.c:34:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h: At top level:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_tt.c:45:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h: At top level:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
cc1: some warnings being treated as errors
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo_vm.o] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo.o] Error 1
cc1: some warnings being treated as errors
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_backlight.o
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_module.o] Error 1
cc1: some warnings being treated as errors
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_execbuf_util.o] Error 1
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_doorbell_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_ioctl.o
make[2]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/drm_gem_ttm_helper.o] Error 1
make[2]: *** Waiting for unfinished jobs....
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_kthread.o
cc1: some warnings being treated as errors
cc1: some warnings being treated as errors
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_tt.o] Error 1
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_bo_util.o] Error 1
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_io.o
  LD [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdxcp/amdxcp.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_seq_file.o
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:54,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/include/kcl/kcl_amdgpu_drm_fb_helper.h:37,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/backport.h:69,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/atombios_crtc.o
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/backport/backport.h:20,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h: In function ‘kcl_register_shrinker’:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/kcl/kcl_shrinker.h:16:16: error: implicit declaration of function ‘register_shrinker’; did you mean ‘kcl_register_shrinker’? [-Werror=implicit-function-declaration]
   16 |         return register_shrinker(shrinker);
      |                ^~~~~~~~~~~~~~~~~
      |                kcl_register_shrinker
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_suspend.o
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_range_manager.c:32:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h: At top level:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_io.c:69:6: warning: no previous prototype for ‘amdkcl_io_init’ [-Wmissing-prototypes]
   69 | void amdkcl_io_init(void)
      |      ^~~~~~~~~~~~~~
cc1: some warnings being treated as errors
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:60:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.c:2903:66: error: ‘DRM_UNLOCKED’ undeclared here (not in a function); did you mean ‘VM_LOCKED’?
 2903 |         DRM_IOCTL_DEF_DRV(AMDGPU_SEM, amdgpu_sem_ioctl, DRM_AUTH|DRM_UNLOCKED|DRM_RENDER_ALLOW)
      |                                                                  ^~~~~~~~~~~~
./include/drm/drm_ioctl.h:155:26: note: in definition of macro ‘DRM_IOCTL_DEF_DRV’
  155 |                 .flags = _flags,                                        \
      |                          ^~~~~~
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm/ttm_range_manager.o] Error 1
make[2]: *** [scripts/Makefile.build:481: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/ttm] Error 2
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.c:2979:10: error: ‘struct drm_driver’ has no member named ‘gem_prime_mmap’; did you mean ‘gem_prime_import’?
 2979 |         .gem_prime_mmap = amdkcl_drm_gem_prime_mmap,
      |          ^~~~~~~~~~~~~~
      |          gem_prime_import
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.c:2979:27: error: initialization of ‘struct drm_gem_object * (*)(struct drm_device *, struct dma_buf_attachment *, struct sg_table *)’ from incompatible pointer type ‘int (*)(struct drm_gem_object *, struct vm_area_struct *)’ [-Werror=incompatible-pointer-types]
 2979 |         .gem_prime_mmap = amdkcl_drm_gem_prime_mmap,
      |                           ^~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.c:2979:27: note: (near initialization for ‘amdgpu_kms_driver.gem_prime_import_sg_table’)
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.c:3009:10: error: ‘const struct drm_driver’ has no member named ‘gem_prime_mmap’; did you mean ‘gem_prime_import’?
 3009 |         .gem_prime_mmap = drm_gem_prime_mmap,
      |          ^~~~~~~~~~~~~~
      |          gem_prime_import
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.c:3009:27: error: initialization of ‘struct drm_gem_object * (*)(struct drm_device *, struct dma_buf_attachment *, struct sg_table *)’ from incompatible pointer type ‘int (*)(struct drm_gem_object *, struct vm_area_struct *)’ [-Werror=incompatible-pointer-types]
 3009 |         .gem_prime_mmap = drm_gem_prime_mmap,
      |                           ^~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.c:3009:27: note: (near initialization for ‘amdgpu_partition_driver.gem_prime_import_sg_table’)
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_connectors.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_suspend.c:32:6: warning: no previous prototype for ‘amdkcl_suspend_init’ [-Wmissing-prototypes]
   32 | void amdkcl_suspend_init(void)
      |      ^~~~~~~~~~~~~~~~~~~
cc1: some warnings being treated as errors
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_mm.o
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_drv.o] Error 1
make[3]: *** Waiting for unfinished jobs....
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_memory.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_sched.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_cache.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_sched.c:24:6: warning: no previous prototype for ‘amdkcl_sched_init’ [-Wmissing-prototypes]
   24 | void amdkcl_sched_init(void)
      |      ^~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_fb.o
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:54,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/include/kcl/kcl_amdgpu_drm_fb_helper.h:37,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/backport.h:69,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:54,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/include/kcl/kcl_amdgpu_drm_fb_helper.h:37,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/backport.h:69,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:54,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/include/kcl/kcl_amdgpu_drm_fb_helper.h:37,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/backport.h:69,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_doorbell_mgr.o] Error 1
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_print.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_crtc.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_mm.c:39:6: warning: no previous prototype for ‘amdkcl_mm_init’ [-Wmissing-prototypes]
   39 | void amdkcl_mm_init(void)
      |      ^~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_reservation.c:37:6: warning: no previous prototype for ‘amdkcl_reservation_init’ [-Wmissing-prototypes]
   37 | void amdkcl_reservation_init(void)
      |      ^~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_connector.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_atomic_helper.o
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_kms.o] Error 1
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:54,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/include/kcl/kcl_amdgpu_drm_fb_helper.h:37,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/backport.h:69,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_mn.o
  LD [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_modes.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_fence.c:239:6: warning: no previous prototype for ‘amdkcl_fence_init’ [-Wmissing-prototypes]
  239 | void amdkcl_fence_init(void)
      |      ^~~~~~~~~~~~~~~~~
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_device.o] Error 1
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_time.o
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_atombios.o] Error 1
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_acpi_table.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_page_alloc.o
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:54,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/include/kcl/kcl_amdgpu_drm_fb_helper.h:37,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/backport.h:69,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_numa.o
In file included from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_device.h:31,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_bo.h:40,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu.h:54,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/include/kcl/kcl_amdgpu_drm_fb_helper.h:37,
                 from /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/backport/backport.h:69,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/include/drm/ttm/ttm_pool.h:77:45: error: ‘MAX_ORDER’ undeclared here (not in a function); did you mean ‘PMD_ORDER’?
   77 |                 struct ttm_pool_type orders[MAX_ORDER];
      |                                             ^~~~~~~~~
      |                                             PMD_ORDER
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_fs_read_write.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_aperture.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_simple_kms_helper.o
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/atombios_crtc.o] Error 1
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_vmscan.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_dma_fence_chain.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_device_cgroup.c:29:6: warning: no previous prototype for ‘amdkcl_dev_cgroup_init’ [-Wmissing-prototypes]
   29 | void amdkcl_dev_cgroup_init(void)
      |      ^~~~~~~~~~~~~~~~~~~~~~
make[3]: *** [scripts/Makefile.build:243: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu/amdgpu_connectors.o] Error 1
make[2]: *** [scripts/Makefile.build:481: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdgpu] Error 2
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_mce_amd.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_cpumask.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_dsc_helper.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_mm_slab.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_irqdesc.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_suballoc.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_dp_helper.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_vmscan.c:25:6: warning: no previous prototype for ‘synchronize_shrinkers’ [-Wmissing-prototypes]
   25 | void synchronize_shrinkers(void)
      |      ^~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_mce_amd.c:16:22: warning: no previous prototype for ‘kcl_smca_get_bank_type’ [-Wmissing-prototypes]
   16 | enum smca_bank_types kcl_smca_get_bank_type(unsigned int cpu, unsigned int bank)
      |                      ^~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_drm_hdcp.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_debugfs_inode.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_workqueue.c:40:6: warning: no previous prototype for ‘amdkcl_workqueue_init’ [-Wmissing-prototypes]
   40 | void amdkcl_workqueue_init(void)
      |      ^~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_debugfs_file.o
  CC [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_sysfs_emit.o
/var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/kcl_numa.c:15:6: warning: no previous prototype for ‘amdkcl_numa_init’ [-Wmissing-prototypes]
   15 | void amdkcl_numa_init(void)
      |      ^~~~~~~~~~~~~~~~
  LD [M]  /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build/amd/amdkcl/amdkcl.o
make[1]: *** [/usr/src/linux-headers-6.8.0-11-generic/Makefile:1926: /var/lib/dkms/amdgpu/6.3.6-1718217.22.04/build] Error 2
make: *** [Makefile:240: __sub-make] Error 2
make: Leaving directory '/usr/src/linux-headers-6.8.0-11-generic'

### Operating System

24.04 (Noble Numbat)

### CPU

AMD Ryzen 7 6800HS with Radeon Graphics

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

GPU is AMD Radeon™ RX 6800S, unable to select that in the GPU list..