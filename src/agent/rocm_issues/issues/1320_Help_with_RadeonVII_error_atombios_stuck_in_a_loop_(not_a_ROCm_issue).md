# Help with RadeonVII error "atombios stuck in a loop" (not a ROCm issue)

> **Issue #1320**
> **状态**: closed
> **创建时间**: 2020-12-05T11:24:30Z
> **更新时间**: 2020-12-08T05:48:39Z
> **关闭时间**: 2020-12-07T22:26:50Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1320

## 描述

This is not a ROCm issue, I know; but maybe somebody in the know could kindly help me a bit:

On Ubuntu 20.04 (Linux kernel 5.3.0-18) a Radeon VII GPU fails at initialization (boot) time with this message in dmesg:
```
[drm:atom_op_jump [amdgpu]] *ERROR* atombios stuck in loop for more than 5secs aborting
[drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing 9300 (len 1031, WS 12, PS 8) @ 0x93A0
[drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing 9274 (len 63, WS 0, PS 8) @ 0x9295
amdgpu 0000:67:00.0: gpu post error!
amdgpu 0000:67:00.0: Fatal error during GPU init
[drm] amdgpu: finishing device.
```

What does this mean -- is the GPU hardware-damaged beyond repair? or is there anything that can be done to fix the GPU?

Thank you!


---

## 评论 (6 条)

### 评论 #1 — valeriob01 (2020-12-05T12:44:43Z)

I have already seen this error and recovered by reinstalling. Try changing your riser if you have one, if that does not work it is possible a kernel issue.
Which kernel do you use?


---

### 评论 #2 — ROCmSupport (2020-12-07T08:46:27Z)

Thanks @preda for reaching out.
I will check with our team and get back with possible solution.
Thank you.


---

### 评论 #3 — ROCmSupport (2020-12-07T12:47:40Z)

Most likely it indicates a hardware failure. The kernel can't read the VBIOS, which is a big problem, and isn't likely to be software. Try powering off for 30sec and restarting. If it still fails, I'd recommend the usual HW testing before an RMA (switch PCIe slots, try a different motherboard, different power connectors from PSU, etc)
Thank you.

---

### 评论 #4 — valeriob01 (2020-12-07T18:21:39Z)

> Most likely it indicates a hardware failure. The kernel can't read the VBIOS, which is a big problem, and isn't likely to be software. Try powering off for 30sec and restarting. If it still fails, I'd recommend the usual HW testing before an RMA (switch PCIe slots, try a different motherboard, different power connectors from PSU, etc)
> Thank you.

I have seen this error and recovered by rolling back to a previous kernel.


---

### 评论 #5 — preda (2020-12-07T22:26:10Z)

@ROCmSupport thank you for the communication!

@valeriob01 I diagnosed the affected GPU by swapping it with another good GPU of the same model, so I ruled out a software issue (the GPU itself is affected). I was just wondering whether the GPU breakage is "soft" and can be fixed "at home" or it's up for RMA. Seems like the latter, and the GPU was RMA'd already. I'm still not clear on what triggered the problem.


---

### 评论 #6 — valeriob01 (2020-12-08T05:48:02Z)

> @ROCmSupport thank you for the communication!
> 
> @valeriob01 I diagnosed the affected GPU by swapping it with another good GPU of the same model, so I ruled out a software issue (the GPU itself is affected). I was just wondering whether the GPU breakage is "soft" and can be fixed "at home" or it's up for RMA. Seems like the latter, and the GPU was RMA'd already. I'm still not clear on what triggered the problem.

So it seems your case is more severe than mine and this error can be triggered under different conditions.


---
