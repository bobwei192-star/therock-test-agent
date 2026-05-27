# Training causes GPU hang after a few seconds with ROCm 2.0

> **Issue #665**
> **状态**: closed
> **创建时间**: 2019-01-08T00:19:50Z
> **更新时间**: 2019-01-08T02:41:14Z
> **关闭时间**: 2019-01-08T02:41:14Z
> **作者**: liamnr
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/665

## 描述

When trying to train a GAN using the following Tensorflow implementation of SAGAN:
https://github.com/taki0112/Self-Attention-GAN-Tensorflow

the system locks up every time after the script has run for a few seconds.
I'm using Linux Mint 19, 4.15 kernel and a RX 470 card.

Command line used for the script:
python3 main.py --phase train --dataset celebA --gan_type hinge --batch_size=1 --img_size=128



[stderr.txt](https://github.com/RadeonOpenCompute/ROCm/files/2734745/stderr.txt)
[kernel.log](https://github.com/RadeonOpenCompute/ROCm/files/2734754/kernel.log)


---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2019-01-08T00:27:11Z)

Hi @liamnr 

I recommend posting this issue to the [tensorflow-upstream project](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues). You're much more likely to get an accurate answer there, as those developers may rarely check this repo's issues.

---

### 评论 #2 — liamnr (2019-01-08T01:26:21Z)

Thank you, I've reposted the issue on tensorflow-upstream.
Though even if it is caused by a problem with tensorflow, it seems wrong to me that it would cause the entire system (or at least the X server) to hang. Isn't it a kernel driver issue as well?

---

### 评论 #3 — jlgreathouse (2019-01-08T02:41:14Z)

It could be an issue sensitized in many layers of our software, firmware, and hardware stack. You're working at basically the highest level, but the path of the error could lead through any of:

 - Your GAN network
 - AMD-enabled Tensorflow
 - MIOpen
 - The HIP runtime
 - The HCC runtime
 - The OpenCL compiler
 - The ROCr runtime
 - The Thunk runtime/driver interface
 - The amdkfd compute driver
 - The amdgpu GPU kernel driver
 - Various pieces of firmware on the multiple microcontrollers on our GPU
 - All the way down to hardware GPU itself
 - and potentially into some other parts of the graphics stack that is not directly related to ROCm.

I would prefer that we start at the top to try to understand the problem. Hopefully we can narrow the problem down and, if required, pass a reduced set of test cases down the stack. Broadcasting a problem to every one of these projects will cause needless noise. Inundating developers with problems that haven't been narrowed down to that project would make it harder to allocate the right people for the right amount of time so that they can fix errors (instead of just putting reports through triage).

Since you have an issue open on that repo, I'm going to close this one for now. Hopefully we can trace your problem from the top of the stack down to a solution for you. :)

---
