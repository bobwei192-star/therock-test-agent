# [Issue]: amdsmi on Windows won't output anything for GPU related commands

> **Issue #2662**
> **状态**: closed
> **创建时间**: 2023-11-22T17:35:06Z
> **更新时间**: 2024-10-01T19:15:51Z
> **关闭时间**: 2024-10-01T19:15:51Z
> **作者**: NeedsMoar
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2662

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

### Problem Description

amdsmi.exe on windows won't report any information.

### Operating System

Microsoft Windows 10 Pro for Workstations 10.0.19045 N/A Build 19045

### CPU

AMD Ryzen Threadripper PRO 5975WX 32-Cores

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

5.5.0 (Windows)

### ROCm Component

amdsmi

### Steps to Reproduce

Run amdsmi with any command.  Only ill-formatted commands, no input (help) or errors due to OS type / host / baremetal related to command context display.  
list and all other commands show nothing. I attempted to plug in the GPU number (0 according to hipinfo and common sense) and same nothing. 
Output to file also fails. This happened before and after I installed a 4090 as well;  it is currently the card being used for both connected displays until I get time to switch those and test the cuda-only mode drivers for the 4090 and see if speed gains are  worth the hassle of restricting that card's features,  so the 7900xtx is headless.  nvidia-smi works fine.  I haven't seen any driver conflicts between the two. 

### Output of /opt/rocm/bin/rocminfo --support

Windows doen't have rocminfo and the support flag doesn't seem to work on hipinfo, but:

hipinfo

--------------------------------------------------------------------------------
device#                           0
Name:                             AMD Radeon RX 7900 XTX
pciBusID:                         35
pciDeviceID:                      0
pciDomainID:                      0
multiProcessorCount:              48
maxThreadsPerMultiProcessor:      2048
isMultiGpuBoard:                  0
clockRate:                        2526 Mhz
memoryClockRate:                  1250 Mhz
memoryBusWidth:                   0
totalGlobalMem:                   23.98 GB
totalConstMem:                    2147483647
sharedMemPerBlock:                64.00 KB
canMapHostMemory:                 1
regsPerBlock:                     0
warpSize:                         32
l2CacheSize:                      4194304
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    65536
maxGridSize.z:                    65536
major:                            11
minor:                            0
concurrentKernels:                1
cooperativeLaunch:                0
cooperativeMultiDeviceLaunch:     0
isIntegrated:                     0
maxTexture1D:                     16384
maxTexture2D.width:               16384
maxTexture2D.height:              16384
maxTexture3D.width:               2048
maxTexture3D.height:              2048
maxTexture3D.depth:               2048
isLargeBar:                       0
asicRevision:                     0
maxSharedMemoryPerMultiProcessor: 64.00 KB
clockInstructionRate:             1000.00 Mhz
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           1
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        1
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
gcnArchName:                      gfx1100
peers:
non-peers:                        device#0

memInfo.total:                    23.98 GB
memInfo.free:                     23.86 GB (99%)

Additional info:
Memory: 512GB (8x64GB) 3200MHz ECC RDIMMs  
Driver Version
23.20.17.03-231016a-396906C-AMD-Software-Adrenalin-Edition
Resizable bar is on gpu-z reports:
BAR0	32768 MB
BAR1	256 MB

as expected.  Device manager shows no conflicts.  
NUMA is setup as single node right now but I could flip on L3 as SRAT to get things onto 4 nodes if that's some suspected issue (don't know why it would be but hey).  IOMMU is off.

