# [Issue]: rocm 5.5 matrix multiply fails with "invalid device function" on

- **Issue #:** 5128
- **State:** closed
- **Created:** 2025-07-31T10:30:51Z
- **Updated:** 2025-07-31T20:55:56Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5128

### Problem Description

I chose this older version because it (still) supports AMD Radeon Pro VII (gfx906), which is confirmed by running "hipinfo --platform"
See Additional Information below.

Compiling in visual studio 2022 using the rocm extension works, i.c. on <samples>/HIP-Basic/matrix_multiplication, using Debug.
Tracing the execution up to line 192, where matrix_multiplication_kernel is started, is ok, message `Matrix multiplication: [2048x1024] * [1024x1024], block size: 16x16`.
The kernel fails to execute, HIP_CHECK(hipGetLastError()) yields `An error encountered: "invalid device function" at main.hip:196`.
As known, the Radeon Pro VII has spectacular fp64 performance, so I am loath to give it up and find it nearly immoral that support for it has been dropped at or just following Rocm 5.6.0. So I would appreciate a fix or advice how to succeed here quite much!
I tried whether I should perhaps use the rocm provided driver (31.0.21002.0). The results with recent and older drivers were the same.

### Operating System

Windows 11 pro 24H2, build 26100.4770

### CPU

AMD Ryzen 9 5900X

### GPU

AMD Radeon PRO VII

### ROCm Version

5.5.0

### ROCm Component

HIP

### Steps to Reproduce

- Install rocm 5.5.0 on windows running visual studio 2022 (11 in my case, probably 10 could be used as well). Include the visual studio extension;
   Include, optionally, driver installation (Have tried with up to date driver and with rocm supplied driver). I now have driver version 31.0.21002.0.
- Install the samples at 5.5.0 from https://github.com/rocm/rocm-examples
- select/execute ROCM-examples\HIP-Basic\matrix_multiplication\matrix_multiplication_vs2022.sln.
- Compile in Debug, ctrl-F7 will do.
- trace using F10, proceed to line 196 and see whether there is the errror report as described above.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

HipInfo indicates:
```
device#                           0
Name:                             AMD Radeon Pro VII
pciBusID:                         11
pciDeviceID:                      0
pciDomainID:                      0
multiProcessorCount:              60
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  0
clockRate:                        1700 Mhz
memoryClockRate:                  1000 Mhz
memoryBusWidth:                   0
totalGlobalMem:                   15.98 GB
totalConstMem:                    2147483647
sharedMemPerBlock:                64.00 KB
canMapHostMemory:                 1
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      4194304
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            9
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
gcnArchName:                      gfx906:sramecc-:xnack-
peers:
non-peers:                        device#0

memInfo.total:                    15.98 GB
memInfo.free:                     15.86 GB (99%)
```