# what is the key issue for GCNs

> **Issue #1456**
> **状态**: closed
> **创建时间**: 2021-04-18T04:49:18Z
> **更新时间**: 2021-06-04T04:26:36Z
> **关闭时间**: 2021-06-04T04:26:36Z
> **作者**: kemaliu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1456

## 描述

now i am try to optimize OCL code on GCN GPU, and want to know some VRAM detail.
I cannot understand the GCN's memory archietecture.
nomally,MMU wont affect the memory IO bandwidth if memory  address is page aligned.
but according to the description in https://github.com/RadeonOpenCompute/ROCm/issues/147
2MB fragments  will enhance bandwidth will enhance vega's bandwidth from 260GB/s to 400+GB/s
I check the driver code, it seam that 2MB fragment forcing BO allocated base address being 2MB align, and GMC PTE set fragment according to fragment size.
But it should not affect the bandwidth so much.
during continuous page-align virtual mem loading, the key issue should be memory bank/channel confliction.
why fragmention setting cause so much memory bandwidth diff? 
does it because the translating from virutal to phy address handled by software,  nor hw like cpu's MMU?
BTW: what is the interleaving mode for GCN's memory?
row--bank--channel--col or some other mode?the mode is fixed by hardware or can be adjusted by driver?

thanks

---

## 评论 (10 条)

### 评论 #1 — ROCmSupport (2021-04-19T07:06:06Z)

Thanks @kemaliu for reaching out.
I will check and get back asap.
Thank you.

---

### 评论 #2 — jlgreathouse (2021-04-19T17:21:08Z)

I believe in the issue described in #147 is related to TLB reach. Your description of "translation from virtual to physical address handled by software, not HW like CPU's MMU" is incorrect. GCN and CDNA GPUs have a hardware TLB system, with hardware page-table walker, very much like you would find on a CPU. Each compute unit has a separate L1 TLB for the Scalar L1 Data cache, Instruction Cache, and Vector L1 Data Cache. 

There is a shared L2 TLB on the chip. It supports caching of two different page sizes into a "smallK" and "bigK" cache, respectively. The bigK cache on the GCN GPUs you are asking about is 32k entries. If you set the fragment size to 2MiB, the L2 TLB can have a "reach" of up to 64 GiB. There is slightly more complexity to our hardware than this, but before the patch discussed in #147, our driver set the bigK page size to 64 KiB, which meant that the TLB only had a reach of up to 2 GiB. The Vega Frontier Edition discussed in #147 has 16 GiB of HBM, so constantly accessing locations across the entire 16 GiB would cause a large number of page table walks, reducing the achievable bandwidth. As such, the use of 2 MiB fragments increased the achievable bandwidth by reducing the amount of bandwidth spent on page table walks.

We interleave L2 cache banks on 256B boundaries, but the mapping of address bits to which L2 cache bank, and the DRAM row, bank, column, channel, and chip-select values are not made public for our GPUs.

---

### 评论 #3 — ROCmSupport (2021-04-20T05:27:24Z)

Thanks @jlgreathouse for the information shared.
@kemaliu , request you to close this issue if you are OK and do not have any more doubts.
Thank you.

---

### 评论 #4 — kemaliu (2021-04-20T18:07:59Z)

thanks for the responce
I have another 2 question about the wavefronts dispatching pattern.

I wrote some testing code.  enqueue single workgroup, localsize=256 globalsize=256
it seem that one workgroup(local size 256)  run on single SIMD, 
because the 4 wavefront, 16x16workitem of the workgroup run in certain order.
and the running order will be disturbed when  globalsize > 256.



question 1.
how many wavefronts can be piped in a single SIMD for multi workgroups whose local size is 256.
according to GCN white paper, there are 4 simd/CU, max 40wavefronts/ CU.It mean that 10 wavefronts can be running in 1 SIMD at save time.

As you know, 256 WI workgroup = 4 wavefronts.
if there are 10 workgroups in 1 CU . 40wavefront = 10workgroup. how the scheduler pipe the 10 workgroups in one CU?the max parallel wavefront number is 40 in a CU, and 10 in one SIMD.
If 1 workgroup(localsize256, 4wavefront) must run parallel in a simd, 10 wavefront of 1 SIMD can only hold 2 complte workgroups.
Does it mean that for workgroup(256 local size), the scheduler can only pipe 8 wavefronts in a single simd at same time, not 10?
or the 4 wavefronts of 1 workgroup can be devided to 2wavefront x 2 and run seperatly?

question 2.
what is the the workgroups dispatching pattern?multi workgroups are dispatched to different CU or different SIMD firstly?
for example, we enqueue 2 workgroup(local_size=256, global_size=512)
WG=workgroup, SIMD index is 0-3 in a CU. CU index start from 0. 

WG0 locate in CU0/SIMD0
where will WG1 be located? CU0/SIMD1 or CU1/SIMD0?


---

### 评论 #5 — jlgreathouse (2021-04-21T14:58:04Z)

