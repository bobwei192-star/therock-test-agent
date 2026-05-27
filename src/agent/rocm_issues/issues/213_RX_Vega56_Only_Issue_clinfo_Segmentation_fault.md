# RX Vega56 Only Issue: clinfo Segmentation fault

> **Issue #213**
> **状态**: closed
> **创建时间**: 2017-09-27T15:42:36Z
> **更新时间**: 2019-02-15T10:16:09Z
> **关闭时间**: 2017-10-24T17:37:17Z
> **作者**: kisow
> **标签**: Bug_Functional_Issue, Question
> **URL**: https://github.com/ROCm/ROCm/issues/213

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)
- **Question** (颜色: #cc317c)

## 描述

With Ryzen 1700 + RX VEGA 56, I have installed ubuntu 16.04 after format SSD, and then I have installed rocm and rocm-opencl-dev, following https://rocm.github.io/ROCmInstall.html and https://rocm.github.io/QuickStartOCL.html, but clinfo is NOT work.

* rocm-smi
  * Is DID right for RX VEGA 56? 
```
$ /opt/rocm/bin/rocm-smi 


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  0   687f   49.0c    7.0W     852Mhz   800Mhz   12.94%   auto      0%       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```

* dmesg
```
$ dmesg | grep kfd
[    0.000000] Linux version 4.11.0-kfd-compute-rocm-rel-1.6-148 (jenkins@jenkins-raptor-5) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #1 SMP Wed Aug 23 12:00:35 CDT 2017
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.11.0-kfd-compute-rocm-rel-1.6-148 root=UUID=4be3295d-2707-4e99-9d54-6cace885e1be ro quiet splash vt.handoff=7
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.11.0-kfd-compute-rocm-rel-1.6-148 root=UUID=4be3295d-2707-4e99-9d54-6cace885e1be ro quiet splash vt.handoff=7
[    1.303216] usb usb1: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.303792] usb usb2: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.304332] usb usb3: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.304537] usb usb4: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.434620] kfd kfd: Initialized module
[    2.240811] kfd kfd: Allocated 3969056 bytes on gart for device 1002:687f
[    2.240975] kfd kfd: Reserved 2 pages for cwsr.
[    2.241021] kfd kfd: added device 1002:687f
```

* clpeak
  * /opt/rocm/opencl/lib/x86_64/libamdocl64.so error
```
Thread 1 "clpeak" received signal SIGSEGV, Segmentation fault.
0x00007ffff37c94e6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
(gdb) bt
#0  0x00007ffff37c94e6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#1  0x00007ffff379c9c3 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#2  0x00007ffff37b96a7 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#3  0x00007ffff3785602 in clIcdGetPlatformIDsKHR () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#4  0x00007ffff7bd276e in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#5  0x00007ffff7bd4647 in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#6  0x00007ffff694aa99 in __pthread_once_slow (once_control=0x7ffff7dd63d8, init_routine=0x7ffff7bd44a0) at pthread_once.c:116
#7  0x00007ffff7bd2d31 in clGetPlatformIDs () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#8  0x000000000040b18a in cl::Platform::get(std::vector<cl::Platform, std::allocator<cl::Platform> >*) ()
#9  0x0000000000407928 in clPeak::runAll() ()
#10 0x000000000040510d in main ()
```

* gdb --args /opt/rocm/opencl/bin/x86_64/clinfo
```
Thread 1 "clinfo" received signal SIGSEGV, Segmentation fault.
0x00007ffff3b4b4e6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
(gdb) bt
#0  0x00007ffff3b4b4e6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#1  0x00007ffff3b1e9c3 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#2  0x00007ffff3b3b6a7 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#3  0x00007ffff3b07602 in clIcdGetPlatformIDsKHR () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#4  0x00007ffff74bd76e in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#5  0x00007ffff74bf647 in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#6  0x00007ffff7096a99 in __pthread_once_slow (once_control=0x7ffff76c13d8, init_routine=0x7ffff74bf4a0) at pthread_once.c:116
#7  0x00007ffff74bdd31 in clGetPlatformIDs () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#8  0x000000000040f687 in ?? ()
#9  0x0000000000407c12 in ?? ()
#10 0x00007ffff6cde830 in __libc_start_main (main=0x407b60, argc=1, argv=0x7fffffffdde8, init=<optimized out>, fini=<optimized out>, 
    rtld_fini=<optimized out>, stack_end=0x7fffffffddd8) at ../csu/libc-start.c:291
#11 0x000000000040e741 in ?? ()
```

* hipInfo
```
$ ./hipInfo 

compiler: hcc version=1.0.17312-d1f4a8a-19aa706-56b5abe, workweek (YYWWD) = 17312
--------------------------------------------------------------------------------
device#                           0
Name:                             Device 687f
pciBusID:                         14
pciDeviceID:                      0
multiProcessorCount:              56
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  1
clockRate:                        1590 Mhz
memoryClockRate:                  800 Mhz
memoryBusWidth:                   2048
clockInstructionRate:             1000 Mhz
totalGlobalMem:                   7.98 GB
maxSharedMemoryPerMultiProcessor: 7.98 GB
totalConstMem:                    16384
sharedMemPerBlock:                64.00 KB
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      0
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            2
minor:                            0
concurrentKernels:                1
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           0
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        0
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
peers:                            
non-peers:                        device#0 

memInfo.total:                    7.98 GB
memInfo.free:                     7.73 GB (97%)
```

---

## 评论 (14 条)

### 评论 #1 — gstoner (2017-09-28T01:10:12Z)

What CPU are you using 

---

### 评论 #2 — kisow (2017-09-30T04:24:13Z)

> With Ryzen 1700 + RX VEGA 56, I have installed ubuntu 16.04 after format SSD, and then I have installed rocm and rocm-opencl-dev, following https://rocm.github.io/ROCmInstall.html and https://rocm.github.io/QuickStartOCL.html, but clinfo is NOT work.

I'm using AMD Ryzen 1700 CPU. 
new AMD system (CPU + GPU)

---

### 评论 #3 — gstoner (2017-09-30T14:10:25Z)

See if you have permission issue also did you use the clinfo info in /opt/rocm/opencl/bin

---

### 评论 #4 — kisow (2017-09-30T15:33:19Z)

there is no permission issue and I use clinfo in /opt/rocm/opencl/bin/x86_64/clinfo.
> gdb --args /opt/rocm/opencl/bin/x86_64/clinfo
 
clinfo had died with **segmentation fault**, not for permission issue of executable binary command.
so, I had attached backtrace of call stack in gdb.

The segmentation fault of clinfo had occurred from **/opt/rocm/opencl/lib/x86_64/libamdocl64.so**.
And also the segmentation fault of clpeak that you had referred in #212 had occurred from  **/opt/rocm/opencl/lib/x86_64/libamdocl64.so**.
opencl Hello World of #212 where I already reported my problem, 
and opencl application that I'm using... 

all opencl applications that I had built using rocm opencl driver had died in same shared object file, **/opt/rocm/opencl/lib/x86_64/libamdocl64.so**.

It seems that this issue is a rocm package or rocm's opencl driver bug.


---

### 评论 #5 — gstoner (2017-09-30T16:24:42Z)

I had to check it was permission issue since it will also cause segfault, 

Next here what we know, CLINFO, OpenCL work on RX Vega 64, Frontier Edition and Mi25 which are all 64 CU version of Vega10.   We looking to see if this firmware issue or in the base driver.   Since the userland and compiler, stack is the same between GPU's.  

We get back to you. 

---

### 评论 #6 — noopole (2017-10-01T16:32:57Z)

I get exactly the same error with RX VEGA 56 and a Pentium G3260 (with a fresh install of Xubuntu16.04.3).

---

### 评论 #7 — psychocrypt (2017-10-01T21:29:00Z)

@gstone What do you changed to solve the permission issue. Do you mean with permission issue: permission to /dev/... or to clinfo or any  other library. 

---

### 评论 #8 — snslide (2017-10-02T19:47:32Z)

Hi, i'm getting the same issue but on a Vega 64, with a freshly installed ubuntu 16.04
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  0   687f   44.0c    17.0W    852Mhz   167Mhz   12.94%   auto      0%       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```
```
uname -a
Linux seeker-desktop 4.11.0-kfd-compute-rocm-rel-1.6-148 #1 SMP Wed Aug 23 12:00:35 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux
```

```
dpkg --get-selections | grep rocm
linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148	install
linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148	install
rocm						install
rocm-dev					install
rocm-device-libs				install
rocm-opencl					install
rocm-opencl-dev					install
rocm-profiler					install
rocm-smi					install
rocm-utils					install
```
```
gdb /opt/rocm/opencl/bin/x86_64/clinfo

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff3b4b4e6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
```

---

### 评论 #9 — gstoner (2017-10-02T19:55:49Z)

@snslide.  try sudo clinfo

---

### 评论 #10 — snslide (2017-10-03T05:00:47Z)

i also get a crash with sudo too

---

### 评论 #11 — gstoner (2017-10-17T12:45:34Z)

@snslide @kisow  Can you trying update ROCm 1.6.4 release  it was posted last night 

---

### 评论 #12 — preda (2017-10-23T14:28:31Z)

I had a similar problem on my recent ROCm 1.6-180 install, in my case was fixed by:
"unset LLVM_BIN".

(somehow I had an LLVM_BIN=/opt/rocm/bin which was breaking things).


---

### 评论 #13 — kisow (2017-10-24T15:16:03Z)

@gstoner 
I have tried amdgpu-pro-17.40-483984.tar.xz that is blockchain driver for ubuntu 16.04
and rocm 1.6-180. clinfo has worked well in both drivers.
OpenCL application that I built against VEGA 56 also work correctly despite it's performance drop compared to in windows blockchain driver as in #216.
Anyway, this issue can be closed.

---

### 评论 #14 — psychocrypt (2019-02-15T10:16:09Z)

which cpu do you use. rocm tequires a cpu which has the feature to do
pciexpress locks


---
