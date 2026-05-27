# Naples / AMDGPU-PRO maximum GPU count 

> **Issue #74**
> **状态**: closed
> **创建时间**: 2017-01-11T12:44:51Z
> **更新时间**: 2017-02-22T15:53:37Z
> **关闭时间**: 2017-02-22T15:53:37Z
> **作者**: MathiasMagnus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/74

## 描述

This question is a follow-up of the original question asked at [devgurus](https://community.amd.com/thread/210699). Copy-pasting text there:

With AMD's Naples server dies allegedly sporting 128 PCI-E 3.0 lanes, it occured to out group to revisit the question of maximum number of GPUs one can leverage in such a system, without having to jump through flaming hoops. 8 channel DDR4 sounds like a sound foundation to decent main memory bandwidth. With P2P transfer between the GPUs depending on the use case, one might be content with

- x16 / GPU = 8 GPUs
- x8 / GPU = 16 GPUs
- x4 / GPU = 32 GPUs

Some configurations will require extenders such as [these](https://community.amd.com/external-link.jspa?url=http%3A%2F%2Fmagma.com%2Fproducts%2Fpcie-expansion%2Fexpressbox-3600%2F) Magma extenders. Now I recall that shoving that many GPUs into a single system is no small feat, due to the issue of BIOS wanting to allocate memory for every PCIE device with only 32 bits, several hundred MBs per device. With Naples around the corner and it having such a ridiculous amount of PCIE lanes: 

1. Is there a limit imposed by any part of the AMDGPU-PRO stack on the number of maximum GPUs one can put in a system?
2. Will Naples help in regard to BIOS issues or is that strictly a matter of the motherboard vendor (extended memory and such)?
3. Is there sample code in the ROCm repo to get P2P transfer? (Through ANY of the supported APIs?)

Answers are much appreciated.

---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-01-11T14:08:57Z)

We can not comment on Naples,  But ROCm we design the stack to support 64 GPU’s in a system.      AMDGPUpro was optimized for Workstation is being tested up to  6 GPU system,  The issue is when you have head on stack.    AMDGPUpro peer to peer capability is based DirectGMA which uses relatively small window BASE ADDRESS window 256K.

ROCm has Peer to Peer API for MultiGPU and also Peer to Peer Via RDMA.  Also ROCm was designed to work with Large Base Address Register - multi-gigabyte


To learn more about ROCm please use this site

https://rocm.github.io/documentation.html

HIP
http://gpuopen-professionalcompute-tools.github.io/HIP/
https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/blob/master/docs/markdown/hip_porting_guide.md

HCC
http://scchan.github.io/hcc/

Via  HIP to simplify your use of Peer to Peer we are porting NCCL over to run on ROCm

We now have developer release of OpenCL now on ROCm that will be doing regular update on for performance and conformance


Greg


On Jan 11, 2017, at 6:44 AM, Nagy-Egri Máté Ferenc <notifications@github.com<mailto:notifications@github.com>> wrote:


This question is a follow-up of the original question asked at devgurus<https://community.amd.com/thread/210699>. Copy-pasting text there:

With AMD's Naples server dies allegedly sporting 128 PCI-E 3.0 lanes, it occured to out group to revisit the question of maximum number of GPUs one can leverage in such a system, without having to jump through flaming hoops. 8 channel DDR4 sounds like a sound foundation to decent main memory bandwidth. With P2P transfer between the GPUs depending on the use case, one might be content with

  *   x16 / GPU = 8 GPUs
  *   x8 / GPU = 16 GPUs
  *   x4 / GPU = 32 GPUs

Some configurations will require extenders such as these<https://community.amd.com/external-link.jspa?url=http%3A%2F%2Fmagma.com%2Fproducts%2Fpcie-expansion%2Fexpressbox-3600%2F> Magma extenders. Now I recall that shoving that many GPUs into a single system is no small feat, due to the issue of BIOS wanting to allocate memory for every PCIE device with only 32 bits, several hundred MBs per device. With Naples around the corner and it having such a ridiculous amount of PCIE lanes:

  1.  Is there a limit imposed by any part of the AMDGPU-PRO stack on the number of maximum GPUs one can put in a system?
  2.  Will Naples help in regard to BIOS issues or is that strictly a matter of the motherboard vendor (extended memory and such)?
  3.  Is there sample code in the ROCm repo to get P2P transfer? (Through ANY of the supported APIs?)

Answers are much appreciated.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/74>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQRl9RZh2DAr4VQ3KjHqde7kbOl9ks5rRM7DgaJpZM4Lgiaj>.



---
