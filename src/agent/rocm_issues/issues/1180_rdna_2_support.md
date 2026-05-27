# rdna 2 support?

> **Issue #1180**
> **状态**: closed
> **创建时间**: 2020-07-13T06:42:33Z
> **更新时间**: 2022-11-17T16:01:57Z
> **关闭时间**: 2020-12-16T11:48:13Z
> **作者**: bernharl
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1180

## 描述

Will ROCM support the rdna 2 architecture when it is released in the future? I and a lot of others would love to be able to do some machine learning research on my personal computer and I would love to switch over to AMD because of their open sourced Linux drivers, but I'm not sure if I could actually make that switch if I can't replace the CUDA support in my Geforce card. 

I think the lack of Navi support is already a missed opportunity for AMD, but it sort of makes sense not to spend a massive amount of time supporting a card that isn't really flagship-tier. However, if the rdna 2 series of cards includes cards significantly more powerful than the 5700XT this wouldn't be the case anymore.

---

## 评论 (62 条)

### 评论 #1 — fishhf (2020-07-16T06:48:20Z)

AMD should support both RDNA 1 and 2. Otherwise people such as me will hop back to Nvidia after getting burned by 5700XT.

---

### 评论 #2 — bernharl (2020-07-16T06:51:48Z)

I agree, ideally it would be like CUDA where any Geforce GPU is supported. If AMD actually wants to compete in the ML market this is a must. People just getting into Machine Learning won't buy enterprise AMD GPUs if they can just buy a middle-tier RTX card.

---

### 评论 #3 — kevin335200 (2020-07-30T10:29:32Z)

Sadly never. AMD has a separate product line called CDNA for computing. I'm afraid RDNA architecture is not suitable for ML by design.

---

### 评论 #4 — bernharl (2020-07-30T10:39:42Z)

This has to change for AMD to be a viable option for startups and individual scientists. 

---

### 评论 #5 — limapedro (2020-08-03T02:17:01Z)

@kevin335200  @bernharl  Well at least for Windows users now is possible to use any DX 12 capable device to use tensorflow (Nvidia GPUs, AMD GPUs and APUs). I hope that the release Navi 2 with Rocm support, but now at least I know that I can use AMD GPUs, I hope that tensorflow-directml will get more optimization soon.

---

### 评论 #6 — bernharl (2020-08-03T12:28:28Z)

@limapedro Might as well use an Nvidia GPU with Cuda if I were to use proprietary software anyway. The reason I want an AMD GPU is because of the open source Linux driver...

Hopefully with ROCM being open source someone could be able to imlement RDNA2 support themselves is AMD refuses to!

---

### 评论 #7 — fishhf (2020-08-27T04:40:45Z)

Tensorflow's XLA backend already have targets that uses LLVM, and RDNA seems to be already in LLVM, I wonder if it's actually a lot of work to create a XLA backend that targets RDNA.
Then both Tensorflow and JAX would run on RDNA.

---

### 评论 #8 — cb88 (2020-09-22T03:15:50Z)

