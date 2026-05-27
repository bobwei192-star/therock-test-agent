# Occupancy Calculator for AMD in Excel (similar to CUDA)

> **Issue #1689**
> **状态**: open
> **创建时间**: 2022-02-22T15:44:15Z
> **更新时间**: 2024-09-11T09:46:18Z
> **作者**: nikl-i
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1689

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- Naraenda

## 描述

Hello! I've made recently an Occupancy Calculator for AMD GPUs similar to [CUDA Occupancy Calculator](https://docs.nvidia.com/cuda/cuda-occupancy-calculator/index.html#abstract)](https://docs.nvidia.com/cuda/cuda-occupancy-calculator/index.html), and would like to share it somehow. 
It's Excel file (like CUDA calculator) and includes several plots and summary information about occupancy factors with links to documentation and other materials.

If case you find useful, it would be great if you could suggest a way to make it more available to community (add to docs or something).
Thanks!

Screenshots:
![occupancy-calc-screenshot-1](https://user-images.githubusercontent.com/10510770/155161767-bc590472-f072-4576-bc46-21648e543acb.png)
![occupancy-calc-screenshot-2](https://user-images.githubusercontent.com/10510770/155161774-868dc1e1-a3be-48b8-bac9-016a4e48eb8e.png)
![occupancy-calc-screenshot-3](https://user-images.githubusercontent.com/10510770/155161776-b922c3c9-6b18-4b2d-945d-fbf1f651038d.png)

Calculator inself (*.xlsx file in *.zip archive):
[ROCm-Occupancy-Calculator.zip](https://github.com/RadeonOpenCompute/ROCm/files/8117804/ROCm-Occupancy-Calculator.zip)

---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2022-02-23T11:02:34Z)

Hi @nikowleye,
Thanks for reaching out.
Very much appreciations to you for sharing this document and information to us, cool.
I will discuss internally and update asap. Thank you.

---

### 评论 #2 — Rmalavally (2022-03-03T04:03:45Z)

Thank you for sharing your document, @nikowleye. We are discussing internally how to proceed with your submission and hope to give you an update soon.

Regards,
AMD ROCm Documentation Team


---

### 评论 #3 — yugr (2022-08-12T11:52:41Z)

@Rmalavally hi, just curious, are there plans to integrate this into ROCm?

---

### 评论 #4 — mazhaojia123 (2023-05-18T11:51:16Z)

Hi, @nikl-i. 

I have some questions about the value of VGPR per CU. Is there any evidence that one CU have 65536 VGPRs ? 

Based on the information provided in *[amd-cdna-whitepaper](https://www.amd.com/system/files/documents/amd-cdna-whitepaper.pdf)*, each CU of the MI100 has a 512KB-sized VGPR file. If there are 65536 VGPRs per CU, does that mean the VGPRs are all 64-bit in size?

---

### 评论 #5 — mazhaojia123 (2023-05-18T12:25:55Z)

> Hi, @nikl-i.
> 
> I have some questions about the value of VGPR per CU. Is there any evidence that one CU have 65536 VGPRs ?
> 
> Based on the information provided in _[amd-cdna-whitepaper](https://www.amd.com/system/files/documents/amd-cdna-whitepaper.pdf)_, each CU of the MI100 has a 512KB-sized VGPR file. If there are 65536 VGPRs per CU, does that mean the VGPRs are all 64-bit in size?

Hi, @ROCmSupport @Rmalavally .
It seems like MI100 has 65536\*2 32-bit VGPRs per CU? Are there any official materials or evidences?

---

### 评论 #6 — jlgreathouse (2023-05-18T22:47:06Z)

gfx9 "GCN" GPUs (i.e., not CDNA accelerators such as MI100 or MI200) have a compute unit architecture that:
- Has 4 separate SIMD16 units, each with their own VGPR file
- Each SIMD16 unit has 256x 64-wide vector general-purpose registers. Each lane of the vector register holds a 4-byte value.
- So a gfx9 GCN CU has: 4 bytes / lane * 64 lanes / VGPR * 256 VGPRs / SIMD * 4 SIMDs / CU = 256 KiB / CU
   - Depending on how you define a VGPR (e.g. if you're counting lanes), then yes, you could say that a CU has 64 * 256 * 4 = 65,536 GPRs. But note that this is really 256 vector registers, you can't individually access all of those GPRs from every lane.
   - Please note that waves are scheduled to the SIMD16, and any individual wave can only access at most 256 VGPRs

You can learn a bit more about the general "GCN" architecture in this presentation: https://www.slideshare.net/DevCentralAMD/gs4106-the-amd-gcn-architecture-a-crash-course-by-layla-mah, e.g., slide 19 describes the "4x SIMD16" architecture of our GCN CUs and shows the VGPR size. See also https://www.olcf.ornl.gov/wp-content/uploads/2019/10/ORNL_Application_Readiness_Workshop-AMD_GPU_Basics.pdf.

On the MI100 CDNA1 accelerator, the compute unit architecture:
- Also has 4 separate SIMD16 units, each with their own vector register file
- Each SIMD16 unit has 512x 64-wide vector registers. 
   - Please note that I did not say general-purpose registers. The register file in MI100 is split in half. There are 256x general-purpose vector registers, and 256x "accumulation" registers that are for use by the matrix multiplication instructions.
   -  "Normal" code cannot easily use these AccVGPRs, because the only VALU instructions that can use them are mov instructions. Our compiler can use these registers for spills & fills from traditional "ArchVGPRs", but you can't use them to e.g. feed an add operation.
   - As described in the CDNA architecture guide (Section 3.6.4 https://www.amd.com/system/files/TechDocs/instinct-mi100-cdna1-shader-instruction-set-architecture%C2%A0.pdf), on MI100 you _always_ allocate an identical number of ArchVGPRs and AccVGPRs. So if you make a kernel that uses 256 VGPRs, you also spend 256 AccVGPRs.
- So from a storage perspective, Figure 5 of the CDNA whitepaper (https://www.amd.com/system/files/documents/amd-cdna-whitepaper.pdf) is correct.
   - 4 bytes / lane * 64 lanes / register * 512 registers / SIMD = 128 KiB of registers per SIMD (and with 4 SIMDs / CU, this yields your calculation of 512 KiB / CU)
- However, from an occupancy calculation perspective, doubling the GPR count on MI100 would not give you extra occupancy for an otherwise identical kernel compared to GCN. Because those new registers can't be used for "normal" architected VGPRs.

On the MI200 CDNA2 accelerator, the compute unit architecture:
- Also has 4 separate SIMD16 units, each with their own vector register file
- Each SIMD16 unit has 512x 64-wide vector general-purpose registers. 
   - On CDNA2, we increased the generality of the register file. All 512 registers can be used for _either_ Arch VGPRs or Acc VGPRs.
   - Any individual wave can only access up to 256 Arch VGPRs and up to 256 Acc VGPRs (See Section 3.6.4 of https://www.amd.com/system/files/TechDocs/instinct-mi200-cdna2-instruction-set-architecture.pdf), but is possible to have 2 waves each with 256 Arch VGPRs and 0 Acc VGPRs on the same SIMD in MI200.
- So from both a storage and an occupancy perspective, MI200 has:
   - 4 bytes / lane * 64 lanes / register * 512 VGPRs / SIMD = 128 KiB of VGPRs per SIMD (and with 4 SIMDs / CU, this yields 512 KiB / CU)

For a bit more coverage of the MI200 topic, you can see the media reports from our HotChips talk: https://chipsandcheese.com/2022/09/18/hot-chips-34-amds-instinct-mi200-architecture/ which gives some extra commentary from the Q&A session of the talk itself (https://hc34.hotchips.org/assets/program/conference/day1/GPU%20HPC/HC2022.AMD.AlanSmith.v14.Final.20220820.pdf), where this was covered in 1 bullet point on slide 8.
Thanks!

---

### 评论 #7 — mazhaojia123 (2023-05-19T06:38:06Z)

Hi, @jlgreathouse.
Thank you very much, your answer is very helpful to me!

---

### 评论 #8 — itej89 (2024-07-20T03:18:11Z)

Hi, I would like to know if there is an updated version of this tool for latest MI300 series? Thanks in advance!

---

### 评论 #9 — etiennemlb (2024-09-11T09:32:10Z)

@jlgreathouse

> gfx9 "GCN" GPUs (i.e., not CDNA accelerators such as MI100 or MI200) have a compute unit architecture that:
> * Each SIMD16 unit has 256x 64-wide vector general-purpose registers. Each lane of the vector register holds a 4-byte value.
> * So a gfx9 GCN CU has: 4 bytes / lane * 64 lanes / VGPR * 256 VGPRs / SIMD * 4 SIMDs / CU = 256 KiB / CU
>
> On the MI200 CDNA2 accelerator, the compute unit architecture:
> * Each SIMD16 unit has 512x 64-wide vector general-purpose registers.
> * So from both a storage and an occupancy perspective, MI200 has:
>   
>   * 4 bytes / lane * 64 lanes / register * 512 VGPRs / SIMD = 128 KiB of VGPRs per SIMD (and with 4 SIMDs / CU, this yields 512 KiB / CU)

That seems like a regression in capabilities from CDNA2 to CDNA3. Am I reading that correctly ?

For instance, for a kernel with:
wg size   256
lds/wg    1024
vgpr/lane 64
sgpr/wave 16

Id get 50% occupancy on CDNA3 and 100% on CDNA2 ?






























































---
