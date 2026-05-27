# Ryzen 4000 series APU support pt2

> **Issue #1732**
> **状态**: closed
> **创建时间**: 2022-04-27T18:54:22Z
> **更新时间**: 2024-10-09T14:51:35Z
> **关闭时间**: 2024-10-09T14:51:35Z
> **作者**: Etaash-mathamsetty
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1732

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

recently I noticed that opencl-amd (from the AUR) version 22.10 works remarkably well, but my vram is 
`  Global memory size                              536870912 (512MiB)`
I want more, 512 MB is not a lot, so I was wondering if rocm could support using the gtt memory space as "vram"

---

## 评论 (15 条)

### 评论 #1 — lanwatch (2023-07-06T09:23:45Z)

Related to https://github.com/RadeonOpenCompute/ROCm/issues/2014

---

### 评论 #2 — Etaash-mathamsetty (2023-07-06T11:31:50Z)

> Related to #2014

that's not just related, that's an identical issue (probably even a duplicate)
I doubt AMD are ever going to support these processors since they didn't give a shit and closed my issue in 2021 as well

welcome to ROCm, my friend

---

### 评论 #3 — winstonma (2023-07-23T13:01:16Z)

@Etaash-mathamsetty [UniversalAMDFormBrowser](https://github.com/DavidS95/Smokeless_UMAF) and followed [this video](https://youtu.be/0jwrWCF5fhc) to config the BIOS to get more GPU dedicated memory. 

---

### 评论 #4 — Etaash-mathamsetty (2023-07-23T16:26:38Z)

> @Etaash-mathamsetty [UniversalAMDFormBrowser](https://github.com/DavidS95/Smokeless_UMAF) and followed [this video](https://youtu.be/0jwrWCF5fhc) to config the BIOS to get more dedicated memory.

it's too late now, I have a PC with an RX 6800, and ROCm still sucks and doesn't work properly, it is what it is
I will definitely use that to overclock my laptop though

---

### 评论 #5 — winstonma (2023-07-24T03:36:21Z)

I wrote a [guide](https://github.com/RadeonOpenCompute/ROCm/issues/2227#issuecomment-1639262658) on how to check Pytorch is using GPU. See if that helps.

The most important thing is, as long as you get the `True` result from the following command line then you would be good to go.

```bash
# To check Pytorch is using GPU
$HSA_OVERRIDE_GFX_VERSION=10.3.0 python -c 'import torch; print(torch.cuda.is_available())'
True
```

---

### 评论 #6 — abhimeda (2024-01-26T05:21:27Z)

@Etaash-mathamsetty Hi, is your issue resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #7 — Etaash-mathamsetty (2024-01-26T05:42:38Z)

> @Etaash-mathamsetty Hi, is your issue resolved on the latest ROCm? If so can we close this ticket?

If the other issue is anything to go with then no, but I'm not testing this since I don't use an integrated GPU anymore and frankly can't bother when rusticl exists.

---

### 评论 #8 — winstonma (2024-01-26T05:52:52Z)

@Etaash-mathamsetty based on the kernel message GTT is available in driver level (e.g. some developer can modify PyTorch to use GTT memory). I guess it prove that GTT memory is working. However the problem now is the support of the applications.

You can hack your BIOS to get more video memory (not GTT) so application would work. At the same time you need to wait for the application developer to add GTT support.

---

### 评论 #9 — Etaash-mathamsetty (2024-01-26T06:02:00Z)

> @Etaash-mathamsetty based on the kernel message GTT is available in driver level (e.g. some developer can modify PyTorch to use GTT memory). I guess it prove that GTT memory is working. However the problem now is the support of the applications.
> 
> You can hack your BIOS to get more video memory (not GTT) so application would work. At the same time you need to wait for the application developer to add GTT support.

I think it's poor driver design if the app developer has to include it, i specifically only use rocm for opencl and I'm 90% sure opencl doesn't allow apps to decide which memory heap to put data on. Mesa Vulkan and opengl and opencl drivers report increased vram for example 

---

### 评论 #10 — winstonma (2024-01-26T06:08:20Z)

> > @Etaash-mathamsetty based on the kernel message GTT is available in driver level (e.g. some developer can modify PyTorch to use GTT memory). I guess it prove that GTT memory is working. However the problem now is the support of the applications.
> > 
> > You can hack your BIOS to get more video memory (not GTT) so application would work. At the same time you need to wait for the application developer to add GTT support.
> 
> I think it's poor driver design if the app developer has to include it, i specifically only use rocm for opencl and I'm 90% sure opencl doesn't allow apps to decide which memory heap to put data on. Mesa Vulkan and opengl and opencl drivers report increased vram for example 

I am not sure who is responsible but I asked this question to the PyTorch ROCm team. They said they need to add GTT support. Although I personally think if GTT memory allocation should be done on driver level then application no need to modify (it just work as long as it support ROCm). But currently this is not the case.

---

### 评论 #11 — Etaash-mathamsetty (2024-01-26T06:10:15Z)

> > > @Etaash-mathamsetty based on the kernel message GTT is available in driver level (e.g. some developer can modify PyTorch to use GTT memory). I guess it prove that GTT memory is working. However the problem now is the support of the applications.
> > > 
> > > You can hack your BIOS to get more video memory (not GTT) so application would work. At the same time you need to wait for the application developer to add GTT support.
> > 
> > I think it's poor driver design if the app developer has to include it, i specifically only use rocm for opencl and I'm 90% sure opencl doesn't allow apps to decide which memory heap to put data on. Mesa Vulkan and opengl and opencl drivers report increased vram for example 
> 
> I am not sure who is responsible but I asked this question to the PyTorch ROCm team. They said they need to add GTT support. Although I personally think if GTT allocation is done on driver level then application no need to modify. But currently this is not the case.

Whole point of this issue is to make that the case, because that's how it is on windows unless AMD decided to release drivers that are litterally worse than their original ones with the swap to rocm

---

### 评论 #12 — winstonma (2024-01-26T10:55:49Z)

Well... I am not sure but 

1. Windows doesn't have the PyTorch that can use ROCm. So ROCm on Windows is sort of broken
2. Windows game can assign the GTT memory
 
Here is my console output from Ubuntu, running ROCm 6.0 driver on my Ryzen 6800U
```
$ sudo dmesg | grep amdgpu
...
[    3.627547] amdgpu 0000:03:00.0: amdgpu: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[    3.627692] [drm] amdgpu: 512M of VRAM memory ready
[    3.627694] [drm] amdgpu: 7614M of GTT memory ready.
[    3.628651] amdgpu 0000:03:00.0: amdgpu: Will use PSP to load VCN firmware
...
```

So I believe GTT can be used. But the dynamic allocation part doesn't happen on Linux application. I am not sure if that fulfill your definition of _support_ but I just try to explain things. If you want more detailed explanation / explanation why the driver doesn't designed as you expected, please ask @abhimeda 

---

### 评论 #13 — Ristovski (2024-01-26T11:21:16Z)

@Etaash-mathamsetty I suggest you read issue https://github.com/ROCm/ROCm/issues/2014 and the comments.

---

### 评论 #14 — Etaash-mathamsetty (2024-01-26T13:49:04Z)

> @Etaash-mathamsetty I suggest you read issue https://github.com/ROCm/ROCm/issues/2014 and the comments.

I already have 

---

### 评论 #15 — winstonma (2024-01-28T23:20:58Z)

> @Etaash-mathamsetty I suggest you read issue #2014 and the comments.

@Ristovski I am not sure which part talk about APU support. I think it is okay if AMD Driver Team said GTT is supported, and upper level application need to modified to get end-to-end support. But it was never specifically mentioned.

Also I think @Etaash-mathamsetty concern is the understanding that the driver should do the GTT allocation (e.g. I don't need a AMD-Supported Windows DirectX to use GTT memory on my system, it's driver who allocate the memory itself). Hope I understand your concern correctly.

---
