# [Issue]: Updating from Adrenaline 25.1.1 to 25.3.1 broke the ROCm acceleration of 7900XTX, Windows, Adrenaline, HIP, Zluda, Comfy UI fork. Trying WSL2+ROCm.

- **Issue #:** 4459
- **State:** closed
- **Created:** 2025-03-07T10:19:02Z
- **Updated:** 2025-06-14T12:39:40Z
- **Labels:** Under Investigation, AMD Radeon RX 7900XTX
- **URL:** https://github.com/ROCm/ROCm/issues/4459

### Problem Description

Updating from Adrenaline 25.1.1 to 25.3.1 broke the ROCm acceleration of 7900XTX, Windows, Adrenaline, HIP, Zluda, Comfy UI fork

I'm having gargantuan issues getting pytorch applications that worked under CUDA to work under ROCm after I upgraded from a RTX3080 to a 7900XTX

### Operating System

PS C:\Users\FatherOfMachines>  (Get-WmiObject Win32_OperatingSystem).Version 10.0.22631

### CPU

PS C:\Users\FatherOfMachines>   (Get-WmiObject win32_Processor).Name 13th Gen Intel(R) Core(TM) i7-13700F

### GPU

PS C:\Users\FatherOfMachines>   (Get-WmiObject win32_VideoController).Name AMD Radeon RX 7900 XTX

### ROCm Version

C:\Program Files\AMD\ROCm\6.2\bin>hipcc --version HIP version: 6.2.41512-db3292736 clang version 19.0.0git (git@github.amd.com:Compute-Mirrors/llvm-project 5353ca3e0e5ae54a31eeebe223da212fa405567a) Target: x86_64-pc-windows-msvc Thread model: posix InstalledDir: C:\Program Files\AMD\ROCm\6.2\bin  C:\Program Files\AMD\ROCm\6.2\bin>hipinfo  device# 0 Name: AMD Radeon RX 7900 XTX pciBusID: 3 pciDeviceID: 0 pciDomainID: 0 multiProcessorCount: 48 maxThreadsPerMultiProcessor: 2048 isMultiGpuBoard: 0 clockRate: 2482 Mhz memoryClockRate: 1250 Mhz memoryBusWidth: 0 totalGlobalMem: 23.98 GB totalConstMem: 2147483647 sharedMemPerBlock: 64.00 KB canMapHostMemory: 1 regsPerBlock: 0 warpSize: 32 l2CacheSize: 4194304 computeMode: 0 maxThreadsPerBlock: 1024 maxThreadsDim.x: 1024 maxThreadsDim.y: 1024 maxThreadsDim.z: 1024 maxGridSize.x: 2147483647 maxGridSize.y: 65536 maxGridSize.z: 65536 major: 11 minor: 0 concurrentKernels: 1 cooperativeLaunch: 0 cooperativeMultiDeviceLaunch: 0 isIntegrated: 0 maxTexture1D: 16384 maxTexture2D.width: 16384 maxTexture2D.height: 16384 maxTexture3D.width: 2048 maxTexture3D.height: 2048 maxTexture3D.depth: 2048 hostNativeAtomicSupported: 1 isLargeBar: 0 asicRevision: 0 maxSharedMemoryPerMultiProcessor: 64.00 KB clockInstructionRate: 1000.00 Mhz arch.hasGlobalInt32Atomics: 1 arch.hasGlobalFloatAtomicExch: 1 arch.hasSharedInt32Atomics: 1 arch.hasSharedFloatAtomicExch: 1 arch.hasFloatAtomicAdd: 1 arch.hasGlobalInt64Atomics: 1 arch.hasSharedInt64Atomics: 1 arch.hasDoubles: 1 arch.hasWarpVote: 1 arch.hasWarpBallot: 1 arch.hasWarpShuffle: 1 arch.hasFunnelShift: 0 arch.hasThreadFenceSystem: 1 arch.hasSyncThreadsExt: 0 arch.hasSurfaceFuncs: 0 arch.has3dGrid: 1 arch.hasDynamicParallelism: 0 gcnArchName: gfx1100 peers: non-peers: device#0  memInfo.total: 23.98 GB memInfo.free: 23.84 GB (99%)

### ROCm Component

_No response_

### Steps to Reproduce

- https://github.com/LeagueRaINi/ComfyUI.git
- Adrenaline 25.3.1
- HIP 6.2.4
- Zluda 

Update from Adrenaline 25.1.1 to 25.3.1 breaks ROCm acceleration. E.g. SD1.5 T2I workflow from <10s now takes 662s.

GIST with the workflow, output repo and details
https://gist.github.com/OrsoEric/5d2222201d167a40486a037e9d6d063b


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

I have been trying to get ROCm acceleration working for about a month. I can get pretty far with enormous effort, but at some point a Comfy UI node won't work and requires me to discard it all and rebuild a new stack from the ground up with another fork to get further.

I did get Flux to accelerate well with this fork + Zluda
https://github.com/LeagueRaINi/ComfyUI.git
But it's too far the mainline and doesn't support Wan nodes, and with the update to Adrenaline 25.3.1 the acceleration broke completely

I'll refrain from wiping the stack so you can ask me diagnostics steps.