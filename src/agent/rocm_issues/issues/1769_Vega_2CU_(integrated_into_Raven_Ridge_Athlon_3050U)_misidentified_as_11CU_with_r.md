# Vega 2CU (integrated into Raven Ridge Athlon 3050U) misidentified as 11CU with rocminfo and clinfo - resulting in OpenCL workload crashes/freezes. 

> **Issue #1769**
> **状态**: closed
> **创建时间**: 2022-07-13T22:57:13Z
> **更新时间**: 2024-05-23T17:36:20Z
> **关闭时间**: 2024-05-23T17:36:20Z
> **作者**: iamhumanipromise
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1769

## 描述

**Firstly: I understand that iGPUs/APUs/Raven Ridge is NOT officially supported. That being said, if someone is able to resolve this for the correct identification of compute units that would be cool. I am currently using the amd-opencl-dev package from the AUR. I have tested this on Arch stable, Manjaro stable, testing and unstable, and SteamOS rolling. Same results.** *The use case that triggered this post regarding OpenCL workloads freezing my SO's laptop is for OpenCL accelerated Darktable on an Athlon 3050U. (A laptop with a dedicated RDNA2 GPU is not in the budget at this time, nor is switching to Apple Silicon.) Hopefully someone resolving this would benefit others, not just me. 

My understanding is that Raven Ridge can have *up to* 11CUs, but for some reason ROCm is just automatically assigning that number to all RR devices, rather than the actual specific number of CUs? (In this case, 2CUs available in total) 

Attached are the results of rocminfo and clinfo. Please let me know if anything else is needed for investigating further

[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/9106602/clinfo.txt)

[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/9106603/rocminfo.txt)


---

## 评论 (2 条)

### 评论 #1 — Spacefish (2022-08-18T19:43:42Z)

Probably the Raven Ridge Chip has 11CUs and the others are just "fused off" in the cheaper SKUs and they never bothered to include all the SKUs in the config files for ROCM.

Edit: looked at the source a littlebit, this info seems to be read from the GPU chip itself..

---

### 评论 #2 — ppanchad-amd (2024-05-09T15:14:07Z)

@iamhumanipromise Sorry for the lack of response. Do you still need still assistance? Thanks!

---
