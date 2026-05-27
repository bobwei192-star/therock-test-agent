# ROCclr build issue, make failed.

> **Issue #1358**
> **状态**: closed
> **创建时间**: 2021-01-12T07:14:15Z
> **更新时间**: 2021-02-08T10:14:46Z
> **关闭时间**: 2021-02-08T10:14:46Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1358

## 描述

I filed this bug here since there seems no ROCclr project on its own.
I downloaded source for 4.0.0 but ROCclr build problem.

I built and installed llvm, ROCm-Compiler-support and ROCm-device-libs ok as prereq.

But build instruction for ROCclr as follows:

### Set the environment variables

```bash
export ROCclr_DIR="$(readlink -f ROCclr)"
export OPENCL_DIR="$(readlink -f ROCm-OpenCL-Runtime)"
```

### Build ROCclr
Here is command to build ROCclr:

```bash
cd "$ROCclr_DIR"
mkdir -p build; cd build
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
make -j$(nproc)
```

It appears settings OPENCL_DIR is necessary.  So i set the env variable and make sure it is ok (below).
But "make" command after cmake resulted in following error:

oot@sriov-guest:~/ROCm/ROCclr/build# env | grep ROCclr
OPENCL_DIR=/root/ROCm/ROCclr/build/ROCm-OpenCL-Runtime
OLDPWD=/root/ROCm/ROCclr
PWD=/root/ROCm/ROCclr/build
ROCclr_DIR=/root/ROCm/ROCclr/build/ROCclr

