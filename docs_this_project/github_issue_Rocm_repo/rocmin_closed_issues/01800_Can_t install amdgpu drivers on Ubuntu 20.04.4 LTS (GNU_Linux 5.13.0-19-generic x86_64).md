# Can't install amdgpu drivers on Ubuntu 20.04.4 LTS (GNU/Linux 5.13.0-19-generic x86_64)

- **Issue #:** 1800
- **State:** closed
- **Created:** 2022-08-25T10:03:23Z
- **Updated:** 2023-12-27T17:28:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/1800

Hi,
System: Ubuntu 20.04.4, Gpu: Radeon Pro W5500, Drivers tested (21.40, 22.10)
https://repo.radeon.com/amdgpu-install/21.40.2/ubuntu/focal/amdgpu-install_21.40.2.40502-1_all.deb
https://repo.radeon.com/amdgpu-install/22.10.4/ubuntu/focal/amdgpu-install_22.10.4.50104-1_all.deb

And I also tested with Linux5.15.0-46-generic/Linux5.11.0-19-generic,it has the similar amdgpu-dkms compiling error.
run command as follow:
```
sudo apt install ./amdgpu-install_22.10.4.50104-1_all.deb
sudo apt update
sudo amdgpu-install 
```

When I try to install drivers, I get this:
`Loading new amdgpu-5.13.20.5.1-1395274 DKMS files...
Building for 5.13.0-19-generic 5.15.0-46-generic
Building for architecture x86_64
Building initial module for 5.13.0-19-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms-firmware.0.crash'
Error! Bad return status for module build on kernel: 5.13.0-19-generic (x86_64)
Consult /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/make.log for more information.`

when open /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/make.log, it has the following log:
`/var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/Makefile:26: "Local GCC version 90404 does not match kernel compiler GCC version 90300"
/var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/Makefile:27: "This may cause unexpected and hard-to-isolate compiler-related issues"
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/drm_gem_ttm_helper.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/amdkcl/kcl_common.o
  CC [M]  /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/ttm/ttm_range_manager.o
In file included from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/backport/backport.h:61,
                 from <command-line>:
/var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/backport/kcl_drm_fb.h: In function ‘_kcl_drm_helper_mode_fill_fb_struct’:
/var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/backport/kcl_drm_fb.h:35:33: error: passing argument 1 of ‘drm_helper_mode_fill_fb_struct’ from incompatible pointer type [-Werror=incompatible-pointer-types]
   35 |  drm_helper_mode_fill_fb_struct(fb, mode_cmd);
      |                                 ^~
      |                                 |
      |                                 struct drm_framebuffer *
In file included from ./include/drm/drm_crtc_helper.h:44,
                 from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/kcl_drm_crtc.h:52,
                 from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/backport/kcl_drm_crtc.h:6,
                 from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/backport/backport.h:52,
                 from <command-line>:
./include/drm/drm_modeset_helper.h:34:56: note: expected ‘struct drm_device *’ but argument is of type ‘struct drm_framebuffer *’
   34 | void drm_helper_mode_fill_fb_struct(struct drm_device *dev,
      |                                     ~~~~~~~~~~~~~~~~~~~^~~
In file included from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/backport/backport.h:61,
                 from <command-line>:
/var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/backport/kcl_drm_fb.h:35:37: error: passing argument 2 of ‘drm_helper_mode_fill_fb_struct’ from incompatible pointer type [-Werror=incompatible-pointer-types]
   35 |  drm_helper_mode_fill_fb_struct(fb, mode_cmd);
      |                                     ^~~~~~~~
      |                                     |
      |                                     const struct drm_mode_fb_cmd2 *
In file included from ./include/drm/drm_crtc_helper.h:44,
                 from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/kcl_drm_crtc.h:52,
                 from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/backport/kcl_drm_crtc.h:6,
                 from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/backport/backport.h:52,
                 from <command-line>:
./include/drm/drm_modeset_helper.h:35:33: note: expected ‘struct drm_framebuffer *’ but argument is of type ‘const struct drm_mode_fb_cmd2 *’
   35 |         struct drm_framebuffer *fb,
      |         ~~~~~~~~~~~~~~~~~~~~~~~~^~
In file included from /var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/amd/backport/backport.h:61,
                 from <command-line>:
/var/lib/dkms/amdgpu/5.13.20.5.1-1395274/build/include/kcl/backport/kcl_drm_fb.h:35:2: error: too few arguments to function ‘drm_helper_mode_fill_fb_struct’
   35 |  drm_helper_mode_fill_fb_struct(fb, mode_cmd);
      |  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from ./include/drm/drm_crtc_helper.h:44
.....
`

I am not really sure as to what I am to do next, can anyone give me any pointers?

Thanks in advance.
