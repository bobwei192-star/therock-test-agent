# [Issue]: Unable to install amdgpu on Ubuntu 22 LTS

- **Issue #:** 4164
- **State:** closed
- **Created:** 2024-12-16T12:50:04Z
- **Updated:** 2024-12-28T00:15:45Z
- **Labels:** Under Investigation, ROCm 6.3.0, Radeon 760M Graphics
- **URL:** https://github.com/ROCm/ROCm/issues/4164

### Problem Description

This is the kernel version I'm running

```
uname -srmv
Linux 6.8.0-49-generic #49~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Nov  6 17:42:15 UTC 2 x86_64
```

### Operating System

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 5 7640U w/ Radeon 760M Graphics

### GPU

Radeon 760M Graphics

### ROCm Version

ROCm 6.3.0

### ROCm Component

_No response_

### Steps to Reproduce

Run the commands described [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)
```
sudo apt update
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
wget https://repo.radeon.com/amdgpu-install/6.3/ubuntu/jammy/amdgpu-install_6.3.60300-1_all.deb
sudo apt install ./amdgpu-install_6.3.60300-1_all.deb
sudo apt update
sudo apt install amdgpu-dkms rocm
```

```
Building for 6.8.0-49-generic
Building for architecture x86_64
Building initial module for 6.8.0-49-generic
ERROR: Cannot create report: [Errno 17] File exists: &apos;/var/crash/amdgpu-dkms.0.crash&apos;
Error! Bad return status for module build on kernel: 6.8.0-49-generic (x86_64)
Consult /var/lib/dkms/amdgpu/6.10.5-2084815.22.04/build/make.log for more information.
<b>dpkg:</b> error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
<font color="#BF616A"><b>E: </b></font>Sub-process /usr/bin/dpkg returned an error code (1)
```

And this is the content of `/var/crash/amdgpu-dkms.0.crash`

