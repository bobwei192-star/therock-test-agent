# Loop in sched_yield for libhsa-runtime causes OpenCLI's clinfo to hang

> **Issue #714**
> **状态**: closed
> **创建时间**: 2019-02-19T09:34:31Z
> **更新时间**: 2019-12-27T09:33:26Z
> **关闭时间**: 2019-04-16T07:25:24Z
> **作者**: elukey
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/714

## 描述

Hi! 

The Wikimedia Foundation is trying to experiment AMD-based GPUs for our future Machine Learning usage, and we are currently trying to make our (old) Hawaii FirePro W9100 work with:

* Debian Buster + Kernel 4.19
* rocm-dev rocm-libs 2.1 debian packages (last found in the AMD debian repo)

What I am currently seeing is described in https://phabricator.wikimedia.org/T148843#4962357, in which any usage of the GPU (in this case OpenCL's clinfo) leads to a thread hanging on the sched_yield system call forever (the gdb stacktrace would be more informative with debug symbols but didn't find any deb package for that). Any attempt to kill the process leads then to a Kernel null pointer exception in the dmesg (all details in the link). As described I tried both rocm 1.9.2 from the archive repos and 2.1 from the current one after reading https://github.com/RadeonOpenCompute/ROCm/issues/702

I tried the following [workarounds](https://phabricator.wikimedia.org/T148843#4963670) after reading https://github.com/RadeonOpenCompute/ROCm/issues/482, but none of them worked. We are using only Debian in our ecosystem so I am not able to test the GPU with Ubuntu.

Here's some details:

* Added the following to the kernel's boot parameters `radeon.cik_support=0 amdgpu.cik_support=1`
* udev rules `SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"`
* The following is boot logging from dmesg

```
[Tue Feb 19 08:35:06 2019] [drm] amdgpu kernel modesetting enabled.
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_mc.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: BAR 2: releasing [mem 0xa0000000-0xa07fffff 64bit pref]
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: BAR 0: releasing [mem 0x90000000-0x9fffffff 64bit pref]
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: BAR 0: assigned [mem 0x38000000000-0x383ffffffff 64bit pref]
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: BAR 2: assigned [mem 0x38400000000-0x384007fffff 64bit pref]
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: VRAM: 16384M 0x000000F400000000 - 0x000000F7FFFFFFFF (16384M used)
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[Tue Feb 19 08:35:06 2019] [drm] amdgpu: 16384M of VRAM memory ready
[Tue Feb 19 08:35:06 2019] [drm] amdgpu: 16384M of GTT memory ready.
[Tue Feb 19 08:35:06 2019] [drm] GART: num cpu pages 262144, num gpu pages 262144
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_pfp.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_me.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_ce.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_mec.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_rlc.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_sdma.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_sdma1.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_uvd.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_vce.bin
[Tue Feb 19 08:35:06 2019] amdgpu 0000:04:00.0: firmware: direct-loading firmware amdgpu/hawaii_smc.bin
[Tue Feb 19 08:35:06 2019] amdgpu: [powerplay] Failed to retrieve minimum clocks.
[Tue Feb 19 08:35:06 2019] amdgpu: [powerplay] Error in phm_get_clock_info
[Tue Feb 19 08:35:06 2019] [drm:dc_create [amdgpu]] *ERROR* DC: Number of connectors is zero!
[Tue Feb 19 08:35:07 2019] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:04:00.0 on minor 1

[Tue Feb 19 08:35:06 2019] kfd kfd: Initialized module
[Tue Feb 19 08:35:07 2019] kfd kfd: Allocated 3969056 bytes on gart
[Tue Feb 19 08:35:07 2019] kfd kfd: added device 1002:67a0
```

I currently have no idea if the following errors are noise or something serious:

```
[Tue Feb 19 08:35:06 2019] amdgpu: [powerplay] Failed to retrieve minimum clocks.
[Tue Feb 19 08:35:06 2019] amdgpu: [powerplay] Error in phm_get_clock_info
[Tue Feb 19 08:35:06 2019] [drm:dc_create [amdgpu]] *ERROR* DC: Number of connectors is zero!
```
EDIT: the above errors go away if I set `amdgpu.dc=0` (that should be 1 by default on recent kernels if I got it correctly).

EDIT2: I can see the following though (repeating once in a while):
```
[Wed Feb 20 12:20:16 2019] amdgpu: [powerplay]
                            failed to send message 282 ret is 254
```

* rocminfo

```
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Xeon(R) CPU E5-2640 v4 @ 2.40GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0
  Queue Min Size:          0
  Queue Max Size:          0
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768KB
  Chip ID:                 0
  Cacheline Size:          64
  Max Clock Frequency (MHz):3400
  BDFID:                   0
  Compute Unit:            20
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32844880KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32844880KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    Intel(R) Xeon(R) CPU E5-2640 v4 @ 2.40GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0
  Queue Min Size:          0
  Queue Max Size:          0
  Queue Type:              MULTI
  Node:                    1
  Device Type:             CPU
  Cache Info:
    L1:                      32768KB
  Chip ID:                 0
  Cacheline Size:          64
  Max Clock Frequency (MHz):3400
  BDFID:                   0
  Compute Unit:            20
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    33025532KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    33025532KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 3
*******
  Name:                    gfx701
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26528
  Cacheline Size:          64
  Max Clock Frequency (MHz):900
  BDFID:                   1024
  Compute Unit:            44
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  67109888
    Dim[2]:                  0
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16777216KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx701
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                FALSE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
*** Done ***
```

* lspci -vv | grep ATI

```
04:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii XT GL [FirePro W9100]
```

We are currently looking to get a more up to date GPU, but making this work would definitely be a great start for testing (or possibly knowing that it will not work for sure to avoid wasting too much time in debugging).

Thanks in advance for the help, let me know if you need further info!

---

## 评论 (7 条)

### 评论 #1 — elukey (2019-02-20T14:25:18Z)

The main problem, to summarize the above, seems to be a loop in calling `sched_yield` in:
```
Thread 1 (Thread 0x7f35fcd8e740 (LWP 5396)):
#0  0x00007f35fce71bf7 in sched_yield () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007f35f8a09225 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007f35f8a01f26 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#3  0x00007f35f8a0ba9e in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#4  0x00007f35f8a3e155 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#5  0x00007f35f8a3e86e in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#6  0x00007f35f8a421cd in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#7  0x00007f35f8a1b147 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#8  0x00007f35f921c60a in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#9  0x00007f35f921e4ac in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#10 0x00007f35f91f1c5f in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#11 0x00007f35f91e3ace in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#12 0x00007f35f91eef92 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#13 0x00007f35f9213104 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#14 0x00007f35f9213f95 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#15 0x00007f35f91ec9d3 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#16 0x00007f35f91eb137 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#17 0x00007f35f91c138a in clIcdGetPlatformIDsKHR () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#18 0x00007f35fcf9198b in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#19 0x00007f35fcf93907 in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#20 0x00007f35fcf63947 in __pthread_once_slow () from /lib/x86_64-linux-gnu/libpthread.so.0
#21 0x00007f35fcf91f21 in clGetPlatformIDs () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#22 0x000000000040f617 in ?? ()
#23 0x0000000000407c12 in ?? ()
#24 0x00007f35fcdb509b in __libc_start_main () from /lib/x86_64-linux-gnu/libc.so.6
#25 0x000000000040e6d1 in ?? ()
```

The missing symbols belongs to libs shipped by:

```
dpkg -S libhsa-runtime64
hsa-rocr-dev: /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9
hsa-rocr-dev: /opt/rocm/hsa/lib/libhsa-runtime64.so.1
hsa-rocr-dev: /opt/rocm/lib/libhsa-runtime64.so

dpkg -S libamdocl64
rocm-opencl: /opt/rocm/opencl/lib/x86_64/libamdocl64.so
```

I didn't find any dbg/debug package to have symbols, is there anybody that knows how to do it? 


---

### 评论 #2 — jlgreathouse (2019-02-20T17:03:15Z)

I'll admit that I do not have time to fully debug this at the moment, but to prevent you from going down a rabbit hole here: this is almost invariably being caused by something like a kernel being launched to the GPU, the OpenCL runtime going to sleep to wait for it to finish, and it never returning. The `sched_yield` call is the sleep to await the return event.

If you would like to try to build debug symbols, you could look into the build scripts available in the [Experimental ROC](https://github.com/RadeonOpenCompute/Experimental_ROC) repo. These have not been configured for Debian, so you would need to make modifications of them.

I'll note a few other things:

- Debian is not a distribution that AMD claims to support at this time. While our software may compile and run there, we do no testing of Debian at this time. The .deb files that we ship from repo.radeon.com are only tested on Ubuntu 16 and Ubuntu 18.
- Hawaii is not a supported platform for our machine learning software stack, so even if you were to get basic things working on Hawaii within your distro, MIOpen and our other libraries are not presently configured to support gfx701.

---

### 评论 #3 — elukey (2019-02-20T17:19:49Z)

Thanks a lot for the answer, I'll dedicate my time to order new hardware then :)



---

### 评论 #4 — delolat (2019-02-22T04:40:28Z)

jlgreathouse, so in all likelihood is it possible to expect a patch sometime within the next month two? I've tried the experimental ROC repo 1.9.2, but had the same problems as 2.1. I'm also inclined to buy new cards as my Fury X with 4gb is not worth pairing with anything new. I was hoping to keep my Hawaii as it has 8GB, but to be honest it is the only thing tethering me to AMD GPU's. 

---

### 评论 #5 — pqyptixa (2019-12-26T01:34:53Z)

Imagine buying new hardware only to find that you won't be able to fully use it, because the software for it has bugs that the manufacturer does not care about.

---

### 评论 #6 — pqyptixa (2019-12-26T13:55:36Z)

@elukey I wonder: had you tried adding amdgpu.runpm=0 to the kernel command line?

---

### 评论 #7 — elukey (2019-12-27T09:33:26Z)

> @elukey I wonder: had you tried adding amdgpu.runpm=0 to the kernel command line?

Not that I remember, all I tried is listed in this issue :)

---
