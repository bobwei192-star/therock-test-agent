# CMake compilation problem with hipblas example on a Nvidia platform.

> **Issue #2019**
> **状态**: closed
> **创建时间**: 2023-04-04T13:13:34Z
> **更新时间**: 2023-04-06T09:43:07Z
> **关闭时间**: 2023-04-06T09:43:07Z
> **作者**: wme7
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2019

## 描述

I'm on an Nvidia plarform and I'm interested in developing a cross platform application. Following the this [instructions](https://hipblas.readthedocs.io/en/latest/install.html#), I  downloaded the hipblas git-repo and installed on the same path of my hip instalaltion (/opt/rocm/hipblas). I simply used `/install.sh -i --cuda`. 

I'm trying to build the [SGEMM](https://github.com/ROCmSoftwarePlatform/hipBLAS/blob/develop/clients/samples/example_sgemm.cpp) example in the library using CMake 3.16. (I'm able to build hipified versions of cuda examples using `hipcc` compiler v5.4.2)

```cmake
cmake_minimum_required(VERSION 3.16)

project(myPrototypes VERSION 1.0.0 LANGUAGES CXX) 

# Find HIP
find_package(HIP REQUIRED)
find_package(HIPBLAS REQUIRED)

# Set compilation standard
set(CMAKE_HIP_STANDARD 17)
set(CMAKE_HIP_STANDARD_REQUIRED ON)
# set(CMAKE_HIP_ARCHITECTURES "XX;XX")

# Test programs
add_executable(hipblas_sgemm.run hipblas_sgemm.cpp)
target_link_libraries(hipblas_sgemm.run PRIVATE roc::hipblas)
```
I call CMake using bash script that reads:
```bash
#!bin/sh
cmake \
  -DCMAKE_MODULE_PATH=/opt/rocm/hip/cmake \
  -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  ..

```
.. using it I build my example as
```bash
$ source ../compileScripts/cmake_cxx_hip.sh 
-- The CXX compiler identification is GNU 8.5.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /opt/rocm/bin/hipcc - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found HIP: /opt/rocm-5.4.0/hip (found version "5.4.22801-aaa1e3d8") 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mdiaz/Depots/LinearAlgebraPrototypes/hipblas_snippets/build
```
however, when I proceed to `make` my sample-app, I get the following output:
```
$ make
[ 50%] Building CXX object CMakeFiles/hipblas_sgemm.run.dir/hipblas_sgemm.cpp.o
[100%] Linking CXX executable hipblas_sgemm.run
nvcc fatal   : Don't know what to do with '/opt/rocm-5.4.0/lib/libhipblas.so.0.1'
make[2]: *** [CMakeFiles/hipblas_sgemm.run.dir/build.make:98: hipblas_sgemm.run] Error 1
make[1]: *** [CMakeFiles/Makefile2:83: CMakeFiles/hipblas_sgemm.run.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```

I'm not sure if this is the expected behavior, or I stumbled on a compilation bug or, I probably, I'm missing something on my CMake configuration. 

Can anyone help me figure out?.

best regards,
- M

---

## 评论 (1 条)

### 评论 #1 — wme7 (2023-04-06T09:42:43Z)

A temporal solution can be found in this post: https://www.reddit.com/r/ROCm/comments/12bmygw/how_do_you_build_apps_with_hipblas_using_cmake/

---
