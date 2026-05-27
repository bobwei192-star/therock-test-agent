# CMake ROC libraries include path issue

> **Issue #1636**
> **状态**: closed
> **创建时间**: 2021-12-11T18:32:11Z
> **更新时间**: 2024-02-21T23:18:01Z
> **关闭时间**: 2024-02-21T23:18:00Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1636

## 负责人

- pfultz2
- lawruble13
- dennyiriawan
- TorreZuk
- saadrahim
- eidenyoshida
- frepaul

## 描述

hipblas, hipsparse, rocblas, rocsolver, rocprim, rocthrust all have a similar pattern.
hip runtime library is the only one get this right.

roc::hipblas target INTERFACE_INCLUDE_PATH is `/opt/rocm-4.5.0/include`
This is OK for people who only use ROCM installation but really bad for development.
I'm currently using AOMP which provides Clang and HIP but not hipblas.
Pulling `/opt/rocm-4.5.0/include` just pollutes all my include paths.

`/opt/rocm-4.5.0/lib/cmake/hipblas/hipblas-targets.cmake` has the following line.
```
# Compute the installation prefix relative to this file.
get_filename_component(_IMPORT_PREFIX "${CMAKE_CURRENT_LIST_FILE}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
```
It goes four level up to get the ROCM root.

Instead the HIP runtime library got this right. In ``
```
get_filename_component(_DIR "${CMAKE_CURRENT_LIST_DIR}" REALPATH)
get_filename_component(_IMPORT_PREFIX "${_DIR}/../../../" REALPATH)
```
so use REALPATH to resolve softlinks and use three level up to locate the HIP root directory instead of the ROC directory.

It is better to have all the affected libraries to adopt the same scheme and get contained in its own folder not pulling the ROCM folder. This should help composability.


---

## 评论 (17 条)

### 评论 #1 — ROCmSupport (2021-12-20T09:22:27Z)

Hi @ye-luo 
Thanks for reaching out. I certainly understood the problem.
I will ask to developer to look into this request and will share an update once I receive.
Thank you.

---

### 评论 #2 — saadrahim (2022-06-20T22:18:45Z)

Hi @ye-luo,
I've reached out to the libraries team and other cmake maintainers who can help with this issue. I hope to provide an update this Friday on the steps we want to take to address this.

---

### 评论 #3 — saadrahim (2022-06-23T21:39:36Z)

How are you building rocm or using it? Can you describe your environment in more detail?

Do you receive any specific error messages?

There is insufficient information to understand your issues. Please help us get more clarity.



---

### 评论 #4 — ye-luo (2022-06-23T22:29:05Z)

OK still persist in rocm 5.1.0. No progress for half a year...
Use https://github.com/ye-luo/cmake_gpu in the test_rocm directory
```
$ mkdir build_rocm; cd build_rocm
$ cmake -DCMAKE_CXX_COMPILER=/opt/rocm-5.1.0/llvm/bin/amdclang++ -DCMAKE_HIP_COMPILER=/opt/rocm-5.1.0/llvm/bin/amdclang++ ..
...
hip runtime HIP_RUNTIME_INCLUDE_PATH = /opt/rocm-5.1.0/hip/include
### this is desired
...
hipblas INTERFACE_INCLUDE_PATH = /opt/rocm-5.1.0/include;/opt/rocm-5.1.0/include
### this is bad, prefer to see /opt/rocm-5.1.0/hipblas/include
```
It works but not in the desired way.

