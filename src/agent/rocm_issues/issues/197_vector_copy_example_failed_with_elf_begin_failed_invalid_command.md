# vector_copy example failed with "elf_begin failed: invalid command"

> **Issue #197**
> **状态**: closed
> **创建时间**: 2017-09-05T09:25:14Z
> **更新时间**: 2018-06-03T15:03:02Z
> **关闭时间**: 2018-06-03T15:03:02Z
> **作者**: beasterio
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/197

## 描述

Hi.
I have installed rocm 1.6 and trying vector_copy test but it failed:
beasterio@beasterio-pc:~/test$ ./vector_copy 
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
elf_begin failed: invalid command

Finalizing the program failed.

in test it uses vector_copy_base.brig, so maybe its not valid.

HelloWorld example works fine. I tried also HIP examples and they are ok too.
Ubuntu 16.04, video - Radeon rx 480.

---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-09-05T13:10:07Z)

We removing this test,  and moving to use HIPinfo instead,  we been slowing working on removing this backend from ROCm.

Greg
On Sep 5, 2017, at 4:25 AM, Konstantin Zverev <notifications@github.com<mailto:notifications@github.com>> wrote:


Hi.
I have installed rocm 1.6 and trying vector_copy test but it failed:
beasterio@beasterio-pc:~/test$ ./vector_copy
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
elf_begin failed: invalid command

Finalizing the program failed.

in test it uses vector_copy_base.brig, so maybe its not valid.

HelloWorld example works fine. I tried also HIP examples and they are ok too.
Ubuntu 16.04, video - Radeon rx 480.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/197>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuVhXYm5uhs3_SFnUAUIllxyD-TIUks5sfRN7gaJpZM4PMrCo>.



---

### 评论 #2 — jedwards-AMD (2017-09-05T14:25:27Z)

The test is being removed, but the error you are receiving indicates the brig file you are loading and parsing with libelf is either corrupted or in a format not compatible with the version of libelf you are using. The vector_copy code, brig files and hsail have not been modified in a long time. I suggest trying another simple sample, like hipInfo, to see if your system setup is correct. As Greg indicated above, vector_copy is out of support.

---

### 评论 #3 — RaymonSHan (2017-11-30T15:36:34Z)

I meet the same message in my RX580 with ubuntu 16.4
and I try hipInfo and some others samples, there are all OKed.

---
