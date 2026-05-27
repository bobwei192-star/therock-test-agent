# Segfault in clinfo on ROCm 3.9.0.30900 on CentOS 8 Stream

> **Issue #1278**
> **状态**: closed
> **创建时间**: 2020-11-06T19:39:58Z
> **更新时间**: 2020-11-09T17:25:48Z
> **关闭时间**: 2020-11-09T17:25:48Z
> **作者**: xudonax
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1278

## 描述

After installing CentOS 8 Stream on a UDOO Bolt V8 I tried to enable ROCm by following [these steps about the upstream kernel drivers](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#using-rocm-with-upstream-kernel-drivers). This seems to work fine, the `/dev/kfd` file is created and I have access to it after adding myself to the `video` group.

This is a fresh install of CentOS 8 Stream. When running `rocminfo` a few times after each other the machine invariably hangs and gets rebooted by the watchdog.

However, running `/opt/rocm/opencl/bin/clinfo causes segfault, gdb gives the following trace:
```
[sanne@CentOS8 ~]$ gdb /opt/rocm/opencl/bin/clinfo
GNU gdb (GDB) Red Hat Enterprise Linux 8.2-12.el8
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /opt/rocm/opencl/bin/clinfo...(no debugging symbols found)...done.
(gdb) start
Temporary breakpoint 1 at 0x402840
Starting program: /opt/rocm-3.9.0/opencl/bin/clinfo
Missing separate debuginfos, use: yum debuginfo-install rocm-opencl-3.6Beta_14_g0c40e05_rocm_rel_3.9_17-1.x86_64
warning: Loadable section ".note.gnu.property" outside of ELF segments
warning: Loadable section ".note.gnu.property" outside of ELF segments
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".

Temporary breakpoint 1, 0x0000000000402840 in main ()
(gdb) continue
Continuing.
warning: Loadable section ".note.gnu.property" outside of ELF segments
warning: Loadable section ".note.gnu.property" outside of ELF segments
warning: Loadable section ".note.gnu.property" outside of ELF segments
warning: Loadable section ".note.gnu.property" outside of ELF segments
[New Thread 0x7fffeed57700 (LWP 4114)]

Thread 1 "clinfo" received signal SIGSEGV, Segmentation fault.
0x00007ffff6832003 in roc::Device::setupCpuAgent() () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
(gdb) bt
#0  0x00007ffff6832003 in roc::Device::setupCpuAgent() () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#1  0x00007ffff683235b in roc::Device::populateOCLDeviceConstants() ()
   from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#2  0x00007ffff68335ce in roc::Device::create() () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#3  0x00007ffff6833ec5 in roc::Device::init() () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#4  0x00007ffff67fe84f in amd::Device::init() () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#5  0x00007ffff68087be in amd::Runtime::init() () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#6  0x00007ffff67f8ed5 in std::call_once<clIcdGetPlatformIDsKHR::{lambda()#1}>(std::once_flag&, clIcdGetPlatformIDsKHR::{lambda()#1}&&)::{lambda()#2}::_FUN() () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#7  0x00007ffff6e88ce7 in __pthread_once_slow () from /lib64/libpthread.so.0
#8  0x00007ffff67f8fd9 in clIcdGetPlatformIDsKHR () from /opt/rocm-3.9.0/opencl/bin/../lib/libamdocl64.so
#9  0x00007ffff7bcea2d in khrIcdVendorAdd () from /opt/rocm-3.9.0/opencl/bin/../lib/libOpenCL.so.1
#10 0x00007ffff7bd094e in khrIcdOsVendorsEnumerate () from /opt/rocm-3.9.0/opencl/bin/../lib/libOpenCL.so.1
#11 0x00007ffff6e88ce7 in __pthread_once_slow () from /lib64/libpthread.so.0
#12 0x00007ffff7bcefa1 in clGetPlatformIDs () from /opt/rocm-3.9.0/opencl/bin/../lib/libOpenCL.so.1
#13 0x000000000040b4dc in cl::Platform::get(std::vector<cl::Platform, std::allocator<cl::Platform> >*) ()
#14 0x0000000000402918 in main ()
(gdb)
```

The output of `rocminfo` is as follows:
```
[sanne@CentOS8 ~]$ /opt/rocm/bin/rocminfo
ROCk module is loaded
Able to open /dev/kfd read-write
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen Embedded V1605B with Radeon Vega Gfx
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen Embedded V1605B with Radeon Vega Gfx
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32(0x20) KB
  Chip ID:                 5597(0x15dd)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2000
  BDFID:                   1024
  Internal Node ID:        0
  Compute Unit:            8
  SIMDs per CU:            4
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16776832(0xfffe80) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx902
  Uuid:                    GPU-XX
  Marketing Name:          AMD Ryzen Embedded V1605B with Radeon Vega Gfx
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 5597(0x15dd)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1100
  BDFID:                   1024
  Internal Node ID:        0
  Compute Unit:            11
  SIMDs per CU:            4
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        160(0xa0)
  Max Work-item Per CU:    10240(0x2800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```

---

## 评论 (2 条)

### 评论 #1 — rkothako (2020-11-09T05:52:20Z)

Hi @xudonax 
Thanks for reaching us with the logs.

From the logs, its clear that you are trying ROCm on gfx902 variant. We are not officially supporting this GPU for ROCm as per our hardware support list @ [https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support](url).

We are supporting ryzen from CPU perspective but not from GPU perspective.

Hope this clarifies.
Please let me know if you need more information.





---

### 评论 #2 — xudonax (2020-11-09T17:25:48Z)

I totally missed that, sorry. Thanks for the pointer in the right direction. I'll close the issue now.

---
