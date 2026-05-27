# error messages: kfd2kgd: Failed to map bo to gpuvm; kfd2kgd: amdgpu_vm_bo_update failed

> **Issue #791**
> **状态**: closed
> **创建时间**: 2019-05-08T19:25:56Z
> **更新时间**: 2019-10-05T08:15:41Z
> **关闭时间**: 2019-10-05T08:15:41Z
> **作者**: Moading
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/791

## 描述

Hi,

i'm developing a multi GPU program that uses MPI parallelization. The setup I'm using is as follows:
Mainboard: X10SRA-F
GPU: 2 x Radeon Pro Duo, i.e. 4 ASICS
OS: ubuntu 18.04.2 LTS, kernel 4.15.0-48-generic, ROCm 2.4

When using about 10.7 GB per GPU in a run where two MPI ranks use 2 GPUs each, the following errors start showing up in dmesg after the program has been running for a while. Also the performance of the program starts to drop when the error messages start showing up.

message 1:
[  374.528056] amdgpu 0000:0a:00.0: bo 000000008621f4e3 va 0x0001907700-0x0001907805 conflict with 0x0001907700-0x0001907802
[  374.528937] kfd2kgd: Failed to map VA 0x1907700000 in vm. ret -22                                                                                                                       
[  374.529847] kfd2kgd: Failed to map bo to gpuvm
[  374.530783] Failed to map to gpu 0/4

message 2:
[  375.487864] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[  375.487871] kfd2kgd: amdgpu_vm_bo_update failed
[  375.488963] kfd2kgd: validate_invalid_user_pages: update PTE failed

Both messages show up many times and they are printed in red!

Is that a problem with ROCm or with my code? The error does not show up when using one GPU per MPI rank only. For smaller data sets the and 2 GPUs per MPI rank the problem does not show up. The code does not produce out of bound memory access, I believe.

Greetings

---

## 评论 (5 条)

### 评论 #1 — alexfriman (2019-05-20T09:08:01Z)

I have similar messages while using single GPU with ROCk and ROCm. The same code works fine with mesa + ROCm drivers.

---

### 评论 #2 — alexfriman (2019-05-30T11:02:59Z)

There is a possible explanation and solution: https://github.com/RadeonOpenCompute/ROCm/issues/785

---

### 评论 #3 — Moading (2019-06-16T22:13:17Z)

@ alexfriman,
I still see the messages in ROCm 2.5-27. The solution proposed in #785 was applied in ROCm 2.5-27. Looking at the file "/usr/src/amdgpu-2.5-27/amd/amdgpu/amdgpu_vram_mgr.c", I see another occurence of kfree in line 178. Maybe that should be replaced as well?
Maybe @kentrussell can have a look at this ?!?

---

### 评论 #4 — kentrussell (2019-06-17T11:17:11Z)

That wouldn't be the same issue. For the amdgpu_vram_mgr_fini (line 178 you're referring to), the kfree lines up with the kzalloc in the amdgpu_vram_mgr_init , so that's not the case. The issue is using kfree on memory that was kvmalloc'd . kvmalloc requires kvfree, while kmalloc require kfree. The kfree on 178 is correct, since it's kzalloc that's used to allocate that memory.

@fxkamd , you're far more familiar with the memory management than I am. Any thoughts?

---

### 评论 #5 — fxkamd (2019-06-17T21:10:18Z)

@kentrussell, what you said is correct. The kfree matches a kzalloc. No problem.

---
