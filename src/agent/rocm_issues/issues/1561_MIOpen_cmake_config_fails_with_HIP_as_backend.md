# MIOpen cmake config fails with HIP as backend

> **Issue #1561**
> **状态**: closed
> **创建时间**: 2021-08-21T03:54:45Z
> **更新时间**: 2021-08-22T19:08:23Z
> **关闭时间**: 2021-08-22T19:08:23Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1561

## 描述

It works with OpenCL as back end but when HIP, it errors out:
Ubuntu1804
ROCm4.3
Use instruction to build the MIOpen. 

```
root@u1804:~/ROCm-4.3/MIOpen/build# cmake -DMIOPEN_BACKEND=HIP ..
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1")
-- Checking for module 'sqlite3'
--   Found sqlite3, version 3.22.0
-- Found BZip2: /usr/lib/x86_64-linux-gnu/libbz2.so (found version "1.0.6")
-- Looking for BZ2_bzCompressInit
-- Looking for BZ2_bzCompressInit - found
-- Performing Test HAS_HIP
-- Performing Test HAS_HIP - Failed
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- ROCclr at /opt/rocm/lib/cmake/rocclr
-- hip::amdhip64 is SHARED_LIBRARY
-- Build with HIP 4.3.21300
-- Hip compiler flags:  -xhip    -isystem /opt/rocm-4.3.0/hip/../include -isystem /opt/rocm/llvm/lib/clang/13.0.0/include/..  -D__HIP_PLATFORM_HCC__=1 -D__HIP_PLATFORM_AMD__=1  -isystem /opt/rocm-4.3.0/hip/include -isystem /opt/rocm/include -L"/opt/rocm/llvm/lib/clang/13.0.0/include/../lib/linux" -lclang_rt.builtins-x86_64 --hip-link    -L"/opt/rocm/llvm/lib/clang/13.0.0/include/../lib/linux" -lclang_rt.builtins-x86_64
-- hip compiler: /opt/rocm/bin/clang-ocl
-- ROCclr at /opt/rocm/lib/cmake/rocclr
-- hip::amdhip64 is SHARED_LIBRARY
-- Build with rocblas
-- HIP backend selected.
-- clang-offload-bundler not found
CMake Error at CMakeLists.txt:312 (message):
  extractkernel not found


-- Configuring incomplete, errors occurred!
See also "/root/ROCm-4.3/MIOpen/build/CMakeFiles/CMakeOutput.log".
See also "/root/ROCm-4.3/MIOpen/build/CMakeFiles/CMakeError.log".
root@u1804:~/ROCm-4.3/MIOpen/build# cmake -DMIOPEN_BACKEND=HIP ..^C
root@u1804:~/ROCm-4.3/MIOpen/build# nano -w ../../build-rocm.sh
root@u1804:~/ROCm-4.3/MIOpen/build# cmake .. -DMIOPEN_BACKEND=HIP
-- ROCclr at /opt/rocm/lib/cmake/rocclr
-- hip::amdhip64 is SHARED_LIBRARY
-- Build with HIP 4.3.21300
-- Hip compiler flags:  -xhip    -isystem /opt/rocm-4.3.0/hip/../include -isystem /opt/rocm/llvm/lib/clang/13.0.0/include/..  -D__HIP_PLATFORM_HCC__=1 -D__HIP_PLATFORM_AMD__=1  -isystem /opt/rocm-4.3.0/hip/include -isystem /opt/rocm/include -L"/opt/rocm/llvm/lib/clang/13.0.0/include/../lib/linux" -lclang_rt.builtins-x86_64 --hip-link    -L"/opt/rocm/llvm/lib/clang/13.0.0/include/../lib/linux" -lclang_rt.builtins-x86_64
-- hip compiler: /opt/rocm/bin/clang-ocl
-- ROCclr at /opt/rocm/lib/cmake/rocclr
-- hip::amdhip64 is SHARED_LIBRARY
-- Build with rocblas
-- HIP backend selected.
-- clang-offload-bundler not found
CMake Error at CMakeLists.txt:312 (message):
  extractkernel not found


-- Configuring incomplete, errors occurred!

```

---

## 评论 (1 条)

### 评论 #1 — gggh000 (2021-08-22T19:08:20Z)

Worked with fresh installation.

---
