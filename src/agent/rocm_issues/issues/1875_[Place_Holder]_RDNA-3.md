# [Place Holder] RDNA-3

> **Issue #1875**
> **状态**: closed
> **创建时间**: 2022-12-12T14:50:35Z
> **更新时间**: 2024-04-24T00:49:42Z
> **关闭时间**: 2024-04-21T15:54:53Z
> **作者**: FCLC
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1875

## 描述

We all know why this issue is here. 

We all know what questions are going to be asked. (Timelines, product categories, which libraries, and will it be self build or do we get binaries?)

If it can be kept open until such a time as all of RDNA 3 is supported across Pro and consumer, that would be swell. 

Thanks, 

FelixCLC

Respectfully, a dis-heartened dev that got burned by RDNA1 and has since ported his HIP and CUDA code to SYCL

---

## 评论 (13 条)

### 评论 #1 — aoolmay (2022-12-13T15:46:05Z)

Urgently need ETA on RDNA3 inclusion too!

RDNA2 PRO cards came about 6 months after gaming cards and you had to wait another 6 months for driver and software stack update.

Not waiting this time.

---

### 评论 #2 — stylerw (2023-02-01T06:28:37Z)

I'll echo this.  I picked up a 7900XTX precisely for RocM style GPU computing with larger memory than the 6950XT, and it's a bit frustrating to find no meaningful RocM support for these cards, even well after release.

I want to support AMD, particularly as a Linux user, but this isn't a great user experience.  Here's hoping for support (both in Torch, Tensorflow, and generalized RocM) sooner rather than later.

---

### 评论 #3 — Mushoz (2023-02-01T12:03:30Z)

@stylerw Not sure if you noticed these, but there is a bigger discussion ongoing about 7900 XTX support here: https://github.com/RadeonOpenCompute/ROCm/issues/1880

There is even a Dockerfile posted that allows you to run Pytorch (Although not as performant as expected and with some bugs) on the 7900 XTX. Furthermore, @saadrahim confirmed in that topic to wait for 5.5.0 for official support.

Lastly, @saadrahim also mentioned that he is asking around to see if they can make a forward-looking statement with regards to a rough timeline for when we can expect this support to land here: https://github.com/RadeonOpenCompute/ROCm/discussions/1836#discussioncomment-4586574

Unfortunately, he hasn't given us a rough timeline yet, but hopefully he can give us more information soon. Anyway, just wanted to share these two topics since you might find those interesting :)

---

### 评论 #4 — aoolmay (2023-02-01T12:20:24Z)

@Mushoz Two things.
Unofficial but somewhat complete implementation from AMD is what most people expect, especially in any kind of production environment.

Last time i waited for AMD to include support, it cost me over 9 months of running RDNA2 cards on a forsaken OpenCL backend and multiple years outdated ML APIs. Rumors and promises of early RDNA3 support ring the same as it did for RDNA2.

Expecting "forward-looking statement", LOL, earliest we get support is when RDNA3 PRO cards drop, same playbook as it happened with RDNA2.

Unfortunately i already jumped ship, time saved on that decision already payed off the price difference in any metric you want to count by.

---

### 评论 #5 — Mushoz (2023-02-01T12:29:41Z)

@aoolmay I understand the sentiment, and I share your frustrations. But I just wanted to help out a fellow user by sharing what little information is currently available.

Having said that, I have been close to selling my 7900 XTX and buying a 4090 instead. It's very unfortunate since I want to support AMD given their open stance on Linux compared to Nvidia. However, an open stance is only worth so much if half of your use cases (Gaming & AI) are unavailable for an unknown amount of time. I am usually a day-1 GPU buyer (upgraded from a 6900XT to a 7900 XTX), but I am strongly considering going for Team Green next release, unless something changes in the meantime. Very unfortunate and disappointing, but it is what it is.

---

### 评论 #6 — aoolmay (2023-02-01T12:34:47Z)

Well, i made the wrong choice last time mostly due to similar "help".
You're giving false hope to people who might be missing deadlines or whatever opportunities.

---

### 评论 #7 — Mushoz (2023-02-01T14:14:10Z)

@aoolmay @stylerw already said that he picked up the 7900 XTX, so there isn't any choice left for him to make. Nor am I trying to give out false hope. I am merely pointing him to a few resources where this discussion is taking place, so that he can also be involved if he wants.

Furthermore, I even explicitly advised a user against buying a 7900 XTX at the moment right here: https://github.com/RadeonOpenCompute/ROCm/discussions/1834#discussioncomment-4839958

I understand it's a super frustrating situation right now. This applies to me as well, since I am now running this 7900 XTX, and I have no clue when ROCm support is to be expected. But I am not quite sure where you are getting that I would be giving out false hope. 

---

### 评论 #8 — aoolmay (2023-02-01T18:04:12Z)

@stylerw could try a 2020 solution in the form of PlaidML. It's an OpenCL backend with an old Keras frontend. You'll be crippled on up to date features, but it'll do basic work for you.

@Mushoz Not attributing to you particularly, but there's enough false hope floating around, i partook in it and spread some too.

---

### 评论 #9 — Odin234 (2023-02-09T00:10:51Z)

I hope this support will come soon. We, users, buying this card with some hope to unleash its computing power.
Personally, I have sentiment for AMD Radeon. Users give support to AMD by buying the newborn baby beast early so the development could be better and faster. I think that is healthy good relationship.

I still have faith in Team Red. After all this years. Always

---

### 评论 #10 — cmlibo (2023-03-15T16:13:32Z)

玩AI不建议买RDNA3的GPU，从6600xt换成7900xt，才发现无法使用，启动就报错，然后在win11中可以使用directml运行，但是很慢，甚至不到Linux下6600xt的一半，显存占用也无法释放，768*768尺寸的都直接报错。这辈子都不会再买AMD的显卡

---

### 评论 #11 — EwoutH (2023-07-01T08:02:22Z)

Can we pin this issue to the top of the repository and close all other RDNA 3 issues? There are now multiple opened every week, it would be great to keep track of RDNA3 support in one place.

---

### 评论 #12 — nartmada (2024-04-21T15:54:53Z)

My apologies to everyone for the lack of response :(

Please refer to the below link for supported GPUs.  

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html
https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html


---

### 评论 #13 — FCLC (2024-04-24T00:49:41Z)

Hey Adam! thanks for the links! 

Whilst it's been great seeing the 7900 XTX, XT and GRE receive support within the ROCm stack, the original point of the issue was not only "will RDNA 3 get support at all"

It was also for the entire RDNA3 product line. While the 7900 series has gotten support, that still leaves open questions for the 7800, 7700 and 7600 lines. 

Last I spoke with an AMD rep on the topic, APU's weren't going to be supported within ROCm, but the recent announcements from AMD seem to contradict that, at which point AMD APU's using RDNA 3 technologies would also be of interest in support. 

If at all possible, I'd ask that the issue be reopened if the plan is to add support for these other RDNA3 based devices, or otherwise mention/clarify that other devices within the RDNA3 stack should not expect to receive ROCm support, be it in the 6.x series or at all. 

Cheers, 

FCLC

---
