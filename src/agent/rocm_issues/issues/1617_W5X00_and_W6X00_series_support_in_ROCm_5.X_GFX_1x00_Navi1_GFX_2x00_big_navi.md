# W5X00 and W6X00 series support in ROCm 5.X  GFX 1x00 Navi1 GFX 2x00 "big" navi

> **Issue #1617**
> **状态**: closed
> **创建时间**: 2021-11-15T15:00:41Z
> **更新时间**: 2023-01-09T02:55:03Z
> **关闭时间**: 2022-02-21T07:58:59Z
> **作者**: FCLC
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1617

## 描述

Without asking for a specific date, we've now seen 5.0 announced during the latest keynote, and we've also had our expectations set for  Navi 1 and Navi 2 support in the "early" 5.x series. What timeframe can we reasonably expect each of RDNA1 and RDNA2 to be enabled in the ROCm stack?

see #1595 , #1592 #1547 #1544 #1539 etc. 

I realize that writing a compute stack for a nascent language is no small feat, all the while trying to meet the deadlines for MI_2X0 support, and while getting the Frontier software stack ready. 

All the same, I don't really care about that, since I can't perform any initial development on my workstation before deploying to clusters that need HIP/ROCm. 

We're over 2 years in for RDNA1 and this week marks 2 years since the W5700 first started shipping (and consequently landed on my desk). 

This isn't news to anyone, but a typical workflow is to develop on the workstation, train/compute in the cloud, then inference at the edge. 

We currently have no good way of doing  the first step outside of: 

A) Using aging hardware that becomes less and less relevant every quarter.
B) Putting an MI100 Server class card in a workstation chassis, 3d printing/manufacturing some sort of high airflow low noise bracket to force enough air through the card to keep it operating correctly. 

That or we use hip as an intermediary to cuda, at which point we may as well just be using DPCT/dpcpp from oneAPI and target anything from AVX to SYCL to FPGA etc. 

---

## 评论 (37 条)

### 评论 #1 — FCLC (2021-11-15T15:40:28Z)

I'd also ask that this issue be left open until such a time as support is officially added to the ROCm stack. 

---

### 评论 #2 — ROCmSupport (2021-11-16T07:45:41Z)

Hi @FCLC 
Thanks for reaching out and sharing your views.
Navi21 support is on the way and its going to be officially supported very soon. Please stay tuned.
I am not closing this thread until Navi is enabled in ROCm officially.
Thank you.

---

### 评论 #3 — unexploredtest (2021-11-16T08:45:06Z)

> I am not closing this thread until Navi is enabled in ROCm officially.

RDNA 1 included?


---

### 评论 #4 — FCLC (2021-11-16T12:57:15Z)

> Navi21 support is on the way and its going to be officially supported very soon. Please stay tuned.
> 
> I am not closing this thread until Navi is enabled in ROCm officially.

@ROCmSupport I appreciate the response. 
Does the above include RDNA1? And if so, what is the general time frame? 

If I understand correctly the expected roadmap is: 
Finalize Navi21 -> Navi22 -> rest of Navi 2x series (Navi 23 and 24)-> Navi10 -> Navi 14/12

Please correct the above as needed.

Thanks, 

-Fclc 

---

### 评论 #5 — ROCmSupport (2021-11-16T13:01:47Z)

Hi @FCLC and @unexploredtest, thanks for your interest on Navi + ROCm.
I do not have concrete data on Navi roadmap. But I am sure that some set of Navi cards are coming with ROCm enabled very soon, I can not share all details right now. Request to wait for some time.
Thank you.

---

### 评论 #6 — FCLC (2021-11-16T14:06:48Z)

> Hi @FCLC and @unexploredtest, thanks for your interest on Navi + ROCm. I do not have concrete data on Navi roadmap. But I am sure that some set of Navi cards are coming with ROCm enabled very soon, I can not share all details right now. Request to wait for some time. Thank you.

Thanks for this. I unfortunately haven't seen any mention of Navi 1. 

Would it be possible to mark/use this issue to log which graphics core's have and have not received support? 

---

### 评论 #7 — FCLC (2021-11-22T17:56:59Z)

Looks like the next release that will expand support for RDNA is coming in early 2022 per #1618 

---

