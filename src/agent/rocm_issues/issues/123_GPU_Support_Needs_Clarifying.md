# GPU Support Needs Clarifying

> **Issue #123**
> **状态**: closed
> **创建时间**: 2017-05-17T12:48:37Z
> **更新时间**: 2017-05-22T19:20:54Z
> **关闭时间**: 2017-05-21T19:02:26Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/123

## 描述

It's not clear in the docs whether some recent but not cutting-edge cards, such as my R9 390, can use RocM. The docs. make it unclear whether the cards simply don't work, or if they just don't play well with the CPU/one-another.

I'm currently trying to use ROCm and hipCaffe, and anything CL-related, even `clinfo`, seems to freeze early and occupy a full CPU core but negligible RAM until killed. I don't know if this is because my hardware isn't supported, or if I'm missing some key component (e.g., I uninstalled AMDGPU-pro, did I need to reinstall another OpenCL driver, or did that come with the ROCm package?).

Could do with some clarification, and I'd appreciate some quick answers also.

---

## 评论 (15 条)

### 评论 #1 — gstoner (2017-05-17T13:02:53Z)

You can not run ROCm stack on AMDGPU driver at the same time they are two different drivers.

Good place to start is here
https://rocm.github.io/install.html

On May 17, 2017, at 7:48 AM, Cathal Garvey <notifications@github.com<mailto:notifications@github.com>> wrote:


It's not clear in the docs whether some recent but not cutting-edge cards, such as my R9 390, can use RocM. The docs. make it unclear whether the cards simply don't work, or if they just don't play well with the CPU/one-another.

I'm currently trying to use ROCm and hipCaffe, and anything CL-related, even clinfo, seems to freeze early and occupy a full CPU core but negligible RAM until killed. I don't know if this is because my hardware isn't supported, or if I'm missing some key component (e.g., I uninstalled AMDGPU-pro, did I need to reinstall another OpenCL driver, or did that come with the ROCm package?).

Could do with some clarification, and I'd appreciate some quick answers also.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/123>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuUF67rSN_Jv9b792HXbY6Z_odLm0ks5r6uylgaJpZM4Nd0EZ>.



---

### 评论 #2 — ghost (2017-05-17T13:07:03Z)

Sorry, that wasn't clear; I uninstalled AMDGPU-pro when installing ROCm. Should I take your message to mean that ROCm *does* include an OpenCL-compatible driver? So, that's not my problem.

*Should* ROCm work with an R9 390? I bought the card to do deep learning on, based on early support in Torch7 and Caffe. I'd love to use the hipCaffe stack, because compared to Tensorflow it uses less proprietary garbage, and compared to Torch7 it's not Lua. :)

---

### 评论 #3 — gstoner (2017-05-17T16:31:17Z)

Let me check the status on R390 and ROCm 1.5,   We test locally  W9100, S9150, S9170 sine we had  a  lot of them available from my previous program.  They are Hawaii based as well.

OpenCL is supported on ROCm,   we even released the source code for it this last week.   Fulfilling our promise on opening up all components in our stack.  It is compatible with OpenCL 1.2 but has OpenCL 2.0 kernel language support as well.


Post ROCm install to get OpenCL on the system you need use this command
sudo apt-get install rocm-opencl-dev

On May 17, 2017, at 8:07 AM, Cathal Garvey <notifications@github.com<mailto:notifications@github.com>> wrote:


Sorry, that wasn't clear; I uninstalled AMDGPU-pro when installing ROCm. Should I take your message to mean that ROCm does include an OpenCL-compatible driver? So, that's not my problem.

Should ROCm work with an R9 390? I bought the card to do deep learning on, based on early support in Torch7 and Caffe. I'd love to use the hipCaffe stack, because compared to Tensorflow it uses less proprietary garbage, and compared to Torch7 it's not Lua. :)

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/123#issuecomment-302084220>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudfxrF7V5aQRDNbEGQ3ZzaxGbKqQks5r6vD3gaJpZM4Nd0EZ>.



---

### 评论 #4 — ghost (2017-05-17T20:01:32Z)

> Let me check the status on R390 and ROCm 1.5

Thanks a million @gstoner!

> Post ROCm install to get OpenCL on the system you need use
> this command
>  sudo apt-get install rocm-opencl-dev

Have done, but with no success.

I may try booting from a persistent live USB or something, and will attempt a clean install on an unaltered Ubuntu 16.04. That would rule out difficulties with a pre-existing CL platform.

