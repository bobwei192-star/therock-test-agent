# Driver Install Issue: OpenCL HelloWorld segfault

- **Issue #:** 212
- **State:** closed
- **Created:** 2017-09-23T07:11:47Z
- **Updated:** 2017-09-27T01:50:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/212

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

