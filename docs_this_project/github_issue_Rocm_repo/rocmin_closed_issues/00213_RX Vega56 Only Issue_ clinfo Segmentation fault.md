# RX Vega56 Only Issue: clinfo Segmentation fault

- **Issue #:** 213
- **State:** closed
- **Created:** 2017-09-27T15:42:36Z
- **Updated:** 2019-02-15T10:16:09Z
- **Labels:** Bug_Functional_Issue, Question
- **URL:** https://github.com/ROCm/ROCm/issues/213

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