I did just discover that I was using the `clinfo` binary previously installed by whatever OpenCL procedure I followed with AMDGPU-pro. I ran the clinfo that came with ROCm, and got this result:

```bash
cathal@thinkum:~/Projects/scrapers/altreich/misesorg$ /opt/rocm/opencl/bin/x86_64/clinfo -v
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

---

### 评论 #5 — gstoner (2017-05-17T21:15:08Z)

Did this work

cd /opt/rocm/hsa/sample make ./vector_copy

On May 17, 2017, at 3:01 PM, Cathal Garvey <notifications@github.com<mailto:notifications@github.com>> wrote:


Let me check the status on R390 and ROCm 1.5

Thanks a million @gstoner<https://github.com/gstoner>!

Post ROCm install to get OpenCL on the system you need use
this command
sudo apt-get install rocm-opencl-dev

Have done, but with no success.

I may try booting from a persistent live USB or something, and will attempt a clean install on an unaltered Ubuntu 16.04. That would rule out difficulties with a pre-existing CL platform.

I did just discover that I was using the clinfo binary previously installed by whatever OpenCL procedure I followed with AMDGPU-pro. I ran the clinfo that came with ROCm, and got this result:

cathal@thinkum:~/Projects/scrapers/altreich/misesorg$ /opt/rocm/opencl/bin/x86_64/clinfo -v
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/123#issuecomment-302215382>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSRcAvVIshULmoQaHNrPzU-RyfU7ks5r61IdgaJpZM4Nd0EZ>.



---

### 评论 #6 — ghost (2017-05-17T21:22:20Z)

I tried that first, per the instructions for installing hipCaffe. Like 
all other OpenCL-related things since installing ROCm, it freezes at 
100% CPU use when trying to get a context, and doesn't crash, or 
proceed, until killed.

If I try too many times (not sure what's the limit here) to launch an 
OpenCL thing or things, then the output from vector_copy changes; 
instead of putting out a few lines on its progress and then hanging, it 
simply reports "Initializing the hsa runtime failed." and exits cleanly.






---

### 评论 #7 — scchan (2017-05-17T21:42:55Z)

Could you do a `uname -a` make sure the correct kernel is loaded?  You should see `compute-rocm-rel-1.5` in the name.  I'd also suggest trying `/opt/rocm/bin/rocm-smi -a` and see if the tool sees the GPU.

---

### 评论 #8 — ghost (2017-05-17T21:51:04Z)

 > $ uname -a
 > Linux thinkum 4.9.0-kfd-compute-rocm-rel-1.5-80 #1 SMP Fri May 12 
16:10:01 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux

 > $ /opt/rocm/bin/rocm-smi
 > ===================   ROCm System Management Interface   
===================
 > ===================          End of ROCm SMI Log         
===================

(Though bear in mind in the second case; for some reason the HIP system 
fails after a few tries, and right now it's failed. Possibly after a 
restart the `rocm-smi` command would work?)

I'm just working on setting up a LiveUSB Ubuntu that I can try a clean 
install on. It's taking longer than expected, sorry.



---

### 评论 #9 — scchan (2017-05-17T22:01:49Z)

It looks like you didn't pass the `-a` switch to rocm-smi :)
I'd suggest that you start with /opt/rocm/hsa/sample/vector_copy first to make sure it works reliably.  

For HIP/HCC, since the compiler generates ISA code for Fiji by default, you'll have to re-compile your programs with specifying the architecture for Hawaii (i.e. R390).  

You could override the default architecture for your card by doing

`export HCC_AMDGPU_TARGET=gfx701`

more details:  https://github.com/RadeonOpenCompute/hcc/wiki#compiling-for-different-gpu-architectures



---

### 评论 #10 — ghost (2017-05-17T22:05:07Z)

Hi, thanks for catching that! Here's the output with "-a":

```
cathal@thinkum:/opt/rocm/hsa/sample$ /opt/rocm/bin/rocm-smi -a


===================   ROCm System Management Interface   
===================