Apparently 5700xt is working in ROCm to some degree now (like darktable and blender but a bit unstable) ... RDNA2 probably isn't *that* different from RDNA1 compute wise and neither of them are incapable of compute, they just aren't optimized for it, CDNA is removing extra stuff from the GPU so they can scale to more CUs as well as reduce hardware overhead that exists in GCN and RDNA that ins requried to perform well for graphics (but doesn't really hurt compute either except maybe be a bit less power efficient given ideal code, RDNA can cope better with non ideal code though). 

Getting compute working on RNDA is very important for workstation users as AMD does sell the pro cards it just hasn't got the same priority as upcoming cards I think we'll see it finally straighten out once RDNA2 and CDNA are out.

---

### 评论 #9 — tuxzz (2020-10-28T16:43:50Z)

If RDNA2 support landed within four weeks after 6800XT sale date and had a similar performance to RTX 3080 on FP32+Tensorflow or other computation task, I would buy a bunch of it for my school laboratory.

---

### 评论 #10 — darkbasic (2020-10-28T17:46:08Z)

I wouldn't hold my breath: chances of getting anything in a reasonable timeframe are low but if you're feeling optimistic I would rather bet on clover being first

---

### 评论 #11 — cb88 (2020-10-28T18:56:49Z)

We basically already have RDNA1 support... it just isn't mainline. So.. I doubt there is a ton else to do for RNDA2.

---

### 评论 #12 — fishhf (2020-10-29T05:29:37Z)

> Apparently 5700xt is working in ROCm to some degree now (like darktable and blender but a bit unstable)

Darktable and blender should be just using OpenCL. OpenCL support is basically there since day 1 when 5700XT is released.

---

### 评论 #13 — MichelBr (2020-10-29T08:31:38Z)

The same here. I'll be looking for a new card/system at the end of the year and the zen 3, together with the rdna2 look great, but I'll only buy it if rocm supports it decently. I recently used rocm on vega with linux and to be honest it works quite well now. The instructions are not too bad and it just worked afterwards.

However, I don't want to fiddle with issues and amd needs to indeed support these cards for non-datacenter-usage (individuals, schools, ...). If they can buy Xilinx, they can also hopefully invest a bit of money in good tensorflow support for invidivuals who work with tensorflow and get more foothold in the ecosystem.

---

### 评论 #14 — darkbasic (2020-10-29T08:57:30Z)

ROCm 3.9 just released, still no RDNA support.

---

### 评论 #15 — xuhuisheng (2020-10-29T09:12:02Z)

There are codes and branches for gfx103x, Guess RDNA2 maybe supported next year?

https://github.com/ROCmSoftwarePlatform/Tensile/tree/gfx10
https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/bf43ad1b3da0e418e28f5c0ade4a2541a5f6d0d6
https://github.com/ROCmSoftwarePlatform/MIOpen/pull/545


---

### 评论 #16 — artyom-beilis (2020-10-29T09:13:22Z)

> We basically already have RDNA1 support... it just isn't mainline. So.. I doubt there is a ton else to do for RNDA2.

But... without MIOpen it does not worth much.

For example there is no implementation of RDNA Wingorad kernels for convolution and without it you will get at best 1/2 of performance potential. Windograd kernels implemented in GCN assembly and there are way too many differences between RDNA and GCN. How different RDNA2 will be? Nobody outside AMD knows.

There was a year to release RNDA... it wasn't done.

---

### 评论 #17 — zhiyuanzhai (2020-12-13T11:09:08Z)

Actually... It seems that RDNA 2 support has been discovered in ROCm codes... Just wait for ROCm 4.0, anyway.

---

### 评论 #18 — ROCmSupport (2020-12-16T11:48:13Z)

Hi @bernharl and all,
ROCm will come up with RDNA2 support but not now.
It will be released in 2021, but no specific timelines as of now. Please stay tuned.

---

### 评论 #19 — darkbasic (2020-12-19T12:29:11Z)

> Hi @bernharl and all,
> ROCm will come up with RDNA2 support but not now.
> It will be released in 2021, but no specific timelines as of now. Please stay tuned.

Will it come with RDNA support as well or RDNA2 only?

---

### 评论 #20 — unexploredtest (2020-12-19T15:43:10Z)

@darkbasic This is what they told me:
https://github.com/RadeonOpenCompute/ROCm/issues/1172#issuecomment-747215616

---

### 评论 #21 — artyom-beilis (2021-08-30T16:54:28Z)

Questions regarding RNDA2, specifically 6600XT

What support level is provided? It is clear that deep-learning/hip stack wound't work. However:

1. Does ROCm/OpenCL work?
2. Is it stable driver?
3. Does miopengemm work? Is performance tuned?
4. What level of MIOpen-OpenCL support is available? Does something work or it will not recognise this card?

I work on cross platform OpenCL deep learning library: https://github.com/artyom-beilis/dlprimitives currently I'm testing AMD on rx560 but it is 4 generations old card. So I bought 6600XT card and I need to know if I should go for Clover or amdgpu-pro drivers or I can use ROCM drivers for OpenCL as I do today.


---

### 评论 #22 — salvatoretrimarchi (2021-09-05T07:39:55Z)

I'm still waiting for that

---

### 评论 #23 — tuxzz (2021-09-05T12:07:56Z)

> Hi @bernharl and all,
> ROCm will come up with RDNA2 support but not now.
> It will be released in 2021, but no specific timelines as of now. Please stay tuned.

The 2021 Q4 is coming.


---

### 评论 #24 — fishhf (2021-09-05T12:45:35Z)

> > Hi @bernharl and all,
> > ROCm will come up with RDNA2 support but not now.
> > It will be released in 2021, but no specific timelines as of now. Please stay tuned.
> 
> The 2021 Q4 is coming.

I wonder what about RDNA1

---

### 评论 #25 — MichelBr (2021-09-05T15:07:45Z)

To be honest. It's the same old story with rocm. How good it is for the
supported cards doesn't matter, as support for the normal retail cards,
which a lot of people have, is always years behind. From my perspective,
only intel and nvidia have decent software support for their whole line-up
from day 1.
Amd is not able to provide this decent software support, unless you buy the
datacenter version.

That's it for the machine learning part. On the retail side, it's even
worse. You can't implement client-side machine learning stuff on amd with
full optimization, as they don't support it decently up till now. Well,
maybe directml  will change it, but I don't believe tensorflow has a
directml backend just yet. Correct me if I'm wrong. Anyway, these questions
just aren't relevant with intel and nvidia. You know they'll support it
from what I'm seeing up till now.

Sorry for this negative rant, but amd just isn't committed to machine
learning at this moment, unless you deploy a datacenter and teach everyone
how to deploy rocm. It's not difficult, but it's only for people with a
datacenter.

Michel

On Sun, Sep 5, 2021 at 2:45 PM fishhf ***@***.***> wrote:

> Hi @bernharl <https://github.com/bernharl> and all,
> ROCm will come up with RDNA2 support but not now.
> It will be released in 2021, but no specific timelines as of now. Please
> stay tuned.
>
> The 2021 Q4 is coming.
>
> I wonder what about RDNA1
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1180#issuecomment-913148458>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAJ7X3WY5RPGOVMSR2WDCA3UANQ7VANCNFSM4OYGP7XA>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


---

### 评论 #26 — artyom-beilis (2021-09-06T17:24:24Z)


> but I don't believe tensorflow has a directml backend just yet. Correct me if I'm wrong. Anyway, these questions just aren't relevant with intel and nvidia. You know they'll support it from what I'm seeing up till now. Sorry for this negative rant, but amd just isn't committed to machine learning at this moment,

To be honest AMD's software is poor. I bought 6600xt that on the box is written Windows 7 is supported... yet no drivers available (lucky me Windows is my secondary role for machine)

I must say that OpenCL works. I had both rocm and amdgpu-pro installed (I wasn't able to run vulkan with 4.3 drivers for some reason so I went back to amdgpu-pro - at least it has support of my second card rx560 for OpenCL on-chipset-connected PCI-E.

In any case to run training on RDNA2 currently you have Keras+PlaidML, Caffe-OpenCL and my DLPrimitives library I'm working on it right now.

You can see my benchmarks here: <https://github.com/artyom-beilis/dlprimitives/blob/master/docs/summary.md#benchmarks-gtx-1080> for 1080/2060s/6600xt that are roughly have similar flopws/memory speed (+-15%)

To be honest I gave up on ROCm, I cound't build pytorch out of the box on rocm 4.3, and apparently support of rx500 series had been "downgraded" so I cound't run out of the box TF or PT on my rx560 once I did a mistake upgrading from rocm 3.7 to 4.3 - I cound't run RF or PT any more.

The only reason I'm looking into AMD's stuff is because it is open source unlike NVidia's closed cudnn/cublas/cuda. I don't like that nvidia hides algorithms and optimizations from me. Also I really hate the need to upgrade cuda API when updating GPU.

I'm working on Open source OpenCL based solution that would work on Windows, Linux - actually any platforms that supports OpenCL.

---

### 评论 #27 — sevagh (2021-09-09T16:37:05Z)

Thanks for the report @artyom-beilis - so, in your opinion would buying an RDNA2 card (e.g. 6800) with the intention of using PlaidML + OpenCL be a good idea? Did you try out PlaidML and Caffe-OpenCL before writing DLPrimitives?

It won't be my primary GPU for deep learning (I have a main NVIDIA card), so it will be more as a fun experiment. I need to either buy a new RDNA2 GPU with PlaidML+OpenCL, or try to look for older Vega GPUs like the Radeon VII to use ROCm, which are super expensive and most likely have been mined on in their lifetime.

---

### 评论 #28 — artyom-beilis (2021-09-09T17:31:22Z)

> Did you try out PlaidML and Caffe-OpenCL before writing DLPrimitives?

I'm active Caffe user and one of the reasons I started using it was OpenCL support.

Caffe-OpenCL has relatively decent performance but still isn't as good as cudnn/miopen (1/2-1/3 in comparison to caffe-cudnn/hipCaffe).

But it has somewhat bigger problems: (a) Caffe isn't developed any more (b) it has very poor memory optimization, so for example with PT/Keras/TF I can get batch of 32 images of ResNet50 on 8GB, for caffe it is only 8-12. I still probably try to add dlprimitives support to Caffe as it is fastest path to get working OpenCL framework with Ok performance.

Regarding PlaidML its performance is poor and even more so on RDNA2. Another problem is that Keras has dropped muti-backend support so its future isn't clear - they are working on being integrated to TF but... these are plans.

Now there is dlprimitives - it is new, fresh - disclosure I work on it. It has very few operators and basic docs but it has decent performance.

Below 6600xt performance (compared with limitations of Caffe)

                    alexnet/64  resnet18/16     resnet50/b8 vgg16/8
    dlprim          77.581      59.989          93.830      155.335
    caffe           98.2334     117.525         201.92      263.124
    keras/plaidml   497.770     384.862         517.945     765.175

But in general I was able go get decent performance comparable to Keras+TF (somewhat lower) when I compare on GTX 1080 or 2060. So I assume similar would be on 6600xt since they are +- with same range of performance. 

See details of benchmarks

https://github.com/artyom-beilis/dlprimitives/blob/master/docs/6600_vs_1080_2060s.md



---

### 评论 #29 — ROCmSupport (2021-10-13T09:19:13Z)

Hi All,
With our internal validation, we are facing few critical issues with Navi cards and hence we are taking little more time to deliver official support with ROCm.
Please stay tuned for 5.0, we might expect good news with 5.0.

---

### 评论 #30 — DenkertM (2021-11-11T03:10:13Z)

Please let 5.0 support the 6600xt, and 6600 cards with kernel 5.11 or newer! 

---

### 评论 #31 — rubmz (2021-11-11T19:18:42Z)

Why didn't I find this thread a month ago when I mistakenly put my money on the wrong horse - 6900XT... now I need to sell it as second hand just to buy an NVidia GForce that will do Pytorch...
What's for sure, AMD has made it very vauge which cards support what technology. Was it for pure greediness or simply because AMD isn't strong with documentation? 
Guess both...

---

### 评论 #32 — artyom-beilis (2021-11-11T19:27:16Z)

> Why didn't I find this thread a month ago when I mistakenly put my money on the wrong horse - 6900XT... now I need to sell it as second hand just to buy an NVidia GForce that will do Pytorch... What's for sure, AMD has made it very vauge which cards support what technology. Was it for pure greediness or simply because AMD isn't strong with documentation? Guess both...

Take a look on this project: 

https://github.com/artyom-beilis/dlprimitives
https://github.com/artyom-beilis/pytorch_dlprim

It is early version but I already get decent performance. You don't need ROCm. Also hopefully ROCm will be ready soon with RDMA support.


---

### 评论 #33 — rubmz (2021-11-11T20:11:30Z)

> > Why didn't I find this thread a month ago when I mistakenly put my money on the wrong horse - 6900XT... now I need to sell it as second hand just to buy an NVidia GForce that will do Pytorch... What's for sure, AMD has made it very vauge which cards support what technology. Was it for pure greediness or simply because AMD isn't strong with documentation? Guess both...
> 
> Take a look on this project:
> 
> https://github.com/artyom-beilis/dlprimitives https://github.com/artyom-beilis/pytorch_dlprim
> 
> It is early version but I already get decent performance. You don't need ROCm. Also hopefully ROCm will be ready soon with RDMA support.

Impressive, but how mature is it?

And, is it possible to simply use the whold full blown PyTorch + transformers "over" OpenCL without ROCM? 

---

### 评论 #34 — artyom-beilis (2021-11-11T20:15:51Z)

It is on early but most of standard vision networks `alexnet, resnet, vgg, densenet161, shufflenet_v2, mobilenets, regnet` etc work and validated in both forward and backpropogation.

So don't expect everything just work but it is on-going and active project.

>  full blown PyTorch + transformers "over" OpenCL without ROCM?

I hand't got into transformers yet. If you have simple example I can test 

---

### 评论 #35 — zhiyuanzhai (2021-11-12T02:09:09Z)

> Was it for pure greediness or simply because AMD isn't strong with documentation?

@rubmz Considering the staggering cost for developing both CPU and GPU, and the fact that AMD is a much smaller company compared to Intel or Nvidia, I believe it's more of the latter situation. 

It is quite familiar to Radeon fans that AMD fails to provide full support for its new product at launch time with new driver, in terms of either functionality or performance.

---

### 评论 #36 — rubmz (2021-11-12T04:39:17Z)

> > Was it for pure greediness or simply because AMD isn't strong with documentation?
> 
> @rubmz Considering the staggering cost for developing both CPU and GPU, and the fact that AMD is a much smaller company compared to Intel or Nvidia, I believe it's more of the latter situation.
> 
> It is quite familiar to Radeon fans that AMD fails to provide full support for its new product at launch time with new driver, in terms of either functionality or performance.

AMD could simply put up a page with more simple card -> tech map. Not all ...well .. card buyers, know what RDNA2 or GCN (or ROCM...) means. Even if you dig in deeper it's not too clear which term goes where...

---

### 评论 #37 — rubmz (2021-11-12T18:42:11Z)

The grotesque about it all, is the cards AMD DO provide support for ROCM/PyTorch are [3~4 years old and far far weaker](https://technical.city/en/video/Radeon-PRO-WX-9100-vs-Radeon-RX-6900-XT)... 


---

### 评论 #38 — MichelBr (2021-11-12T20:17:50Z)

It's a shame that somebody can do this in their free time (I thought so),
but AMD isn't willing to spend the resources on this. The ROCM team seems
great, but I have given up on AMD on this front (unfortunately). No hassle
approaches, so you can focus on the work at hand, seems to be intel or
nvidia.

The only positive thing I heard is that facebook/meta has a deal with AMD
now, but still. That's probably only for the instinct cards.

On Fri, Nov 12, 2021 at 7:42 PM rubmz ***@***.***> wrote:

> The grotesque about it all, is the cards AMD DO provide support for
> ROCM/PyTorch are 3~4 years old and far far weaker
> <https://technical.city/en/video/Radeon-PRO-WX-9100-vs-Radeon-RX-6900-XT>
> ...
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1180#issuecomment-967335184>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAJ7X3RGAVC5HWMTBLABR3TULVNY5ANCNFSM4OYGP7XA>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


---

### 评论 #39 — cb88 (2021-11-12T20:34:46Z)

> 
> 
> The grotesque about it all, is the cards AMD DO provide support for ROCM/PyTorch are [3~4 years old and far far weaker](https://technical.city/en/video/Radeon-PRO-WX-9100-vs-Radeon-RX-6900-XT)...

Except that isn't true as evidenced by the closure of this ticket and official support for the W6800.... which is the same chip as the 6900XT you referenced.

Also we still have no indication that any of the older GPUs newer than the R9 series have been dropped other than MI25 (and that seems to still be up for debate since some AMDers dissent this drop of support also since its just a Vega10.

---

### 评论 #40 — MichelBr (2021-11-12T21:14:37Z)

I'm not going into details here, but the fact is that AMD doesn't really
advertise rocm (pytorch, tensorflow, ...) as supported for their normal
cards like nvidia (and apparently also intel) does. Let's say you develop a
nice neural network for a consumer application, which is nowadays maybe a
corner case, but it's growing. Which platform should one target?

Mac is easy ...
nvidia is indeed limited to external cards or more expensive laptops, but
you know it's well supported and works fine normally.
intel is going to support all their processors (let's say from tigerlake)
and. well, forget the mobile market with the apu's. Forget the desktop
market, because it isn't officially supported on any card.

So, if someone has to make a choice, besides for a datacenter, currently, I
wouldn't choose AMD if the price is anywhere in the neighborhood of the
other 2.

Don't get me wrong. I like ROCM and I like it's opensource and well
supported on linux. I used it with tensorflow in the past and it worked
well (vega), but you can't compare it to the support that the others
provide on this front.

But please correct me if this seems wrong.

Kind regards

On Fri, Nov 12, 2021 at 9:34 PM cb88 ***@***.***> wrote:

> The grotesque about it all, is the cards AMD DO provide support for
> ROCM/PyTorch are 3~4 years old and far far weaker
> <https://technical.city/en/video/Radeon-PRO-WX-9100-vs-Radeon-RX-6900-XT>
> ...
>
> Except that isn't true as evidenced by the closure of this ticket and
> official support for the W6800.... which is the same chip as the 6900XT you
> referenced.
>
> Also we still have no indication that any of the older GPUs newer than the
> R9 series have been dropped other than MI25 (and that seems to still be up
> for debate since some AMDers dissent this drop of support also since its
> just a Vega10.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1180#issuecomment-967504418>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAJ7X3R3CIWG7XBC4F3B4EDULV27FANCNFSM4OYGP7XA>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


---

### 评论 #41 — artyom-beilis (2021-11-12T21:37:13Z)

In general AMD's support of their cards is poor. 

- No APUs (and AMD's APUs are most powerful today).
- No Windows/Mac
- No RDNA1/2 yet,
- GCN4 (like rx 570) require direct PCI-E lines to CPU (and declared as dropped)

Quality of drivers... There are Intel GPU drivers (excellent), there are NVidia drivers (not perfect but work) and the are... AMD. My graphics card crashing if I overuse memory or virtually anything else little bit less standard.

There are two good things about rocm:

1. It is opensource (mostly https://github.com/ROCmSoftwarePlatform/MIOpen/issues/480)
2. With MIOpen It gives comparable performance to cudnn

But in general if you looking for something that allow you do be less nVidia dependent it isn't the way

---

### 评论 #42 — rubmz (2021-11-12T21:47:09Z)

There is the OneAPI from Intel, which supposedly might/should support all AMD cards (on linux ...).
Yet I'm not sure if/how?



---

### 评论 #43 — artyom-beilis (2021-11-12T21:56:11Z)

> There is the OneAPI from Intel, which supposedly might/should support all AMD cards (on linux ...). Yet I'm not sure if/how?

I don't remember if oneAPI incuded rocm or not... but even if it does it will be dependent on ROCm.

See today you can try to use Keras with PlaidML (with poor performance) or Caffe/OpenCL - (with no dev in near future and old arch) and of course early stage dlprimitives/pytorch-opencl-dlprimitives that I want to integrate AMD's MIOpen-OpenCL, Intel's and AMD's open source DNN libraries into it for better performance in not so far future.

---

### 评论 #44 — limapedro (2021-11-13T20:12:26Z)

Well, there is pytorch-directml now on pre release. I've been using tensorflow-directml for a couple of months, it's great, I hope that they migrate to tensorflow 2.x soon and enable multi-gpu support, there were some article about how AMD improved performance on directml a couple of weeks ago.

Sources down below:

https://devblogs.microsoft.com/windowsai/introducing-pytorch-directml-train-your-machine-learning-models-on-any-gpu/

https://wccftech.com/amd-microsoft-bring-tensorflow-directml-to-life-4x-improvement-with-rdna-2-gpus/


---

### 评论 #45 — rubmz (2021-11-13T20:24:38Z)

> Well, there is pytorch-directml now on pre release. I've been using tensorflow-directml for a couple of months, it's great, I hope that they migrate to tensorflow 2.x soon and enable multi-gpu support, there were some article about how AMD improved performance on directml a couple of weeks ago.
> 
> Sources down below:
> 
> https://devblogs.microsoft.com/windowsai/introducing-pytorch-directml-train-your-machine-learning-models-on-any-gpu/
> 
> https://wccftech.com/amd-microsoft-bring-tensorflow-directml-to-life-4x-improvement-with-rdna-2-gpus/

For a moment there I had grown expectations, then I read it's for windows.... 

---

### 评论 #46 — limapedro (2021-11-13T20:30:24Z)

@rubmz Yeah it's a downside of directml, I hope that Microsoft could bring for linux, maybe there is a way of running, it can run on Windows Subsystem for linux, so I guess is just some piece missing. But the directml stack seems the best one now, it can run on almost any GPU available now 92% of current GPUs according to steam hardware survey.

---

### 评论 #47 — rubmz (2021-11-13T20:35:52Z)

Don't think it would work on linux, but hey guess some AMD users have Windows. So, happy for them!
I'm gona sell this card 😅 no more AMD for me even if I will have to pay a few hundreds of dollars more...

---

### 评论 #48 — husmen (2022-02-23T08:32:22Z)

> Hi All, With our internal validation, we are facing few critical issues with Navi cards and hence we are taking little more time to deliver official support with ROCm. Please stay tuned for 5.0, we might expect good news with 5.0.

2022 is here, ROCm 5.0 is out, yet no progress or update on this issue. I guess having any hope at this point would be foolish.

---

### 评论 #49 — ROCmSupport (2022-02-23T10:31:04Z)

Hi @husmen 
Navi21 is enabled from ROCm 5.0 onwards. Request to try the same. Thank you.


---

### 评论 #50 — MichelBr (2022-02-23T10:36:23Z)

Please compare this to Intel, although I think the room team is fantastic
and probably with passion.
I have an Intel NUC pro with. Tiger lake we graphics. Intel had optimized
libraries for tensorflow, pytorch, scikit, ...

I said it before and will reiterate, there is no apparent interest from AMD
management in ml for devs with non-datacenter hardware. It's a shame after
all these years.

Michel

Op wo 23 feb. 2022 11:31 schreef ROCmSupport ***@***.***>:

> Hi @husmen <https://github.com/husmen>
> Navi21 is enabled from ROCm 5.0 onwards. Request to try the same. Thank
> you.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1180#issuecomment-1048641755>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAJ7X3QCTKMOJQPTXNPPM4TU4SZPLANCNFSM4OYGP7XA>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


---

### 评论 #51 — artyom-beilis (2022-02-23T10:42:32Z)

> Navi21 is enabled from ROCm 5.0 onwards. Request to try the same. Thank you.

Does it mean MIOpen supports NAVI? Does it mean I can build pytorch and run in on RDNA GPU?

---

### 评论 #52 — ROCmSupport (2022-02-23T11:26:44Z)

> > Navi21 is enabled from ROCm 5.0 onwards. Request to try the same. Thank you.
> 
> Does it mean MIOpen supports NAVI? Does it mean I can build pytorch and run in on RDNA GPU?

Yes

---

### 评论 #53 — artyom-beilis (2022-02-23T14:12:54Z)

> > Does it mean MIOpen supports NAVI? Does it mean I can build pytorch and run in on RDNA GPU?
> 
> Yes

So why it doesn't appear in release notes: https://github.com/RadeonOpenCompute/ROCm ?

---

### 评论 #54 — cb88 (2022-02-23T16:11:26Z)

> > > Does it mean MIOpen supports NAVI? Does it mean I can build pytorch and run in on RDNA GPU?
> > 
> > 
> > Yes
> 
> So why it doesn't appear in release notes: https://github.com/RadeonOpenCompute/ROCm ?

Spamming this ticket with AMD hate isn't helpful. And there are two Navi21 cards listed as supported in that very link so ... yeah. It *would* be nice if they officially supported all cards and all AMD GPUs but that appears to much to ask on current gen hardware and with the resources they have so lay off.

---

### 评论 #55 — artyom-beilis (2022-02-23T17:54:12Z)

I see

> PRO v620, PRO W6800

i.e. if I own rx 6600xt, 6700xt or 6500 I need to hope it will work :-)...

Ok good step forward. I hope non-pro GPU will work as well.

> Spamming this ticket with AMD hate isn't helpful

It isn't spamming, It is clarification. You can't tell me that I hate AMD considering I purchaded rx560 and rt 6600xt and develop [dlprimitives](https://github.com/artyom-beilis/dlprimitives) that fully support AMD...

I just honestly _disappointed_ of the level of AMD commitment for deep learning world :-)

---

### 评论 #56 — zhiyuanzhai (2022-02-28T17:26:45Z)

Oh… just do some tests before making remarks, please! 

All it takes is just someone who indeed has an RX6000 card and make a try to setup ROCm in his system. If you have one of those, just do the test; if you don't have one, then shut up and wait someone else to do it. What is the point yelling here? Are you really waiting for a good result?

---

### 评论 #57 — Taris9047 (2022-09-12T00:30:51Z)

Installed ROCm 5.2.0

Here's rocminfo output:
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 3700X 8-Core Processor 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 3700X 8-Core Processor 
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3600                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32790724(0x1f458c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32790724(0x1f458c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32790724(0x1f458c4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1030                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 6700 XT              
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      3072(0xc00) KB                     
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29663(0x73df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2725                               
  BDFID:                   3072                               
  Internal Node ID:        1                                  
  Compute Unit:            40                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1030         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             

But compiling an example code from https://github.com/ROCm-Developer-Tools/HIP-Examples/blob/master/vectorAdd/vectoradd_hip.cpp

still shows error: 
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"

So, no Joy... Still Sep. 11th 2022.

---

### 评论 #58 — xuhuisheng (2022-09-12T01:22:34Z)

@Taris9047 
Please show you compile cmd args, maybe you used wrong AMDGPU_TARGETS.

The plain hip cpp sample didn't depends re-build package, so the `hipErrorNoBinaryForGpu` could only report by itself.

Although I had no gfx1030 card, but navi10 card can run on ROCm-5.2.3 with `HSA_OVERRIDE_GFX_VERSION=10.3.0` to pretend gfx1030 card, so it can verify that rocm-libs and tensorflow-rocm can support gfx1030 properly.

---

### 评论 #59 — Taris9047 (2022-09-12T01:32:12Z)

> 

My Makefile is as is:
```HIP_PATH?= $(wildcard /opt/rocm/hip)
ifeq (,$(HIP_PATH))
	HIP_PATH=/opt/rocm
endif

HIPCC=$(HIP_PATH)/bin/hipcc
TARGET=hcc

SOURCES = vector_add.cpp
OBJECTS = $(SOURCES:.cpp=.o)

EXECUTABLE = ./vector_add

CXXFLAGS = -g
CXX=$(HIPCC)

.PHONY: test

all: $(EXECUTABLE) test

$(EXECUTABLE): $(OBJECTS)
	$(HIPCC) $(OBJECTS) -o $@

test: $(EXECUTABLE)
	$(EXECUTABLE)

clean:
	rm -rf $(EXECUTABLE) $(OBJECTS) $(HIP_PATH)/src/*.o
```

So, I'm not sure what went wrong.. AMDGPU_TARGETS does not exist in the makefile. I've also tried with the `HSA_OVERRIDE_GFX_VERSION=10.3.0` hack but no joy.

I can confirm `tensorflow-rocm` can run with the hack, though! Weird... my card is is 1030 card... but still need to use the hack...

---

### 评论 #60 — xuhuisheng (2022-09-12T02:42:20Z)

Try `AMD_LOG_LEVEL=3 ./vector_add` to see which hsa target missed.

---

### 评论 #61 — Taris9047 (2022-09-12T14:54:56Z)

```
:3:rocdevice.cpp            :416 : 59032119740 us: 215311: [tid:0x7fcf63de6880] Initializing HSA stack.
:3:comgrctx.cpp             :33  : 59032127673 us: 215311: [tid:0x7fcf63de6880] Loading COMGR library.
:3:rocdevice.cpp            :207 : 59032130787 us: 215311: [tid:0x7fcf63de6880] Numa selects cpu agent[0]=0xd98c20(fine=0xd98e10,coarse=0xd990d0) for gpu agent=0xd9a780
:3:rocdevice.cpp            :1611: 59032130991 us: 215311: [tid:0x7fcf63de6880] HMM support: 1, xnack: 0, direct host access: 0

:3:hip_context.cpp          :50  : 59032132323 us: 215311: [tid:0x7fcf63de6880] Direct Dispatch: 1
:1:hip_code_object.cpp      :460 : 59032132340 us: 215311: [tid:0x7fcf63de6880] hipErrorNoBinaryForGpu: Unable to find code object for all current devices!
:1:hip_code_object.cpp      :461 : 59032132343 us: 215311: [tid:0x7fcf63de6880]   Devices:
:1:hip_code_object.cpp      :464 : 59032132347 us: 215311: [tid:0x7fcf63de6880]     amdgcn-amd-amdhsa--gfx1030 - [Not Found]
:1:hip_code_object.cpp      :468 : 59032132350 us: 215311: [tid:0x7fcf63de6880]   Bundled Code Objects:
:1:hip_code_object.cpp      :485 : 59032132353 us: 215311: [tid:0x7fcf63de6880]     host-x86_64-unknown-linux - [Unsupported]
:1:hip_code_object.cpp      :483 : 59032132356 us: 215311: [tid:0x7fcf63de6880]     hipv4-amdgcn-amd-amdhsa--gfx1031 - [code object v4 is amdgcn-amd-amdhsa--gfx1031]
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
Aborted (core dumped)
```
Here it is.

Also, here's compile `make` command message.
```
/opt/rocm/hip/bin/hipcc -g   -c -o vector_add.o vector_add.cpp
/opt/rocm/hip/bin/hipcc vector_add.o -o vector_add
./vector_add
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
make: *** [Makefile:25: test] Aborted (core dumped)
```

Additionally, here is `tensorflow-rocm` test output:
```
Python 3.10.4 (main, Mar 31 2022, 08:41:55) [GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> tf.add(1,2).numpy()
2022-09-12 11:59:34.205727: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.452499: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.452561: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.452809: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-09-12 11:59:34.453459: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.453525: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.453562: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.453665: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.453707: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.453746: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-09-12 11:59:34.453767: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 11772 MB memory:  -> device: 0, name: AMD Radeon RX 6700 XT, pci bus id: 0000:0c:00.0
3
```
I can also run some tensorflow tutorial codes without too much of problem either. The NUMA node error also present when my GPU was NVIDIA brand. So, it's some kind of Linux stuff and I believe the same [workaround](https://stackoverflow.com/questions/44232898/memoryerror-in-tensorflow-and-successful-numa-node-read-from-sysfs-had-negativ) would work out. Also, `tensorflow-rocm` finds my 6700XT without problem!

---

### 评论 #62 — xuhuisheng (2022-09-12T22:18:30Z)

It is weird that the add_vector compiled with amdgpu_target gfx1031, which need gfx1030 on runtime. So it reports missfire.

I think you shoud check hip-config, maybe there is some clue, e.g. hardcode gfx1031.

---
