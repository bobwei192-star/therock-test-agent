# Is dkms for kernel 6.1^ in the roadmap

> **Issue #2013**
> **状态**: closed
> **创建时间**: 2023-04-03T06:15:11Z
> **更新时间**: 2023-10-23T01:18:30Z
> **关闭时间**: 2023-10-23T01:18:30Z
> **作者**: alfonsocv12
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2013

## 描述

I'm not sure if this is an official AMD project. My question is simple is there a 6.1^ dkms version in the roadmap, if it is can I help with something I'm not an expert on GPUs but I want to have a server running and I use vanilla Debian so this could come in handy for me

---

## 评论 (6 条)

### 评论 #1 — xuhuisheng (2023-04-03T06:26:26Z)

1. Yes, here is the official AMD project.
2. Actually the dkms sources always commit to the linux kernel with amdgpu driver. So we can use upstream dkms from linux kernel. The difference is linux release version may stay an old version of kernel, so related dkms is an old version, so amdgpu driver cannot support new AMD gpu card.

But 6.1 is a quite new version, so I guess the built-in version of amdgpu and dkms from 6.1 may support at least RDNA2, likes RX6800.

From kernelnewbie, it said kernel-6.1 even support gfx11.0.3. <https://kernelnewbies.org/Linux_6.1#Graphics>

---

### 评论 #2 — alfonsocv12 (2023-04-03T06:31:35Z)

So I can just install dkms from my mirror and run

`sudo amdgpu-install --usecase=hiplibsdk,rocm --no-dkms`

And I should be able to use my GPU with pytorch?

---

### 评论 #3 — xuhuisheng (2023-04-03T07:11:24Z)

@alfonsocv12 
The installation script is OK.

And before test pytorch, I suggest you test your gpu with `/opt/rocm/bin/rocminfo` to see which isa version of your card, likes gfx1030. And make sure pytorch-rocm can support this card.

Good luck.

---

### 评论 #4 — alfonsocv12 (2023-04-03T07:20:59Z)

I have done this, `$ rocminfo` outputs 

```batch
ISA INFO:
    ISA 1
        Name:                 amdgcn-amd-amdhsa-gfx1030
```

---

### 评论 #5 — xuhuisheng (2023-04-03T07:22:42Z)

gfx1030 should fine.

---

### 评论 #6 — alfonsocv12 (2023-04-03T07:30:41Z)

Thanks a lot @xuhuisheng its working now 🥳

```
>>>import torch
>>>torch.cuda.is_available()
True
```

I'm going to make a medium post on the topic for people trying to get a similar setup

---
