# Bridge for AMD MI100 Accelerator

> **Issue #1496**
> **状态**: closed
> **创建时间**: 2021-06-21T13:04:04Z
> **更新时间**: 2021-06-25T04:42:30Z
> **关闭时间**: 2021-06-23T07:43:05Z
> **作者**: question12345
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1496

## 描述

Hello,

I have a Server with two MI100 Accelerator and they are connected through the AMD bridge. 

The OS installed is Centos 7.9. I am able to see the 2 GPUs with these two commands: 
/opt/rocm/bin/rocminfo 
/opt/rocm/opencl/bin/clinfo 

but I don't know how to see if the bridge is working or not. Is there a specific command I should execute to check if the bridge is working? 

thank you

---

## 评论 (5 条)

### 评论 #1 — FilipVaverka (2021-06-21T18:21:19Z)

I think (without having any experience with this configuration) you should be able to see P2P in `clinfo` output:

> Number of P2P devices (AMD)                     {something}

Now, this should be there even if only PCI-E P2P is available. So next I would try `rocm-bandwidth-test` ([hopefully with better results than me](https://github.com/RadeonOpenCompute/ROCm/issues/1495)) which does P2P bandwidth tests, so you should see high bandwidth between GPUs connected with the bridge.

There may be better tools to verify your configuration, but this is what I would try first.

---

### 评论 #2 — ROCmSupport (2021-06-23T05:03:57Z)

Thanks @question12345 for reaching out.
Let me take a look.

---

### 评论 #3 — ROCmSupport (2021-06-23T05:06:20Z)

Hi @question12345 
I got your problem. You wish to check whether XGMI card is detected properly or not.
You can check this in dmesg, a simple command **dmesg | grep hive** shows the correct result.

For example:
I have a machine with 4GPUs connected to XGMI bridge.
[taccuser@rocm-qa-lr ~]$ **dmesg | grep hive**
[    5.955582] amdgpu 0000:3f:00.0: XGMI: Add node 3, hive 0x847de836f311c61a.
[    6.208173] amdgpu 0000:43:00.0: XGMI: Add node 2, hive 0x847de836f311c61a.
[    6.459841] amdgpu 0000:46:00.0: XGMI: Add node 0, hive 0x847de836f311c61a.
[    6.732090] amdgpu 0000:49:00.0: XGMI: Add node 1, hive 0x847de836f311c61a.

Hope this helps.
Thank you.

---

### 评论 #4 — question12345 (2021-06-24T10:17:10Z)

Thanks for the asnwer. 

So, here is my problem:

The 2 MI100 without the bridge are seen by the system:

========================== Link Type between two GPUs ==========================
            GPU0 GPU1
GPU0  0         PCIE
GPU1 PCIE     0

******************

Instead, If I connect them with the bridge then the system doesn't see them anymore at all.

The bridge is a 4 slots bridge, but I have only 2 MI100.

Is it possible that having a 4 slots bridge for only 2 MI100 then it does not work?

regards

---

### 评论 #5 — ROCmSupport (2021-06-25T04:42:30Z)

Hi @question12345 
The latest question in the previous comment was already answered by me @ https://github.com/RadeonOpenCompute/ROCm/issues/1503
Please take a look and hope it helps.
Thank you.

---
