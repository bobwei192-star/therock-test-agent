# Support Ubuntu 20.10 (Groovy Gorilla)

> **Issue #1263**
> **状态**: closed
> **创建时间**: 2020-10-21T13:49:57Z
> **更新时间**: 2021-04-25T16:56:59Z
> **关闭时间**: 2020-11-03T12:17:21Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1263

## 描述

ROCm has supported Ubuntu 20.04 since release 3.8 (See: <https://github.com/RadeonOpenCompute/ROCm/issues/1074>). ROCm surely aims to extend support to the most relevant versions operating system versions. Hence, the next regular Ubuntu release is the next logical step towards this goal. Ubuntu 20.10 is due to be released tomorrow (See: [Release Notes](https://discourse.ubuntu.com/t/groovy-gorilla-release-notes/15533)). Now is a good time to start the effort to add it to the supported operating system versions. 

---

## 评论 (13 条)

### 评论 #1 — Bengt (2020-10-21T13:53:27Z)

Here is a user falsely expecting that there is support for Ubuntu 20.10: https://github.com/RadeonOpenCompute/ROCm/issues/1188#issuecomment-699754544

---

### 评论 #2 — xuhuisheng (2020-10-21T13:55:01Z)

I tested rocm-3.8 on ubuntu-20.10 with upstream kernel 5.8 /dev/kfd, worked fine.

---

### 评论 #3 — Bengt (2020-10-21T13:56:22Z)

Thanks for that information, @xuhuisheng. So supporting Ubuntu 20.10 should not be too much effort.

---

### 评论 #4 — xuhuisheng (2020-10-22T08:06:25Z)

> Here is a user falsely expecting that there is support for Ubuntu 20.10: [#1188 (comment)](https://github.com/RadeonOpenCompute/ROCm/issues/1188#issuecomment-699754544)

@Bengt I have to clarify myself, that I know the ubuntu-20.10 is not supported by ROCm officially. Just want to try ROCm on kernel-5.8, seems it could work properly.  I can run small examples like mnist on tensorflow-rocm / pytorch.

AMD said that the upstream kernel driver after kernel-5.6 could use 15/16 system memory, so it is good news to use ROCm on ubuntu-20.10 with kernel-5.8 built in kernel driver. Then we neednot install rocm-dkms manually.
https://github.com/RadeonOpenCompute/ROCm#rocm-support-in-upstream-linux-kernels

And sources could be compiled successly only with small modifies, because of the gcc10.  Ubuntu-20.04.2 maybe released early next year. So I think it wont be a big problem for future upgrades.





---

### 评论 #5 — Ruedii (2020-10-22T11:41:09Z)

There was a single change to the instructions needed regarding the addition of a "render" group in Ubuntu 20.10 

It would be ideal to list the Ubuntu versions separately in the distro listing.  Even if the packages are the same, this would provide quick ways to create patched packages for patches.  This would also open the doorway for sharing package trees for Ubuntu, Debian and other Debian Derivatives. 

---

### 评论 #6 — YifeiLu-1 (2020-10-23T12:54:00Z)

Ubuntu 20.04 was offcially supported on ROCm 3.7 in Sepetember, 5 months after the Ubuntu 20.04 release. So considering none LTS Ubuntus only have 9 months support, it will be very resource consuming for AMD to do so.

---

### 评论 #7 — Bengt (2020-10-25T19:49:23Z)

@YifeiLuDublin Thanks for raising the point, that it can be laborious to support many operating system versions. As it turns out, there is but very little effort necessary to support Ubuntu 20.10 since 20.04 is supported already and the differences are only minor. On the flip side, supporting regular Ubuntu releases like 20.10 might actually save some effort, because it makes the step towards supporting LTS releases smaller. Supporting LTS versions has been an issue in the past. For example, supporting Ubuntu 20.04 LTS was delayed by 4 months. See https://github.com/RadeonOpenCompute/ROCm/issues/1074#issuecomment-716169937

---

### 评论 #8 — rkothako (2020-11-02T06:23:41Z)

Hi @YifeiLuDublin, @xuhuisheng , @Bengt , @Ruedii 
ROCm officially supports LTS versions of Ubuntu only.
All other versions(other than LTS) might work with ROCm but there will not be any official support.
Hope this clarifies.

---

### 评论 #9 — xuhuisheng (2020-11-02T08:18:23Z)

@rkothako I understand that the offcial supporting will cost much.
Will we provide a unoffical supporting page, like this version is not supported offically, but it may run successfully on yourself risk. In other word, could AMD allow community driven version. Just like, there is no supporting on ROCm-3.9.0 with gfx803. Could I provide community version for gfx803?

---

### 评论 #10 — baryluk (2020-11-02T08:37:42Z)

@xuhuisheng It is up to you. You can compile rocm from sources, or use packages for 20.04 for example. It doesn't take much to make them work. If you want to provide something like unofficial PPA for Ubuntu 20.04 you can.

---

### 评论 #11 — Bengt (2020-11-02T14:24:59Z)

@rkothako You sound like you are associated with AMD. Are you speaking on their behalf?

@xuhuisheng Please stay on topic. GFX803 was discussed before: https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479

@baryluk Yes, I can confirm that using 20.04 packages works. I have recently upgraded my workstation to Ubuntu 20.10 and can run Tensorflow-ROCm on the included 5.8 Kernel without any issues so far. I followed to the official installation instructions aside from skipping rocm-dkms.

---

### 评论 #12 — rkothako (2020-11-03T07:41:53Z)

Hi @Bengt, Yes, I am sharing the information from AMD side.

---

### 评论 #13 — Bengt (2020-11-03T12:17:21Z)

@rkothako Alright then, you denying support for Ubuntu 20.10 (on AMD's behalf) settles the issue I was having with ROCm. I am sorry to hear that there will be no support, since there is obviously demand for it and supporting 20.10 should take very little effort from AMD's side. Anyways, thanks for the clarification. I think we can close this issue and quote your statement here, if and when the request arises again.

Personally, I will continue using ROCm under the regular releases of Ubuntu. I will however have a hard time recommending using ROCm in the future. Using an unsupported operating system version is nothing I can recommend friends and colleagues and since I will no longer use the supported long term release of Ubuntu, I will no longer be able to vouch ROCm it working fine. I am very sorry about that, because I think ROCm is awesome and would like to spread its use whenever I get the chance.

---