### 评论 #8 — Djip007 (2021-12-11T10:51:27Z)

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#confirm-you-have-a-rocm-capable-gpu
the RNDA2 AMD Radeon™ PRO W6800 is list as supported
is with release 4.5.2 RDNA2 in some card enable ???

---

### 评论 #9 — FCLC (2021-12-11T15:04:30Z)

> the RNDA2 AMD Radeon™ PRO W6800 is list as supported
> is with release 4.5.2 RDNA2 in some card enable ???

Yes, as of 4.5.x, the W6800 (and to my knowledge its consumer counter parts) have near if not complete support within ROCm. 

The underlying GPU die, Navi21, has different sub versions beyond the Main die in the W6800. 

The sub versions can be found here: [off site link](https://www.techpowerup.com/gpu-specs/amd-navi-21.g923)

NB: The sub versions are considered different dies, and must be enabled separately 

---

### 评论 #10 — Djip007 (2021-12-11T18:50:20Z)

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/173#issuecomment-991679054
I did some test on a 6900XT... can confirm (if neaded) rocm / tensorflow is enable (test with rocm/tensorflow-autobuilds container...)

---

### 评论 #11 — FCLC (2021-12-11T19:04:28Z)

> I did some test on a 6900XT... can confirm (if neaded) rocm / tensorflow is enable

That would be superb if possible!  Per #1631 support was problematic as of 2 weeks ago 

---

### 评论 #12 — FCLC (2022-01-10T01:16:28Z)

@ROCmSupport Any movement on this? Should we expect movement this quarter? 

---

### 评论 #13 — ROCmSupport (2022-01-25T10:38:38Z)

Hi @FCLC 
I am sure that some set of Navi series cards are already enabled and it will be officially supported in/from this quarter. Please stay tuned for our latest updates via our documentation and release notes. Thank you.

---

### 评论 #14 — FCLC (2022-02-10T18:28:33Z)

From the updated documentation in the [ROCm 5.0 guide](https://docs.amd.com/bundle/ROCm_Installation_Guide-v5.0/page/Prerequisite_Actions.html#d3848e335) it seems that there has't been much movement on expanding the support lineup. 

Seems that 5.0 added official support for Radeon Pro V620 and W6800 Workstation GPUs. 

---

### 评论 #15 — gobenji (2022-02-11T01:26:01Z)

> I did some test on a 6900XT... can confirm (if neaded) rocm / tensorflow is enable (test with rocm/tensorflow-autobuilds container...)

I tried with a 6700XT. OpenCL works but not tensorflow.

In rocm/tensorflow-autobuilds:
```
root@10befa294fc0:/workspace# python3
Python 3.9.10 (main, Jan 15 2022, 18:56:52) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> tf.__version__
'2.9.0'
>>> tf.reduce_sum(tf.random.normal([1000, 1000]))
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
```

However it is still based on rocm-4.5.2

---

### 评论 #16 — FCLC (2022-02-11T19:17:03Z)

> However it is still based on rocm-4.5.2

if you could try again with the new release that would be of some help! 

---

### 评论 #17 — gobenji (2022-02-11T23:13:39Z)

> if you could try again with the new release that would be of some help!

Same result with the newer image.
Looking into the image, I'm not sure but I guess this is the list of available "code objects" that tensorflow is looking for:
```
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx1010.hsaco         
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx1011.hsaco              
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx1012.hsaco              
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx1030.hsaco                
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx803.hsaco                 
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx900.hsaco                      
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx906-xnack-.hsaco         
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx908-xnack-.hsaco         
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx90a-xnack+.hsaco         
/opt/rocm-5.0.0/lib/library/Kernels.so-000-gfx90a-xnack-.hsaco
```
[chip names - product names](https://llvm.org/docs/AMDGPUUsage.html#processors)
So maybe it will work on 6800, 6800xt and 6900xt gpus (gfx1030).

---

### 评论 #18 — xuhuisheng (2022-02-11T23:44:52Z)

@gobenji RX6700XT may be gfx1031, you could check it by `/opt/rocm/bin/rocminfo`.

---

### 评论 #19 — FCLC (2022-02-12T00:44:22Z)

> @gobenji RX6700XT may be gfx1031, you could check it by `/opt/rocm/bin/rocminfo`.

The 6700xt is GFX1031, both cards that received full support in 5.0 are GFX1030 based unfortunately, so I doubt this will be functional. 

This means that as of ROCm 5.0:
All GFX1030 (W6800 V 620, rx 6900xt 6800(xt) etc.) are supported.  

GFX 1031 and all other RDNA 2 GPU's are not supported or have little/partial support. 


RDNA 1 has zero/no support 2 and a half years after launch. 



---

### 评论 #20 — jasondrusso (2022-02-12T05:09:08Z)

I tested ROCm 5.0 with a 6800xt, and I'm still seeing the 'hipErrorNoBinaryForGpu: Unable to find code object for all current devices' error. 

---

### 评论 #21 — FCLC (2022-02-12T14:32:02Z)

> I tested ROCm 5.0 with a 6800xt, and I'm still seeing the 'hipErrorNoBinaryForGpu: Unable to find code object for all current devices' error.

Had you fully purged ROCm 4.x? that could be a factor 

---

### 评论 #22 — jasondrusso (2022-02-12T22:02:09Z)

Yes, I'm pretty sure I removed everything from 4.x before I installed 5.0. I removed the old amd drivers to upgrade to 21.50 & also removed the 4.x repos.

---

### 评论 #23 — FCLC (2022-02-13T17:01:47Z)

> Yes, I'm pretty sure I removed everything from 4.x before I installed 5.0. I removed the old amd drivers to upgrade to 21.50 & also removed the 4.x repos.

Interesting, since it's fundamentally the same gpu it should be able to deal with the same compute kernels. I'd recommend opening a new issue and then referencing this issue. 

---

### 评论 #24 — jasondrusso (2022-02-13T19:27:34Z)

Ok thanks. But before I do, does it matter that I'm trying this with Tensorflow 1.15 and python 3.7? 

---

### 评论 #25 — FCLC (2022-02-13T22:30:56Z)

> Ok thanks. But before I do, does it matter that I'm trying this with Tensorflow 1.15 and python 3.7? 

You would have to double check the docs. Beyond that, I'm more on the HPC side than ai side. Others may be better equipped to answer that question.

---

### 评论 #26 — gobenji (2022-02-13T23:49:11Z)

> Ok thanks. But before I do, does it matter that I'm trying this with Tensorflow 1.15 and python 3.7?

How did you try those versions with rocm 5.0.0? The versions in the rocm/tensorflow-autobuilds image are python 3.9.10 and tensorflow 2.9.0.

What result do you get if you use the docker image directly?
```
docker run --rm --device=/dev/kfd --device=/dev/dri --security-opt seccomp=unconfined rocm/tensorflow-autobuilds python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

---

### 评论 #27 — jasondrusso (2022-02-14T16:27:24Z)

I outlined how I set up & tested rocm 5.0 with Tensorflow 1 here: https://github.com/RadeonOpenCompute/ROCm/issues/1676

I don't have docker, but when I run the test above with a Python 3.9 venv & Tensorflow 2.8.0 (latest version I can find in pip), I get the following error:

2022-02-14 11:14:10.639407: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:832] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-02-14 11:14:10.639462: E tensorflow/stream_executor/rocm/rocm_driver.cc:1196] failed to query max grid dim x: HIP_ERROR_InvalidValue
2022-02-14 11:14:10.639481: F tensorflow/core/platform/statusor.cc:33] Attempting to fetch value instead of handling error NOT_FOUND: could not retrieve ROCM device attribute (7): HIP_ERROR_InvalidValue

---

### 评论 #28 — FCLC (2022-02-15T19:12:40Z)

Tho this is far from official support, this repository may be of some use:

https://github.com/xuhuisheng/rocm-build

It purports to have found ways to add compilation targets for non-officially supported GPU's. I'd personally caution anyone considering using this to limit its use to development environments only and not production machines. 

I'm currently busy preparing for AVX512FP16 and AMX BF16/INT8 kernels so don't have time to test in the immediate.

If anyone can confirm if the above does or does not work, that would be superb. 

In the meantime hoping to see an update from the ROCm team soon :sweat_smile: 

---

### 评论 #29 — jasondrusso (2022-02-18T21:10:58Z)

Newest version of tensorflow-rocm 2.8.0 seems to work with the 6800xt.

---

### 评论 #30 — ROCmSupport (2022-02-21T07:58:59Z)

Hi All,
Thanks you.
As Radeon Pro W6800 enabled(Navi21 workstation card) from ROCm 5.0 onwards, I am closing this thread.
Hope this helps.
Please let me know if you need more information and request to file new tickets for quick resolutions.
Thank you.

---

### 评论 #31 — FCLC (2022-02-21T15:31:47Z)

> 

Hi, Since this thread was about all of Navi, including generation 1, I do not think the above fits the criteria for closing this issue. 

As of now only 1 GPU sub-group amongst both RDNA generations has received support, that being Navi 21 (and by extension it's consumer equivalents)

This leaves those running other RDNA workstation class cards such as the:
W6600 (Navi 23)
W6400 (Navi 24)
W5700 (Navi 10)
W5500 (Navi 14) 
Radeon Pro v520 (Navi 12)

and all of their mobile equivalents out to dry.

Outside of the above cores, Navi 22 does not have a workstation equivalent, but is worth taking note of. 




---

### 评论 #32 — jasondrusso (2022-02-23T22:58:48Z)

> > 
> 
> Hi, Since this thread was about all of Navi, including generation 1, I do not think the above fits the criteria for closing this issue.
> 
> As of now only 1 GPU sub-group amongst both RDNA generations has received support, that being Navi 21 (and by extension it's consumer equivalents)
> 
> This leaves those running other RDNA workstation class cards such as the: W6600 (Navi 23) W6400 (Navi 24) W5700 (Navi 10) W5500 (Navi 14) Radeon Pro v520 (Navi 12)
> 
> and all of their mobile equivalents out to dry.
> 
> Outside of the above cores, Navi 22 does not have a workstation equivalent, but is worth taking note of.

As 'Navi' is a pretty large category of products, with new ones being added, I wonder if it would be better to close this issue and open new issues for each specific Navi group. At the very least, it might make tracking support amongst the product lines easier.

---

### 评论 #33 — FCLC (2022-02-24T01:28:11Z)

@ROCmSupport in reference to https://github.com/RadeonOpenCompute/ROCm/issues/1617#issuecomment-1047000685

And 
https://github.com/RadeonOpenCompute/ROCm/issues/1617#issuecomment-1049297130

Would it be better to open a new issue for each of the sub groups of cards still missing support or reopen this issue? 

I'm happy to see that some progress was made by introducing support for Navi 21, but want to make sure that other cards aren't left to fall to the wayside. 

---

### 评论 #34 — felixniemeyer (2022-07-27T16:33:51Z)

I sold my 5700 some time ago because ROCm support would just never come...
It's sad, but I realize, there are just too few people who want to do 
- compute stuff (machine learning, video editing, maybe mining for fun) 
- on a AMD GPU instead of getting a NVIDIA card (modern and < 900USD) 
- on Linux

It seems to me, that I have to give up one of these three things else I'd wait forever... :-(

---

### 评论 #35 — FCLC (2022-07-27T16:39:20Z)

> I sold my 5700 some time ago because ROCm support would just never come...
> 
> It's sad, but I realize, there are just too few people who want to do 
> 
> - compute stuff (machine learning, video editing, maybe mining for fun) 
> 
> - on a AMD GPU instead of getting a NVIDIA card (modern and < 900USD) 
> 
> - on Linux
> 
> 
> 
> It seems to me, that I have to give up one of these three things else I'd wait forever... :-(

Actually, after having spent ~a dozen hours building the entire stack, it's seems like gfx1010/Navi10 cards are usable, even if the work needed to do so it somewhat ridiculous 

---

### 评论 #36 — maxap (2022-12-15T21:32:40Z)

> 

what did you do to make it work? I'm in need for this

---

### 评论 #37 — jasondrusso (2023-01-09T02:55:03Z)

Rocm 5.4.1 should work pretty good with navi now. I have a 6800xt and using the amdgpu-install script installed easily when run with rocm usecase. However, to use with tensorflow, there are some extra packages you might have to install (I think I have to add rocm-smi, hipfft, miopen and one or two others) to get that to work with rocm (not to mention pip install tensorflow-rocm).

---
