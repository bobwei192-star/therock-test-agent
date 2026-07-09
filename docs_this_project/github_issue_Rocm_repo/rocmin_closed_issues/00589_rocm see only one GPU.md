# rocm see only one GPU

- **Issue #:** 589
- **State:** closed
- **Created:** 2018-10-27T14:04:10Z
- **Updated:** 2021-01-26T12:28:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/589

Hi guys , after many format i got rocm  to cooperate.
The problem is it only see one GPU
the goal is to get this running hashcat. (hc only see 1 gpuas well)

i should say this is a old mining rig i bought used, could it be something in the bios ?

```
root@x:/home/x/Desktop/hashcat-4.2.1# /opt/rocm/bin/rocminfo
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
  Name:                    Intel(R) Pentium(R) CPU G4400 @ 3.30GHz
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
  Max Clock Frequency (MHz):3300
  BDFID:                   0
  Compute Unit:            2
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3910956KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3910956KB
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
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26591
  Cacheline Size:          64
  Max Clock Frequency (MHz):1281
  BDFID:                   256
  Compute Unit:            32
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  16778240
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
      Size:                    4194304KB
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
      Name:                    amdgcn-amd-amdhsa--gfx803
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
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
root@x:/home/x/Desktop/hashcat-4.2.1# lspci | grep 470
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
08:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
root@x:/home/x/Desktop/hashcat-4.2.1#
```