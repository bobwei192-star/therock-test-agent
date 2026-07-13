# Loop in sched_yield for libhsa-runtime causes OpenCLI's clinfo to hang

- **Issue #:** 714
- **State:** closed
- **Created:** 2019-02-19T09:34:31Z
- **Updated:** 2019-12-27T09:33:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/714

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