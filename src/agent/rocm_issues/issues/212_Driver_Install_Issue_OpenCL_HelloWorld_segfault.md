# Driver Install Issue: OpenCL HelloWorld segfault

> **Issue #212**
> **状态**: closed
> **创建时间**: 2017-09-23T07:11:47Z
> **更新时间**: 2017-09-27T01:50:32Z
> **关闭时间**: 2017-09-27T01:50:32Z
> **作者**: antinucleon
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/212

## 描述

I am trying to run this with VEGA
```
 wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cpp
 wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cl
```
But I get

```
(gdb) run
Starting program: /home/bing/opt/HelloWorld 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff37c94e6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
(gdb) bt
#0  0x00007ffff37c94e6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#1  0x00007ffff379c9c3 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#2  0x00007ffff37b96a7 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#3  0x00007ffff3785602 in clIcdGetPlatformIDsKHR ()
   from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#4  0x00007ffff7bd276e in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#5  0x00007ffff7bd4647 in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#6  0x00007ffff694aa99 in __pthread_once_slow (once_control=0x7ffff7dd63d8, 
    init_routine=0x7ffff7bd44a0) at pthread_once.c:116
#7  0x00007ffff7bd2d31 in clGetPlatformIDs ()
   from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#8  0x00000000004015ea in CreateContext() ()
#9  0x0000000000401d8a in main ()

```

Seems the gpu is installed correctly

```
bing@Monster:~/opt$ /opt/rocm/bin/rocm-smi 


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  0   6863   60.0c    11.0W    852Mhz   945Mhz   13.73%   auto      0%       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================

bing@Monster:~/opt$ /opt/rocm/bin/rocm-smi 


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  0   6863   60.0c    10.0W    852Mhz   945Mhz   13.73%   auto      0%       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================

```

System: Ubuntu 16.04, Xeon E6-2670
```
Linux Monster 4.11.0-kfd-compute-rocm-rel-1.6-148 #1 SMP Wed Aug 23 12:00:35 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux
```
Any suggestion?



---

## 评论 (13 条)

### 评论 #1 — gstoner (2017-09-23T13:47:29Z)

cd /opt/rocm/hip/samples/1_Utils/hipInfo
sudo make. 
./hipinfo 

This will tell us if your GPU is installed correctly 

---

### 评论 #2 — gstoner (2017-09-23T13:50:39Z)

After this pull this one https://github.com/krrishnarraj/clpeak.  we compile this one a lot. 


---

### 评论 #3 — gstoner (2017-09-23T13:56:00Z)

You should see this 

~/clpeak$ ./clpeak 

Platform: AMD Accelerated Parallel Processing
  Device: gfx900
    Driver version  : 1.1 (HSA,LC) (Linux x64)
    Compute units   : 64
    Clock frequency : 1500 MHz

    Global memory bandwidth (GBPS)
      float   : 296.07
      float2  : 348.27
      float4  : 377.63
      float8  : 349.40
      float16 : 108.61

    Single-precision compute (GFLOPS)
      float   : 12105.07
      float2  : 12104.08
      float4  : 12010.71
      float8  : 11938.48
      float16 : 11863.80

    No half precision support! Skipped

    Double-precision compute (GFLOPS)
      double   : 767.09
      double2  : 766.71
      double4  : 765.88
      double8  : 764.33
      double16 : 761.19

    Integer compute (GIOPS)
      int   : 2341.71
      int2  : 2330.76
      int4  : 2317.60
      int8  : 2315.08
      int16 : 2334.70

    Transfer bandwidth (GBPS)
      enqueueWriteBuffer         : 13.18
      enqueueReadBuffer          : 15.75
      enqueueMapBuffer(for read) : 47828.14
        memcpy from mapped ptr   : 14.88
      enqueueUnmap(after write)  : 186737.72
        memcpy to mapped ptr     : 15.42

    Kernel launch latency : 11.40 us

 

---

### 评论 #4 — antinucleon (2017-09-24T03:54:55Z)

Unable to get it work

```
./hipInfo 
compiler: nvcc
error: 'unknown error'(1030) at hipInfo.cpp:189
error: API returned error code.
error: TEST FAILED
```

---

### 评论 #5 — ekondis (2017-09-24T07:42:37Z)

@gstoner Running clpeak on my system seems to take for forever to just compile the OpenCL kernels (using Fiji GPU). It freezes after the "Clock frequency : 1000 MHz" message.

I'm using ROCm version 1.6-148.

This is certainly a different issue but I was surprised that you could actually run clpeak under ROCm.

---

### 评论 #6 — gstoner (2017-09-24T13:14:16Z)

@ekondis. We run it all the time,  we are working on a new in-process compiler( aka JIT) for LLVM.  It was checked in recently.  We still in beta on OpenCL.   But we run your test all the time.  Results above are on 148. 

---

### 评论 #7 — gstoner (2017-09-24T13:16:34Z)

@antinucleon    We need to get to the basics, it looks like your driver is not installed properly.   So you have  Ubuntu 16.04, Xeon E5-2670 what another GPU is in the system.  Looks like NVIDIA driver is also on the system based on the HIP error

---

### 评论 #8 — antinucleon (2017-09-24T15:00:04Z)

@gstoner I have wiped and reinstalled Ubuntu for 2 times, and I pulled out NVIDIA card, so I am sure there is no NV driver.

---

### 评论 #9 — kisow (2017-09-25T13:28:47Z)

I have the same problems. I'm using Ryzen 1700 + RX VEGA 56.
I have installed ubuntu 16.04 after format SSD, and then I have installed rocm and rocm-opencl-dev, following https://rocm.github.io/ROCmInstall.html and https://rocm.github.io/QuickStartOCL.html, but clinfo is NOT work.

* rocm-smi
  * Is DID right for RX VEGA 56? (not GFX900?)
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

### 评论 #10 — gstoner (2017-09-25T14:09:23Z)

@antinucleon  Are you using a RX based Vega10 with 56 CU's 

---

### 评论 #11 — antinucleon (2017-09-25T18:49:14Z)

@gstoner I am using rx vega frontier with 64 cu

---

### 评论 #12 — gstoner (2017-09-26T15:21:03Z)

@antinucleon Xeon E5-2670 is this a Sandybridge based CPU, if so this does not meet the minimum CPU spec for ROCm we need Xeon E5 v3 ( Haswell)  or EPYC/Ryzen CPU with PCIe Gen 3 with Atomic Completors ( PCIe Atomics) support. 

---

### 评论 #13 — antinucleon (2017-09-27T01:50:25Z)

@gstoner Thank you. I think it should be the reason :(

---
