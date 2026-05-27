# installing older version 1.6

> **Issue #517**
> **状态**: closed
> **创建时间**: 2018-08-29T22:19:08Z
> **更新时间**: 2018-08-30T01:03:18Z
> **关闭时间**: 2018-08-30T01:03:18Z
> **作者**: trinayan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/517

## 描述

Hi,

I want to install an older version of ROCM (v 1.6) to test the AMD gem5  GPU simulator since it mentions that as the official version supported. Could anyone help me get started on how to do this?. I need it for a project and would appreciate the help.
Thanks.

Best,
Trinayan

---

## 评论 (3 条)

### 评论 #1 — atgutier (2018-08-29T23:42:38Z)

Hi Trinayan,

We have some documentation on the gem5 wiki about our GPU model: http://gem5.org/GPU_Models#Runtime_software_and_toolchain

We use the roc-1.6.x branch for the repos mentioned in the above link.

If you have any further gem5 questions we have a mailing list. gem5.org has more information.

Tony

---

### 评论 #2 — trinayan (2018-08-30T00:59:32Z)

@atgutier : Thanks Tony. Actually I tried to run the simulator and got errors. My question was posted a few days back(https://www.mail-archive.com/gem5-users@gem5.org/msg15909.html). But not sure if anyone has looked into it yet. One of the many reasons for the error mentioned there could be that the system I was using had rocm 1.8 instead. So just want to install the 1.6 version and try the simulator again. In case you think the error mentioned there points to some other potential problem please let me know. I am very interested in using the simulator for my research work and would be glad if i can get any assistance in setting the simulator up. Thank you. 

---

### 评论 #3 — jlgreathouse (2018-08-30T01:03:18Z)

Hi @trinayan 

For reference, we keep old versions of our ROCm installation packages at http://repo.radeon.com/rocm/archive/

You can use these to create e.g. a [local apt repo ](https://www.linux.com/learn/create-your-own-local-apt-repository-avoid-dependency-hell)and install the binaries using that.

Beyond that, it looks like that question is actually related to gem5 rather than ROCm, so I recommend you follow up with that group in their mailing list.

---
