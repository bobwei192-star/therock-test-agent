# Error while installing ROCm 1.4-16 on ubuntu 16.04 LTS:

- **Issue #:** 59
- **State:** closed
- **Created:** 2016-12-22T18:56:45Z
- **Updated:** 2017-01-05T00:02:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/59

Im trying to install ROCm 1.4-16 on my machine with Ubuntu 16.04. The system is a AMD APU with intergrated GPU. I received the following error message during installation.
ERROR (dkms apport): kernel package linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16 is not supported
Error! Bad return status for module build on kernel: 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64).
I have attached the corresponding log file as .txt file

[makelog.txt](https://github.com/RadeonOpenCompute/ROCm/files/669587/makelog.txt)
Any pointers to what may be wrong and how to fix this issue is much appreciated.

Thanks in advance! 

Log file Details:

DKMS make.log for amdgpu-pro-16.50-362463 for kernel 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64)
Wed Dec 21 12:24:03 PST 2016
make: Entering directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'
  LD      /var/lib/dkms/amdgpu-pro/16.50-362463/build/built-in.o
  LD      /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/built-in.o
  CC [M]  /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h: In function ‘kcl_ttm_bo_reserve’:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:116:9: error: too many arguments to function ‘ttm_bo_reserve’
  return ttm_bo_reserve(bo, interruptible, no_wait, false, ticket);
         ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
                 from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
                 from <command-line>:0:
include/drm/ttm/ttm_bo_driver.h:877:19: note: declared here
 static inline int ttm_bo_reserve(struct ttm_buffer_object *bo,
                   ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h: In function ‘kcl_ttm_bo_move_accel_cleanup’:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:153:11: error: incompatible type for argument 4 of ‘ttm_bo_move_accel_cleanup’
    evict, no_wait_gpu, new_mem);
           ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
                 from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
                 from <command-line>:0:
include/drm/ttm/ttm_bo_driver.h:1046:12: note: expected ‘struct ttm_mem_reg *’ but argument is of type ‘bool {aka _Bool}’
 extern int ttm_bo_move_accel_cleanup(struct ttm_buffer_object *bo,
            ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:152:9: error: too many arguments to function ‘ttm_bo_move_accel_cleanup’
  return ttm_bo_move_accel_cleanup(bo, fence,
         ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
                 from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
                 from <command-line>:0:
include/drm/ttm/ttm_bo_driver.h:1046:12: note: declared here
 extern int ttm_bo_move_accel_cleanup(struct ttm_buffer_object *bo,
            ^
scripts/Makefile.build:291: recipe for target '/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o' failed
make[2]: *** [/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o] Error 1
scripts/Makefile.build:440: recipe for target '/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu] Error 2
Makefile:1428: recipe for target '_module_/var/lib/dkms/amdgpu-pro/16.50-362463/build' failed
make: *** [_module_/var/lib/dkms/amdgpu-pro/16.50-362463/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'
