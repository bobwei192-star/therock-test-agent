# vector_copy failed on my aarch64 system

> **Issue #232**
> **状态**: closed
> **创建时间**: 2017-10-23T02:19:16Z
> **更新时间**: 2017-10-23T14:07:15Z
> **关闭时间**: 2017-10-23T14:07:15Z
> **作者**: lintcoder
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/232

## 描述

@gstoner  Hi, I have been busy on trying to build ROCm on my ubunu16.04-arm64 server which is running on Cavium Thunder X for a very long time.
Here is the detail for every building process:
1. ROCK-Kernel-Driver (branch roc-1.6.3 commit cb1930)
2. ROCT-Thunk-Interface (branch roc-1.6.3 commit 25a9bc)
after that I get directory /opt/rocm/libhsakmt/
3. ROCR-Runtime (branch roc-1.6.1)
after that I get directory /opt/rocm/hsa/
While I‘ve noticed that ROCm platform relies on a few closed source components which are only available through the ROCm repositories as hsa-ext-rocr-dev package, since I have been building whole project on an aarch64 system, I wonder where could I get these components suitable for this platform and if it will be necessary for running the examples here or making the rocm work?

4. hcc (branch aarch64  commit bd70a7)
after that I get directory /opt/rocm/hcc-1.0
5. HIP (branch master e8de9d)
after that I get directory /opt/rocm/hip
6. atmi(branch master)
from the output of cmake, atmi seems not supported on aarch64.

Now with these components built, a C-based test that whchung provided at https://gist.github.com/whchung/79b92141d7274e0b3dda20b688db21aa can run successfully on my platform. While the sample vector_copy in ROCR/sample failed with these output:

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
Create the program failed.

Besides my AMD GPU card is RX460, I wonder with the situation refered above, will the ROCM on my system supported mesa opengl, since I want to make some tests on opengl? 



---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-10-23T14:06:38Z)

Please use HIPinfo instead of this test.   The shader compiler which this test is using is being deprecated 

---
