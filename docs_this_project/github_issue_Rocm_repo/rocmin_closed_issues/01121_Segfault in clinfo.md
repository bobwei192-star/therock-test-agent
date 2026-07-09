# Segfault in clinfo

- **Issue #:** 1121
- **State:** closed
- **Created:** 2020-05-31T01:12:27Z
- **Updated:** 2021-02-17T05:23:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/1121

I've installed the ROCM runtime on my (Debian testing) machine (upstream kernel 5.3.14-1, dual-socket Haswell Xeon) following the instructions. When I run clinfo, I get a segfault. Adding "HSAKMT_DEBUG_LEVEL=7" sheds a bit more light, but not much:

```
$ HSAKMT_DEBUG_LEVEL=7  /opt/rocm-3.3.0/opencl/bin/x86_64/clinfo
acquiring VM for 13bc using 7
SVM alt (coherent):    0x1e00000 - 0x100167ffff
SVM (non-coherent): 0x1001680000 - 0x3fffffffff
Failed to map remapped mmio page on gpu_mem 0
[hsaKmtAllocMemory] node 0
[hsaKmtMapMemoryToGPU] address 0x1e08000
[hsaKmtAllocMemory] node 0
bind_mem_to_numa mem 0x1e01000 flags 0x40 size 0x1000 node_id 0
[hsaKmtMapMemoryToGPUNodes] address 0x1e01000 number of nodes 1
[hsaKmtAllocMemory] node 2
[hsaKmtAllocMemory] node 0
bind_mem_to_numa mem 0x1e14000 flags 0x40 size 0x2000 node_id 0
[hsaKmtMapMemoryToGPUNodes] address 0x1e14000 number of nodes 1
[hsaKmtAllocMemory] node 0
bind_mem_to_numa mem 0x1e04000 flags 0x1040 size 0x1000 node_id 0
[hsaKmtMapMemoryToGPUNodes] address 0x1e04000 number of nodes 1
[1]    1726631 segmentation fault (core dumped)  HSAKMT_DEBUG_LEVEL=7 /opt/rocm-3.3.0/opencl/bin/x86_64/clinfo‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍
```

The backtrace from gdb is not very informative, other than placing the crash somewhere inside the OpenCL runtime:
```
Thread 1 "clinfo" received signal SIGSEGV, Segmentation fault.
__GI___libc_free (mem=0x437265776f500403) at malloc.c:3102
3102    malloc.c: No such file or directory.
(gdb) bt
#0  __GI___libc_free (mem=0x437265776f500403) at malloc.c:3102
#1  0x00007ffff7a1ef65 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#2  0x00007ffff7a23737 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#3  0x00007ffff79ec4bf in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#4  0x00007ffff79e7096 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#5  0x00007ffff79b9b15 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#6  0x00007ffff7b37e39 in ?? () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#7  0x00007ffff79b9c4c in clIcdGetPlatformIDsKHR () from /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so
#8  0x00007ffff7e4dae3 in ?? () from /lib/x86_64-linux-gnu/libOpenCL.so.1
#9  0x00007ffff7e4e4e3 in clGetPlatformIDs () from /lib/x86_64-linux-gnu/libOpenCL.so.1
#10 0x000000000040cdd1 in ?? ()
#11 0x0000000000403b8c in ?? ()
#12 0x00007ffff7c70e0b in __libc_start_main (main=0x403aa0, argc=1, argv=0x7fffffffe688, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe678) at ../csu/libc-start.c:308
#13 0x000000000040c1fe in ?? ()‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍
```
What can I do to troubleshoot this?

AMD Device from lspci:
```
81:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev cb)                                    
81:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Fiji HDMI/DP Audio [Radeon R9 Nano / FURY/FURY X]     ‍‍
```

Device nodes:
```
$ ls -lah /dev/kfd /dev/dri /dev/shm                                                                                                                                    andreask_work@stout 0:16
crw-rw---- 1 root gpu  242, 0 Dec  2 11:18 /dev/kfd
```

/dev/dri:
```
total 0
drwxr-xr-x  3 root root      120 Dec  2 11:18 .
drwxr-xr-x 19 root root     3.5K Dec 14 07:00 ..
drwxr-xr-x  2 root root      100 Dec  2 11:18 by-path
crw-rw----  1 root gpu  226,   0 Dec  2 11:18 card0
crw-rw----  1 root gpu  226,   1 Dec  2 11:18 card1
crw-rw----  1 root gpu  226, 128 Dec  2 11:18 renderD128
```

/dev/shm:
```
total 8.0K
drwxrwxrwt  2 root root   80 May 26 14:19 .
drwxr-xr-x 19 root root 3.5K Dec 14 07:00 ..
-rw-rw-r--  1 root gpu     8 May 27 00:13 hsakmt_shared_mem
-rw-rw-r--  1 root gpu    32 Dec  7 22:23 sem.hsakmt_semaphore‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍
```

Thanks!