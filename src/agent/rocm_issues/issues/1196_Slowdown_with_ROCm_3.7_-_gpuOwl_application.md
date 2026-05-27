# Slowdown with ROCm 3.7 - gpuOwl application

> **Issue #1196**
> **状态**: closed
> **创建时间**: 2020-08-21T03:55:35Z
> **更新时间**: 2024-01-27T23:21:43Z
> **关闭时间**: 2024-01-27T23:21:43Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1196

## 描述

https://github.com/preda/gpuowl/issues/188

---

## 评论 (31 条)

### 评论 #1 — preda (2020-08-21T05:37:21Z)

Inlining the numbers from above ( preda/gpuowl#188 ):
ROCm 3.3 performance
gpu1 gpu2
min: 2404 us/it 2427 us/it
max: 2443 us/it 2510 us/it

ROCm 3.7 performance
gpu1 gpu2
min: 2501 us/it 2524 us/it
max: 2538 us/it 2612 us/it

about 102 us/it slower on gpu2.


---

### 评论 #2 — preda (2020-08-21T05:42:18Z)

Fixing my comment.
The previous gpuowl performance issue was: https://github.com/RadeonOpenCompute/ROCm/issues/1124
which was reporting a 5% regression from 3.3 to 3.5, which is pretty much on par with what is reported here.

Thus, I expect similar gpuowl performance between 3.5 and 3.7. The problem was not aggravated in 3.7, but not fixed either.

---

### 评论 #3 — valeriob01 (2020-08-21T06:05:40Z)

I hoped to be able to use RDC to monitor gpus (available in 3.7) but instead I am going to rollback to 3.3


---

### 评论 #4 — ROCmSupport (2020-12-16T10:54:24Z)

Hi @preda 
Can you please try with the latest ROCm release version: 3.10 and update please.
Thank you.

---

### 评论 #5 — preda (2020-12-16T13:16:14Z)

Per kernel timings, ROCm 3.3:
```
carryFused     :    264 us/call
tailFusedSquare :    192 us/call
```

ROCm 3.10:
```
carryFused     :    281 us/call
tailFusedSquare :    211 us/call
```

Comparing occupancy for the top two kernels above, left is 3.3, right is 3.10:
```
carryFused       :    Occupancy: =     6       | carryFused       :    Occupancy: =     5
tailFusedSquare  :    Occupancy: =     3       | tailFusedSquare  :    Occupancy: =     2
---------------------
carryFused       :    NumVgprs:   =    39       | carryFused       :    NumVgprs: =    41
tailFusedSquare  :    NumVgprs: =    79       | tailFusedSquare  :    NumVgprs: =   103
```

This was measured with the latest commit https://github.com/preda/gpuowl/tree/28dbf8888036bfdfc9147cbdaa552e1cbd04cc91

The run configuration used was [equivalent to]:
```
-prp 101603651 -B1 0 -proof 7 -nospin
```
add -time to get kernel timing info.

This was run on a RadeonVII with sclk 3 and memfreq 1160. On Ubuntu 20.04 with Linux kernel 5.10.0 .
The overall slowdown observed was about 6%.


---

### 评论 #6 — ROCmSupport (2021-01-05T09:27:49Z)

Hi @preda 
I am getting lot of errors like missing files, linkage errors etc.

For ex:
taccuser@taccuser-SYS-4028GR-TR2:~/gpuowl$ make
echo \"`git describe --tags --long --dirty --always`\" > version.new
diff -q -N version.new version.inc >/dev/null || mv version.new version.inc
echo Version: `cat version.inc`
Version: "v7.2-21-g28dbf88"
g++ -MT ProofCache.o -MMD -MP -MF .d/ProofCache.Td -Wall -O2 -std=c++17   -c -o ProofCache.o ProofCache.cpp
In file included from ProofCache.cpp:3:0:
ProofCache.h:8:10: fatal error: filesystem: No such file or directory
 #include <filesystem>
          ^~~~~~~~~~~~
compilation terminated.
Makefile:33: recipe for target 'ProofCache.o' failed
make: *** [ProofCache.o] Error 1

---

### 评论 #7 — preda (2021-01-05T09:53:12Z)

Please use a newer version of g++, like 9 or 10. 8 might also work fine. Would help to report the version of the compiler you're using, obtained with:
```
g++ --version
```

If errors persist, just paste them here instead of mentioning "lots of errors" which is not specific enough.

---

### 评论 #8 — preda (2021-01-05T09:56:16Z)

On a side note, the slowdown relative to ROCm 3.3 is still present in ROCm 4.0. The reason is wasteful VGPR allocation which reduces occupancy of some key kernels.

---

### 评论 #9 — baryluk (2021-01-05T11:12:45Z)

@preda Could you remaind me what GPU are you using? And what does clinfo reports about the amount of "Local memory" in 3.3 and 4.0? I noticed on my Fury X (FIJI, GFX8), that is incorrectly reports amount of 64KB of local memory, where I believe it has only 32KB per core. The OpenCL driver from AMD Pro drivers, reports it correctly, even if they include the OpenCL based on rocm. This might explain why compiler is doing so poorly and reduces performance so much.

I wonder if maybe it is similar with your GPU.


---

### 评论 #10 — preda (2021-01-05T11:36:27Z)

@baryluk The GPU is Radeon VII. The diff between clinfo on 3.3 and 4.0 is:
```
4c4
<   Platform Version                                OpenCL 2.1 AMD-APP (3098.0)
---
>   Platform Version                                OpenCL 2.0 AMD-APP (3212.0)
6,7c6
<   Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
<   Platform Host timer resolution                  1ns
---
>   Platform Extensions                             cl_khr_icd cl_amd_event_callback 
12c11
<   Device Name                                     gfx906+sram-ecc
---
>   Device Name                                     gfx906
16c15
<   Driver Version                                  3098.0 (HSA1.1,LC)
---
>   Driver Version                                  3212.0 (HSA1.1,LC)
30c29
<   Graphics IP (AMD)                               9.6
---
>   Graphics IP (AMD)                               9.0
82c81
<   Max memory allocation                           14588628172 (13.59GiB)
---
>   Max memory allocation                           14588628168 (13.59GiB)
95c94
<   Max size for global variable                    14588628172 (13.59GiB)
---
>   Max size for global variable                    14588628168 (13.59GiB)
102,103c101,102
<     Max size for 1D images from buffer            65536 pixels
<     Max 1D or 2D image array size                 2048 images
---
>     Max size for 1D images from buffer            4294967295 pixels
>     Max 1D or 2D image array size                 8192 images
107c106
<     Max 3D image size                             2048x2048x2048 pixels
---
>     Max 3D image size                             16384x16384x8192 pixels
113c112
<   Max pipe packet size                            1703726284 (1.587GiB)
---
>   Max pipe packet size                            1703726280 (1.587GiB)
119c118
<   Max constant buffer size                        14588628172 (13.59GiB)
---
>   Max constant buffer size                        14588628168 (13.59GiB)
```

They both report
```
Local memory size                               65536 (64KiB)
Local memory syze per CU (AMD)                  65536 (64KiB)
```

---

### 评论 #11 — baryluk (2021-01-05T14:10:39Z)

Interesting indeed. Thanks @preda 

---

### 评论 #12 — ROCmSupport (2021-01-28T08:36:12Z)

Hi @preda 
Have moved to machine with gcc9 and able to build the application using make.
But application is running for more than 2 hours and still running. Now sure how much time it takes to complete.
I used this command: ./gpuowl -prp 96359411 -time
Can you please share a small test/sample to reproduce this problem.
Thank you.

---

### 评论 #13 — preda (2021-01-28T17:41:58Z)

It is normal that it takes a long time, on the order of 24 hours depending on the GPU and exponent (the "exponent" is the number you pass to -prp, in your case 96359411). But in order to measure the performance you don't need to run a full exponent to completion -- the software outputs performance numbers periodically, something like 1396 us/it, that meaning: 1396 microseconds ("us") per iteration. That number being smaller means that the program runs faster, as it takes less time to run one iteration.

You can also run gpuowl with -iters \<N\>, and the program will stop after the given number of iterations. Run with -iters 100000 , should take or the order of minutes to complete (depending on GPU).

-time is not needed to measure performance, it is only needed to output per-kernel timing information. Obtaining this information (timing per kernel) slows down the run a bit though. So to compare two setups (e.g. two ROCm versions on the same hardware), run without -time, with -iters \<N\> , and record both the iteration time displayed and the clock time. (that can be obtained with the "time" Unix command), e.g.:
```
time ./gpuowl -prp 102363257 -iters 100000 -B1 0 -nospin -proof 1 -device 0
```
if using version 7.2.21

To stop cleanly, give it a Ctrl-C or "kill -INT".
To reset to a clean state, simply remove (or move) the folder "102363257" (i.e. the exponent) that contains the savefiles, and restart the program.

Let me know what other questions appear.


---

### 评论 #14 — ROCmSupport (2021-01-29T10:10:21Z)

Thanks @preda 
I am able to reproduce the problem.
I am observing 4% drop between 3.3 and 3.5 using the command: _time ./gpuowl -prp 102363257 -iters 100000 -B1 0 -nospin -proof 1 -device 0_
I will start debugging it and will assign to component accordingly. Please stay tuned for more updates.
Thank you.


---

### 评论 #15 — ROCmSupport (2021-01-29T13:00:59Z)

**3.3 scores:**
2021-01-29 15:29:50 459888c172da5eee 102363257 OK       800   0.00% 6e5d40814e8972fb  664 us/it + check 0.39s + save 0.28s; ETA 18:52
2021-01-29 15:29:56 459888c172da5eee 102363257        10000   0.01% 62cee1a7d612e416  664 us/it
2021-01-29 15:30:03 459888c172da5eee 102363257        20000   0.02% be681c958feac273  664 us/it
2021-01-29 15:30:09 459888c172da5eee 102363257        30000   0.03% f5e77003c5ff62ea  665 us/it
2021-01-29 15:30:16 459888c172da5eee 102363257        40000   0.04% 83bae23d7e091516  666 us/it
2021-01-29 15:30:23 459888c172da5eee 102363257        50000   0.05% 7081b36c3348edd3  666 us/it
2021-01-29 15:30:29 459888c172da5eee 102363257        60000   0.06% fcc65b9f70ccd618  666 us/it
2021-01-29 15:30:36 459888c172da5eee 102363257        70000   0.07% 7f44897e8bca208f  666 us/it
2021-01-29 15:30:43 459888c172da5eee 102363257        80000   0.08% d5fcf6c4ca6ce951  666 us/it
2021-01-29 15:30:49 459888c172da5eee 102363257        90000   0.09% 909b339c2637035e  667 us/it
2021-01-29 15:30:56 459888c172da5eee 102363257 Stopping, please wait..
2021-01-29 15:30:57 459888c172da5eee 102363257 OK    100000   0.10% a536e30314385089  670 us/it + check 0.41s + save 0.32s; ETA 19:05
2021-01-29 15:30:57 459888c172da5eee Exiting because "stop requested"
2021-01-29 15:30:57 459888c172da5eee Bye

real    1m11.769s
user    0m5.723s
sys     0m0.202s

**3.5 scores:**
2021-01-29 15:27:21 459888c172da5eee 102363257 OK       800   0.00% 6e5d40814e8972fb  687 us/it + check 0.40s + save 0.28s; ETA 19:31
2021-01-29 15:27:27 459888c172da5eee 102363257        10000   0.01% 62cee1a7d612e416  687 us/it
2021-01-29 15:27:34 459888c172da5eee 102363257        20000   0.02% be681c958feac273  688 us/it
2021-01-29 15:27:41 459888c172da5eee 102363257        30000   0.03% f5e77003c5ff62ea  688 us/it
2021-01-29 15:27:48 459888c172da5eee 102363257        40000   0.04% 83bae23d7e091516  689 us/it
2021-01-29 15:27:55 459888c172da5eee 102363257        50000   0.05% 7081b36c3348edd3  689 us/it
2021-01-29 15:28:01 459888c172da5eee 102363257        60000   0.06% fcc65b9f70ccd618  690 us/it
2021-01-29 15:28:08 459888c172da5eee 102363257        70000   0.07% 7f44897e8bca208f  690 us/it
2021-01-29 15:28:15 459888c172da5eee 102363257        80000   0.08% d5fcf6c4ca6ce951  690 us/it
2021-01-29 15:28:22 459888c172da5eee 102363257        90000   0.09% 909b339c2637035e  690 us/it
2021-01-29 15:28:29 459888c172da5eee 102363257 Stopping, please wait..
2021-01-29 15:28:30 459888c172da5eee 102363257 OK    100000   0.10% a536e30314385089  691 us/it + check 0.41s + save 0.29s; ETA 19:38
2021-01-29 15:28:30 459888c172da5eee Exiting because "stop requested"
2021-01-29 15:28:30 459888c172da5eee Bye

real    1m14.102s
user    0m5.939s
sys     0m0.215s

Same issue is seen with ROCm 4.0 also.

---

### 评论 #16 — ROCmSupport (2021-02-03T09:08:13Z)

Hi @preda 
Can you please confirm whether this issue is always reproducible?
Looks like I am not able to reproduce today.
I am getting same scores with both 3.3 and 3.5 today. Looks like this issue is intermittent.

3.5 scores observed today:
-----------------------------
2021-02-03 14:31:48 459888c172da5eee 102363257 OK       800   0.00% 6e5d40814e8972fb  668 us/it + check 0.39s + save 0.28s; ETA 19:00
2021-02-03 14:31:55 459888c172da5eee 102363257        10000   0.01% 62cee1a7d612e416  668 us/it
2021-02-03 14:32:01 459888c172da5eee 102363257        20000   0.02% be681c958feac273  668 us/it
2021-02-03 14:32:08 459888c172da5eee 102363257        30000   0.03% f5e77003c5ff62ea  669 us/it
2021-02-03 14:32:15 459888c172da5eee 102363257        40000   0.04% 83bae23d7e091516  669 us/it
2021-02-03 14:32:21 459888c172da5eee 102363257        50000   0.05% 7081b36c3348edd3  670 us/it
2021-02-03 14:32:28 459888c172da5eee 102363257        60000   0.06% fcc65b9f70ccd618  670 us/it
2021-02-03 14:32:35 459888c172da5eee 102363257        70000   0.07% 7f44897e8bca208f  670 us/it
2021-02-03 14:32:41 459888c172da5eee 102363257        80000   0.08% d5fcf6c4ca6ce951  670 us/it
2021-02-03 14:32:48 459888c172da5eee 102363257        90000   0.09% 909b339c2637035e  671 us/it
2021-02-03 14:32:55 459888c172da5eee 102363257 Stopping, please wait..
2021-02-03 14:32:56 459888c172da5eee 102363257 OK    100000   0.10% a536e30314385089  671 us/it + check 0.40s + save 0.30s; ETA 19:03
2021-02-03 14:32:56 459888c172da5eee Exiting because "stop requested"
2021-02-03 14:32:56 459888c172da5eee Bye

real    1m12.074s
user    0m5.697s
sys     0m0.190s

3.3 scores observed today:
-----------------------------
2021-02-03 14:36:39 459888c172da5eee 102363257 OK       800   0.00% 6e5d40814e8972fb  668 us/it + check 0.39s + save 0.26s; ETA 18:59
2021-02-03 14:36:45 459888c172da5eee 102363257        10000   0.01% 62cee1a7d612e416  668 us/it
2021-02-03 14:36:52 459888c172da5eee 102363257        20000   0.02% be681c958feac273  668 us/it
2021-02-03 14:36:59 459888c172da5eee 102363257        30000   0.03% f5e77003c5ff62ea  669 us/it
2021-02-03 14:37:05 459888c172da5eee 102363257        40000   0.04% 83bae23d7e091516  670 us/it
2021-02-03 14:37:12 459888c172da5eee 102363257        50000   0.05% 7081b36c3348edd3  670 us/it
2021-02-03 14:37:19 459888c172da5eee 102363257        60000   0.06% fcc65b9f70ccd618  670 us/it
2021-02-03 14:37:25 459888c172da5eee 102363257        70000   0.07% 7f44897e8bca208f  670 us/it
2021-02-03 14:37:32 459888c172da5eee 102363257        80000   0.08% d5fcf6c4ca6ce951  670 us/it
2021-02-03 14:37:39 459888c172da5eee 102363257        90000   0.09% 909b339c2637035e  671 us/it
2021-02-03 14:37:45 459888c172da5eee 102363257 Stopping, please wait..
2021-02-03 14:37:46 459888c172da5eee 102363257 OK    100000   0.10% a536e30314385089  671 us/it + check 0.41s + save 0.31s; ETA 19:03
2021-02-03 14:37:46 459888c172da5eee Exiting because "stop requested"
2021-02-03 14:37:46 459888c172da5eee Bye

real    1m12.131s
user    0m5.681s
sys     0m0.225s


---

### 评论 #17 — preda (2021-02-03T11:41:30Z)

The issue, in my observation, is consistent (not intermittent). OTOH you should keep an eye on the GPU temperature and the related throttling or boosting. Basically, keep gpuowl running for 5minutes or more until a stable-state is reached before measuring. Also, set the fan speed to a high speed manually as to prevent thermal throttling. Also, it's recomended to underclock the GPU (e.g. by setting sclk to level 3) which helps with throttling.

The issues also manifests in different ISA compilation, which can be dumped with -dump <folder>, where different occupancy and VGPRs allocation is observed, and this is consistent IMO as well -- but feel free to compare the generated ISA.

---

### 评论 #18 — ROCmSupport (2021-02-10T07:24:01Z)

Thanks @preda 
I switched to a different machine and am able to reproduce this 100% now after setting sclk to 3 and max fan levels.
I am working on finding faulty package.

---

### 评论 #19 — ROCmSupport (2021-02-10T09:16:02Z)

**Latest update on this issue:**
This issue is caused due to changes in the comgr. Issue/Regression is observed from ROCm 3.5 and even today with ROCm 4.0 and 4.1 internal code too. Scores were good with ROCm 3.3 and so I can say that its regression from ROCm 3.5.

Filed an internal ticket and assigned to comgr team.
Please stay tuned for more updates. Thank you.

---

### 评论 #20 — valeriob01 (2021-03-12T16:36:00Z)

> **Latest update on this issue:**
> This issue is caused due to changes in the comgr. Issue/Regression is observed from ROCm 3.5 and even today with ROCm 4.0 and 4.1 internal code too. Scores were good with ROCm 3.3 and so I can say that its regression from ROCm 3.5.
> 
> Filed an internal ticket and assigned to comgr team.
> Please stay tuned for more updates. Thank you.

Does the comgr package been corrected?


---

### 评论 #21 — preda (2021-03-13T08:28:45Z)

The bug concerns the LLVM GCN code generation and the related register allocation. There has been at least one regression among the LLVM changes; that regression was not detected at the time because of a lack of proper performance regression testing.

The "comgr" is a red herring, comgr being simply the entry point to the LLVM compiler.

---

### 评论 #22 — valeriob01 (2021-03-13T12:11:34Z)

@ROCmSupport What is the current status of development on this topic ?


---

### 评论 #23 — ROCmSupport (2021-03-15T09:28:16Z)

Hi @valeriob01 
I will check with dev and get back to you with an update soon

---

### 评论 #24 — valeriob01 (2021-03-23T14:34:48Z)

> Hi @valeriob01
> I will check with dev and get back to you with an update soon

-Hello @ROCmSupport I don't know what you mean with "soon" however 8 days seems a more than reasonable slice of time for the task.

---

### 评论 #25 — valeriob01 (2021-03-24T02:34:43Z)

Good news !
Installed ROCm 4.1.0 ... net gain of ~ -30 us/it

---

### 评论 #26 — ROCmSupport (2021-03-24T04:23:38Z)

Thanks @valeriob01 for the update.
But still drop is there right?
Dev is working on further fix and so please expect further improvements in future releases.
I will keep sharing the updates.
Thank you.

---

### 评论 #27 — ROCmSupport (2022-02-08T09:53:06Z)

Hi @valeriob01 
Hope this issue is fixed with the latest compiler changes in ROCm 4.5/4.5.1.
Can you please check and confirm whether this issue is still observed.
Thank you.

---

### 评论 #28 — selroc (2022-02-08T13:41:12Z)

> Hi @valeriob01 Hope this issue is fixed with the latest compiler changes in ROCm 4.5/4.5.1. Can you please check and confirm whether this issue is still observed. Thank you.

This issue is not fixed, we still see slowdowns.


---

### 评论 #29 — ROCmSupport (2022-02-09T14:06:11Z)

Thanks.
I just checked with 5.0 internal builds and able to reproduce the problem here too.
I have informed the same to developer.

20220209 19:52:23 459888c172da5eee 102363257 OK       800   0.00% 6e5d40814e8972fb  683 us/it + check 0.40s + save 0.29s; ETA 19:24
20220209 19:52:29 459888c172da5eee 102363257     10000 62cee1a7d612e416  683
20220209 19:52:36 459888c172da5eee 102363257     20000 be681c958feac273  684
20220209 19:52:43 459888c172da5eee 102363257     30000 f5e77003c5ff62ea  685
20220209 19:52:50 459888c172da5eee 102363257     40000 83bae23d7e091516  686
20220209 19:52:57 459888c172da5eee 102363257     50000 7081b36c3348edd3  686
20220209 19:53:03 459888c172da5eee 102363257     60000 fcc65b9f70ccd618  687
20220209 19:53:10 459888c172da5eee 102363257     70000 7f44897e8bca208f  687
20220209 19:53:17 459888c172da5eee 102363257     80000 d5fcf6c4ca6ce951  687
20220209 19:53:24 459888c172da5eee 102363257     90000 909b339c2637035e  688
20220209 19:53:31 459888c172da5eee 102363257 Stopping, please wait..
20220209 19:53:32 459888c172da5eee 102363257 OK    100000   0.10% a536e30314385089  688 us/it + check 0.41s + save 0.28s; ETA 19:32
20220209 19:53:32 459888c172da5eee Exiting because "stop requested"
20220209 19:53:32 459888c172da5eee Bye


---

### 评论 #30 — nartmada (2024-01-27T04:04:30Z)

Hi @selroc and @valeriob01, do you still see this issue with latest ROCm 6.0.0?  I am trying to rebaseline the issue.  Thanks.

---

### 评论 #31 — selroc (2024-01-27T19:13:06Z)

Yu can close it.


---
