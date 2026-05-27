# Support Ubuntu custom kernel

> **Issue #2458**
> **状态**: closed
> **创建时间**: 2023-09-15T02:35:18Z
> **更新时间**: 2024-01-21T23:09:46Z
> **关闭时间**: 2023-11-10T16:08:38Z
> **作者**: winstonma
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2458

## 描述

Currently AMD ROCm driver supports Ubuntu default kernel, but when I install DKMS module on kernel v6.5.3 I got the error from the log file.

```
In file included from /var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/ttm/backport/backport.h:15,
                 from <command-line>:
/var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/include/kcl/backport/kcl_mm_backport.h: In function ‘kcl_get_user_pages_remote’:
/var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/include/kcl/backport/kcl_mm_backport.h:36:38: error: passing argument 1 of ‘get_user_pages_remote’ from incompatible pointer type [-Werror=incompatible-pointer-types]
   36 |         return get_user_pages_remote(tsk, mm, start, nr_pages, !!(gup_flags & FOLL_WRITE),
      |                                      ^~~
      |                                      |
      |                                      struct task_struct *
In file included from ./include/linux/scatterlist.h:8,
                 from ./include/linux/dma-mapping.h:11,
                 from /var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/include/kcl/kcl_dma_mapping.h:5,
                 from /var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/ttm/backport/backport.h:8:
./include/linux/mm.h:2397:46: note: expected ‘struct mm_struct *’ but argument is of type ‘struct task_struct *’
 2397 | long get_user_pages_remote(struct mm_struct *mm,
      |                            ~~~~~~~~~~~~~~~~~~^~
/var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/include/kcl/backport/kcl_mm_backport.h:36:43: warning: passing argument 2 of ‘get_user_pages_remote’ makes integer from pointer without a cast [-Wint-conversion]
   36 |         return get_user_pages_remote(tsk, mm, start, nr_pages, !!(gup_flags & FOLL_WRITE),
      |                                           ^~
      |                                           |
      |                                           struct mm_struct *
./include/linux/mm.h:2398:42: note: expected ‘long unsigned int’ but argument is of type ‘struct mm_struct *’
 2398 |                            unsigned long start, unsigned long nr_pages,
      |                            ~~~~~~~~~~~~~~^~~~~
/var/lib/dkms/amdgpu/6.2.4-1646729.22.04/build/include/kcl/backport/kcl_mm_backport.h:36:64: warning: passing argument 5 of ‘get_user_pages_remote’ makes pointer from integer without a cast [-Wint-conversion]
   36 |         return get_user_pages_remote(tsk, mm, start, nr_pages, !!(gup_flags & FOLL_WRITE),
      |                                                                ^~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                |
      |                                                                int
```

I am not sure but I guess it is caused by the flag settings problem at the very early stage. Would it be possible to get it supported? Thanks a lot

I attached the [make.log](https://github.com/RadeonOpenCompute/ROCm/files/12614979/make.log) for the reference.

