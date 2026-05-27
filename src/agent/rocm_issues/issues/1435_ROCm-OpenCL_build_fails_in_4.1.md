# ROCm-OpenCL build fails in 4.1

> **Issue #1435**
> **状态**: closed
> **创建时间**: 2021-03-31T04:32:25Z
> **更新时间**: 2021-04-07T06:40:30Z
> **关闭时间**: 2021-04-06T19:54:39Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1435

## 描述

**used to build in previous version but appears to have broken in 4.1:


root@guest:~/ROCm/ROCm-OpenCL-Runtime# nano -w README.md
root@guest:~/ROCm/ROCm-OpenCL-Runtime# cd build
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# make
[  9%] Built target OpenCL
[ 12%] Built target IcdLog
[ 21%] Built target OpenCLDriverStub
Scanning dependencies of target icd_loader_test
[ 25%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_kernel.c.o
[ 28%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/main.c.o
[ 28%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_platforms.c.o
[ 31%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/icd_test_match.c.o
[ 31%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_program_objects.c.o
[ 34%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_sampler_objects.c.o
[ 34%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_buffer_object.c.o
[ 37%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_cl_runtime.c.o
[ 37%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/callbacks.c.o
[ 40%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_create_calls.c.o
[ 40%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_clgl.c.o
[ 43%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_image_objects.c.o
[ 43%] Linking C executable icd_loader_test
[ 43%] Built target icd_loader_test
[ 43%] Building CXX object amdocl/CMakeFiles/amdocl64.dir/cl_memobj.cpp.o
In file included from /root/ROCm/ROCm-OpenCL-Runtime/amdocl/cl_memobj.cpp:21:0:
/root/ROCm/ROCm-OpenCL-Runtime/amdocl/cl_common.hpp:31:10: fatal error: top.hpp: No such file or directory
 #include "top.hpp"
          ^~~~~~~~~
compilation terminated.
amdocl/CMakeFiles/amdocl64.dir/build.make:62: recipe for target 'amdocl/CMakeFiles/amdocl64.dir/cl_memobj.cpp.o' failed
make[2]: *** [amdocl/CMakeFiles/amdocl64.dir/cl_memobj.cpp.o] Error 1
CMakeFiles/Makefile2:1453: recipe for target 'amdocl/CMakeFiles/amdocl64.dir/all' failed
make[1]: *** [amdocl/CMakeFiles/amdocl64.dir/all] Error 2
Makefile:129: recipe for target 'all' failed
make: *** [all] Error 2
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# git remote -v
roc-github      http://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime (fetch)
roc-github      http://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime (push)
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# git branch
* (no branch)
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# git branch -r
  m/roc-4.1.x -> rocm-4.1.0
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build#**


---

## 评论 (9 条)

### 评论 #1 — gggh000 (2021-03-31T04:37:12Z)

Looking back at 4.0, I can see ROCm-opencl-runtime builds OK. From readme, it requires ROCclr installation first.
In 4.0, ROCclr build OK, however, the ROCclr build fails on 4.1 with following(  below ). Therefore, it may be possible, ROCclr is the one that is broken. Compile is broken asking for opencl.h therefore it seems sort of chicken egg problem or circular dependency problem going on here. 


root@guest:~/ROCm/ROCclr/build# !206
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
-- Code Object Manager found at /opt/rocm/lib/cmake/amd_comgr.
-- HSA Runtime found at /opt/rocm/lib/cmake/hsa-runtime64.
-- Opencl found at /opt/rocm/opencl/include.
-- Found: /usr/lib/x86_64-linux-gnu/libnuma.so
-- Configuring done
-- Generating done
-- Build files have been written to: /root/ROCm/ROCclr/build
root@guest:~/ROCm/ROCclr/build# make
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
root@guest:~/ROCm/ROCclr/build#


---

### 评论 #2 — ROCmSupport (2021-03-31T07:23:26Z)

Hi @gggh000 
Thanks for reaching out.
I am not able to reproduce the problem with ROCm 4.1.

_Exact steps I followed:_
Installed rocm-dkms.
git clone https://github.com/ROCm-Developer-Tools/ROCclr.git
git clone -b master-next https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git
export ROCclr_DIR="$(readlink -f ROCclr)"
export OPENCL_DIR="$(readlink -f ROCm-OpenCL-Runtime)"
cd "$ROCclr_DIR"
mkdir -p build; cd build
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
make -j$(nproc)

---

### 评论 #3 — gggh000 (2021-03-31T16:52:46Z)

I followd your steps and it is same, failing. What is your output of "git branch -r" from rocclr directory?

[  8%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/rocmemory.cpp.o
In file included from /root/ROCm/ROCclr/device/rocm/roccounters.hpp:24:0,
                 from /root/ROCm/ROCclr/device/rocm/roccounters.cpp:21:
/root/ROCm/ROCclr/include/top.hpp:36:10: fatal error: CL/opencl.h: No such file or directory
 #include "CL/opencl.h"
          ^~~~~~~~~~~~~
In file included from /root/ROCm/ROCclr/device/rocm/rocprintf.cpp:21:0:
/root/ROCm/ROCclr/include/top.hpp:36:10: fatal error: CL/opencl.h: No such file or directory
 #include "CL/opencl.h"
          ^~~~~~~~~~~~~
compilation terminated.
compilation terminated.
device/rocm/CMakeFiles/oclrocm.dir/build.make:62: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o' failed
make[2]: *** [device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
device/rocm/CMakeFiles/oclrocm.dir/build.make:75: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/rocprintf.cpp.o' failed
make[2]: *** [device/rocm/CMakeFiles/oclrocm.dir/rocprintf.cpp.o] Error 1
/root/ROCm/ROCclr/device/rocm/rocmemory.cpp:27:10: fatal error: CL/cl_ext.h: No such file or directory
 #include "CL/cl_ext.h"
          ^~~~~~~~~~~~~
compilation terminated.
device/rocm/CMakeFiles/oclrocm.dir/build.make:101: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/rocmemory.cpp.o' failed
make[2]: *** [device/rocm/CMakeFiles/oclrocm.dir/rocmemory.cpp.o] Error 1
In file included from /root/ROCm/ROCclr/device/rocm/rocdevice.hpp:25:0,
                 from /root/ROCm/ROCclr/device/rocm/rocprogram.hpp:30,
                 from /root/ROCm/ROCclr/device/rocm/rocprogram.cpp:23:
/root/ROCm/ROCclr/include/top.hpp:36:10: fatal error: CL/opencl.h: No such file or directory
 #include "CL/opencl.h"
          ^~~~~~~~~~~~~
compilation terminated.
device/rocm/CMakeFiles/oclrocm.dir/build.make:88: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/rocprogram.cpp.o' failed
make[2]: *** [device/rocm/CMakeFiles/oclrocm.dir/rocprogram.cpp.o] Error 1
CMakeFiles/Makefile2:122: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/all' failed
make[1]: *** [device/rocm/CMakeFiles/oclrocm.dir/all] Error 2
Makefile:129: recipe for target 'all' failed
make: *** [all] Error 2
root@sriov-guest:~/ROCm/ROCclr/build#
root@sriov-guest:~/ROCm/ROCclr/build# ls -l /opt/^C
root@sriov-guest:~/ROCm/ROCclr/build# dpkg -l | grep rocm-dkms
ii  rocm-dkms                                  4.1.0.40100-26                                   amd64        Radeon Open Compute (ROCm) Runtime software stack
root@sriov-guest:~/ROCm/ROCclr/build#


---

### 评论 #4 — gggh000 (2021-03-31T16:54:09Z)

remember, you want to do this on clean system, if you did extra steps prior to this day on machine and being used a while as a build machine, steps could be omitted. 

---

### 评论 #5 — ROCmSupport (2021-04-01T05:20:32Z)

Hi @gggh000 
OpenCL headers are not detected and I feel the paths are wrong.

Can you please do both of the below steps in the same directory path.
For example:
cd ~
git clone https://github.com/ROCm-Developer-Tools/ROCclr.git
git clone -b master-next https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git

Looks like you might have pulled _ROCm-OpenCL-Runtime_ inside _ROCclr_, which is wrong.


I tried on a fresh and clean system, not able to reproduce the problem when I followed the steps mentioned in the above comment blindly.
I just copied and pasted and no issues observed.
Thank you.

---

### 评论 #6 — gggh000 (2021-04-05T19:22:39Z)

I did not pulled ROCm-OpenCL-Runtime inside ROCclr, not reason to,
On 4.1, I am consistently getting this error. 


---

### 评论 #7 — ROCmSupport (2021-04-06T06:26:50Z)

Hi @gggh000 
OpenCL headers are not detected in your machine.

Can you please try the below steps, exactly, on the same and different machine and share me an update.

Install ROCm 4.1 as _sudo apt install rocm-dkms_
git clone https://github.com/ROCm-Developer-Tools/ROCclr.git
git clone -b master-next https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git
export ROCclr_DIR="$(readlink -f ROCclr)"
export OPENCL_DIR="$(readlink -f ROCm-OpenCL-Runtime)"
cd "$ROCclr_DIR"
mkdir -p build; cd build
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
make -j$(nproc)

---

### 评论 #8 — gggh000 (2021-04-06T19:54:35Z)

I think I might have set the path wrong, I can build ok now, I thought I closed this issue yesterday. 

---

### 评论 #9 — ROCmSupport (2021-04-07T06:40:29Z)

Thanks @gggh000 for the closure.
Happy to see that issue is fixed at your end.
Thank you.

---
