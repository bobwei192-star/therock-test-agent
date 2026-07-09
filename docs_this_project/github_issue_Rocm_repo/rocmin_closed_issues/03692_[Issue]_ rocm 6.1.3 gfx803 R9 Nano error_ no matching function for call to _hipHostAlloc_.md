# [Issue]: rocm 6.1.3 gfx803 R9 Nano error: no matching function for call to 'hipHostAlloc'

- **Issue #:** 3692
- **State:** closed
- **Created:** 2024-09-09T16:33:53Z
- **Updated:** 2024-12-10T05:21:11Z
- **Labels:** Under Investigation, AMD Radeon VII, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3692

### Problem Description

Error preparing Rocm 6.1.3 application with vintage hardware https://github.com/djygithub/craydgemm

### Operating System

NAME="Ubuntu" VERSION="22.04.4 LTS (Jammy Jellyfish)"

### CPU

 AMD Ryzen 7 1700 Eight-Core Processor

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.1.0

### ROCm Component

HIP

### Steps to Reproduce

Prepare application from https://github.com/djygithub/craydgemm

`/opt/rocm-6.1.3/bin/hipify-perl
 Matrix_Multiplication_GPU_DOUBLE_GIOPS_PINNED_TWO.cu > mmgpudoublegiops.cpp

/opt/rocm-6.1.3/bin/hipcc -O2 -o mmdblgpugiops  mmgpudoublegiops.cpp 

`mmgpudoublegiops.cpp:121:2: error: no matching function for call to 'hipHostAlloc'
  121 |         hipHostAlloc(&a,bytes_a,hipHostMallocDefault);
`

Worked around issue by changing the output file of hipify-perl (mmgpudoublegiops.cpp):

//allocate arrays
	//a = (int*) malloc( bytes_a );
	**hipHostMalloc**(&a,bytes_a,hipHostMallocDefault);
	CHECK(a == 0 ? hipErrorOutOfMemory : hipSuccess );
	//b = (int*) malloc( bytes_b );
	**hipHostMalloc**(&b,bytes_b,hipHostMallocDefault);
	CHECK(b == 0 ? hipErrorOutOfMemory : hipSuccess );
	//c = (int*) malloc( bytes_b );
	**hipHostMalloc**(&c,bytes_c,hipHostMallocDefault);
	CHECK(c == 0 ? hipErrorOutOfMemory : hipSuccess );

FWIW GFLOPS/second on the R9 using this application went up substantially from ROCM 4.1 to ROCM 6.1.3:
https://davidjyoung.com/cmg/sqldgemm24.pdf
![Slide36](https://github.com/user-attachments/assets/945125e8-a358-40c7-aea8-94de977fd53b)

Thanks.


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

david@r7pxeclient:~$ rocminfo --support
ROCk module version 6.7.0 is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.13
Runtime Ext Version:     1.4
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 7 1700 Eight-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 1700 Eight-Core Processor
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
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3000
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    32797028(0x1f47164) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32797028(0x1f47164) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32797028(0x1f47164) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx803
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon (TM) R9 Fury Series
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 29440(0x7300)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1000
  BDFID:                   2304
  Internal Node ID:        1
  Compute Unit:            64
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
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
  Packet Processor uCode:: 729
  SDMA engine uCode::      34
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    4194304(0x400000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    4194304(0x400000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
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
david@r7pxeclient:~$


### Additional Information

_No response_