While our current GCN and CDNA GPUs allows up 40 wavefronts in any particular CU, we have a limitation that we can only have (32 compute wavefronts * ${number_of_physical_cus}) wavefronts in flight at once. So a CU with 40 waves on it will necessarily mean that some CUs have fewer waves on them. (It's slightly more complex than this due to our multi-shader-engine design, but hopefully this makes the point clear). This design was partially done to leave room for things like pixel shader waves in graphics workloads, and partially to help mitigate under-utilization for workloads with waves that complete at different speeds.

Workgroups must run on the same CU, but different waves from a single workgroup can run in the same SIMD or different SIMDs. There is no limitation that waves from a workgroup must run in the same SIMD.

The workload dispatching pattern is that the asynchronous compute engine (ACE) reads the kernel dispatch packet, then cracks the kernel into workgroups. It distributes workgroups to the shader engines in a round-robin manner. See slides 8-16 of [this presentation](https://www.olcf.ornl.gov/wp-content/uploads/2019/09/AMD_GPU_HIP_training_20190906.pdf) for an illustration.

Once the workloads have been distributed to the SEs, the per-SE workgroup manager in each SE will crack the workgroups into 64-thread wavefronts in an X-then-Y-then-Z walk of the workgroup's dimensionality. The workgroup manager will look for any CU with enough open wave-slots, and then attempt to schedule the waves into those slots once the entire workgroup can fit. In an empty GPU, the workgroup manager will attempt to spread workgroups across CUs (e.g., sending two workgroups to an empty SE will result in one workgroup in two different CUs), and it will attempt to spread wavefronts across SIMDs (e.g. sending a 4-wave workgroup to an empty CU will result in one wave per SIMD).

You could attempt to analyze these work distribution algorithms using the HW_ID values as demonstrated in the HIP `__smid()` function, [as described here](https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-4.1.1/include/hip/hcc_detail/device_functions.h#L1310).

---

### 评论 #6 — DTolm (2021-04-25T17:56:15Z)

@jlgreathouse @kemaliu 
I believe I have a related issue (L2 cache bank conflicts) in my VkFFT code. I can describe it as the following: bandwidth drops when I try to do distant, but coalesced memory accesses, i.e. data are still grouped in 128b transactions but target addresses with > 2^18 bytes between them (and the bigger the distance - the bigger the drop). This has the biggest impact when distant accesses are separated by the power of 2 amount of bytes (I have previously asked about this here: https://github.com/RadeonOpenCompute/ROCm/issues/1294). 

The only documentation on this issue available is from Tahiti age: https://rocmdocs.amd.com/en/latest/Programming_Guides/Opencl-optimization.html#channel-conflicts

The issue is present both in Vulkan and HIP backends of VkFFT. I tried to solve this by splitting the buffer logically into smaller chunks of memory (~16KB range), though AMD Vulkan implementation couldn't handle more than 128 buffers bound (even though It was supported by the specification). So, I am not sure what can be done about this without an understanding of what is actually happening. Nvidia GPUs don't seem to have this issue.

---

### 评论 #7 — kemaliu (2021-05-06T02:17:49Z)

> 
> 
> @jlgreathouse @kemaliu
> I believe I have a related issue (L2 cache bank conflicts) in my VkFFT code. I can describe it as the following: bandwidth drops when I try to do distant, but coalesced memory accesses, i.e. data are still grouped in 128b transactions but target addresses with > 2^18 bytes between them (and the bigger the distance - the bigger the drop). This has the biggest impact when distant accesses are separated by the power of 2 amount of bytes (I have previously asked about this here: #1294).
> 
> The only documentation on this issue available is from Tahiti age: https://rocmdocs.amd.com/en/latest/Programming_Guides/Opencl-optimization.html#channel-conflicts
> 
> The issue is present both in Vulkan and HIP backends of VkFFT. I tried to solve this by splitting the buffer logically into smaller chunks of memory (~16KB range), though AMD Vulkan implementation couldn't handle more than 128 buffers bound (even though It was supported by the specification). So, I am not sure what can be done about this without an understanding of what is actually happening. Nvidia GPUs don't seem to have this issue.

I read your issue. It seems you have the same quesion about the TLB and address pins' management .
but if you use the large stride like 2^18 and small data transaction(128bit/16Bytes), this accessing mode must  causing the low memory bandwidth in all platform. normally the memory hardware interleaving mode is col:channel:bank:row or col_low:chan:bank:col_high:row. but all the modes can handle small memory stride only. small stride data blocks will locate in different bank/channel, but large aligned stride data blocks must cause serious bank/channel confliction.
in your 1D benchmark, there is a bandwidth dropping between 2^12  & 2^13 . hbm channel width 128 bit = 16 B, 2^12/16B = 256.  and the hbm col address pin is 8.  maybe it is the reason of the bandwidth dropping.
you can test the different stride like (2^18 + 0x80) or (2^18+0x200) and so on...the bandwidth may be much higher than 2^18 stride.

---

### 评论 #8 — DTolm (2021-05-06T20:38:07Z)

Hello,
On Nvidia GPUs, this issue is less impactful - the only needed change to restore full bandwidth after 2^18 strides was to go from 32b to 128b coalescing, so it seems there is a way around this. 
The drop at 2^12 is happening due to the fact that I start transfer 2x more memory there, so it is not related to the issue. The question is only about strides >  2^18. Having padding is not really an option as the overall buffer is user-defined and I can't force them to have a special layout for each case. I thought that I can find a way around it by reorganizing read/write orders (and have the non-power-of-2 strides emulated), but it would have been much easier if I understood the issue better. 
Best regards,
Dmitrii  

---

### 评论 #9 — ROCmSupport (2021-06-02T11:58:58Z)

Hi all,
I hope this issue can be closed if we do not have any more points to discuss.
Thank you.

---

### 评论 #10 — ROCmSupport (2021-06-04T04:26:36Z)

Thanks all.
I am closing this as there is no more questions/update from anyone.
Feel free to file a new issue, if any.
Thank you.

---
