# RX580 - clinfo stucks and never show any result

- **Issue #:** 1008
- **State:** closed
- **Created:** 2020-02-01T22:00:49Z
- **Updated:** 2021-04-19T12:57:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/1008

Hello,

I have several RX580 and I want to try deep learning with tensor flow on it.

I chose ubuntu 18.04.3 LTS as OS
I followed the instructions here : https://rocm.github.io/ROCmInstall.html 

At the end of the instructions below it advice to run these:
 /opt/rocm/bin/rocminfo
 /opt/rocm/opencl/bin/x86_64/clinfo

rocminfo works perfectly and here is the result : 
``` ROCk module is loaded
user is not member of "video" group, the default DRM access group. Users must be a member of the "video" group or another DRM access group in order for ROCm applications to run successfully.
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
  Name:                    Intel Xeon E312xx (Sandy Bridge, IBRS update)
  Marketing Name:          Intel Xeon E312xx (Sandy Bridge, IBRS update)
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
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            8
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    8101140(0x7b9d14) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8101140(0x7b9d14) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx803
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X]
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 26591(0x67df)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1411
  BDFID:                   64
  Internal Node ID:        1
  Compute Unit:            36
  SIMDs per CU:            4
  Shader Engines:          4
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
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    2560(0xa00)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8388608(0x800000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx803
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
But when I run  /opt/rocm/opencl/bin/x86_64/clinfo 
It never produce any result and if I kill the process or try reboot (by ssh), the computer crashes until I physically press the reset button.
I already tried a strace on the process and it seems to loop on : 
```
...
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
sched_yield()                           = 0
```

I already googled and try to check dmseg 
* dmesg | grep amdgpu =>
```
[    2.254300] [drm] amdgpu kernel modesetting enabled.
[    2.254953] amdgpu 0000:00:08.0: remove_conflicting_pci_framebuffers: bar 0: 0x800000000 -> 0x80fffffff
[    2.254955] amdgpu 0000:00:08.0: remove_conflicting_pci_framebuffers: bar 2: 0x810000000 -> 0x8101fffff
[    2.254956] amdgpu 0000:00:08.0: remove_conflicting_pci_framebuffers: bar 5: 0xc8000000 -> 0xc803ffff
[    2.424505] amdgpu 0000:00:08.0: GPU pci config reset
[    2.542224] amdgpu 0000:00:08.0: BAR 2: releasing [mem 0x810000000-0x8101fffff 64bit pref]
[    2.542224] amdgpu 0000:00:08.0: BAR 0: releasing [mem 0x800000000-0x80fffffff 64bit pref]
[    2.543952] amdgpu 0000:00:08.0: BAR 0: assigned [mem 0x800000000-0x80fffffff 64bit pref]
[    2.544065] amdgpu 0000:00:08.0: BAR 2: assigned [mem 0x810000000-0x8101fffff 64bit pref]
[    2.547900] amdgpu 0000:00:08.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[    2.547900] amdgpu 0000:00:08.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    2.547900] [drm] amdgpu: 8192M of VRAM memory ready
[    2.547900] [drm] amdgpu: 5933M of GTT memory ready.
[    2.594408] amdgpu: [powerplay] hwmgr_sw_init smu backed is polaris10_smu
[    2.767056] [drm] Initialized amdgpu 3.33.0 20150101 for 0000:00:08.0 on minor 1
```
* dmesg | grep kfd=>
```
[    3.861401] kfd kfd: Allocated 3969056 bytes on gart
[    3.864100] kfd kfd: added device 1002:67df
```

I also tried to run directly tensorflow but the first instruction that requires the gpu behave exactly as the clinfo

Any idea ?
