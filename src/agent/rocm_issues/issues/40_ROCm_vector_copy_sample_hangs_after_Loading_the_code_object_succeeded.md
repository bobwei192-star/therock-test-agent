# ROCm vector_copy sample hangs after "Loading the code object succeeded"

> **Issue #40**
> **状态**: closed
> **创建时间**: 2016-10-21T17:50:09Z
> **更新时间**: 2016-10-21T19:02:03Z
> **关闭时间**: 2016-10-21T19:02:03Z
> **作者**: mbevand
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/40

## 描述

I followed the directions at ROCm Install  on a machine running a fresh Ubuntu server 16.04 64-bit install (headless, no graphical desktop). I have a R9 Nano in the machine. I rebooted into the 4.4.0-kfd-compute-rocm-rel-1.2-31 kernel, then tried to compile and run the vector_copy sample:

```
$ cd /opt/rocm/hsa/sample
$ make
$ ./vector_copy
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is Fiji.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
```

It hangs there for multiple minutes using 100% CPU. I try Control-C multiple times eventually the process is killed. And I see this error in dmesg:

```
[  253.260002] kfd: qcm fence wait loop timeout expired 
[  253.260025] kfd: unmapping queues failed. 
[  253.260040] kfd: the cp might be in an unrecoverable state due to an unsuccessful queues preemption
```

Why does vector_copy not run? I should point out this machine has a CPU _without_ PCIe Gen3 atomics. It's a 2008-era Core 2 Duo E8400, on a mobo with Intel P31 chipset. (Don't ask why it is so old—it's just a spare CPU & mobo I had laying around for a quick test ) Is the lack of atomics causing this problem? 


---

## 评论 (3 条)

### 评论 #1 — ghost (2016-10-21T18:30:57Z)

Yes, as you suspected the lack of PCIe atomics is the source of the issue.

This mechanism is used to signal work completion. So even though all the operations are technically complete, vector_copy never received a notification and it's still waiting for a signal.

PCIe atomics is currently a requirement for ROCm


---

### 评论 #2 — mbevand (2016-10-21T19:00:25Z)

Thanks Andres! I will be on my way to buy a PCIe 3.0 and atomics-enabled machine... :)


---

### 评论 #3 — ghost (2016-10-21T19:02:03Z)

No problem. Sorry for the trouble!


---
