# Issue Installing on Debian Stretch

- **Issue #:** 499
- **State:** closed
- **Created:** 2018-08-12T00:44:31Z
- **Updated:** 2018-08-20T17:38:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/499

I tried following the instructions to install,  but I am getting an error on the actuall apt installation step:
Building initial module for 4.9.0-7-amd64
Error! Bad return status for module build on kernel: 4.9.0-7-amd64 (amd64)
Consult /var/lib/dkms/amdgpu/1.8-192/build/make.log for more information.

That log's contents are as below:

```
 DKMS make.log for amdgpu-1.8-192 for kernel 4.9.0-7-amd64 (amd64)
  2 Sat Aug 11 20:40:24 EDT 2018
  3 make: Entering directory '/usr/src/linux-headers-4.9.0-7-amd64'
  4   LD      /var/lib/dkms/amdgpu/1.8-192/build/built-in.o
  5   LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/built-in.o
  6   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_drm.o
  7   LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/built-in.o
  8   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/chash.o
  9   LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/built-in.o
 10   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_module.o
 11   LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/built-in.o
 12   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o
 13 In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/backport/backport.h:11:0,
 14                  from <command-line>:0:
 15 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
 16 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
 17   fence->status = error;
 18        ^~
 19 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:301: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_module.o' failed
 20 make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_module.o] Error 1
 21 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:552: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd' failed
 22 make[3]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd] Error 2
 23 make[3]: *** Waiting for unfinished jobs....
 24   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_device.o
 25 /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_drm.c:677:13: warning: ‘drm_atomic_print_state’ defined but not used [-Wunused-function]
 26  static void drm_atomic_print_state(const struct drm_atomic_state *state)
 27              ^~~~~~~~~~~~~~~~~~~~~~
 28 In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/../backport/backport.h:8:0,
 29                  from <command-line>:0:
 30 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
 31 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
 32   fence->status = error;
 33        ^~
 34 In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/../backport/backport.h:8:0,
 35                  from <command-line>:0:
 36 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
 37 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
 38   fence->status = error;
 39        ^~
 40   LD [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/amdchash.o
 41   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/main.o
 42   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/symbols.o
 43 At top level:
 44 /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c:837:1: warning: ‘amdgpu_get_crtc_scanout_position’ defined but not used [-Wunused-function]
 45  amdgpu_get_crtc_scanout_position(struct drm_device *dev, unsigned int pipe,
 46  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 47 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:301: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o' failed
 48 make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o] Error 1
 49 make[4]: *** Waiting for unfinished jobs....
 50   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.o
 51   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.o
 52 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:301: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_device.o' failed
 53 make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_device.o] Error 1
 54 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:552: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu' failed
 55 make[3]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu] Error 2
 56   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_kthread.o
 57   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_io.o
 58 In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.c:22:0:
 59 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
 60 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
 61   fence->status = error;
 62        ^~
 63 In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.c:20:0:
 64 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
 65 /var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
 66   fence->status = error;
 67        ^~
 68 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:301: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.o' failed
 69 make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.o] Error 1
 70 make[4]: *** Waiting for unfinished jobs....
 71 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:301: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.o' failed
 72 make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.o] Error 1
 73 /usr/src/linux-headers-4.9.0-7-common/scripts/Makefile.build:552: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl' failed
 74 make[3]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl] Error 2
 75 /usr/src/linux-headers-4.9.0-7-common/Makefile:1526: recipe for target '_module_/var/lib/dkms/amdgpu/1.8-192/build' failed
 76 make[2]: *** [_module_/var/lib/dkms/amdgpu/1.8-192/build] Error 2
 77 Makefile:152: recipe for target 'sub-make' failed
 78 make[1]: *** [sub-make] Error 2
 79 Makefile:8: recipe for target 'all' failed
```