```
ProblemType: Package
DKMSBuildLog:
 DKMS make.log for amdgpu-6.10.5-2084815.22.04 for kernel 6.8.0-49-generic (x86_64)
 lun 16 dic 2024, 00:00:06, CET
 make: Entering directory '/usr/src/linux-headers-6.8.0-49-generic'
 warning: the compiler differs from the one used to build the kernel
   The kernel was built by: x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
   You are using:           gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
   CC [M]  /var/tmp/amd.MPVyukgA/scheduler/sched_main.o
   CC [M]  /var/tmp/amd.MPVyukgA/scheduler/sched_fence.o
   CC [M]  /var/tmp/amd.MPVyukgA/scheduler/sched_entity.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdxcp/amdgpu_xcp_drv.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdxcp/./backport/kcl_drm_drv.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_tt.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_bo.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_bo_util.o
   CC [M]  /var/tmp/amd.MPVyukgA/drm_gem_ttm_helper.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_bo_vm.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/main.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdgpu/amdgpu_drv.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_module.o
 /var/tmp/amd.MPVyukgA/amd/amdkcl/main.c:14:12: warning: no previous prototype for ‘amdkcl_init’ [-Wmissing-prototypes]
    14 | int __init amdkcl_init(void)
       |            ^~~~~~~~~~~
 /var/tmp/amd.MPVyukgA/amd/amdkcl/main.c:29:13: warning: no previous prototype for ‘amdkcl_exit’ [-Wmissing-prototypes]
    29 | void __exit amdkcl_exit(void)
       |             ^~~~~~~~~~~
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_common.o
   LD [M]  /var/tmp/amd.MPVyukgA/amd/amdxcp/amdxcp.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_kernel_params.o
 In file included from /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_helper.h:34,
                  from /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_helper_backport.h:5,
                  from /var/tmp/amd.MPVyukgA/amd/backport/backport.h:56,
                  from <command-line>:
 /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_cec.h: In function ‘_kcl_drm_dp_cec_register_connector’:
 /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_cec.h:67:53: error: passing argument 2 of ‘drm_dp_cec_register_connector’ from incompatible pointer type [-Werror=incompatible-pointer-types]
    67 |         drm_dp_cec_register_connector(aux, connector->name, connector->dev->dev);
       |                                            ~~~~~~~~~^~~~~~
       |                                                     |
       |                                                     char *
 In file included from /var/tmp/amd.MPVyukgA/include/kcl/header/drm/display/drm_dp_helper.h:6,
                  from /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_helper.h:33:
 ./include/drm/display/drm_dp_helper.h:727:58: note: expected ‘struct drm_connector *’ but argument is of type ‘char *’
   727 |                                    struct drm_connector *connector);
       |                                    ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~
 /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_cec.h:67:9: error: too many arguments to function ‘drm_dp_cec_register_connector’
    67 |         drm_dp_cec_register_connector(aux, connector->name, connector->dev->dev);
       |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ./include/drm/display/drm_dp_helper.h:726:6: note: declared here
   726 | void drm_dp_cec_register_connector(struct drm_dp_aux *aux,
       |      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_helper_backport.h: At top level:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_helper_backport.h:24:19: error: static declaration of ‘drm_dp_read_dpcd_caps’ follows non-static declaration
    24 | static inline int drm_dp_read_dpcd_caps(struct drm_dp_aux *aux,
       |                   ^~~~~~~~~~~~~~~~~~~~~
 ./include/drm/display/drm_dp_helper.h:510:5: note: previous declaration of ‘drm_dp_read_dpcd_caps’ with type ‘int(struct drm_dp_aux *, u8 *)’ {aka ‘int(struct drm_dp_aux *, unsigned char *)’}
   510 | int drm_dp_read_dpcd_caps(struct drm_dp_aux *aux,
       |     ^~~~~~~~~~~~~~~~~~~~~
 In file included from /var/tmp/amd.MPVyukgA/amd/backport/backport.h:57:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h: In function ‘_kcl_drm_dp_atomic_find_vcpi_slots’:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:59:33: error: ‘struct drm_dp_mst_topology_mgr’ has no member named ‘pbn_div’
    59 |                 pbn_backup = mgr->pbn_div;
       |                                 ^~
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:60:20: error: ‘struct drm_dp_mst_topology_mgr’ has no member named ‘pbn_div’
    60 |                 mgr->pbn_div = pbn_div;
       |                    ^~
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:63:21: error: implicit declaration of function ‘drm_dp_atomic_find_vcpi_slots’; did you mean ‘drm_dp_atomic_find_time_slots’? [-Werror=implicit-function-declaration]
    63 |         req_slots = drm_dp_atomic_find_vcpi_slots(state, mgr, port, pbn);
       |                     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       |                     drm_dp_atomic_find_time_slots
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:66:20: error: ‘struct drm_dp_mst_topology_mgr’ has no member named ‘pbn_div’
    66 |                 mgr->pbn_div = pbn_backup;
       |                    ^~
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h: In function ‘_kcl_drm_dp_mst_topology_mgr_resume’:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:102:16: error: too few arguments to function ‘drm_dp_mst_topology_mgr_resume’
   102 |         return drm_dp_mst_topology_mgr_resume(mgr);
       |                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/tmp/amd.MPVyukgA/include/kcl/header/drm/display/drm_dp_mst_helper.h:6,
                  from /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:25:
 ./include/drm/display/drm_dp_mst_helper.h:870:1: note: declared here
   870 | drm_dp_mst_topology_mgr_resume(struct drm_dp_mst_topology_mgr *mgr,
       | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_execbuf_util.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdgpu/amdgpu_device.o
   CC [M]  /var/tmp/amd.MPVyukgA/drm_buddy.o
 cc1: some warnings being treated as errors
 make[3]: *** [scripts/Makefile.build:243: /var/tmp/amd.MPVyukgA/amd/amdgpu/amdgpu_drv.o] Error 1
 make[3]: *** Waiting for unfinished jobs....
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/dma-buf/dma-resv.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_dma-resv.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_backlight.o
   LD [M]  /var/tmp/amd.MPVyukgA/amddrm_ttm_helper.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_ioctl.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_range_manager.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_resource.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_kthread.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_io.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_seq_file.o
   LD [M]  /var/tmp/amd.MPVyukgA/scheduler/amd-sched.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_pool.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_suspend.o
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_suspend.c:32:6: warning: no previous prototype for ‘amdkcl_suspend_init’ [-Wmissing-prototypes]
    32 | void amdkcl_suspend_init(void)
       |      ^~~~~~~~~~~~~~~~~~~
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_io.c:69:6: warning: no previous prototype for ‘amdkcl_io_init’ [-Wmissing-prototypes]
    69 | void amdkcl_io_init(void)
       |      ^~~~~~~~~~~~~~
 In file included from /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_helper.h:34,
                  from /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_helper_backport.h:5,
                  from /var/tmp/amd.MPVyukgA/amd/backport/backport.h:56,
                  from <command-line>:
 /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_cec.h: In function ‘_kcl_drm_dp_cec_register_connector’:
 /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_cec.h:67:53: error: passing argument 2 of ‘drm_dp_cec_register_connector’ from incompatible pointer type [-Werror=incompatible-pointer-types]
    67 |         drm_dp_cec_register_connector(aux, connector->name, connector->dev->dev);
       |                                            ~~~~~~~~~^~~~~~
       |                                                     |
       |                                                     char *
 In file included from /var/tmp/amd.MPVyukgA/include/kcl/header/drm/display/drm_dp_helper.h:6,
                  from /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_helper.h:33:
 ./include/drm/display/drm_dp_helper.h:727:58: note: expected ‘struct drm_connector *’ but argument is of type ‘char *’
   727 |                                    struct drm_connector *connector);
       |                                    ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~
 /var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_cec.h:67:9: error: too many arguments to function ‘drm_dp_cec_register_connector’
    67 |         drm_dp_cec_register_connector(aux, connector->name, connector->dev->dev);
       |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ./include/drm/display/drm_dp_helper.h:726:6: note: declared here
   726 | void drm_dp_cec_register_connector(struct drm_dp_aux *aux,
       |      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_helper_backport.h: At top level:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_helper_backport.h:24:19: error: static declaration of ‘drm_dp_read_dpcd_caps’ follows non-static declaration
    24 | static inline int drm_dp_read_dpcd_caps(struct drm_dp_aux *aux,
       |                   ^~~~~~~~~~~~~~~~~~~~~
 ./include/drm/display/drm_dp_helper.h:510:5: note: previous declaration of ‘drm_dp_read_dpcd_caps’ with type ‘int(struct drm_dp_aux *, u8 *)’ {aka ‘int(struct drm_dp_aux *, unsigned char *)’}
   510 | int drm_dp_read_dpcd_caps(struct drm_dp_aux *aux,
       |     ^~~~~~~~~~~~~~~~~~~~~
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_pci.o
 In file included from /var/tmp/amd.MPVyukgA/amd/backport/backport.h:57:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h: In function ‘_kcl_drm_dp_atomic_find_vcpi_slots’:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:59:33: error: ‘struct drm_dp_mst_topology_mgr’ has no member named ‘pbn_div’
    59 |                 pbn_backup = mgr->pbn_div;
       |                                 ^~
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:60:20: error: ‘struct drm_dp_mst_topology_mgr’ has no member named ‘pbn_div’
    60 |                 mgr->pbn_div = pbn_div;
       |                    ^~
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_mm.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_memory.o
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:63:21: error: implicit declaration of function ‘drm_dp_atomic_find_vcpi_slots’; did you mean ‘drm_dp_atomic_find_time_slots’? [-Werror=implicit-function-declaration]
    63 |         req_slots = drm_dp_atomic_find_vcpi_slots(state, mgr, port, pbn);
       |                     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       |                     drm_dp_atomic_find_time_slots
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:66:20: error: ‘struct drm_dp_mst_topology_mgr’ has no member named ‘pbn_div’
    66 |                 mgr->pbn_div = pbn_backup;
       |                    ^~
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h: In function ‘_kcl_drm_dp_mst_topology_mgr_resume’:
 /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:102:16: error: too few arguments to function ‘drm_dp_mst_topology_mgr_resume’
   102 |         return drm_dp_mst_topology_mgr_resume(mgr);
       |                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/tmp/amd.MPVyukgA/include/kcl/header/drm/display/drm_dp_mst_helper.h:6,
                  from /var/tmp/amd.MPVyukgA/include/kcl/backport/kcl_drm_dp_mst_helper_backport.h:25:
 ./include/drm/display/drm_dp_mst_helper.h:870:1: note: declared here
   870 | drm_dp_mst_topology_mgr_resume(struct drm_dp_mst_topology_mgr *mgr,
       | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_fence.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_device.o
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_mm.c:58:6: warning: no previous prototype for ‘amdkcl_mm_init’ [-Wmissing-prototypes]
    58 | void amdkcl_mm_init(void)
       |      ^~~~~~~~~~~~~~
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_cache.o
 cc1: some warnings being treated as errors
 make[3]: *** [scripts/Makefile.build:243: /var/tmp/amd.MPVyukgA/amd/amdgpu/amdgpu_device.o] Error 1
 make[2]: *** [scripts/Makefile.build:481: /var/tmp/amd.MPVyukgA/amd/amdgpu] Error 2
 make[2]: *** Waiting for unfinished jobs....
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_fb.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_sys_manager.o
   CC [M]  /var/tmp/amd.MPVyukgA/ttm/ttm_agp_backend.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_print.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_edid.o
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_fence.c:239:6: warning: no previous prototype for ‘amdkcl_fence_init’ [-Wmissing-prototypes]
   239 | void amdkcl_fence_init(void)
       |      ^~~~~~~~~~~~~~~~~
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_crtc.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_connector.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_atomic_helper.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_device_cgroup.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_mn.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_modes.o
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_fb.c: In function ‘drm_fb_helper_fill_info’:
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_fb.c:45:9: error: implicit declaration of function ‘drm_fb_helper_fill_fix’; did you mean ‘drm_fb_helper_fill_info’? [-Werror=implicit-function-declaration]
    45 |         drm_fb_helper_fill_fix(info, fb->pitches[0], fb->format->depth);
       |         ^~~~~~~~~~~~~~~~~~~~~~
       |         drm_fb_helper_fill_info
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_fb.c:45:40: error: invalid use of undefined type ‘struct drm_framebuffer’
    45 |         drm_fb_helper_fill_fix(info, fb->pitches[0], fb->format->depth);
       |                                        ^~
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_fb.c:45:56: error: invalid use of undefined type ‘struct drm_framebuffer’
    45 |         drm_fb_helper_fill_fix(info, fb->pitches[0], fb->format->depth);
       |                                                        ^~
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_time.o
   CC [M]  /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_acpi_table.o
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_fb.c:46:9: error: implicit declaration of function ‘drm_fb_helper_fill_var’; did you mean ‘drm_fb_helper_fill_info’? [-Werror=implicit-function-declaration]
    46 |         drm_fb_helper_fill_var(info, fb_helper,
       |         ^~~~~~~~~~~~~~~~~~~~~~
       |         drm_fb_helper_fill_info
 cc1: some warnings being treated as errors
 make[3]: *** [scripts/Makefile.build:243: /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_drm_fb.o] Error 1
 make[3]: *** Waiting for unfinished jobs....
 /var/tmp/amd.MPVyukgA/amd/amdkcl/kcl_device_cgroup.c:29:6: warning: no previous prototype for ‘amdkcl_dev_cgroup_init’ [-Wmissing-prototypes]
    29 | void amdkcl_dev_cgroup_init(void)
       |      ^~~~~~~~~~~~~~~~~~~~~~
   LD [M]  /var/tmp/amd.MPVyukgA/ttm/amdttm.o
 make[2]: *** [scripts/Makefile.build:481: /var/tmp/amd.MPVyukgA/amd/amdkcl] Error 2
 make[1]: *** [/usr/src/linux-headers-6.8.0-49-generic/Makefile:1925: /var/tmp/amd.MPVyukgA] Error 2
 make: *** [Makefile:240: __sub-make] Error 2
 make: Leaving directory '/usr/src/linux-headers-6.8.0-49-generic'
DKMSKernelVersion: 6.8.0-49-generic
Date: Mon Dec 16 00:00:11 2024
DuplicateSignature: dkms:amdgpu-dkms:1:6.10.5.60300-2084815.22.04:/var/tmp/amd.MPVyukgA/include/kcl/kcl_drm_dp_cec.h:67:53: error: passing argument 2 of ‘drm_dp_cec_register_connector’ from incompatible pointer type [-Werror=incompatible-pointer-types]
Package: amdgpu-dkms 1:6.10.5.60300-2084815.22.04
PackageVersion: 1:6.10.5.60300-2084815.22.04
SourcePackage: amdgpu-dkms
Title: amdgpu-dkms 1:6.10.5.60300-2084815.22.04: amdgpu kernel module failed to build
```


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is NOT loaded, possibly no GPU devices

### Additional Information

_No response_