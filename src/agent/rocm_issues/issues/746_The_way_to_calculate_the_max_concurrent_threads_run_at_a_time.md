# The way to calculate the max concurrent threads run at a time?

> **Issue #746**
> **状态**: closed
> **创建时间**: 2019-03-20T01:15:53Z
> **更新时间**: 2019-05-06T04:01:23Z
> **关闭时间**: 2019-03-20T03:42:32Z
> **作者**: ghostplant
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/746

## 标签

- **Question** (颜色: #cc317c)

## 描述

There are naming differences as well as hardware differences when comparing AMD ROCm with NVidia CUDA, so what is the way to compute the max concurrent threads run at a time using HIP API for different AMD architectures?

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2019-03-20T02:16:16Z)

Programmatically? No, not directly. There is no API akin to `cudaOccupancyMaxActiveBlocksPerMultiprocessor()` at this time. 

I'll use the terminology "wavefront" (which you might know as warp in CUDA), and "workgroup" (which you might know as thread block in CUDA). You can find out more about the details of our hardware in:
 - [This GCN Crash Course presentation.](https://www.slideshare.net/DevCentralAMD/gs4106-the-amd-gcn-architecture-a-crash-course-by-layla-mah)
 - [This GCN whitepaper](https://www.amd.com/documents/gcn_architecture_whitepaper.pdf)
 - [This GCN presentation](http://developer.amd.com/wordpress/media/2013/06/2620_final.pdf)

If you want to see how some of our performance tools like [RCP](https://github.com/GPUOpen-Tools/RCP/) perform occupancy calculations, you can see their [documentation here](https://github.com/GPUOpen-Tools/RCP/blob/v5.6/docs/source/occupancy.rst#kernel-occupancy-for-amd-radeon-hd-7000-series-or-newer-based-on-graphics-core-next-architecture).

If you want to manually calculate occupancy limits, there are a number of rules to keep in mind (many of which are covered by the RCP manual above):
- AMD GPUs are divided into compute units (CUs).
    - For instance, Radeon Vega 64 GPUs have 64 CUs.
- Each CU is divided into 4x 16-wide SIMDs.
- Each SIMD can hold up to 10 wavefronts (thus you could fit up to 40 waves in a CU -- there are 4 buckets, one for each SIMD, that can each hold 10 waves)
- Each CU can hold up to 16 workgroups, and all wavefronts from a CU must be on the same CU
    - So if you are running 2-wavefront workgroups, you could have a maximum of 32 wavefronts
    - If you are running a 1-wave workgroup, this limitation does not hold. This 16-workgroup limitation is for resources such as the inter-wavefront barrier hardware within the CU.
- There are a total of 256 VGPRs in each SIMD, so if you use a lot of VGPRs in your kernel, you may only be able to fit a small number of wavefronts
    - For instance, if you want to use 129 VGPRs in your kernel, you could only fit 1 wavefront in each SIMDs, so 4 wavefronts in the CU.
    - [That would also limit your workgroup size to 256 threads in this case.](https://github.com/RadeonOpenCompute/ROCm/issues/330)
- There is a total of 64 KiB of LDS space in the entire compute unit, so if you allocate too much LDS space (shared memory in HIP, local data in OpenCL) you can limit the number of workgroups in your CU
    - For instance, if you allocate 16 KiB of LDS data for each workgroup, you could only fit 4 workgroups in your CU.
- There are 512 SGPRs in each SIMD, so if you allocate too many SGPRs, it can limit the number of waves per SIMD.
    - For instance, if you allocate 100 SGPRs per wave, then you could only fit 5 waves in each SIMD, so only up to 20 waves in the CU.
- AMD GPUs are also split into [shader engines](https://www.anandtech.com/show/13923/the-amd-radeon-vii-review/2) (SEs), each of which has a subset of the total CUs.
    - See more info on [Slide 52 here](https://www.slideshare.net/DevCentralAMD/gs4106-the-amd-gcn-architecture-a-crash-course-by-layla-mah).
    - For instance, Vega 10 chips have 4 SEs, our current APUs have a single SE, Polaris 11 and 12 have 2 SEs.
    - In ROCm, each of these SEs will only schedule {Number of CUs in that SE} * 32 compute waves into all of the CUs within that SE.
    - This allows us to make sure there is space for graphics work to make forward progress, for instance.

---

### 评论 #2 — ghostplant (2019-03-20T03:42:32Z)

@jlgreathouse Very detailed, but quite complex to me as the calculation depends on lots of resources and even including analyzing the algorithm. So in a general way, evaluating the best by enumerating every combination cases among blocks/threads/shared-mem/vgprs might be a better choice for me to figure out how to well run a self-defined kernel on some GPUs.
Thank you!

---

### 评论 #3 — ghostplant (2019-05-06T04:01:23Z)

Hi @jlgreathouse, can you suggest a recommended VGPRs/SGPRs profiler for HIP kernel program? I found the most critical bottleneck is caused by these 2 points.

---
