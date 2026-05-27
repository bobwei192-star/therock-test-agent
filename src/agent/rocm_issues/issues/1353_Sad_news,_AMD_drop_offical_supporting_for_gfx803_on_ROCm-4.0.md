# Sad news, AMD drop offical supporting for gfx803 on ROCm-4.0

> **Issue #1353**
> **状态**: closed
> **创建时间**: 2020-12-30T10:05:45Z
> **更新时间**: 2021-03-08T21:09:57Z
> **关闭时间**: 2021-01-04T05:53:40Z
> **作者**: xuhuisheng
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1353

## 描述

I noticed that gfx803 had been removed from ROCm-4.0 offical supporting list on 2020-12-19.
https://github.com/RadeonOpenCompute/ROCm/commit/2b7f806b106f2b19036bf8e7af4f3dad7bc6222e#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5L408

Indeed, gfx803 is an old card and ROCm should put limit resources to support new hardwares. The bad part is the only GPU what I have is RX580 which is gfx803. The price of GPU is higher, which I didn't expect. I think I should try to find a way to let my gfx803 work longer by myself.

Feel free to close my gfx803 related issues and pull requests.

* https://github.com/RadeonOpenCompute/ROCm/issues/1265
* https://github.com/ROCmSoftwarePlatform/rocBLAS/issues/1172
* https://github.com/ROCmSoftwarePlatform/rocRAND/pull/159 

---

## 评论 (18 条)

### 评论 #1 — Moading (2020-12-30T14:05:57Z)

Hi @xuhuisheng , this is indeed bad news but it had to happen sooner or later.

I think however, that things will continue working but we will not be able to use new features. I am using a cluster with Radeon Pro Duo GPUs for my work. Could you please test if OpenCL 2.0 device side enqueue is working on your RX580? The test program can be found in #540.

Greetings!

---

### 评论 #2 — xuhuisheng (2020-12-30T22:29:24Z)

@Moading 
Sorry, I have only one GPU. cannot do this test.

```
work@c6a389e478c0:~/test$ ./a.out
prob: a clGetDeviceIDs -1
ncpus: 0 ngpus: 1
this program needs more than 1 GPUs!

```

---

### 评论 #3 — Moading (2020-12-30T22:54:08Z)

Hi @xuhuisheng, the test works also with one GPU, just comment out the lines that check for the number of GPUs. Sorry for the trouble...

---

### 评论 #4 — xuhuisheng (2020-12-30T23:01:08Z)

After comment out gpu number checking, The program hang after a,b,c.
I am not familier with openCL. will find some time to check this.

GPU: RX580
OS: Ubuntu-20.04.1
ROCm: ROCm-4.0

```
work@c6a389e478c0:~/test$ ./a.out
prob: a clGetDeviceIDs -1
ncpus: 0 ngpus: 1
testing GPU 0
a
b
c

```

Actually, hanging on the `clFinish` waiting for `clEnqueueNDRangeKernel`. rocm-smi didnot show VRAM or GPU usage. dmesg didnt show error.

My mistake, after wait for minutes, it show `done` and exit properly. I think it said success.

```
prob: a clGetDeviceIDs -1
ncpus: 0 ngpus: 1
testing GPU 0
a
b
c
passed
done

```

---

### 评论 #5 — Moading (2020-12-31T10:10:38Z)

Hi @xuhuisheng, thanks for your effort. I also observe the program hanging in the clFinish call. This means device side enqueue is not working properly. Thanks for confirming!

---

### 评论 #6 — umeshu (2021-01-02T07:23:00Z)

What the frog.

I just bought this GPU two months ago solely for the ROCm tensor flow and also since it was listed as officially supported. Obviously, I didn't expect this removal would come very soon after. Oh dang, it..., I should have chosen the leather jacket guy GPU. 

A small suggestion to the ROCm team: write a warning/heads up to the Hardware-and-Software-Support section that you intend to remove official support for a few select GPUs in near future. It's a small thing but it's a nice gesture and will be highly appreciated by everyone. 




---

### 评论 #7 — ROCmSupport (2021-01-04T05:53:40Z)

Thanks @xuhuisheng for filing this.
Thanks @umeshu for the suggestions. Will keep in mind and try to follow the same.
Yes, gfx8 support is officially dropped from now.
AMD ROCm is having plans to support of adding new hardware slowly like we have added MI100 support.
Please wait and stay tuned for the updates.
Thank you.



---

### 评论 #8 — imakin (2021-01-14T05:48:25Z)

Is there any guarantee that currently supported GPUs will remain supported in the future? 

---

### 评论 #9 — umeshu (2021-01-14T10:32:45Z)

> Is there any guarantee that currently supported GPUs will remain supported in the future?

I haven't seen any source that gives that kind of information, nor any plan on how ROCm will support their GPUs. 

So I think it's not too much, to say that for us --the users, it's merely a bet. Two months ago I saw a gfx803 was supported, so I built my new PC under AMD environment with my hard-earned money, and suddenly, I woke up in the morning, as South Park would put it, "Then it's gone". It was a wrong bet.  

So based on that experience, unless there is a clear path on what GPUs and for how long they intend to support them minimally, I would stay away from AMD cards. 

I hope they will address this issue, but meanwhile, the leather jacket guy's cards would be a safe bet. That's my two cents. 




 

 

---

### 评论 #10 — imakin (2021-01-14T11:20:17Z)

