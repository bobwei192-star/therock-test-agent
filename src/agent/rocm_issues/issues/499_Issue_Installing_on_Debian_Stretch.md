# Issue Installing on Debian Stretch

> **Issue #499**
> **状态**: closed
> **创建时间**: 2018-08-12T00:44:31Z
> **更新时间**: 2018-08-20T17:38:45Z
> **关闭时间**: 2018-08-12T13:53:44Z
> **作者**: tarfeef101
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/499

## 描述

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

---

## 评论 (4 条)

### 评论 #1 — PsySc0rpi0n (2018-08-12T09:51:16Z)

Did the same yesterday on the same Kernel version 4.9.0-7. Tried to upgrade to Kernel 4.17. Different error but still not compatible. Apparently only way is to use Kernel 4.13.
Also tried to install amdgpu-pro 18.20 from AMD site but still could not manage to resolve unmet dependencies and other errors!

---

### 评论 #2 — tarfeef101 (2018-08-12T13:53:32Z)

Geez... I did like, everything to try and get it to work. Even tried modifying the amd pro driver installation scripts to make it not check my distro.

In the end I just swapped cards with another rig of mine. Now I'm using a 1060, and it literally tool 1 apt install to work perfectly. 

AMD: C'mon guys. I want to support you, but you gotta support more than just windows... Pls.

---

### 评论 #3 — godofdream (2018-08-20T17:16:13Z)

I would like to see this issue reopenend as it wasn't fixed.
let's begin with some simple stuff: libnuma-dev is not marked as dependency for the dkms package
next point: it's not compatible with all kernels, what are the error messages of specific kernels.

Mine:
`DKMS make.log for amdgpu-1.8-192 for kernel 4.9.0-8-amd64 (x86_64)
Mo 20. Aug 19:06:09 CEST 2018
make: Verzeichnis „/usr/src/linux-headers-4.9.0-8-amd64“ wird betreten
  LD      /var/lib/dkms/amdgpu/1.8-192/build/built-in.o
  LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/chash.o
  LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_drm.o
  LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_module.o
  LD      /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o
In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/backport/backport.h:11:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
  fence->status = error;
       ^~
/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_drm.c:677:13: warning: ‘drm_atomic_print_state’ defined but not used [-Wunused-function]
 static void drm_atomic_print_state(const struct drm_atomic_state *state)
             ^~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/../backport/backport.h:8:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
  fence->status = error;
       ^~
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:301: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_module.o“ scheiterte
make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_module.o] Fehler 1
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:552: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd“ scheiterte
make[3]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd] Fehler 2
make[3]: *** Es wird auf noch nicht beendete Prozesse gewartet...
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_device.o
  LD [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/amdchash.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/main.o
In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/../backport/backport.h:8:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
  fence->status = error;
       ^~
At top level:
/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c:837:1: warning: ‘amdgpu_get_crtc_scanout_position’ defined but not used [-Wunused-function]
 amdgpu_get_crtc_scanout_position(struct drm_device *dev, unsigned int pipe,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:301: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o“ scheiterte
make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o] Fehler 1
make[4]: *** Es wird auf noch nicht beendete Prozesse gewartet...
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_kthread.o
In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.c:22:0:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
  fence->status = error;
       ^~
In file included from /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.c:20:0:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h: In function ‘kcl_dma_fence_set_error’:
/var/lib/dkms/amdgpu/1.8-192/build/include/kcl/kcl_fence.h:163:7: error: ‘struct fence’ has no member named ‘status’
  fence->status = error;
       ^~
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:301: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.o“ scheiterte
make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.o] Fehler 1
make[4]: *** Es wird auf noch nicht beendete Prozesse gewartet...
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:301: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_device.o“ scheiterte
make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_device.o] Fehler 1
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:552: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu“ scheiterte
make[3]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu] Fehler 2
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:301: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.o“ scheiterte
make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.o] Fehler 1
/usr/src/linux-headers-4.9.0-8-common/scripts/Makefile.build:552: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl“ scheiterte
make[3]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl] Fehler 2
/usr/src/linux-headers-4.9.0-8-common/Makefile:1526: die Regel für Ziel „_module_/var/lib/dkms/amdgpu/1.8-192/build“ scheiterte
make[2]: *** [_module_/var/lib/dkms/amdgpu/1.8-192/build] Fehler 2
Makefile:152: die Regel für Ziel „sub-make“ scheiterte
make[1]: *** [sub-make] Fehler 2
Makefile:8: die Regel für Ziel „all“ scheiterte
make: *** [all] Fehler 2
make: Verzeichnis „/usr/src/linux-headers-4.9.0-8-amd64“ wird verlassen
`

@AMD do you need a freelancer giving you a helping hand with the linux drivers? contact me.

---

### 评论 #4 — godofdream (2018-08-20T17:38:45Z)

`
DKMS make.log for amdgpu-1.8-192 for kernel 4.17.0-0.bpo.1-amd64 (x86_64)
Mo 20. Aug 19:25:49 CEST 2018
make: Verzeichnis „/usr/src/linux-headers-4.17.0-0.bpo.1-amd64“ wird betreten
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_module.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/chash.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o
  LD [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/lib/amdchash.o
/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c: In function ‘amdgpu_pmops_runtime_suspend’:
/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c:727:2: error: implicit declaration of function ‘vga_switcheroo_set_dynamic_switch’ [-Werror=implicit-function-declaration]
  vga_switcheroo_set_dynamic_switch(pdev, VGA_SWITCHEROO_OFF);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/scheduler/gpu_scheduler.o
cc1: some warnings being treated as errors
/usr/src/linux-headers-4.17.0-0.bpo.1-common/scripts/Makefile.build:317: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o“ scheiterte
make[4]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.o] Fehler 1
/usr/src/linux-headers-4.17.0-0.bpo.1-common/scripts/Makefile.build:564: die Regel für Ziel „/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu“ scheiterte
make[3]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu] Fehler 2
make[3]: *** Es wird auf noch nicht beendete Prozesse gewartet...
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_device.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_chardev.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_topology.o
  LD [M]  /var/lib/dkms/amdgpu/1.8-192/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_pasid.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_doorbell.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_flat_memory.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_process.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_queue.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_mqd_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_mqd_manager_cik.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_mqd_manager_vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_mqd_manager_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_drm_global.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_kernel_queue.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_kernel_queue_cik.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_kernel_queue_vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_kernel_queue_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_packet_manager.o
  LD [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_process_queue_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_device_queue_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_device_queue_manager_cik.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_device_queue_manager_vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_device_queue_manager_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_interrupt.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_events.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/cik_event_interrupt.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_int_process_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_dbgdev.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_dbgmgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_crat.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_rdma.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_peerdirect.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_ipc.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_iommu.o
  CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/kfd_debugfs.o
  LD [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdkfd/amdkfd.o
/usr/src/linux-headers-4.17.0-0.bpo.1-common/Makefile:1585: die Regel für Ziel „_module_/var/lib/dkms/amdgpu/1.8-192/build“ scheiterte
make[2]: *** [_module_/var/lib/dkms/amdgpu/1.8-192/build] Fehler 2
Makefile:146: die Regel für Ziel „sub-make“ scheiterte
make[1]: *** [sub-make] Fehler 2
Makefile:8: die Regel für Ziel „all“ scheiterte
make: *** [all] Fehler 2
make: Verzeichnis „/usr/src/linux-headers-4.17.0-0.bpo.1-amd64“ wird verlassen

`

---