Then make the directory empty and try a different way. Hit another bug due to empty CLANGRT_BUILTINS
```
$ rm -rf build_rocm
$ mkdir build_rocm; cd build_rocm
$ cmake -DCMAKE_CXX_COMPILER=/opt/rocm-5.1.0/llvm/bin/amdclang++ -DCMAKE_HIP_COMPILER=/opt/rocm-5.1.0/llvm/bin/amdclang++ ..
$ cmake -DCMAKE_CXX_COMPILER=/opt/rocm-5.1.0/bin/amdclang++ -DCMAKE_HIP_COMPILER=/opt/rocm-5.1.0/bin/amdclang++ ..
-- The CXX compiler identification is Clang 14.0.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /opt/rocm-5.1.0/bin/amdclang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- The HIP compiler identification is Clang 14.0.0
-- Detecting HIP compiler ABI info
-- Detecting HIP compiler ABI info - failed
-- Check for working HIP compiler: /opt/rocm-5.1.0/bin/amdclang++
-- Check for working HIP compiler: /opt/rocm-5.1.0/bin/amdclang++ - broken
CMake Error at /soft/spack/opt/spack/linux-ubuntu20.04-zen2/gcc-9.4.0/cmake-3.22.4-6k2x53b2drzdsrfcjitm65uit5wjqx3w/share/cmake-3.22/Modules/CMakeTestHIPCompiler.cmake:65 (message):
  The HIP compiler

    "/opt/rocm-5.1.0/bin/amdclang++"

  is not able to compile a simple test program.

  It fails with the following output:

    Change Dir: /home/yeluo/opt/cmake_gpu/test_rocm/build_rocm/CMakeFiles/CMakeTmp
    
    Run Build Command(s):/usr/bin/make -f Makefile cmTC_56108/fast && /usr/bin/make  -f CMakeFiles/cmTC_56108.dir/build.make CMakeFiles/cmTC_56108.dir/build
    make[1]: Entering directory '/home/yeluo/opt/cmake_gpu/test_rocm/build_rocm/CMakeFiles/CMakeTmp'
    Building HIP object CMakeFiles/cmTC_56108.dir/testHIPCompiler.hip.o
    /opt/rocm-5.1.0/bin/amdclang++ -D__HIP_ROCclr__=1 -I/opt/rocm-5.1.0/hip/include -I/opt/rocm-5.1.0/include -isystem /opt/rocm-5.1.0/llvm/lib/clang/14.0.0 --cuda-host-only  --offload-arch=gfx906 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -o CMakeFiles/cmTC_56108.dir/testHIPCompiler.hip.o -x hip -c /home/yeluo/opt/cmake_gpu/test_rocm/build_rocm/CMakeFiles/CMakeTmp/testHIPCompiler.hip
    Linking HIP executable cmTC_56108
    /soft/spack/opt/spack/linux-ubuntu20.04-zen2/gcc-9.4.0/cmake-3.22.4-6k2x53b2drzdsrfcjitm65uit5wjqx3w/bin/cmake -E cmake_link_script CMakeFiles/cmTC_56108.dir/link.txt --verbose=1
    /opt/rocm-5.1.0/bin/amdclang++  --cuda-host-only  --offload-arch=gfx906 --hip-link CMakeFiles/cmTC_56108.dir/testHIPCompiler.hip.o -o cmTC_56108  /opt/rocm-5.1.0/lib/libamdhip64.so.5.1.50100 -lCLANGRT_BUILTINS-NOTFOUND 
    ld.lld: error: unable to find library -lCLANGRT_BUILTINS-NOTFOUND
    clang-14: error: linker command failed with exit code 1 (use -v to see invocation)
    make[1]: *** [CMakeFiles/cmTC_56108.dir/build.make:100: cmTC_56108] Error 1
    make[1]: Leaving directory '/home/yeluo/opt/cmake_gpu/test_rocm/build_rocm/CMakeFiles/CMakeTmp'
    make: *** [Makefile:127: cmTC_56108/fast] Error 2
    
    

  

  CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt:4 (enable_language)


-- Configuring incomplete, errors occurred!
See also "/home/yeluo/opt/cmake_gpu/test_rocm/build_rocm/CMakeFiles/CMakeOutput.log".
See also "/home/yeluo/opt/cmake_gpu/test_rocm/build_rocm/CMakeFiles/CMakeError.log".
```
Please make all the CMake in rocm robust. 
See this collection of issues https://github.com/RadeonOpenCompute/ROCm/issues/1259#issuecomment-991753189



---

### 评论 #5 — cgmb (2022-06-24T00:01:54Z)

> Use https://github.com/ye-luo/cmake_gpu in the test_rocm directory
> 
> ```
> $ mkdir build_rocm; cd build_rocm
> $ cmake -DCMAKE_CXX_COMPILER=/opt/rocm-5.1.0/llvm/bin/amdclang++ -DCMAKE_HIP_COMPILER=/opt/rocm-5.1.0/llvm/bin/amdclang++ ..
> ...
> hip runtime HIP_RUNTIME_INCLUDE_PATH = /opt/rocm-5.1.0/hip/include
> ### this is desired
> ...
> hipblas INTERFACE_INCLUDE_PATH = /opt/rocm-5.1.0/include;/opt/rocm-5.1.0/include
> ### this is bad, prefer to see /opt/rocm-5.1.0/hipblas/include
> ```

