# modprobe amdgpu crashes on Ubuntu 18.04 / kernel 4.18.x with amdgpu firmware binaries dated 12/08/2018

> **Issue #716**
> **状态**: closed
> **创建时间**: 2019-02-20T20:17:05Z
> **更新时间**: 2019-03-14T15:18:49Z
> **关闭时间**: 2019-03-14T14:46:58Z
> **作者**: bpsegal
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/716

## 描述

Setup:

* ASUS x86_64 Ubuntu 18.04 Bionic with 4.18.0-041800-generic kernel (or can be any point release 4.18.x or any 4.19.x)
* Vega 10 gfx900 WX 9100 GPU
* I have the amdgpu kernel module blacklisted so it doesn't load on boot

Then 
`sudo modprobe amdgpu`  will result in a kernel crash forcing a full power-cycle to recover (I can get the kernel logs as needed) when using `vega10_*.bin` firmware binaries dated 12/08/2018.

Is this a known issue?

Part of the reason I'm motivated to use the latest amdgpu (vega10) firmware is that my OpenCL testcase hangs on the clEnqueueMapBuffer (see Issue [67](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/67))

and some investigation shows my testcase is working in all instances where the latest firmware is successfully loaded by amdgpu (either dkms amdgpu on 4.15 or vanilla amdgpu in 4.20).

I'm wondering if there's an up-to-date kernel 4.18 that works with the latest provided firmware binaries.

Thanks for any insight you can provide!

-Ben

---

## 评论 (5 条)

### 评论 #1 — kentrussell (2019-03-14T10:06:01Z)

There is a known issue with 2.2 with the 4.18 kernel (though your issue was 2.1, it is still incompatible with the 4.18 kernel). A fix will be included in 2.3. For now, you'll need to stick with the upstream kernel, or downgrade to 4.15. I have updated the documentation at https://github.com/RadeonOpenCompute/ROCm/pull/736 to clarify this. Thanks for the bug report. I'll leave it open until 2.3 so that other users can hopefully find it
You can also build the kernel yourself from the ROCK github code tree (https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver) and install that instead of using the DKMS package, as it's just the DKMS package that has the issue (the monolithic kernel works, and is based on 4.18).

---

### 评论 #2 — jlgreathouse (2019-03-14T14:46:58Z)

Dupe of #731 

I understand this issue came first, but rather than have a bunch of reports for the same issue floating around, I'll close this one and leave the other open. The title of that one is a bit more generic. :)

---

### 评论 #3 — bpsegal (2019-03-14T15:10:59Z)

Hi @kentrussell and @jlgreathouse .  Thanks for your response to my reported issue, but I am not convinced this is completely a dupe of #731 .  In my case, I'm not talking about *building* the dkms module on top of a vanilla 4.18.x kernel [although I did identify that as a problem in OpenCL issue #67], but rather, the *startup* of the *vanilla* amdgpu device driver (packaged with 4.18.x) using the most recent amdgpu* firmware packaged with the linux kernel.  In this case, the modprobe of amdgpu fails during HW IP initialization.  

If I "downgrade" the firmware, I can start the amdgpu device driver, but with diminished functionality (in particular the SDMA queues are not functional).  One thing I can try, however, is directly building from the ROCK-Kernel source (based on 4.18), and see where that leads.

---

### 评论 #4 — jlgreathouse (2019-03-14T15:14:35Z)

If you are having problems with the Vanilla amdgpu, I would recommend taking your problem to the [amd-gfx mailing list](https://lists.freedesktop.org/mailman/listinfo/amd-gfx). This ROCm issue tracker is specifically for ROCm and our ROCm-specific drivers, not for our upstream drivers.

---

### 评论 #5 — bpsegal (2019-03-14T15:18:49Z)

ok, thanks.

---