> > Is there any guarantee that currently supported GPUs will remain supported in the future?
> 
> I haven't seen any source that gives that kind of information, nor any plan on how ROCm will support their GPUs.
> 
> So I think it's not too much, to say that for us --the users, it's merely a bet. Two months ago I saw a gfx803 was supported, so I built my new PC under AMD environment with my hard-earned money, and suddenly, I woke up in the morning, as South Park would put it, "Then it's gone". It was a wrong bet.
> 
> So based on that experience, unless there is a clear path on what GPUs and for how long they intend to support them minimally, I would stay away from AMD cards.
> 
> I hope they will address this issue, but meanwhile, the leather jacket guy's cards would be a safe bet. That's my two cents.

I have the similar experience with you. I saw the rx550 on the support list, and i brought it. I was also planning to buy an rx580 just for ROCm a week ago. Glad i didn't and i bought the jetson and also an RTX intead recently.
It's sad for me to move from AMD because i really like the opensource driver on my linux.

AMD has Vega64 which is versatile (support both gaming and ROCm). I wish AMD would make more GPUs like this in the future. The leather jacket guy has all his GPUs as versatile as that. Supported in tensorflow and pytorch (except the old GPUs cuda capatibility < 3.5)

I'm still looking forward for AMD and i still cherish the ROCm project though

---

### 评论 #11 — umeshu (2021-01-16T06:37:37Z)

> > > Is there any guarantee that currently supported GPUs will remain supported in the future?
> > 
> > 
> > I haven't seen any source that gives that kind of information, nor any plan on how ROCm will support their GPUs.
> > So I think it's not too much, to say that for us --the users, it's merely a bet. Two months ago I saw a gfx803 was supported, so I built my new PC under AMD environment with my hard-earned money, and suddenly, I woke up in the morning, as South Park would put it, "Then it's gone". It was a wrong bet.
> > So based on that experience, unless there is a clear path on what GPUs and for how long they intend to support them minimally, I would stay away from AMD cards.
> > I hope they will address this issue, but meanwhile, the leather jacket guy's cards would be a safe bet. That's my two cents.
> 
> I have the similar experience with you. I saw the rx550 on the support list, and i brought it. I was also planning to buy an rx580 just for ROCm a week ago. Glad i didn't and i brought the jetson and also an RTX intead recently.
> It's sad for me to move from AMD because i really like the opensource driver on my linux.
> 
> AMD has Vega64 which is versatile (support both gaming and ROCm). I wish AMD would make more GPUs like this in the future. The leather jacket guy has all his GPUs as versatile as that. Supported in tensorflow and pytorch (except the old GPUs cuda capatibility < 3.5)
> 
> I'm still looking forward for AMD and i still cherish the ROCm project though

Mee too, the main reason I wanted to use AMD GPUs was that ROCm is open-source software. 

Hopefully, AMD will put more resources on ROCm and make it a successful project. 

IMHO, what the ROCm team could do under limited resources is to provide solid performance only for a few select GPU with a clear plan on support period. This way users can have trust and a thriving community may grow out of it. 

Until that happens, using AMD GPUs for ML under ROCm is merely a bet. 

For an Oil Sultan, that kind of bet is a non-issue, but for peasants, that is a huge deal. 

And It's Gone... Poof! (https://www.youtube.com/watch?v=o4ZeTdOjLUk)

 



---

### 评论 #12 — Moading (2021-01-16T20:54:18Z)

I am developing a multi GPU HPC application. The application calls a series of OpenCL kernels. I see incorrect results in ROCM 4.0 for gfx906 and I'm pretty sure the problem is also present for gfx803 but I have not checked. My motivation to investigate is zero now. I'll live with 2.10 for another year before investing in new hardware. Going with OpenCL and being vendor independent was a good choice.

---

### 评论 #13 — jrcichra (2021-01-17T20:59:30Z)

@BishopWolf brought this to my attention. I luckily got into ML with my RX580 right before this happened. I have a docker container with gfx803 support built in for pytorch, if you don't mind using a 2 month old copy of `rocm/pytorch`:

Dockerfile executed two months ago:

```
FROM rocm/pytorch:latest
RUN git clone https://github.com/xuhuisheng/rocSPARSE && cd rocSPARSE && bash install.sh -di
```

`docker run` docs here: https://github.com/jrcichra/rocm-pytorch-gfx803

I am saddened to hear gfx803 is losing support. If you need a quick solution to use a gfx803 card, hopefully this helps.


---

### 评论 #14 — angimenez (2021-03-08T02:31:05Z)

Hello! I have the same problem. I purchased a rx580x for machine learning, but I can't use it for this. Can you help me with any workaround? Thank you, I don't have money for purchase nvidia GPU for now. 
I need to use Tensorflow and pytorch :)

---

### 评论 #15 — xuhuisheng (2021-03-08T02:36:52Z)

@angimenez ROCm-3.5.1 is OK.

---

### 评论 #16 — angimenez (2021-03-08T15:19:09Z)

@xuhuisheng thank you for reply. Can I execute apt install rocm-dev3.5.1 and works well?

---

### 评论 #17 — angimenez (2021-03-08T20:14:46Z)

How I can install rocm 3.5.1 on Ubuntu 20.04? 

---

### 评论 #18 — unexploredtest (2021-03-08T21:09:57Z)

@angimenez I think this might help:
https://github.com/boriswinner/RX580-rocM-tensorflow-ubuntu20.4-guide

---
