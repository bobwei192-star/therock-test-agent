# Will my setup rx 580 (Polaris/gfx803) setup function in AMD's ROCm and HIP applications (eg. blender when it adds legacy cards support) ?

> **Issue #1745**
> **状态**: closed
> **创建时间**: 2022-05-29T13:23:16Z
> **更新时间**: 2024-01-26T08:45:19Z
> **关闭时间**: 2024-01-26T08:45:19Z
> **作者**: CosmicFusion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1745

## 描述

OS : Arch linux Rolling x64
System : 

{CPU : i5-4570s
               RAM : 16GB 1666mhz ddr3
               GPU : RX 580 8GB}


Driver : mesa-tkg-git + amdgpu-pro (userspace only) + ROCm

Mesa ver :  22.2.0-devel

AMDGPU-PRO ver : 22.10

AMDGPU-PRO pkgs : 


{local/amdgpu-pro-libgl 22.10_1395274-1
                                    local/amf-amdgpu-pro 22.10_1395274-1
                                    local/lib32-amdgpu-pro-libgl 22.10_1395274-1
                                    local/lib32-opencl-legacy-amdgpu-pro 22.10.1_1401426-1
                                    local/lib32-vulkan-amdgpu-pro 22.10_1395274-1
                                     local/opencl-legacy-amdgpu-pro 22.10.1_1401426-1
                                     local/vulkan-amdgpu-pro 22.10_1395274-1}



ROCm ver : 5.1.1

ROCm pkgs : 


{local/rocblas 5.1.1-1 (patched for polaris)
                       local/rocm-cmake 5.1.3-1
                       local/rocm-core 5.1.3-1
                       local/rocm-device-libs 5.1.1-1
                       local/rocm-hip-runtime 5.1.3-1
                       local/rocm-language-runtime 5.1.3-1
                       local/rocm-llvm 5.1.1-1
                       local/rocm-opencl-runtime 5.1.1-1 (patched for polaris)
                       local/rocminfo 5.1.1-2}


my end goal is to know if i have a system that : 

- [x] Supports AMD's ROCm OpenCL runtime
- [x] Supports AMD's ROCm HIP runtime
- [ ] Supports Blender's Implementation of ROCm HIP 


And i have included as much debugging outputs as i can. 
                      
[clinfo output](https://github.com/RadeonOpenCompute/ROCm/files/8793412/cl-output.txt)
[hipInfo output](https://github.com/RadeonOpenCompute/ROCm/files/8793413/hip-output.txt)
[rocminfo output](https://github.com/RadeonOpenCompute/ROCm/files/8793414/rocm-output.txt)
["vulkaninfo --summary" output](https://github.com/RadeonOpenCompute/ROCm/files/8793415/vulkan-output.txt)



---

## 评论 (6 条)

### 评论 #1 — xuhuisheng (2022-06-24T13:12:33Z)

1. arch linux might merge gfx803 patch to support gfx803. Or not. <https://github.com/rocm-arch/rocm-arch/issues/741>
2. hip did support gfx803. It just a simple layer on the top of driver, compiler.
3. not familiar with blender.

---

### 评论 #2 — CosmicFusion (2022-06-24T13:16:28Z)

> 1. arch linux might merge gfx803 patch to support gfx803. Or not. <https://github.com/rocm-arch/rocm-arch/issues/741>
> 2. hip did support gfx803. It just a simple layer on the top of driver, compiler.
> 3. not familiar with blender.

```
1. arch linux might merge gfx803 patch to support gfx803. Or not. <https://github.com/rocm-arch/rocm-arch/issues/741>
```

Actually I don't know why this issue is open , your patch is already merged into the AUR .

```
hip did support gfx803. It just a simple layer on the top of driver, compiler.
```

Well that's a relief.

```
not familiar with blender.
```

Guess we'll wait and see then :(

---

### 评论 #3 — acxz (2022-07-10T14:40:55Z)

> arch linux might merge gfx803 patch to support gfx803.

https://github.com/rocm-arch/rocm-arch/issues/741#issuecomment-1093822651


> Actually I don't know why this issue is open

https://github.com/rocm-arch/rocm-arch/issues/741#issuecomment-1093968521

---

### 评论 #4 — Mhowser (2022-09-08T04:24:05Z)

Has anybody been able to test this now that the patch is out? I would do it myself, but due to IRL circumstances I can't swap out my current operating system for Arch on my desktop PC yet.

---

### 评论 #5 — abhimeda (2024-01-26T05:35:45Z)

@CosmicFusion  Hi, is your issue resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #6 — CosmicFusion (2024-01-26T08:45:08Z)

I no longer own the card, so for me it's technically resolved 

---
