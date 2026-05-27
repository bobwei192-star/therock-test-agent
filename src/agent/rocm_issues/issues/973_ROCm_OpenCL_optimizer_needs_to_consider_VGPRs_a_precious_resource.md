# ROCm OpenCL optimizer needs to consider VGPRs a precious resource

> **Issue #973**
> **状态**: closed
> **创建时间**: 2019-12-18T23:21:58Z
> **更新时间**: 2023-12-18T15:55:54Z
> **关闭时间**: 2023-12-18T15:55:53Z
> **作者**: gwoltman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/973

## 描述

My apologies in advance if the tone of this report comes off too negative. 

In github.com's preda/gpuowl project the optimzer can and should do a much better job with register allocation.  

Consider the carryFused kernel in gpuowl.cl.  The default compilation uses 109 VGPRs giving an occupancy of 2.  By chance I stuck in unroll(1) attribute to prevent unrolling a loop that is executed just 4 times.  VGPR register usage dropped to 38, occupancy up to 6, 20% performance improvement.  This is a fairly straightforward routine where even unrolled it is very easy to get register usage under 48.   With work one could probably get to 32 or less.

To show how ludicrous some of ROCm optimizer's decisions can be, a similar routine used to take one input/output pointer accessing 8 scattered values.  The optimizer precalculated all 8 pointers (16 VGPRs) and did not reuse them untli data was output at the end of the kernel.  These pointers could be recalculated with just 2 integer instructions!

Sadly, my attempts at working around the optimizer are often unsuccessful.  In carryFused with loop unrolling, if you use the attribute that limits VGPR usage to 64, the compiler generates the horrible 109 register code and spills 45 of them to global memory.  That's a performance loser.
Other kernels do not have an unroll(1) point that leads to well optimized code.  I've thrown in __asm volatile to try to stop the optimizer from going nuts to no avail.

I understand register allocation is a tough problem.  If a kernel uses lots of local memory, being piggish with register allocation makes sense.  Ideally, the compiler would know how hard it is to regenerate a value, how long it needs to keep a value before it is reused, and offer an attribute that gave the programmer control on say a scale from 1 to 10 as to how aggressive registers are consumed.  I'm sure you can think of other valid approaches.

Note that any effort you put forth will benefit more than just me.  All OpenCL users stand to gain significantly.

When I last used CUDA about 8 years ago, their compiler did an impressive job in its decision making when told to limit a kernel to N registers.  The final step in development was to look at each kernel disassembly and any kernels that were just over an occupancy crossover point would be changed to use a register or two less for a nice final performance bump.

---

## 评论 (6 条)

### 评论 #1 — b-sumner (2020-01-13T20:28:10Z)

@gwoltman thank you for these comments.  We definitely realize we have work to do in this area, and understand the value of doing so.

We would like to look more deeply at the carryFused kernel, but we don't see a unit test for it.  In fact, the only test mentioned in the repo is the self-test, and it's not clear that it uses this kernel at all.  Is a unit test something that you or preda can help with?  It would allow us to focus on this more quickly.

---

### 评论 #2 — gwoltman (2020-01-13T22:18:01Z)

Start with ROCm 2.10 (there may be a bug in gpuowl using ROCm 3.0).
git clone https://github.com/preda/gpuowl.git
cd gpuowl
make

To test all is working, run gpuowl thusly:  "./gpuowl -prp 95300003"
You should get output lines that look like this:
2020-01-13 17:04:27 gfx906+sram-ecc-0 95300003 OK        0 loaded: blockSize 400, 0000000000000003
2020-01-13 17:04:29 gfx906+sram-ecc-0 95300003 OK      800   0.00%; 1269 us/it; ETA 1d 09:36; 46c98a6a8ac389aa (check 0.65s)
Hit ^C.   The key thing to look for is the "OK".  If instead you see "EE" then the program is not working.

Create a directory called "dump".   Run "./gpuowl -prp 95300003 -dump dump" to generate assembly code in the dump directory.  The 5Msomething.s file will show you the carryFused kernel and its register usage.  By default, carryFused loops are not unrolled.

Run "./gpuowl -prp 95300003 -dump dump -use UNROLL_ALL" to generate the disassembly for carryFused with loops unrolled.  I'm seeing register usage go from 36 to 110.


---

### 评论 #3 — gwoltman (2020-01-14T02:05:13Z)

Also,  "./gpuowl -prp 95300003 -time"  will output the time spent in each kernel.

---

### 评论 #4 — gwoltman (2020-01-15T05:14:02Z)

If you like optimizer mysteries, I have more.  For example, "./gpuowl -prp 95300003 -time -use LESS_ACCURATE" eliminates 6 or so lines of code but runs slower.  I think it is the fftMiddleIn and/or fftMiddleOut kernels that are slower with no change in occupancy.

---

### 评论 #5 — nartmada (2023-12-13T23:07:30Z)

Hi @gwoltman, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #6 — nartmada (2023-12-18T15:55:53Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
