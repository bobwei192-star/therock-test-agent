# ARM AArch64: cannot find -lhsakmt on AArch64 based System via KVM

> **Issue #187**
> **状态**: closed
> **创建时间**: 2017-08-24T08:48:54Z
> **更新时间**: 2018-06-03T15:00:09Z
> **关闭时间**: 2018-06-03T15:00:09Z
> **作者**: lintcoder
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/187

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I am trying to build ROCT-Thunk-Interface and ROCR-Runtime on my ubunu16.04-arm64 server which is running on qemu. Here are my steps:
First build ROCT-Thunk-Interface,
1.make
2.make deb
3.sudo dpkg -i build/deb/hsakmt-dev-2.0.0-arm64.deb
after that, path /opt/rocm/libhsakmt and /opt/rocm/include /opt/rocm/lib generated,

Then build ROCR-Runtime,
1.cd src
2.mkdir build & cd build
3.cmake -D CMAKE_PREFIX_PATH=/opt/rocm/libhsakmt ../
4.make
on the 4th step, error occurs as follows:

[100%] Linking CXX shared library libhsa-runtime64.so
/usr/bin/ld: cannot find -lhsakmt
collect2: error: ld returned 1 exit status
CMakeFiles/hsa-runtime64.dir/build.make:927: recipe for target 'libhsa-runtime64.so.1.0.0' failed
make[2]: *** [libhsa-runtime64.so.1.0.0] Error 1
CMakeFiles/Makefile2:104: recipe for target 'CMakeFiles/hsa-runtime64.dir/all' failed
make[1]: *** [CMakeFiles/hsa-runtime64.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2



---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-08-24T16:03:37Z)

If your trying to get 1.6.3 source it just rolling out 

Greg



---

### 评论 #2 — gstoner (2017-08-24T16:58:33Z)

Ok. I just saw this is ARM server and you're using it in KVM,  a big issue is are you supporting PCIe Atomics Pass through in KVM if no the Kernel driver will not boot.  Even if you fix the build issues.     

We are going to go back and clean up the ARM code,  but it will still need PCIe Atomics.   We also. post instruction on how to use KVM with ROCm 


---
