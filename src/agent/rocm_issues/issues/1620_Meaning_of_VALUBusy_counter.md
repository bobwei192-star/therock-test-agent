# Meaning of VALUBusy counter

> **Issue #1620**
> **状态**: closed
> **创建时间**: 2021-11-18T10:39:06Z
> **更新时间**: 2022-04-07T08:20:20Z
> **关闭时间**: 2022-04-07T08:20:20Z
> **作者**: yugr
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1620

## 描述

Hi, we have a quick (and maybe dumb) question about `VALUBusy` counter. Here's its formula from [metrics.xml](https://github.com/ROCm-Developer-Tools/rocprofiler/blob/amd-master/test/tool/metrics.xml)
```
100*SQ_ACTIVE_INST_VALU*4/SIMD_NUM/GRBM_GUI_ACTIVE
```
`SIMD_NUM` here stands for all SIMDs in GPU i.e. `simds_per_cu * cu_num`.

Does `*4` term stand for number of SIMDs per single CU? If yes, does `VALUBusy` count cases when only some (even just 1) out of 4 SIMDs are processing a vector instruction, whereas others may be stalled ?

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-11-22T07:42:03Z)

Hi @yugr 
Thanks for reaching out.

VALUBusy : The percentage of GPUTime vector ALU instructions are processed. Value range: 0% (bad) to 100% (optimal)

For the information of VALUBusy and other, please check ROCm_Tools documentation @ [https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html](url)
<Always copy the address and paste in web browser>

Hope this helps. Please reach out to me for anymore information.
Thank you.

---

### 评论 #2 — yugr (2021-11-22T07:54:53Z)

Thank you for the suggestion but in fact we already inspected that link and unfortunately the description is a bit vague:

> The percentage of GPUTime vector ALU instructions are processed

It's not fully clear what "processed" means here. [metrics.xml](https://github.com/ROCm-Developer-Tools/rocprofiler/blob/amd-master/test/tool/metrics.xml) gives the following formula:
```
100*SQ_ACTIVE_INST_VALU*4/SIMD_NUM/GRBM_GUI_ACTIVE
```
where `SIMD_NUM` stands for total number of SIMDs in GPU (i.e. `simds_per_cu * cu_num`, see [metrics.h](https://github.com/ROCm-Developer-Tools/rocprofiler/blob/amd-master/src/core/metrics.h)). So in my understanding (due to the `*4` factor) it means the "amount of time _at least one SIMD unit_ in each CU is processing a VALU instruction". Could you confirm this?

---

### 评论 #3 — ROCmSupport (2021-11-22T07:59:16Z)

Thanks @yugr 
Let me reach Profiler developer for better information and update soon on this. Thank you.

---

### 评论 #4 — FruitClover (2022-03-04T17:31:37Z)

Hello @ROCmSupport, is there any update on this?

---

### 评论 #5 — jlgreathouse (2022-04-06T19:52:57Z)

The metrics.xml file you're looking at was built around the performance monitors in our GCN and CDNA hardware, so please note that the answer I'm about to give does not necessarily apply to our RDNA hardware.

In GCN and CDNA, our compute units are made up of 4 SIMD-16 units to do their vector ALU (VALU) math. However, our wavefronts (the unit of execution that the hardware sends into the VALU) are 64 wide. When we execute a 64-wide instruction, the hardware actually takes 4 cycles to send all lanes into the VALU. For a single wavefront, the instruction issue logic will put Lanes 0-15 into a SIMD16 in cycle 0, lanes 16-31 into the same SIMD16 in cycle 1, lanes 32-47 into the same SIMD16 in cycle 2, and lanes 48-63 into the same SIMD16 in cycle 3.

We do not split the 64-wide wavefront across the 4 SIMD units. Instead, during the cycles where we are issuing lanes >=16, the issue logic moves on to issuing waves into the other SIMDs. As an example, if wavefront 0 is being issued into SIMD16-0, then we will issue wavefront 0 lanes 0-15 to SIMD16-0 in cycle 0. We will issue wavefront 0 lanes 16-31 to SIMD16-0 in cycle 1, but we will **also** start issuing wavefront 1 lanes 0-15 into SIMD16-1 in cycle 1. This is how we utilize all 4 SIMD units in a CU: multi-cycling individual within a SIMD, and issuing multiple waves into the different SIMDs.

I describe this background because I think it's important to understand what the SQ_ACTIVE_INST_VALU counter is actually counting. This counter increments once for each _initial decision to issue an instruction into the VALU_. In other words, even though SIMD0 may be actively doing work in cycles 0 (lanes 0-15), 1 (lanes 16-31), 2 (lanes 32-47), and 3 (lanes 48-63), this counter would only increment once. If we therefore wanted to know the number of cycles that SIMD0 was actively doing work, we must multiply this counter by 4. A 64-wide wavefront in GCN/CDNA always takes 4 cycles to issue through the SIMD16 unit.

Now, imagine that I have a single CU and that CU has a single wavefront in it. If we issue something from that wavefront at every possible opportunity, then SIMD0 is active every cycle. SQ_ACTIVE_INST_VALU will go up once every 4 cycles (when we issue an instruction from this wavefront), and we will multiply it by 4 to say "The SIMD0 VALU was active every cycle".

But with respect to answering the question "How busy were the VALUs in the imaginary 1CU GPU with 1 wavefront": because SIMD1-3 were all idle throughout, really this GPU was only 25% busy. So we later divide by "simds_per_cu [4] * cu_num [1]". This takes us from 100% busy to 25% busy in this example.

But if we had two wavefronts in this CU, each issue into VALU every opportunity they get, we would see that two SIMDs are each at 100% utilization. SQ_ACTIVE_INST_VALU increments in cycle 0, cycle 1, cycle 4, cycle 5, etc. So after 800 cycles (e.g. GRBM_GUI_ACTIVE is 800), SQ_ACTIVe_INST_VALU would have gone up 400 times. We multiply by 4 to say 1600 instruction-cycles, and divide by 4 SIMDs to get 400 useful cycles in this CU. 400 useful cycles / 800 cycles --> 50% VALUBusy.

Hopefully that helps make clear what the underling performance event is measuring, and why this performance metric's formula is calculated as written.

---

### 评论 #6 — yugr (2022-04-07T08:20:20Z)

@jlgreathouse thanks a lot for the detailed answer, it's all clear now.

---
