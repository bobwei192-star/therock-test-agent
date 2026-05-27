# OpenCL codegen: poor optimization of #VGPR used

> **Issue #1002**
> **状态**: closed
> **创建时间**: 2020-01-18T18:18:59Z
> **更新时间**: 2023-12-18T17:24:14Z
> **关闭时间**: 2023-12-18T17:24:13Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1002

## 描述

On ROCm 2.10, RadeonVII

In GpuOwl, the change referenced below speeds-up a big kernel by more than 33% by passing two arguments referencing the same memory buffer (thus the same data) instead of one in order to disable the ROCm optimizer from caching the data, once read, into VGPRs. This reduces the number of VGPRs used by the kernel from 156 to 125 and thus increases occupancy from 1 to 2.

| tailFusedMulDelta | Before | After |
| --- | --- | --- |
| NumVGPRsForWavesPerEU | 156 | 125 |
| Occupancy | 1 | 2 |

https://github.com/preda/gpuowl/commit/1e0ce1d8abf9f8b189373085a6cbdc2e2d814d33

This change is a work-around-the-optimizer, because it actively hides information from the compiler (in this case it hides the equivalence of the two buffer arguments).

The optimizer should be able to balance the desire to cache once-read data into VGPRs versus the VGPR pressure. In this particular case the register pressure is extreme (as it reduces occupancy to 1) yet the optimizer still uses a lot of VGPRs to "keep data around".


---

## 评论 (14 条)

### 评论 #1 — kerbowa (2020-01-20T06:18:51Z)

@preda would you be able to share steps on how to reproduce your observations?

---

### 评论 #2 — preda (2020-01-20T08:38:49Z)

Repro steps:

1. check out the gpuowl project: https://github.com/preda/gpuowl . (recommended: check out the most recent version on the master branch)
2. compile using either make or scons: simply invoke "make" or "scons" in the source dir
3. run with:
./gpuowl -pm1 95339399 -B1 30000
You need to wait a bit (about 1minute) until "stage-2" of P-1 is reached -- this is indicated by "P2" in the log lines, such as:

```
2020-01-20 19:22:15 95339399 P2  758/2880: 7042 primes; setup  2.20 s,   0.899 ms/prime
```

At this point it is possible to stop with Ctrl-C, change options/recompile, and restart which will continue.
To restart from the very beginning simply remove the folder 95339399 which contains the savefiles.

Two very useful options: -dump <folder> and -time (in addition to the previous options)
a) create an empty folder, let's say "foo"; run with "-dump foo" to get an ISA dump of the kernels in foo/
b) run with -time to get detailed per-kernel timing

Afterwards revert the change mentioned above, recompile, and compare timings and ISA dumps for the kernel tailFusedMulDelta.

Let me know if something isn't working or unclear.

---

### 评论 #3 — preda (2020-03-06T09:14:02Z)

Another example of the same, please have a look at this commit
https://github.com/preda/gpuowl/commit/b23e0d538dcd6cd10d35a058084494099f14a5e5
which increases performance (by reducing the number of VGPRs and thus increasing occupancy) by adding a _volatile_ qualifier to global memory to disable caching the values read in VGPRs.

The optimizer should make a better decision about whether to cache or not in VGPRs -- decreasing the occupancy from 3 to 2 is a very large cost to pay for some cached values.

Please note that the solution consisting in using "volatile" in imperfect, rough, with secondary costs; a good optimizer could do much better.

(this was compiled with ROCm 3.1 OpenCL, targeting Radeon VII)

---

### 评论 #4 — preda (2020-03-06T11:20:03Z)

Also with ROCm 3.1,
https://github.com/preda/gpuowl/commit/612febd684938d3bd3716a928070a63c20d4a8e5
which applies the "duplicate buffers" trick against the optimizer, reduces the number of VGPRs for the k_tailFused from 112 to 81 (corresponding to occupancy 2 -> 3).

Really, the cost of just re-executing the memory read when the data is still in the L1/L2 cache is nothing compared to that wastage of VGPRs.

---

### 评论 #5 — ROCmSupport (2021-04-19T12:59:05Z)

Hi @preda 
Thanks for reaching out.
Request you to share an update on ROCm 4.1.
Thank you.

---

### 评论 #6 — preda (2021-04-19T13:40:45Z)

@ROCmSupport ROCm 4.1 is not working for me on Radeon VII with the upstream amdgpu driver.


---

### 评论 #7 — valeriob01 (2021-04-19T14:29:11Z)

@preda not sure I am using the upstream driver but I have upgraded to ROCm 4.1 and it detects my Radeon VIIs.


---

### 评论 #8 — preda (2021-04-19T15:20:18Z)

@valeriob01 did you install rocm-dkms?

---

### 评论 #9 — valeriob01 (2021-04-19T15:41:59Z)

Yes.


---

### 评论 #10 — valeriob01 (2021-04-19T17:21:53Z)

> @ROCmSupport ROCm 4.1 is not working for me on Radeon VII with the upstream amdgpu driver.

Did you do a fresh install from scratch ?
upgrade is not working for 4.1


---

### 评论 #11 — preda (2021-04-19T17:58:02Z)

> Yes.

@valeriob01 the fact that you installed rocm-dkms means that you are using the "custom" amdgpu driver that comes with ROCm. In my case I want to use the amdgpu driver that is part of the official Linux kernel. My goal should be aligned with AMD's position, as they activelly open-source and merge amdgpu to the Linux kernel. Thus the situation here, that ROCm contains a driver that is not merged to any Linux kernel, is a bit mistifying; hopefully a temporary situation, I'm waiting to be able to run ROCm on Radeon VII without needing dkms, as before.

---

### 评论 #12 — ROCmSupport (2021-04-20T05:14:06Z)

Hi @preda 
As we mentioned, rocm 4.1 does not work without dkms for now, which is a temporary situation.
Hence I recommend you to roll back to old rocm like 4.0 or rocm4.1 with dkms.
Thank you.

---

### 评论 #13 — nartmada (2023-12-14T03:20:53Z)

Hi @preda, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #14 — nartmada (2023-12-18T17:24:14Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
