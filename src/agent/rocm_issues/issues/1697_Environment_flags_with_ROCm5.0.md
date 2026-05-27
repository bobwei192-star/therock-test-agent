# Environment flags with ROCm5.0

> **Issue #1697**
> **状态**: closed
> **创建时间**: 2022-03-02T21:16:15Z
> **更新时间**: 2022-03-08T07:19:52Z
> **关闭时间**: 2022-03-07T20:19:04Z
> **作者**: aoolmay
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1697

## 描述

I've just completed some big tasks, where GPU per task was necessary, now I'd like to run several smaller jobs concurrently on my GPUs. The main problem i'm having right now is memory occupancy with certain workloads hogging 100% regardless of actual use. In that case performance degrades dramatically due to constant memory swapping.

I vaguely remember from old ROCm versions, there were environment flags you can set for certain needs, like limiting max GPU RAM use per process and so on, unfortunately i lost track of those. At the same time i'm sure there are other tweaks possible to be applied in this manner. Is there somewhere a comprehensive or at least mostly complete reference for those?

Regards

---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2022-03-03T11:06:25Z)

Hi @aoolmay 
Thanks for reaching out. 
AFAIK, /opt/rocm-xxx/bin/rocm-smi --help(-h) gives you more idea, request to try and explore all possible options.
And also HIP_VISIBLE_DEVICES and ROCR_VISIBLE_DEVICES flags control the number of GPUs.
Hope this helps. Update me once you got the resolution.
Feel free to reach me for any doubts/queries.
Thank you.

---

### 评论 #2 — aoolmay (2022-03-03T11:46:02Z)

Hello,
I use rocm-smi regularly, as far as i understand -h page it doesn't provide such functionality. I think it's a kernel module interface, similar to passing ROCR_VISIBLE_DEVICES. I even experimented on ROCm 4.3 with kernel arguments passed on boot via GRUB, but don't recall memory allocation per process was exposed being there.

My own OpenCL code doesn't have this problem since i explicitly control memory allocation. PlaidML(just as another example) doesn't have this problem, it seems to allocate only what it needs. Tensorflow is the memory hog i have in mind that takes 100% of available memory even for small tasks. As i remember using old(pre 3.0 version) ROCm with WX5100 and WX7100, there was a switch, again similarly used like ROCR_VISIBLE_DEVICES, that limited adress space to x% and even a hog like TF would abide by this setting. Unfortunately i lost the cheat sheet i had for that and google search comes up empty, amddocs also comes up empty on the subject.

I realize i can limit memory internally from Tensorflow code, but i'm just interested about that interface. Any information is sparse and when encountered it's from seasoned users with single use case solution. I think it should be publicized(unless it's been phased out?) since it now lives in arcane knowledge limbo, I hope this points you better towards what i'm looking for.
Regards,

---

### 评论 #3 — ROCmSupport (2022-03-03T12:55:50Z)

Hi @aoolmay 
Let me share some more data.

CLANG flags   --> https://github.com/ROCm-Developer-Tools/HIP/blob/master/docs/markdown/clang_options.md
kernel params --> https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c
ROCr flags       --> https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/master/src/core/util/flag.h
amdgpu flags --> https://www.kernel.org/doc/html/v5.13/gpu/amdgpu.html

The only thunk variables are:
src/fmm.c: disableCache = getenv("HSA_DISABLE_CACHE");
src/fmm.c: pagedUserptr = getenv("HSA_USERPTR_FOR_PAGED_MEM");
src/fmm.c: checkUserptr = getenv("HSA_CHECK_USERPTR");
src/fmm.c: reserveSvm = getenv("HSA_RESERVE_SVM");
src/fmm.c: guardPagesStr = getenv("HSA_SVM_GUARD_PAGES");
src/topology.c: envvar = getenv("HSA_OVERRIDE_GFX_VERSION");
src/openclose.c: envvar = getenv("HSAKMT_DEBUG_LEVEL");
src/openclose.c: envvar = getenv("HSA_ZFB");

---

### 评论 #4 — aoolmay (2022-03-03T13:16:00Z)

@ROCmSupport
Thanks for that, but while i have your attention i want to highlight another feature i'm trying to exploit besides memory managment, a more important issue actually.
Navi cards have terrible multitasking capability. Testing multiple workloads in all flavors (OpenCL, PlaidML, Tensorflow) shows seemingly random GPU time partitioning. I understand you don't support non workstation cards officially, but i expect the same behavior form W6800 which you could test, maybe even MI100 has the same issue(?).
For example: 1x identical workload completes in 25 minutes, 2x identical workloads complete in 30 and 40 minutes, 3x identical workloads complete epoch in 35, 50, 35 minutes and so on. I'm sure you can replicate it on any reasonably long running task. If you're willing to follow up on this with me i'll put in time to provide you a modified MNIST benchmark with memory management included.
Old WX5100 and WX7100 that i have running today(under OpenCL and PlaidML) schedule work perfectly evenly. Up to 15x simultaneous workloads i tend to use in my projects. Time sharing predictability is very important to me since i'm running live services and uneven time to complete between the fastest and slowest process nets me with +15-20% lag on total service.

---

### 评论 #5 — ROCmSupport (2022-03-08T07:19:52Z)

Thanks for closing this issue, considering that your problem is solved.
Feel free to file a new ticket, if any, for quick resolution.
Thank you.

---
