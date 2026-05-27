# BOINC Vega-based GPU processing does not work with ROCm

> **Issue #1569**
> **状态**: closed
> **创建时间**: 2021-09-01T08:49:08Z
> **更新时间**: 2021-12-31T08:09:48Z
> **关闭时间**: 2021-12-31T08:09:48Z
> **作者**: Wedge009
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1569

## 描述

**Background**
For many years now (even back during fglrx days) I've been using [BOINC](https://boinc.berkeley.edu/) successfully with AMD GPUs on Linux via amdgpu-pro. However, that changed with amdgpu-pro 20.45 onwards, when PAL-based OpenCL was dropped in favour of ROCr. While my Fiji-based GPUs still work okay using the 'legacy' OpenCL support in amdgpu-pro, my Vega-based GPUs (both Vega10 and Vega20) cannot process GPU tasks with ROCr-based OpenCL From amdgpu-pro versions 20.45 through to 21.10 inclusive, GPU tasks would crash immediately on attempting to run. With amdgpu-pro 21.20 to 21.30 (current release at time of writing), GPU tasks don't crash but instead appear to stall indefinitely - GPUs appear idle and there is no application progress.

This saga is documented in https://community.amd.com/t5/opencl/amdgpu-pro-20-45-rocr-vs-pal-opencl-breaks-boinc-gpu-processing/td-p/453227

**Relevance to ROCm**
I'm still not entirely clear on the relationship between ROCm and ROCr other than ROCr seems to be a run-time sub-set of ROCm?

The reason I'm reporting this here is because I finally managed to get BOINC running with ROCm 4.3 on Ubuntu 20.04.3 (kernel 5.11.0-27) yesterday. However, my experience appears to be identical to the aforementioned stalled processing with ROCr-based OpenCL support from amdgpu-pro. I've been told that BOINC and ROCm appear to work just fine on Polaris-based GPUs.

As a work-around, I've been relying on the last PAL-based OpenCL release of amdgpu-pro, version 20.40. That's not a feasible long-term solution, however, as amdgpu-pro 20.40 does not install with Ubuntu kernels beyond 5.4.0-54. If there is indeed a connection between the behaviour I'm observing for ROCm and ROCr-based OpenCL support from amdgpu-pro, I can report my findings here as well as on AMD Community.

---

## 评论 (21 条)

### 评论 #1 — Wedge009 (2021-09-03T00:34:17Z)

I recently received information of a user who has successfully got BOINC working with ROCm. Same Threadripper 3960X CPU, same Radeon VII GPU, difference is they are using Arch Linux with self-compiled ROCm 4.3.1 while I'm using Ubuntu with official ROCm 4.3.0 packages. I've yet to get any feedback on how they got their ROCm set-up working but I wonder if there's an issue somewhere in the Ubuntu packaging...

---

### 评论 #2 — ROCmSupport (2021-09-13T07:43:02Z)

Thanks @Wedge009 for reaching out.
I got the context well.
Can you please update me with the below information initially.

1. whats the GPU you are using?
2. outputs of /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo

I am not sure about BOINC and never deployed any projects on my machines so far and so no idea on that.
I will definitely help w.r.to ROCm.
Thank you.

---

### 评论 #3 — Wedge009 (2021-09-13T08:09:49Z)

1. As mentioned in the initial post, I'm using both Vega10 (Vega 64) and Vega20 (Radeon VII), albeit in separate machines.
- My recent attempt with Radeon VII resulted in an awful slow-down of the KDE Plasma shell (very poor responsiveness ultimately freezing the whole system) even when not doing any GPU processing. I thought that ROCm focused on OpenCL so I assumed the regular amdgpu drivers in the kernel would handle normal display operations - but perhaps I'm wrong there? Removing ROCm has restored a functional desktop to me (this machine is my primary day-to-day workstation).
- I had experimented with Vega 64 when I wrote the first post and while I didn't have the same crippling lack of responsiveness as with ROCm on Radeon VII, I was not able to get any processing done under ROCm - GPU usage was 0% and the GPU application appeared to have stalled indefinitely, mirroring my experience with ROCr-based OpenCL under amdgpu-pro.
- In both cases I have to revert to the last amdgpu-pro with PAL-based OpenCL, version 20.40, for day-to-day work as per my saga in https://community.amd.com/t5/opencl/amdgpu-pro-20-45-rocr-vs-pal-opencl-breaks-boinc-gpu-processing/td-p/453227