I don't understand the problem. Why is it bad?

---

### 评论 #6 — ye-luo (2022-06-24T00:49:50Z)

Hipblas is a library not necessary to be installed inside rocm installation. It should be based on the install root of hipblas /opt/rocm-5.1.0/hipblas instead of rocm root /opt/rocm-5.1.0. So I build my own hipblas and install it in a different location, the include directory can be correctly set by CMake.

---

### 评论 #7 — cgmb (2022-06-24T03:18:31Z)

> It should be based on the install root of hipblas /opt/rocm-5.1.0/hipblas

It is based on the install root of hipblas. It's just that `/opt/rocm-5.1.0/hipblas` is not the hipblas install root. In the ROCm 5.1 binary release, the install root of hipblas is `/opt/rocm-5.1.0`.

### ROCm 5.1

    CMAKE_INSTALL_PREFIX=/opt/rocm-5.1.0
    CMAKE_INSTALL_INCLUDEDIR=hipblas/include
    CMAKE_INSTALL_LIBDIR=hipblas/lib

In the next release, the library directory will change.

### ROCm 5.2

    CMAKE_INSTALL_PREFIX=/opt/rocm-5.2.0
    CMAKE_INSTALL_INCLUDEDIR=include
    CMAKE_INSTALL_LIBDIR=lib



---

### 评论 #8 — saadrahim (2022-06-24T03:33:19Z)

> Hipblas is a library not necessary to be installed inside rocm installation. It should be based on the install root of hipblas /opt/rocm-5.1.0/hipblas instead of rocm root /opt/rocm-5.1.0. So I build my own hipblas and install it in a different location, the include directory can be correctly set by CMake.

hipBLAS is component that is a part of rocm. ROCm is moving towards unix/linux standard folder structure. We will no longer have specific folders for components that are part of rocm. The standard /bin, /lib(64), /share, and /include type of directories in `/opt/rocm-${VERSION}`,  where `${VERSION}` is the rocm version number, will contain files from all ROCm components. 

However, I am concerned about your statement 
_

> Pulling /opt/rocm-4.5.0/include just pollutes all my include paths.

_
There may be a separate issue that needs reporting.

---

### 评论 #9 — ye-luo (2022-06-24T03:55:55Z)

I cannot verify ROCm 5.2 since it yet to be released. However, in 5.1.
```
yeluo@epyc-server:/opt/rocm-5.1.0/hipblas/include$ ls -lrt
total 1416
-rw-r--r-- 1 1003 root 506683 Mar 21 16:16 hipblas_module.f90
-rw-r--r-- 1 1003 root 929992 Mar 21 16:16 hipblas.h
-rw-r--r-- 1 1003 root    548 Mar 21 17:35 hipblas-version.h
-rw-r--r-- 1 1003 root   1031 Mar 21 17:35 hipblas-export.h
yeluo@epyc-server:/opt/rocm-5.1.0/include$ ls -lrt hipblas.h
lrwxrwxrwx 1 1003 root 28 Mar 21 17:35 hipblas.h -> ../hipblas/include/hipblas.h
```
It seems that `/opt/rocm-5.1.0/hipblas/include` is the actual hipblas include install path. `/opt/rocm-5.1.0/include/hipblas.h` seems being added after install for convenience. No?

Consider 5.2 file folder layout has been changed, I will need to re-evaluate the situation.

---

### 评论 #10 — cgmb (2022-06-24T04:44:28Z)

