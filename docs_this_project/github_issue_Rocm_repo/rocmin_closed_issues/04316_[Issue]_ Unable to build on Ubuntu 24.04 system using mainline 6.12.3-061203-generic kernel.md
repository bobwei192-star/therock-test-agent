# [Issue]: Unable to build on Ubuntu 24.04 system using mainline 6.12.3-061203-generic kernel

- **Issue #:** 4316
- **State:** closed
- **Created:** 2025-01-30T01:39:46Z
- **Updated:** 2025-03-10T10:30:32Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4316

### Problem Description

amdgpu-dkms build fails due to (please see `make.log` below!!): 

```
In file included from ./include/linux/rhashtable-types.h:12,
                 from ./include/linux/sched/ext.h:15,
                 from ./include/linux/sched.h:85,
                 from ./include/linux/dma-fence.h:21,
                 from /tmp/amd.jcuhIcCy/include/linux/dma-resv.h:43,
                 from /tmp/amd.jcuhIcCy/amd/amdkcl/dma-buf/dma-resv.c:37:
./include/linux/alloc_tag.h:212:2: error: expected identifier or ‘(’ before ‘{’ token
  212 | ({                                                                      \
      |  ^
./include/linux/slab.h:1053:49: note: in expansion of macro ‘alloc_hooks’
 1053 | #define kvrealloc(...)                          alloc_hooks(kvrealloc_noprof(__VA_ARGS__))
      |                                                 ^~~~~~~~~~~
/tmp/amd.jcuhIcCy/include/kcl/kcl_slab.h:42:14: note: in expansion of macro ‘kvrealloc’
   42 | extern void *kvrealloc(const void *p, size_t oldsize, size_t newsize, gfp_t flags);
      |              ^~~~~~~~~
  CC [M]  /tmp/amd.jcuhIcCy/amd/amdkcl/kcl_page_alloc.o
```


### Operating System

Linux Mint 22.1 (Ubuntu 24.04) kernel v6.12.3

### CPU

AMD Ryzen Threadripper 7960X 24-Cores

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.3.2

### ROCm Component

_No response_

### Steps to Reproduce

- Use Ubuntu 24.04
- Use the [latest mainline kernel](https://kernel.ubuntu.com/mainline/) (including headers and modules): v6.12.3-061203-generic
- Using gcc v14
- Following: https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#rocm-install-quick

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

[make.log](https://github.com/user-attachments/files/18596210/make.log)