2. I don't have the outputs on hand, but I can obtain them next time I attempt to use ROCm. I confirm that `clinfo` and `rocminfo` both correctly report the respective GPU when ROCm is installed, although I do have to manually hack `/etc/OpenCL/vendors/amdocl64_40300.icd` to use an absolute path for `libamdocl64.so` in order to get `clinfo` (and consequently BOINC) to obtain the GPU information correctly.

FYI, BOINC is a framework for contributing to distributed computing projects, most famously SETI@home, but many other scientific projects too. Tasks may be run on CPU or GPU and while BOINC's GPU detection can be a bit finicky, once CAL (which I know is deprecated), OpenCL, or CUDA-capable GPUs are detected, GPU processing under BOINC has usually been straightforward, on both Windows and Linux, for both AMD (at least for PAL-based OpenCL) and Nvidia GPUs.

---

### 评论 #4 — ROCmSupport (2021-09-13T08:17:41Z)

Thanks for the information @Wedge009 
Please make sure that system is clean (without installing amdgpu or similar) before installing rocm.

Thank you.

---

### 评论 #5 — Wedge009 (2021-09-13T08:23:54Z)

To clarify, amdgpu-pro is removed before attempting to install ROCm, and vice-versa.

I understand amdgpu is part of the kernel and doesn't make sense to remove, unless I want to have a broken system that cannot display anything.

Edit: And even when I install amdgpu-pro for its OpenCL implementation, I do so headlessly (option `--headless`) so amdgpu is still used for display.

---

### 评论 #6 — ROCmSupport (2021-09-23T09:48:27Z)

Hi @Wedge009 
I recommend to try with simple apps to reproduce the problem.
Do you wish to share any update on this issue?

---

### 评论 #7 — Wedge009 (2021-09-23T10:08:42Z)

The only reason I have to use ROCm is for OpenCL functionality with BOINC tasks. PAL-based OpenCL in amdgpu-pro works fine, so I never really understood why ROCr was forced as a replacement (eg I believe Windows drivers still include PAL implementation since ROCm appears to be Linux-only for now). I've recently discovered another user who was able to run BOINC with ROCr-based OpenCL from amdgpu-pro, but he admits he doesn't remember how he managed to get it working - only that it took a lot of manual work to do so, which suggests that it's difficult to get a working configuration for everyone.

For my own Radeon VII system, ROCm produced an unstable/unresponsive system under KDE Plasma - forget trying to run 'simple' programs, even just having a working system was not possible. Vega 64 seemed to give a functional system, but BOINC tasks would just stall (no GPU load, no application progress) under either ROCm or ROCr-based OpenCL from amdgpu-pro.

I haven't yet seen any updated ROCm packages for Ubuntu beyond 4.3.0 and the current release is still 4.3.1 - when the packages are updated I was thinking to give it another try, and also obtain those `clinfo` and `rocminfo` outputs to show that the system is at least recognising the GPUs. Given PAL-based OpenCL works fine, I'm always reticent to try ROCm again given the hassle and operational down-time, but I keep trying because I don't think I can stay on an old version of amdgpu-pro indefinitely, especially when the next LTS Ubuntu is released (I believe scheduled for April 2022).

---

### 评论 #8 — ROCmSupport (2021-10-06T02:26:12Z)

Thanks for the update @Wedge009, I got clarity of your things.
Yes, currently its with 4.3.1, and we do not have plans to release 4.4 as per internal strategy.
We have plans to release 4.5 soon, approximately, in a month or with little more time, which is coming with advanced driver mechanism. 
Request you to try the same. Thank you.

---

### 评论 #9 — Wedge009 (2021-10-06T02:33:53Z)

No worries. I'm continuing to watch for both amdgpu-pro and ROCm releases as with every release I give it a try to see if things have improved for my hardware configuration. I'm also considering running off-line tests by running GPU tasks directly instead of running through the automated BOINC framework. At time of writing amdgpu-pro is still at 21.30 and as you say ROCm is still 4.3.1.

---

### 评论 #10 — Wedge009 (2021-10-17T07:26:26Z)

