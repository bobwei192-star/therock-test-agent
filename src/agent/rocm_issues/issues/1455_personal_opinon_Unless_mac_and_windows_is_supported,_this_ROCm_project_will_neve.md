# personal opinon: Unless mac and windows is supported, this ROCm project will never be as popular as CUDA

> **Issue #1455**
> **状态**: closed
> **创建时间**: 2021-04-15T03:59:58Z
> **更新时间**: 2021-06-10T06:54:18Z
> **关闭时间**: 2021-04-19T07:01:48Z
> **作者**: duwangthefirst
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1455

## 描述

personal opinon: Unless mac and windows is supported, this ROCm project will never be as popular as CUDA.

If One is willing to build a ubuntu server, nvidia gpu is obviously a better choice for CUDA comes with a lot of learning resource.

However latest MacOS  device only provide AMD gpus, so why doesn't ROCm support MacOS ? More developer will be attracted once this feature comes true.

---

## 评论 (6 条)

### 评论 #1 — Degerz (2021-04-16T06:14:48Z)

> However latest MacOS device only provide AMD gpus, so why doesn't ROCm support MacOS ?

AMD GPUs won't be included or supported anymore on future Mac systems ... 

---

### 评论 #2 — AGenchev (2021-04-16T23:19:50Z)

@duwangthefirst most of us use **Linux**, but yes, users want painless experience, which still does not happen. MACs are going to use ARM CPU. Nvidia has a CUDA version working on every card and APU (Jetsons) they make, ROCm works only on few selected cards even the newest (6800) are not supported... Actually the DNN users don't use ROCm or Hip directly; they care if PyTorch, TensorFlow, MXNet can run accelerated or not whehter with ROcm, OpenCL, OpenGL, Vulkan backend.
The excuse for Vega 10 APUs is that MB manufacturers messed with BIOS and did not properly adjust certain tables, but if AMD gave them reference MB BIOS, they wouldn't mess, so this is vague... AMD could make **x86** Jetson equivalents but they didn't see the niche where Nvidia sells their previous-gen (12nm) stuff claiming this way to enable us to make self-driving cars.

---

### 评论 #3 — ROCmSupport (2021-04-19T07:01:48Z)

Hi @duwangthefirst 
Thanks for reaching out.
We do not have plans to support mac and windows as of now.
We will share via our docs, once we have plans in future.
Thank you.

---

### 评论 #4 — AGenchev (2021-04-21T09:52:01Z)

@duwangthefirst: There is a new development on Microsoft side if you want to go this route - they are enabling TensorFlow over DirectX acceleration for any GPU - be it AMD, Intel, Nv. For me DX is a bad route - they should implement it over Vulkan or OpenCL to be portable to Linux, but they're playing their ****!# game.

---

### 评论 #5 — gwc4github (2021-06-02T16:30:57Z)

> Hi @duwangthefirst
> Thanks for reaching out.
> We do not have plans to support mac and windows as of now.
> We will share via our docs, once we have plans in future.
> Thank you.

@AGenchev, @duwangthefirst  I was surprised to here this after reading this article by Niles Burbank – Director PM at AMD, Mayank Daga – Director, Deep Learning Software at AMD
https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/

It lists Mac OS (at least in the image) as supported.  Have plans changed?



---

### 评论 #6 — ROCmSupport (2021-06-03T04:52:51Z)

Hi @gwc4github 
ROCm + Linux is the highlighted combination in the link you shared.

If you change Linux to Mac in the OS section, ROCm will be disabled, so its confirmed that ROCm+MacOS is not a supported combination right now.
You can check this image too.
![image](https://user-images.githubusercontent.com/74597123/120588892-9c641100-c455-11eb-84d4-fe4ed2473d91.png)


---
