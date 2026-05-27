# source code of rocm-core 

> **Issue #1705**
> **状态**: closed
> **创建时间**: 2022-03-17T12:09:50Z
> **更新时间**: 2024-05-23T17:23:10Z
> **关闭时间**: 2024-05-23T17:23:10Z
> **作者**: xlindo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1705

## 描述

Hello, 

I would like to compile ROCm totally from source code on RISC-V, but I can not find all the source codes, e.g. **rocm-core**. I just found https://repo.radeon.com/rocm/apt/4.5.2/pool/main/r/rocm-core/ for amd64 as `.deb`, apparently it can not work.

Can anyone help me?

It will also be great if anyone can give me the relative works on ROCm for RISC-V.

Thanks.

---

## 评论 (11 条)

### 评论 #1 — xuhuisheng (2022-03-18T00:53:11Z)

There is only a rocm-version.h in the rocm-core.
<https://github.com/xuhuisheng/rocm-build/blob/master/meta/rocm-core_5.0.0.50000-49_amd64/include/rocm/rocm_version.h>

---

### 评论 #2 — xlindo (2022-03-18T03:25:05Z)

> There is only a rocm-version.h in the rocm-core. https://github.com/xuhuisheng/rocm-build/blob/master/meta/rocm-core_5.0.0.50000-49_amd64/include/rocm/rocm_version.h

Thanks for your reply.

Your repo is de facto guide to me. 

Have you ever thought of a compilation for ROCm on an unsupported GPU architecture? Or can you give me some tips for the **key source code components** related to heterogeneous architecture?



---

### 评论 #3 — xuhuisheng (2022-03-18T03:30:17Z)

@xlindo 
Yes, I use my building scripts to support my RX580 - aka. gfx803 with latest ROCm-5.0.2.
<https://github.com/xuhuisheng/rocm-gfx803>

The mininium components should be ends with MIOpen, they are required by tensorflow and pytorch.

---

### 评论 #4 — xlindo (2022-03-18T05:04:03Z)

> @xlindo Yes, I use my building scripts to support my RX580 - aka. gfx803 with latest ROCm-5.0.2. https://github.com/xuhuisheng/rocm-gfx803
> 
> The mininium components should be ends with MIOpen, they are required by tensorflow and pytorch.

So it means once I compiled MIOpen successfully on my platform, the upper framework will work well?

How about ROCm runtime, which components are necessary and hardware dependent?

Thanks a lot, but the components and steps are so many for compilation.🤣

---

### 评论 #5 — xuhuisheng (2022-03-18T05:53:43Z)

@xlindo 
Yes, you need 00.rocm-core to 35.miopen, all of them need for tensorflow or pytorch to build and run.

There are three steps:

* when you properly build HIP, you can run some hip samples, like square, that make you using GPU to run some real samples.
* when you properly build miopen, you can use miopen to run some plan, something like cnn
* when you properly build tensorflow/pytorch, you can use python.

Bascly this is my path.

---

### 评论 #6 — xlindo (2022-03-18T06:10:52Z)

> @xlindo Yes, you need 00.rocm-core to 35.miopen, all of them need for tensorflow or pytorch to build and run.
> 
> There are three steps:
> 
> * when you properly build HIP, you can run some hip samples, like square, that make you using GPU to run some real samples.
> * when you properly build miopen, you can use miopen to run some plan, something like cnn
> * when you properly build tensorflow/pytorch, you can use python.
> 
> Bascly this is my path.

Great! Thanks a lot.

I will try it now.

---

### 评论 #7 — ROCmSupport (2022-03-29T08:46:20Z)

Hi @xlindo 
We are working on providing source content to be available to public, will keep posted via our documentation once its available.
Hope you got the suggestions/inputs meanwhile from our community friend @xuhuisheng, who is really helpful.
Please let know if you need anything more, request to close this ticket if you do not need anything more.
Thank you.

---

### 评论 #8 — xlindo (2022-04-02T15:04:51Z)

@ROCmSupport 

Please close it, thx

---

### 评论 #9 — ROCmSupport (2022-04-18T05:19:55Z)

Thanks @xlindo 
I am closing this

---

### 评论 #10 — tpkessler (2023-01-30T19:17:31Z)

Hi, Arch Linux package maintainer here! Any progress on the source code for rocm-core @ROCmSupport? It's required to build pytorch with ROCm backend.

---

### 评论 #11 — ppanchad-amd (2024-05-08T14:23:50Z)

@tpkessler Apologies for the lack of response.  Do you still need assistance? Thanks!

---
