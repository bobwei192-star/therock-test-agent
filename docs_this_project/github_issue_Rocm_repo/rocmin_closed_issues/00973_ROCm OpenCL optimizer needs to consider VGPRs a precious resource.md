# ROCm OpenCL optimizer needs to consider VGPRs a precious resource

- **Issue #:** 973
- **State:** closed
- **Created:** 2019-12-18T23:21:58Z
- **Updated:** 2023-12-18T15:55:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/973

My apologies in advance if the tone of this report comes off too negative. 

In github.com's preda/gpuowl project the optimzer can and should do a much better job with register allocation.  

Consider the carryFused kernel in gpuowl.cl.  The default compilation uses 109 VGPRs giving an occupancy of 2.  By chance I stuck in unroll(1) attribute to prevent unrolling a loop that is executed just 4 times.  VGPR register usage dropped to 38, occupancy up to 6, 20% performance improvement.  This is a fairly straightforward routine where even unrolled it is very easy to get register usage under 48.   With work one could probably get to 32 or less.

To show how ludicrous some of ROCm optimizer's decisions can be, a similar routine used to take one input/output pointer accessing 8 scattered values.  The optimizer precalculated all 8 pointers (16 VGPRs) and did not reuse them untli data was output at the end of the kernel.  These pointers could be recalculated with just 2 integer instructions!

Sadly, my attempts at working around the optimizer are often unsuccessful.  In carryFused with loop unrolling, if you use the attribute that limits VGPR usage to 64, the compiler generates the horrible 109 register code and spills 45 of them to global memory.  That's a performance loser.
Other kernels do not have an unroll(1) point that leads to well optimized code.  I've thrown in __asm volatile to try to stop the optimizer from going nuts to no avail.

I understand register allocation is a tough problem.  If a kernel uses lots of local memory, being piggish with register allocation makes sense.  Ideally, the compiler would know how hard it is to regenerate a value, how long it needs to keep a value before it is reused, and offer an attribute that gave the programmer control on say a scale from 1 to 10 as to how aggressive registers are consumed.  I'm sure you can think of other valid approaches.

Note that any effort you put forth will benefit more than just me.  All OpenCL users stand to gain significantly.

When I last used CUDA about 8 years ago, their compiler did an impressive job in its decision making when told to limit a kernel to N registers.  The final step in development was to look at each kernel disassembly and any kernels that were just over an occupancy crossover point would be changed to use a register or two less for a nice final performance bump.