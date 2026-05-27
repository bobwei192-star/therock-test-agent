# Debian/Ubuntu hip-rocclr's libamdhip64_static.a pointing to missing libamdhip64_static_temp.a

> **Issue #1189**
> **状态**: closed
> **创建时间**: 2020-08-11T23:39:53Z
> **更新时间**: 2021-01-06T11:48:53Z
> **关闭时间**: 2021-01-06T11:48:53Z
> **作者**: JustinTArthur
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1189

## 描述

Recently someone in #ROCm on Freenode attempted to compile the Square HIP sample bundled with ROCm Debian packages, but compilation with the included Makefile failed due to missing static lib deps. The Makefile's projected command:

    /opt/rocm/hip/bin/hipcc -use-staticlib square.cpp -o square.out

simply won't work with the rocm-dev package set:

    /usr/bin/ld: /opt/rocm-3.5.0/hip/lib/libamdhip64_static.a: error adding symbols: No such file or directory

Via `strace`, the underlying error comes from a search for a path that doesn't exist:
```
stat("/src/out/ubuntu-16.04/16.04/build/hip-on-rocclr/lib/libamdhip64_static_temp.a", 0x7ffd28fe3e20) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/src/out/ubuntu-16.04/16.04/build/hip-on-rocclr/lib/libamdhip64_static_temp.a", O_RDONLY) = -1 ENOENT (No such file or directory)
write(2, "nm: /opt/rocm-3.5.0/hip/lib/liba"..., 76nm: /opt/rocm-3.5.0/hip/lib/libamdhip64_static.a: No such file or directory
```
`libamdhip64_static_temp.a` isn't bundled in the hip-rocclr Debian package, furthermore that specific /src/out/ubuntu-16.04 directory couldn't exist at this point, especially on an Ubuntu 20 LTS system.

I'm attaching a [Dockerfile](https://github.com/RadeonOpenCompute/ROCm/files/5059938/Dockerfile.txt) (as a .txt for GitHub) for reproducing this using the official Debian packages and installation instructions, regardless of host Linux or GPUs. To reproduce:

    docker build -t debian-hipcc-static-problem -f Dockerfile.txt .
    docker run --rm -i -t debian-hipcc-static-problem




---

## 评论 (4 条)

### 评论 #1 — JustinTArthur (2020-08-11T23:42:37Z)

cc'ing @mangupta in case they have any ideas.

---

### 评论 #2 — ROCmSupport (2020-12-16T10:33:20Z)

Thanks @JustinTArthur for reaching out.
I will pass this issue to our developers and share an update soon.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-01-05T04:05:50Z)

Hi @JustinTArthur 
Got update from developer that "Support for static mode was not part of ROCm 3.5".
Hence recommend to try with the latest ROCm 4.0 and verify.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-01-06T11:48:53Z)

Hi @JustinTArthur 
Verified the issue and its fixed and no more observed with ROCm 4.0.

taccuser@taccuser-SYS-4028GR-TR2:/tmp/square$ /opt/rocm/hip/bin/hipcc -use-staticlib square.hipref.cpp -o square.out
taccuser@taccuser-SYS-4028GR-TR2:/tmp/square$ ls
CMakeLists.txt  Makefile  README.md  square.cu  square.hipref.cpp  square.out
taccuser@taccuser-SYS-4028GR-TR2:/tmp/square$ ./square.out
info: running on device Vega 20
info: architecture on AMD GPU device is: gfx906
info: allocate host mem (  7.63 MB)
info: allocate device mem (  7.63 MB)
info: copy Host2Device
info: launch 'vector_square' kernel
info: copy Device2Host
info: check result
PASSED!
 

---
