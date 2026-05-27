# hsa_signal_wait_acquire() doesn't return on /opt/rocm/hsa/sample/vector_copy

> **Issue #13**
> **状态**: closed
> **创建时间**: 2016-06-06T06:51:24Z
> **更新时间**: 2018-10-25T00:35:40Z
> **关闭时间**: 2016-06-20T14:55:20Z
> **作者**: LWisteria
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/13

## 描述

cont. https://github.com/RadeonOpenCompute/hcc/issues/71

["verify-installation"](https://github.com/RadeonOpenCompute/ROCm#verify-installation) step doesn't succeed because hsa_signal_wait_acquire() doesn't return.

Environment is following:
- Ubuntu 14.04.4
- Core i7-3770K
- AMD Radeon R9 FuryX
- DDR3-1600 2GBx4

Steps to reproduce are following:
1. Clean-install ubuntu 14.04.4 ("Erase disk and install ubuntu")
2. Boot normally, and I got "low level graphic mode" (this is expected for FuryX, right?).
3. Enter console mode with "Ctrl+Alt+F1".
4. Install hcc; following https://github.com/RadeonOpenCompute/ROCm#add-the-rocm-apt-repository
5. reboot
6. Enter console mode again
7. export PATH=${PATH}:/opt/rocm/bin
8. cp -r /opt/rocm/hsa/sample/ ~/sample
9. cd ~/sample
10. make
11. ./vector_copy output following but doesn't finish.

```
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
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
```

This seems [hsa_signal_wait_acquire()](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-1.1.0/sample/vector_copy.c#L409) doesn't return.

What's the problem and how can I fix this?

Note that I use Ivy Bridge CPU so ROCm doen't support the CPU according to @whchung .
Could you point me to the notice for the supported CPU on any wiki page or other documents etc?

Thanks.


---

## 评论 (4 条)

### 评论 #1 — gstoner (2016-06-06T17:53:10Z)

This telling you Your processor does not support platform atomics.   We only tested on Haswell or newer CPU.

Get Outlook for iOShttps://aka.ms/o0ukef

On Sun, Jun 5, 2016 at 11:51 PM -0700, "YOSHIFUJI Naoki" <notifications@github.com<mailto:notifications@github.com>> wrote:

cont. RadeonOpenCompute/hcc#71https://github.com/RadeonOpenCompute/hcc/issues/71

"verify-installation"https://github.com/RadeonOpenCompute/ROCm#verify-installation step doesn't succeed because hsa_signal_wait_acquire() doesn't return.

Environment is following:
-   Ubuntu 14.04.4
-   Core i7-3770K
-   AMD Radeon R9 FuryX
-   DDR3-1600 2GBx4

Steps to reproduce are following:
1.  Clean-install ubuntu 14.04.4 ("Erase disk and install ubuntu")
2.  Boot normally, and I got "low level graphic mode" (this is expected for FuryX, right?).
3.  Enter console mode with "Ctrl+Alt+F1".
4.  Install hcc; following https://github.com/RadeonOpenCompute/ROCm#add-the-rocm-apt-repository
5.  reboot
6.  Enter console mode again
7.  export PATH=${PATH}:/opt/rocm/bin
8.  cp -r /opt/rocm/hsa/sample/ ~/sample
9.  cd ~/sample
10. make
11. ./vector_copy output following but doesn't finish.

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
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.

This seems hsa_signal_wait_acquire()https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-1.1.0/sample/vector_copy.c#L409 doesn't return.

What's the problem and how can I fix this?

Note that I use Ivy Bridge CPU so ROCm doen't support the CPU according to @whchunghttps://github.com/whchung .
Could you point me to the notice for the supported CPU on any wiki page or other documents etc?

Thanks.

## 

You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/13, or mute the threadhttps://github.com/notifications/unsubscribe/AD8DuU2DI9ueb_XgbE8Pk1P4CnvHs74-ks5qI8NsgaJpZM4Ium1u.


---

### 评论 #2 — earcam (2018-10-24T21:34:15Z)

Hi,

Apologies for commenting on an old, closed ticket - just one question.

I have the same CPU/GPU combo, and see this is [not supported](https://github.com/RadeonOpenCompute/ROCm#not-supported-or-very-limited-support-under-rocm) (Fiji with Ivybridge).

Would you please clarify if that's; never to be supported, possibly supported or certain to be supported?

Thank you

---

### 评论 #3 — jlgreathouse (2018-10-24T23:33:53Z)

If you have an Ivy Bridge that does not support PCIe atomics, then we do not currently have it on our roadmap to support gfx8 chips like Fiji for that CPU. Apparently [some Ivy Bridge-E chips do support PCIe atomics](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/217), but others don't. I don't have a precise list on hand -- the main point is whether they support atomics. If your chip doesn't support atomics, I would lean towards "gfx8 most likely never supported". See [this thread](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422836032) for more details.

---

### 评论 #4 — earcam (2018-10-25T00:04:25Z)

thanks @jlgreathouse - your linked comment clarifies perfectly why it's "most likely never supported".

(I checked the aged i7-3770K's datasheet, and unsurprisingly there's no mention of PCIe* 3.0 atomic operation)

---
