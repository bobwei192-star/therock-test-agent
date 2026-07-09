# Questionable optimization choices

- **Issue #:** 1095
- **State:** closed
- **Created:** 2020-05-03T16:09:11Z
- **Updated:** 2024-01-19T05:51:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1095

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

 




