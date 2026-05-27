# ROCm not uninstalling and messing up pytorch-cpu RX6600XT

> **Issue #1727**
> **状态**: closed
> **创建时间**: 2022-04-18T22:01:59Z
> **更新时间**: 2024-04-05T23:41:11Z
> **关闭时间**: 2024-04-05T23:41:11Z
> **作者**: march-o
> **标签**: application:pytorch
> **URL**: https://github.com/ROCm/ROCm/issues/1727

## 标签

- **application:pytorch** (颜色: #bfdadc)

## 描述

So I recently installed ROCm and anaconda and pytorch on new linux dualboot. But after finding out that my gpu is not compatible, I uninstalled ROCm and that version of pytorch and even reinstalled anaconda. But after installing pytorch-cpu and running in python it shows:
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"

I dont know what to do, I have gone through the uninstall proceedure 3 times and it still isnt working. 

My gpu: RX6600XT(I understand that it is not supported but I thought I'll try to install since other similar gpus worked.)
ROCm version: 5.0.0
Rocm pytorch version: pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm4.5.2

After running sudo amdgpu-uninstall : 
sudo: amdgpu-uninstall: command not found

After running sudo apt autoremove amdgpu-dkms or sudo apt autoremove rocm-core: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package amdgpu-dkms

At location /etc/apt/sources.list.d is no amd or rocm repository.

At this point I am considering just reinstalling linux.

I am new to linux and this stuff so sorry in advance if I accidantly messed up something simple.
Thanks.


---

## 评论 (9 条)

### 评论 #1 — ffleader1 (2022-04-30T04:17:27Z)

It seems that you tried to install Pytorch on Global Environment. This is 99% NOT recommended. In Python, always use virtual environment.

---

### 评论 #2 — march-o (2022-05-01T12:29:49Z)

@ffleader1. I didn't, I used anaconda. My first troubleshooting steps were to reinstall anaconda. I kind of solved the issue by installing PyTorch on an environment with a different python. But python 3.8 now is dead on that pc so that's sad. But thanks for the concern!

---

### 评论 #3 — ffleader1 (2022-05-01T12:43:07Z)

> @ffleader1. I didn't, I used anaconda. My first troubleshooting steps were to reinstall anaconda. I kind of solved the issue by installing PyTorch on an environment with a different python. But python 3.8 now is dead on that pc so that's sad. But thanks for the concern!

I think I was being more or less rude and all, so sorry about that. Anyway, are you a windows guy (as you said you were not familiar with Linux and all). I think while it may sound ridiculous, installing Rocm on Windows has more potential than on Linux.

---

### 评论 #4 — march-o (2022-05-01T21:40:12Z)

> > @ffleader1. I didn't, I used anaconda. My first troubleshooting steps were to reinstall anaconda. I kind of solved the issue by installing PyTorch on an environment with a different python. But python 3.8 now is dead on that pc so that's sad. But thanks for the concern!
> 
> I think I was being more or less rude and all, so sorry about that. Anyway, are you a windows guy (as you said you were not familiar with Linux and all). I think while it may sound ridiculous, installing Rocm on Windows has more potential than on Linux.

That does sound ridiculous, but I might try it someday. I'm moving most of my coding stuff on Linux and I like it better there for that stuff(obviously). Also, I have a great setup at my new job with Nvidia, but I just really wanted to be able to make small personal projects at home, but I can't do that without a gpu(apart from colab). I guess 6600XT just didn't make the cut :(, at least just for now I hope

---

### 评论 #5 — ffleader1 (2022-05-02T01:23:55Z)

> 

While I did not try (I own no Navi card), it seems that you can have a non-Navi 23 card supported by recompiling rocm, but replacing the device string. So for example, the 6800 is Navi 21, gfx1031, but the 6600XT is Navi 23, gfx1033. 

So what one out to be doing is string replace gfx1031 to gfx1033 and recompile Rocm. I have a Vega 56 only so I can't really test it. It just that I have been looking up this topic and, yeah, people have tried and it worked, supposedly.

Also, microsoft does have this Antares thing.
https://github.com/microsoft/antares
Quite honestly it is ridiculously easy to install and works with everything. Basically 1-liner on WSL:

`pip3 install --upgrade antares
BACKEND=c-rocm_win64 antares`

Again, supposedly, this should be enough, and in the future, and Antares would probably not even require Wsl.

All in all, I really want to see AMD thrive in ML space and they are doing not really great, and Microsoft had to carry them for some reason.

---

### 评论 #6 — Kayzwer (2023-04-10T04:07:42Z)

cp /usr/share/libdrm/amdgpu.ids /opt/amdgpu/share/libdrm/

---

### 评论 #7 — hongxiayang (2023-12-05T20:53:41Z)

Looks like your gpu type is not in the official supported list:
https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html

Can you run
```
rocminfo | grep gfx
```

---

### 评论 #8 — abhimeda (2024-01-25T03:35:50Z)

@march-o  Hi, was the above answer helpful? If so, can we close this ticket?

---

### 评论 #9 — nartmada (2024-04-05T23:41:11Z)

Closing the ticket.  @march-o, please reopen if you still need guidance on your issue.  Thank you.

---
