# rock-dkms installation fail on kernel 4.14

- **Issue #:** 637
- **State:** closed
- **Created:** 2018-12-19T03:30:39Z
- **Updated:** 2023-12-19T02:29:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/637

I try to install rock-dkms-1.9-307 on my aarch64 server. 
- os: centos 7
- kernel: 4.14
- gcc: 7.3

Download rpm package from `http://repo.radeon.com/rocm/yum/rpm/`  and run `rpm -ivh rock-dkms-1.9-307.el7.noarch.rpm` . But got error:
```
In file included from <command-line>:0:0:
././include/linux/kconfig.h:67:1:
fatal error: /usr/src/kernels/4.14.62-5.hxt.aarch64/include/drm/drm_backport.h: No such file or directory
#endif /* __LINUX_KCONFIG_H */
 ^
compilation terminated.
```
So i check the file in rpm package and delete those line in `amdgpu-1.9-307.el7/Makefile` and `amdgpu-1.9-307.el7/amd/dkms/Makefile`
```
subdir-ccflags-y += \
        -include /usr/src/kernels/$(KERNELRELEASE)/include/drm/drm_backport.h
```
And rebuild rpm package.  
But Still got error while installing:
```
In file included from /var/lib/dkms/amdgpu/1.9-307.el7/build/amd/amdkcl/kcl_drm.c:1:0:
/var/lib/dkms/amdgpu/1.9-307.el7/build/include/kcl/kcl_drm.h: In function ‘kcl_drm_universal_plane_init’:
/var/lib/dkms/amdgpu/1.9-307.el7/build/include/kcl/kcl_drm.h:295:6: error: incompatible type for argument 7 of ‘drm_universal_plane_init’
      formats, format_count, type, name);
      ^
In file included from ./include/drm/drm_crtc.h:45:0,
                 from ./include/drm/drmP.h:69,
                 from /var/lib/dkms/amdgpu/1.9-307.el7/build/include/kcl/kcl_drm.h:6,
                 from /var/lib/dkms/amdgpu/1.9-307.el7/build/amd/amdkcl/kcl_drm.c:1:
./include/drm/drm_plane.h:548:5: note: expected ‘const uint64_t *’ but argument is of type ‘enum drm_plane_type’
 int drm_universal_plane_init(struct drm_device *dev,
     ^
In file included from /var/lib/dkms/amdgpu/1.9-307.el7/build/amd/amdkcl/kcl_drm.c:1:0:
/var/lib/dkms/amdgpu/1.9-307.el7/build/include/kcl/kcl_drm.h:295:6: error: incompatible type for argument 8 of ‘drm_universal_plane_init’
      formats, format_count, type, name);
      ^
In file included from ./include/drm/drm_crtc.h:45:0,
                 from ./include/drm/drmP.h:69,
                 from /var/lib/dkms/amdgpu/1.9-307.el7/build/include/kcl/kcl_drm.h:6,
                 from /var/lib/dkms/amdgpu/1.9-307.el7/build/amd/amdkcl/kcl_drm.c:1:
./include/drm/drm_plane.h:548:5: note: expected ‘enum drm_plane_type’ but argument is of type ‘const char *’
 int drm_universal_plane_init(struct drm_device *dev,
     ^
In file included from /var/lib/dkms/amdgpu/1.9-307.el7/build/amd/amdkcl/kcl_drm.c:1:0:
/var/lib/dkms/amdgpu/1.9-307.el7/build/include/kcl/kcl_drm.h:295:6: error: too few arguments to function ‘drm_universal_plane_init’
      formats, format_count, type, name);
      ^
In file included from ./include/drm/drm_crtc.h:45:0,
                 from ./include/drm/drmP.h:69,
                 from /var/lib/dkms/amdgpu/1.9-307.el7/build/include/kcl/kcl_drm.h:6,
                 from /var/lib/dkms/amdgpu/1.9-307.el7/build/amd/amdkcl/kcl_drm.c:1:
./include/drm/drm_plane.h:548:5: note: declared here
 int drm_universal_plane_init(struct drm_device *dev,
     ^
make[2]: *** [/var/lib/dkms/amdgpu/1.9-307.el7/build/amd/amdkcl/kcl_drm.o] Error 1
make[2]: *** Waiting for unfinished jobs....
```

Any suggestion to fix this ! Thanks