Sorry, I did get the include directory wrong for ROCm 5.1. I've edited my post to also add the hipblas prefix to the includedir. I'm perhaps oversimplifying, as well, because the includedir and the libdir were not actually the standard cmake variables. That hipblas prefix was being added [in rocm-cmake](https://github.com/RadeonOpenCompute/rocm-cmake/blob/rocm-5.1.0/share/rocm/cmake/ROCMInstallTargets.cmake#L87-L89).

In ROCm 5.2 the libraries no longer use the `PREFIX` option in rocm-cmake, so the libdir and includedir will no longer be prefixed by the package name.

In ROCm 5.3, the `CMAKE_INSTALL_INCLUDEDIR` and `CMAKE_INSTALL_LIBDIR` will be customizable at configure time when building the libraries from source.

---

### 评论 #11 — ye-luo (2022-06-29T15:12:48Z)

@cgmb This remains super confusing what is going on with 5.2

I noticed
```
/opt/rocm-5.2.0/include/hipblas.h
```
gcc prints ": warning : This file is deprecated. Use the header file from /opt/rocm-5.2.0/include/hipblas/hipblas.h by using #include <hipblas/hipblas.h>" but ROCm clang hides this message. It is bad to have non-uniform behavior.

Then it redirects to
```
/opt/rocm-5.2.0/include/hipblas/hipblas.h
```

However if my source code is changed to `#include <hipblas/hipblas.h>`
I cannot not use the following
```
yeluo@epyc-server:/opt/rocm-5.2.0$ ls hipblas/include/
hipblas-export.h  hipblas.h  hipblas_module.f90  hipblas-version.h
```
If such files exist in the release distribution, make them work or delete.

---

### 评论 #12 — ye-luo (2022-06-29T15:13:42Z)

@saadrahim besides library issue, I still struggle with the HIP as a CMake language https://github.com/ROCm-Developer-Tools/HIP/pull/2776

---

### 评论 #13 — cgmb (2022-07-01T17:05:22Z)

> I noticed
> 
> ```
> /opt/rocm-5.2.0/include/hipblas.h
> ```
> 
> gcc prints ": warning : This file is deprecated. Use the header file from /opt/rocm-5.2.0/include/hipblas/hipblas.h by using #include <hipblas/hipblas.h>" but ROCm clang hides this message. It is bad to have non-uniform behavior.

Agreed. [I pointed that out myself](https://github.com/RadeonOpenCompute/rocm-cmake/pull/89#issuecomment-1106807377), but I don't know how to make it consistent across all compilers. In any case, this should be resolved in ROCm 5.4 when it gets promoted from a message to an actual warning.

> However if my source code is changed to #include <hipblas/hipblas.h>
> I cannot not use the following
> 
> yeluo@epyc-server:/opt/rocm-5.2.0$ ls hipblas/include/
> hipblas-export.h  hipblas.h  hipblas_module.f90  hipblas-version.h
> 
> If such files exist in the release distribution, make them work or delete.

The files in `/opt/rocm/hipblas/include` exist only for backwards-compatibility and are planned to be deleted a few releases after the deprecation message had been upgraded to a warning.

---

### 评论 #14 — cgmb (2022-07-01T17:56:05Z)

> roc::hipblas target INTERFACE_INCLUDE_PATH is `/opt/rocm-4.5.0/include`
> This is OK for people who only use ROCM installation but really bad for development.
> I'm currently using AOMP which provides Clang and HIP but not hipblas.
> Pulling `/opt/rocm-4.5.0/include` just pollutes all my include paths.

After carefully reading through this thread again, I finally understand your problem. I'm sorry that it was not fixed in ROCm 5.2. The ability to swap out libraries in the manner you're describing does sound handy (though probably only useful to advanced users).

With that said, there are some workarounds (e.g., replace hip with a dummy package created by `equivs`). Though, the most practical option is probably to build the libraries you need from source on top of AOMP. That will give you complete control over the layout.

---

### 评论 #15 — TorreZuk (2022-07-05T14:37:40Z)

> Pulling /opt/rocm-4.5.0/include just pollutes all my include paths.

I understand your complaint, at a couple meetings I tried unsuccessfully to discourage the switching to #include <library/libIncludeFile.h> style in the new include/ root to allow simple include path switching.   If you want to override an installed search path with a local one an -isystem prefixed to your compiler flags should work.  

It may be too late for us to switch back to this style :
hipblas INTERFACE_INCLUDE_PATH = /opt/rocm-5.1.0/include/hipblas
#include <libIncludeFile.h>

I would suggest you make new issues for non-include path ones like the compiler detection, or deprecations etc. so include paths can be the focus in this one.   If you still can't use hipBLAS for your use case you can also make a hipblas ticket.


---

### 评论 #16 — abhimeda (2024-02-21T19:26:40Z)

@ye-luo Hi is this resolved on the most recent ROCm? If so can we close this ticket?


---

### 评论 #17 — ye-luo (2024-02-21T23:18:00Z)

I no more have issues with recent ROCm releases.

---
