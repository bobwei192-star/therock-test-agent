# Unable to build rock-dkms for kernel 4.9.0-4-amd64

- **Issue #:** 292
- **State:** closed
- **Created:** 2017-12-29T18:19:23Z
- **Updated:** 2018-06-03T15:29:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/292

Hello and Happy New Year (almost). Thanks for the great work being done to advance computational GPU platforms. I am not sure if I should even worry about this, but I thought it was worth bringing to your attention since I couldn't find an issue for it already.

I was trying to follow these [ROCm Install Instructions](https://rocm.github.io/ROCmInstall.html) and on this command: `apt-get install -y rocm-opencl-dev rocm-dkms rocminfo`, it is trying to install `rock-dkms`. Not sure if that is a requisite for `rocm-dkms`, `rocm-opencl-dev`, or `rocminfo`; therefore, I'm not really sure if it's important. Nevertheless, it's failing.

Here's my build log:

```
DKMS make.log for rock-1.7.60-ubuntu for kernel 4.9.0-4-amd64 (amd64)
Fri Dec 29 18:09:07 UTC 2017
make: Entering directory '/usr/src/linux-headers-4.9.0-4-amd64'
  LD      /var/lib/dkms/rock/1.7.60-ubuntu/build/built-in.o
  LD      /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/built-in.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_drm.o
  LD      /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/built-in.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_drv.o
In file included from /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_ttm.h:27:0,
                 from /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu.h:55,
                 from /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../backport/include/kcl/kcl_amdgpu.h:5,
                 from /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../backport/backport.h:10,
                 from <command-line>:0:
/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../scheduler/gpu_scheduler.h:27:49: error: operator '==' has no left operand
 #if (defined OS_NAME_RHEL) && (OS_VERSION_MAJOR == 6)
                                                 ^~
In file included from /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../backport/backport.h:18:0,
                 from <command-line>:0:
/var/lib/dkms/rock/1.7.60-ubuntu/build/include/kcl/kcl_acpi.h:8:49: error: operator '<=' has no left operand
 #if (defined OS_NAME_RHEL) && (OS_VERSION_MAJOR <= 6)
                                                 ^~
In file included from /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../backport/backport.h:20:0,
                 from <command-line>:0:
/var/lib/dkms/rock/1.7.60-ubuntu/build/include/kcl/kcl_hwmon.h: In function 'kcl_hwmon_device_register_with_groups':
/var/lib/dkms/rock/1.7.60-ubuntu/build/include/kcl/kcl_hwmon.h:15:49: error: operator '<=' has no left operand
 #if (defined OS_NAME_RHEL) && (OS_VERSION_MAJOR <= 6)
                                                 ^~
At top level:
/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_drv.c:807:1: warning: 'amdgpu_get_crtc_scanout_position' defined but not used [-Wunused-function]
 amdgpu_get_crtc_scanout_position(struct drm_device *dev, unsigned int pipe,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/src/linux-headers-4.9.0-4-common/scripts/Makefile.build:298: recipe for target '/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_drv.o' failed
make[4]: *** [/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_drv.o] Error 1
/usr/src/linux-headers-4.9.0-4-common/scripts/Makefile.build:549: recipe for target '/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu' failed
make[3]: *** [/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu] Error 2
make[3]: *** Waiting for unfinished jobs....
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_drm_global.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/kcl_pci.o
  LD [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdkcl/amdkcl.o
/usr/src/linux-headers-4.9.0-4-common/Makefile:1510: recipe for target '_module_/var/lib/dkms/rock/1.7.60-ubuntu/build' failed
make[2]: *** [_module_/var/lib/dkms/rock/1.7.60-ubuntu/build] Error 2
Makefile:150: recipe for target 'sub-make' failed
make[1]: *** [sub-make] Error 2
Makefile:8: recipe for target 'all' failed
make: *** [all] Error 2
make: Leaving directory '/usr/src/linux-headers-4.9.0-4-amd64'
```

Any feedback is appreciated. Thanks and thanks again for the advancement of this technology.