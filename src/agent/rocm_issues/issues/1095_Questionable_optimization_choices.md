# Questionable optimization choices

> **Issue #1095**
> **状态**: closed
> **创建时间**: 2020-05-03T16:09:11Z
> **更新时间**: 2024-01-19T05:51:37Z
> **关闭时间**: 2024-01-19T05:51:36Z
> **作者**: gwoltman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1095

## 描述

In gpuowl's fftMiddleIn kernel, the kernel loads data from memory, calcs some trig values, performs lots of float ops, writes results.

Looking at the disassembly:
1) the first lines load the 2 kernel arguments with s_load_dwordx2 
2) followed by 145 opcodes mostly calculating trig values
3) then the kernel starts the first of 10 loads from memory with global_load_dwordx4 instructions.
4) There are about 10 more trig opcodes before the first "s_waitcnt vmcnt".

My understanding is the trig calculations are "front-loaded" so that they can hide the latency of memory operations.   However, the two kernel args are almost always read from the L1 cache -- not much latency needs hiding.  The 10 global memory reads have much more latency to hide.

My suggestion is that the optimizer make better assumptions about hiding memory latency. Assume arguments to the kernel are from L1 cache and other reads are from global memory.  "Front-load" opcodes accordingly.  

In my case, this would mean moving most of the 145 trig ops after the global memory loads.

P.S.  In the above, when I say trig ops that is mostly two loads of a constant followed by a double-precision FMA instruction.

 






---

## 评论 (4 条)

### 评论 #1 — b-sumner (2020-05-03T17:45:40Z)

My understanding is that kernel arguments (in the HSA kernarg segment) are usually uncached so we don't require any cache operations to make them visible by the time the kernel starts.

Also, scheduling is complex.  We can't just look at a code and understand how all of the heuristics and tradeoffs in the compiler are going to play out.

If you could provide a small stand-alone example that you think illustrates questionable scheduling decisions, we would be happy to look at it.

---

### 评论 #2 — gwoltman (2020-05-04T00:22:27Z)

You are more of an expert than I on GPU memory caching.  I appreciate that scheduling is complex, in the example I've given even without caching is it best to take the 155 trig ops and put 145 of them after the s_load_dwordx2 but only ~10 after each global_load_dword_x4?  Would an even distribution be better for most GPUs?

I do not have a small example for you, but were having a kinda theoretical discussion.  I do not have any timings that show a superior way to distribute opcodes to minimize load latency.  I bring it up as food for thought for you to consider.  I've planted the seed, feel free to close the issue if you so desire.

P.S.  I've been diving into disassembly of this kernel trying to find a nasty optimizer bug - still have not found it.  No fun plowing through hundreds of lines of disassembly trying to find out what went wrong.  While doing so, I'm raising side issues that pop into my head.  Hope you don't mind!

---

### 评论 #3 — nartmada (2024-01-19T04:22:47Z)

Hi @gwoltman, do we still need this ticket to be opened? :) If not, please close it.  Thanks.

---

### 评论 #4 — gwoltman (2024-01-19T05:51:36Z)

I've ceased development on this project.  Closin issue.

---