===================   ROCm System Management Interface   
===================
============================================================================
GPU[0] 		: GPU ID: 0x67b1
============================================================================
============================================================================
GPU[0] 		: Temperature: 68.0c
============================================================================
============================================================================
GPU[0] 		: GPU Clock Level: 7 (1040Mhz)
GPU[0] 		: GPU Memory Clock Level: 1 (1500Mhz)
============================================================================
============================================================================
GPU[0] 		: Fan Level: 89 (34.9)%
============================================================================
============================================================================
GPU[0] 		: Current PowerPlay Level: auto
============================================================================
============================================================================
GPU[0] 		: Current OverDrive value: 0%
============================================================================
============================================================================
GPU[0] 		: Minimum SCLK: 1008MHz
GPU[0] 		: Minimum MCLK: 0MHz
GPU[0] 		: Activity threshold: 30%
GPU[0] 		: Hysteresis Up: 0ms
GPU[0] 		: Hysteresis Down: 5ms
============================================================================
============================================================================
GPU[0] 		: Cannot get GPU power Consumption: Average GPU Power not 
supported
============================================================================
============================================================================
GPU[0] 		: Supported GPU clock frequencies on GPU0
GPU[0] 		: 0: 300Mhz
GPU[0] 		: 1: 500Mhz
GPU[0] 		: 2: 726Mhz
GPU[0] 		: 3: 892Mhz
GPU[0] 		: 4: 935Mhz
GPU[0] 		: 5: 972Mhz
GPU[0] 		: 6: 1008Mhz
GPU[0] 		: 7: 1040Mhz *
GPU[0] 		:
GPU[0] 		: Supported GPU Memory clock frequencies on GPU0
GPU[0] 		: 0: 150Mhz
GPU[0] 		: 1: 1500Mhz *
GPU[0] 		:
============================================================================
===================          End of ROCm SMI Log         
===================

```

I'll try exporting that and rebuilding the tests, thank you! Although, 
perhaps the tooling, such as the libs and `clinfo`, would need 
rebuilding also in that case? Would I need to do a source-level 
re-build of ROCm including kernel modules, for this to work? :/




---

### 评论 #11 — ghost (2017-05-17T22:13:00Z)

Output when I try with the env-var set (PS: I had to restart to get HIP 
to work again, and now my screen has started flickering after a clean 
reboot...)

```bash
cathal@thinkum:~/sample$ export HCC_AMDGPU_TARGET=gfx701
cathal@thinkum:~/sample$ make
gcc -c -I/opt/rocm/include -o vector_copy.o vector_copy.c -std=c99
gcc -Wl,--unresolved-symbols=ignore-in-shared-libs vector_copy.o 
-L/opt/rocm/lib -lhsa-runtime64 -o vector_copy
cathal@thinkum:~/sample$ ./vector_copy
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx701.
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

...and there it hangs, forever. `top` shows it running at 100% CPU and 
0.1% mem. :/

---

### 评论 #12 — ghost (2017-05-18T12:00:40Z)

OK, breakthrough, kinda:

1. Set up new hard drive with fresh Ubuntu 16.04 LTS install.
2. Follow installation instructions [here](https://github.com/ROCmSoftwarePlatform/hipCaffe/blob/hip/README.ROCm.md) as far as checking `vector_copy`.

With the provided envvar you suggested, this now builds and runs. And. the ROCm `clinfo` program runs. So that's great!

Problem: This is all done in TTY1, because after installing `rocm` and restarting, the login screen won't display. I get a white screen with pretty pastel specks all over it. TTYs will load, but if I try to go to the login screen, I just get an unchanging white/cream field with pastel speckles. :/

I'll build Caffe later and see how that goes, meanwhile I need to boot back into my actual harddrive. Though, the AMDGPU-pro -> ROCm transition seems to have destabilised that install, so I think I'll be reinstalling soon!

---

### 评论 #13 — ghost (2017-05-21T19:02:26Z)

Giving up on this, at least for now. It looks like ROCm is being developed with very limited card support right now, and I need a stable system more than I need Tensorflow.

Thanks anyway..

---

### 评论 #14 — gstoner (2017-05-22T17:14:18Z)

@cathalgarvey 

Sorry for the trouble with the R9-390,   ROCm is more optimized for GFX8 and newer GPU which support Atomics.  GFX7 had a number of limitation relative to newer hardware.   For your purpose would of running Tensorflow RX480 be better GPU.  If you let me know your contact info privately,  we can get one out to you for testing. 

---

### 评论 #15 — ghost (2017-05-22T19:20:54Z)

Wow, that's really generous @gstoner - I couldn't turn down an offer like that. :)

I'll email your HSA email, very happy to be a guinea pig for Open Source GPU deep learning!

---