"root@sriov-guest:~/ROCm/ROCclr/build# make
[  2%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o
In file included from /root/ROCm/ROCclr/device/rocm/roccounters.hpp:24:0,
                 from /root/ROCm/ROCclr/device/rocm/roccounters.cpp:21:
/root/ROCm/ROCclr/include/top.hpp:36:10: fatal error: CL/opencl.h: No such file or directory
 #include "CL/opencl.h"
          ^~~~~~~~~~~~~
compilation terminated.
device/rocm/CMakeFiles/oclrocm.dir/build.make:62: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o' failed
make[2]: *** [device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o] Error 1
CMakeFiles/Makefile2:122: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/all' failed
make[1]: *** [device/rocm/CMakeFiles/oclrocm.dir/all] Error 2
Makefile:129: recipe for target 'all' failed
make: *** [all] Error 2
"

I dont think building ROCm-OpenCL-Runtime is prereq because 1. it does not say so in the ROCclr's readme and ROCm-OpenCL-Runtime build readme specified ROCclr build is a prereq.


---

## 评论 (9 条)

### 评论 #1 — xuhuisheng (2021-01-12T07:21:53Z)

`git clone https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime`
and set its dir to OPENCL_DIR

---

### 评论 #2 — ROCmSupport (2021-01-12T07:23:19Z)

Thanks @gggh000 for reaching us.
Request you to install/use OpenCL RT path to solve the issue.

---

### 评论 #3 — ROCmSupport (2021-01-12T07:53:51Z)

And also, we are working on providing proper build instructions for complete ROCm. Please track #1188 closely for the updates.

---

### 评论 #4 — gggh000 (2021-01-12T18:47:10Z)

> `git clone https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime`
> and set its dir to OPENCL_DIR

I dont see why it would work. I already pointed to existing directory which downloaded the source.

---

### 评论 #5 — gggh000 (2021-01-12T18:47:39Z)

> Request you to install/use OpenCL RT path to solve the issue.

How do i do that? I dont know what OpenCL RT and how to get it and install. 

---

### 评论 #6 — xuhuisheng (2021-01-15T08:36:58Z)

Didn't have to build ROCm-OpenCL-Runtime first, ROCclr only need OpenCL headers.

My environment is Ubuntu-20.04.1

**env|grep ROCm**

```
work@00923371e74e:~/ROCm/ROCclr/build$ env|grep ROCm  
PWD=/home/work/ROCm/ROCclr/build
OPENCL_DIR=/home/work/ROCm/ROCm-OpenCL-Runtime/
ROCclr_DIR=/home/work/ROCm/ROCclr/
OLDPWD=/home/work/ROCm/ROCclr

```

**cmake**

```
work@00923371e74e:~/ROCm/ROCclr/build$ cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
-- The C compiler identification is GNU 9.3.0
-- The CXX compiler identification is GNU 9.3.0
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
-- Code Object Manager found at /opt/rocm/lib/cmake/amd_comgr.
-- HSA Runtime found at /opt/rocm/lib/cmake/hsa-runtime64.
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Found: /usr/lib/x86_64-linux-gnu/libnuma.so
-- Configuring done
-- Generating done
-- Build files have been written to: /home/work/ROCm/ROCclr/build

```

then **make**

```
work@00923371e74e:~/ROCm/ROCclr/build$ make
Scanning dependencies of target oclrocm
[  2%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o
[  4%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocprintf.cpp.o
[  6%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocprogram.cpp.o
[  8%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocmemory.cpp.o
[ 10%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocdevice.cpp.o
[ 13%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocblit.cpp.o
[ 15%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rockernel.cpp.o
[ 17%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocvirtual.cpp.o
[ 19%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocglinterop.cpp.o
[ 21%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocappprofile.cpp.o
[ 23%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocsettings.cpp.o
[ 26%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocschedcl.cpp.o
[ 28%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rochostcall.cpp.o
[ 28%] Built target oclrocm
Scanning dependencies of target amdrocclr_static
[ 30%] Building CXX object CMakeFiles/amdrocclr_static.dir/thread/thread.cpp.o
[ 32%] Building CXX object CMakeFiles/amdrocclr_static.dir/thread/monitor.cpp.o
[ 34%] Building CXX object CMakeFiles/amdrocclr_static.dir/thread/semaphore.cpp.o
[ 36%] Building CXX object CMakeFiles/amdrocclr_static.dir/utils/flags.cpp.o
[ 39%] Building CXX object CMakeFiles/amdrocclr_static.dir/utils/debug.cpp.o
[ 41%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/appprofile.cpp.o
[ 43%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/device.cpp.o
[ 45%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/hwdebug.cpp.o
[ 47%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/blitcl.cpp.o
[ 50%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/blit.cpp.o
[ 52%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/devkernel.cpp.o
[ 54%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/devwavelimiter.cpp.o
[ 56%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/devprogram.cpp.o
[ 58%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/devhcprintf.cpp.o
[ 60%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/devhcmessages.cpp.o
[ 63%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/activity.cpp.o
[ 65%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/kernel.cpp.o
[ 67%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/context.cpp.o
[ 69%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/command.cpp.o
[ 71%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/ndrange.cpp.o
[ 73%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/runtime.cpp.o
[ 76%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/memory.cpp.o
[ 78%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/program.cpp.o
[ 80%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/commandqueue.cpp.o
[ 82%] Building CXX object CMakeFiles/amdrocclr_static.dir/platform/agent.cpp.o
[ 84%] Building CXX object CMakeFiles/amdrocclr_static.dir/os/os_win32.cpp.o
[ 86%] Building CXX object CMakeFiles/amdrocclr_static.dir/os/alloc.cpp.o
[ 89%] Building CXX object CMakeFiles/amdrocclr_static.dir/os/os.cpp.o
[ 91%] Building CXX object CMakeFiles/amdrocclr_static.dir/os/os_posix.cpp.o
[ 93%] Building CXX object CMakeFiles/amdrocclr_static.dir/compiler/lib/utils/options.cpp.o
[ 95%] Building CXX object CMakeFiles/amdrocclr_static.dir/elf/elf.cpp.o
[ 97%] Building CXX object CMakeFiles/amdrocclr_static.dir/device/comgrctx.cpp.o
[100%] Linking CXX static library libamdrocclr_static.a
[100%] Built target amdrocclr_static
work@00923371e74e:~/ROCm/ROCclr/build$ 

```

run `make -d`, it shows that found opencl.h from opencl2.2

```
      Considering target file '/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers/opencl2.2/CL/opencl.h'.
       Looking for an implicit rule for '/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers/opencl2.2/CL/opencl.h'.

```

We can find `opencl2.2` from CMakeLists.txt from ROCclr.
<https://github.com/ROCm-Developer-Tools/ROCclr/blob/main/device/rocm/CMakeLists.txt#L24>

```
target_include_directories(oclrocm
  PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
    # GL and EGL headers
    $<BUILD_INTERFACE:${OPENCL_DIR}/khronos/headers>
    $<BUILD_INTERFACE:${OPENCL_DIR}/khronos/headers/opencl2.2>
    $<TARGET_PROPERTY:amd_comgr,INTERFACE_INCLUDE_DIRECTORIES>

```

after cmake, `find . -type f -print|xargs grep opencl`

```
work@00923371e74e:~/ROCm/ROCclr/build$ find . -type f -print|xargs grep opencl
./CMakeFiles/amdrocclr_static.dir/DependInfo.cmake:  "/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers/opencl2.2"
./CMakeFiles/amdrocclr_static.dir/flags.make:CXX_INCLUDES = -I/home/work/ROCm/ROCclr -I/home/work/ROCm/ROCclr/include -I/home/work/ROCm/ROCclr/device/rocm -I/home/work/ROCm/ROCclr/compiler/lib/include -I/home/work/ROCm/ROCclr/compiler/lib -I/home/work/ROCm/ROCclr/compiler/lib/backends/common -I/home/work/ROCm/ROCclr/elf -I/home/work/ROCm/ROCm-OpenCL-Runtime -I/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers -I/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers/opencl2.2 -isystem /opt/rocm/include -isystem /opt/rocm/include/hsa 
./device/rocm/CMakeFiles/oclrocm.dir/DependInfo.cmake:  "/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers/opencl2.2"
./device/rocm/CMakeFiles/oclrocm.dir/flags.make:CXX_INCLUDES = -I/home/work/ROCm/ROCclr -I/home/work/ROCm/ROCclr/include -I/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers -I/home/work/ROCm/ROCm-OpenCL-Runtime/khronos/headers/opencl2.2 -I/opt/rocm/include -I/home/work/ROCm/ROCm-OpenCL-Runtime -I/home/work/ROCm/ROCclr/compiler/lib -I/home/work/ROCm/ROCclr/compiler/lib/include -I/home/work/ROCm/ROCclr/compiler/lib/backends/common -I/home/work/ROCm/ROCclr/elf -I/home/work/ROCm/ROCclr/build/device/rocm -I/opt/rocm/include/hsa 
./lib/cmake/rocclr/rocclr-targets.cmake:  INTERFACE_INCLUDE_DIRECTORIES "/home/work/ROCm/ROCclr;/home/work/ROCm/ROCclr/include;/home/work/ROCm/ROCclr/device/rocm;/home/work/ROCm/ROCclr/compiler/lib/include;/home/work/ROCm/ROCclr/compiler/lib;/home/work/ROCm/ROCclr/compiler/lib/backends/common;/home/work/ROCm/ROCclr/elf;/home/work/ROCm/ROCm-OpenCL-Runtime/;/home/work/ROCm/ROCm-OpenCL-Runtime//khronos/headers;/home/work/ROCm/ROCm-OpenCL-Runtime//khronos/headers/opencl2.2;\$<TARGET_PROPERTY:amd_comgr,INTERFACE_INCLUDE_DIRECTORIES>"

```


---

### 评论 #7 — ROCmSupport (2021-01-18T09:26:18Z)

@gggh000,
     I hope the issue is resolved with the suggested package.
     kindly let us know if you are still facing this problem.

---

### 评论 #8 — ROCmSupport (2021-01-27T07:15:55Z)

Hi @gggh000 
Please share an update on the issue. Will close it, if you are not able to reproduce anymore.
Thank you.

---

### 评论 #9 — ROCmSupport (2021-02-08T10:14:46Z)

Hi @gggh000 
Closing this as there is no response from you for the last 3 to 4 weeks.
Assuming that issue is resolved.
Request you to open a new issue, if you find any.
Thank you.

---
