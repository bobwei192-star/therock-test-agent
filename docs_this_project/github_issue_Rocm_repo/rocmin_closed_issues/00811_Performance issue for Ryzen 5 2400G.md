# Performance issue for Ryzen 5 2400G

- **Issue #:** 811
- **State:** closed
- **Created:** 2019-06-04T11:35:48Z
- **Updated:** 2024-03-22T02:44:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/811

Hi,

I am trying to do some (baseline) password cracking and I am kind of disappointed by the performance I get with the GPU from the Ryzen 5 system above.

One of the hashes I am interested in is plain SHA512 password hashes of Linux. Here I get only double the performance of the CPU (using the Intel OpenCL driver):

```
prompt> hashcat -D1,2 -b -m1800
[..]
OpenCL Platform #1: Advanced Micro Devices, Inc.
================================================
* Device #1: gfx902-xnack, 12817/15079 MB allocatable, 11MCU

OpenCL Platform #2: Intel(R) Corporation
========================================
* Device #2: AMD Ryzen 5 2400G with Radeon Vega Graphics, 7539/30159 MB allocatable, 8MCU

Benchmark relevant options:
===========================
* --opencl-device-types=1,2
* --optimized-kernel-enable

Hashmode: 1800 - sha512crypt $6$, SHA512 (Unix) (Iterations: 5000)

Speed.#1.........:     5947 H/s (47.22ms) @ Accel:64 Loops:32 Thr:64 Vec:1
Speed.#2.........:     2530 H/s (80.15ms) @ Accel:512 Loops:256 Thr:1 Vec:4
Speed.#*.........:     8478 H/s

Started: Fri May 31 13:06:58 2019
Stopped: Fri May 31 13:07:07 2019
```

(The performance of the GPU doesn't improve I omit the CPU which is good). If I do a comparison with other systems though there's an odd thing with a user posting his benchmark using Windows (https://hashcat.net/forum/thread-7513.html): It's almost the same but for this specific hash I am getting not even 1/3rd of what he claims. At the moment I do not have any reasons to doubt that as other (different) machines I tested indicate that this should be better. I have now windows on this machine though.

Hashcat maintainers responded that there's no difference on the OS (https://hashcat.net/forum/thread-8388.html)

My question: is there any known deficiencies in the ROCm driver which might affect this?

My System: 
```
prompt> uname -a
Linux REDACTED 5.0.8-1-default #1 SMP Wed Apr 17 09:25:56 UTC 2019 (8b88553) x86_64 x86_64 x86_64 GNU/Linux
prompt> grep -A 5 -B5 kfd /var/log/boot.msg    # using upstream driver
<6>[    4.806387] [drm] Display Core initialized with v3.2.08!
<6>[    4.808016] usb 3-2: new full-speed USB device number 2 using xhci_hcd
<6>[    4.855362] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
<6>[    4.855363] [drm] Driver supports precise vblank timestamp query.
<6>[    4.870009] [drm] VCN decode and encode initialized successfully(under SPG Mode).
<6>[    4.870763] kfd kfd: Allocated 3969056 bytes on gart
<6>[    4.870784] Topology: Add APU node [0x15dd:0x1002]
<6>[    4.870975] kfd kfd: added device 1002:15dd
<6>[    4.873316] [drm] fb mappable at 0x78FA00000
<6>[    4.873317] [drm] vram apper at 0x78F000000
<6>[    4.873317] [drm] size 14745600
<6>[    4.873318] [drm] fb depth is 24
<6>[    4.873318] [drm]    pitch is 10240
prompt> ls -l /dev/kfd
crw-rw-rw-+ 1 root video 244, 0 Apr 23 14:28 /dev/kfd
prompt> rpm -qa | grep '^rocm'      # yes. not the latest but shouldn't matter much, right? 
rocm-clang-ocl-0.4.0_7ce124f-1.x86_64
rocm-utils-2.1.96-1.x86_64
rocm-opencl-devel-1.2.0-2019020220.x86_64
rocminfo-1.0.0-1.x86_64
rocm-opencl-1.2.0-2019020220.x86_64
prompt> hashcat -I
hashcat (v5.1.0) starting...

OpenCL Info:

Platform ID #1
  Vendor  : Advanced Micro Devices, Inc.
  Name    : AMD Accelerated Parallel Processing
  Version : OpenCL 2.1 AMD-APP (2814.0)

  Device ID #1
    Type           : GPU
    Vendor ID      : 1
    Vendor         : Advanced Micro Devices, Inc.
    Name           : gfx902-xnack
    Version        : OpenCL 1.2 
    Processor(s)   : 11
    Clock          : 1250
    Memory         : 12817/15079 MB allocatable
    OpenCL Version : OpenCL C 2.0 
    Driver Version : 2814.0 (HSA1.1,LC)

Platform ID #2
  Vendor  : Intel(R) Corporation
  Name    : Intel(R) OpenCL
  Version : OpenCL 1.2 

  Device ID #2
    Type           : CPU
    Vendor ID      : 8
    Vendor         : Intel(R) Corporation
    Name           : AMD Ryzen 5 2400G with Radeon Vega Graphics
    Version        : OpenCL 1.2 (Build 475)
    Processor(s)   : 8
    Clock          : 0
    Memory         : 7539/30159 MB allocatable
    OpenCL Version : OpenCL C 1.2 
    Driver Version : 1.2.0.475
```

Thx, Dirk