It's a different system - but with Ubuntu 20.04.3 LTS and `rocm-dkms` 4.3.0 installed from scratch - but same Vega 64 GPU model and same results with respect to GPU remaining idle during a BOINC GPU task. This time I grabbed the outputs for `clinfo` and `rocminfo` as requested. As best as I can see, the Vega 64 GPU is correctly listed in both tools.

[clinfo-4.3.0-vega64.txt](https://github.com/RadeonOpenCompute/ROCm/files/7359007/clinfo-4.3.0-vega64.txt)
[rocminfo-4.3.0-vega64.txt](https://github.com/RadeonOpenCompute/ROCm/files/7359008/rocminfo-4.3.0-vega64.txt)

---

### 评论 #11 — Wedge009 (2021-11-02T00:37:01Z)

Noting 4.5.0 just released, packages are available, will retest in the next few days.

---

### 评论 #12 — ROCmSupport (2021-11-02T11:32:20Z)

Thanks @Wedge009 
Please verify with ROCm 4.5 and update, Thank you.

---

### 评论 #13 — Wedge009 (2021-11-03T00:45:41Z)

Something seems to be wrong with the Ubuntu packages for 4.5 release. `rocm-dkms` depends on `rock-dkms`, but it doesn't appear to be available:

https://repo.radeon.com/rocm/apt/4.3/pool/main/r/rock-dkms/
https://repo.radeon.com/rocm/apt/4.5/pool/main/r/rock-dkms/ (returns HTTP 404)

---

### 评论 #14 — ROCmSupport (2021-11-10T11:51:19Z)

Hi @Wedge009 
rock-dkms is deprecated now and new installation process introduced.
Please check @ [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html](url)
Thank you.

---

### 评论 #15 — seesturm (2021-11-10T12:09:55Z)

In case someone wants to know what changed with new ROCm release but does not want to read whole installation guide:
Looks like rocm-dkms is replaced by amdgpu-dkms from AMDGPU repository. AMDGPU repository location can be found in section [Base URLs For AMDGPU and ROCm Stack Repositories](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#id48)

---

### 评论 #16 — Wedge009 (2021-11-10T12:15:58Z)

Yep - I also wonder, since I'm only interested in OpenCL support, whether it's sufficient to just install `rocm-opencl-sdk`, but perhaps I'll stick to the top-level `amdgpu-dkms` for now.

I don't know if it's significant, but I just noticed that 4.5 disappeared from https://github.com/RadeonOpenCompute/ROCm/releases. It only shows 4.3.1 as 'latest' now, at time of writing.

---

### 评论 #17 — Wedge009 (2021-11-12T22:57:31Z)

I haven't had a chance to try 4.5 yet (waiting on outstanding tasks to finish on current working driver first), but I noticed [amdgpu-pro 21.40.1](https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-40-1) just released and seems to match the install script method described in https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html. So looks like everything is being unified, no more separate ROCm and amdgpu-pro releases.

---

### 评论 #18 — ROCmSupport (2021-11-16T09:23:25Z)

Hi @Wedge009 
You can take 4.5 from https://github.com/RadeonOpenCompute/ROCm/tags, if you wish.
request to try the actual issue with ROCm 4.5 and update asap. Thank you.

---

### 评论 #19 — Wedge009 (2021-11-16T11:02:50Z)

Haven't forgotten - I intend to set-up and test amdgpu-pro 21.40.1 with Vega soon. Have already got it running fine with legacy OpenCL on Fiji (which is not ROCm-based, I know).

---

### 评论 #20 — Wedge009 (2021-11-17T09:35:49Z)

What a pleasant surprise. I got ROCr-based OpenCL from amdgpu-install 21.40.1 running successfully on one host with Vega10, no hacks or work-arounds needed. All I did was remove amdgpu-pro 20.40, update to current HWE kernel, and run `amdgpu-install --opencl=rocr` (with reboots in between).

Hopefully that bodes well for my other two hosts (one with Vega10, the other with Vega20) still stuck on kernel 5.4. I'll be sure to close this once I get around to updating them, if it's successful.

---

### 评论 #21 — Wedge009 (2021-12-31T08:09:48Z)

It turns out that the struggles I was having with Vega20 was apparently due to a hardware fault with one the cards - it seems it's not reliable but neither is it 100% broken. Unfortunate for me, but fortunate in terms of the software support situation. Closing this as resolved with release of amdgpu 21.40.1.40501.

---
