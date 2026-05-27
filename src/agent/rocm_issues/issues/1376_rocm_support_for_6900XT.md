# rocm support for 6900XT 

> **Issue #1376**
> **状态**: closed
> **创建时间**: 2021-02-10T19:38:39Z
> **更新时间**: 2022-08-30T00:22:46Z
> **关闭时间**: 2021-02-11T06:13:26Z
> **作者**: powderluv
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1376

## 描述

Following up on the issue here with RocBLAS on GFX1030 architecture (6900XT) : https://github.com/ROCmSoftwarePlatform/rocBLAS/issues/1185  

Do we expect rocm / rocblas support for 6900XT ?  The current builds from the gfx10 branch seems to fail as listed in the bug above.  

---

## 评论 (20 条)

### 评论 #1 — Djip007 (2021-02-11T00:21:55Z)

https://github.com/RadeonOpenCompute/ROCm/issues/887#issuecomment-770574455

---

### 评论 #2 — powderluv (2021-02-11T02:46:25Z)

This is incredibly disappointing that you buy the latest AMD cards and you have to wait 2yrs for ROCm / compute support ? (starting with 5700Xt and now 6900xt).  Imagine buying an RTX3090 and waiting for CUDA to support it sometime in the future. 

Everyone here is a champion of AMD hardware and are trying to be seed it into their workflow. I hope the decision makers at AMD are aware of these gaps for developers. SW is as important as the HW and all the released hardware must atleast have beta support for ROCM if we want to consider rocm as an alternative to CUDA. 


---

### 评论 #3 — hwchong (2021-02-11T04:46:27Z)

It does appear that ROCm is abandonware. You're probably better off sticking with CUDA or if you really need AMD hardware then Vulkan compute.

---

### 评论 #4 — powderluv (2021-02-11T05:48:26Z)

I have been able to test Vulkan Compute on the 6900XT and it performs reasonably when compared to the 3090 via vulkan.  Only problem is for any ML workloads the  TF/Pytorch framework integrations are all ROCm and not VkCompute.  

---

### 评论 #5 — xuhuisheng (2021-02-11T06:00:08Z)

Good news is AMD said navi will be supported in 2021. At least, it is a hope.

---

### 评论 #6 — ROCmSupport (2021-02-11T06:13:26Z)

Hi @powderluv and all,
We have plans to support Navi series of cards in future but I can not comment right now on specific version/series of Navi and so I request you to wait for few more days.
Please stay tuned for the updates via our documentation.
Thank you.

---

### 评论 #7 — banderlog (2021-03-05T16:25:40Z)

Aha, it is still better to buy NVIDIA GPUs for ML then.
 
There is no way for the red team to even take decent participation in the whole ML/DL thing without ROCm support of the own **two** last GPU generations. For actual competition, ROCm should be no more buggy than CUDA. In how many years that will be achieved? I bet that no sooner than the next GPU generation arrives (another ~3 years).   

That is sad.

---

### 评论 #8 — NightHammer1000 (2021-04-14T07:52:28Z)

ROCm Support should be one of the TOP Priorities at AMD atm.
The most powerfull Card cant be used in a field where it would be immensly usefull? 
Thats just sad.

---

### 评论 #9 — ottworks (2021-06-11T17:55:56Z)

This is just sad. They're the only cards you can get at MSRP right now and they don't even have AMD's official support.

---

### 评论 #10 — zocker-160 (2021-06-11T20:20:55Z)

> They're the only cards you can get at MSRP right now 

Now think about why that might be, surely not because the demand is so high because everybody wants them.....

---

### 评论 #11 — MichelBr (2021-07-09T10:07:53Z)

It's also one of the reasons I'm looking at intel after a long time. At least they have tensorflow-support throughout their whole new line. Certainly with the new tigerlake-graphics and upcoming dg2. You should even be able to virtualize them, although that isn't my goal.

Anyway, I also have been monitoring and even worked with rocm on vega. But their bad hardware-support for the radeaon graphics is really disappointing. Their product works, I know that from experience. There's just no interest in supporting the normal graphics pipeline. Yes, even if it won't be optimal, it would be better than executing it on the cpu mostly if you have such a powerful card.

Look at what apple is doing with the m1 and the new os. I guess that ml will be a bigger and bigger part of the experience. 

---

### 评论 #12 — rubmz (2021-12-11T15:50:33Z)

> Hi @powderluv and all, We have plans to support Navi series of cards in future but I can not comment right now on specific version/series of Navi and so I request you to wait for few more days. Please stay tuned for the updates via our documentation. Thank you.

"In the future" - you're a sad joke.

---

### 评论 #13 — DrewRidley (2022-04-01T14:44:50Z)

Is this still on AMD's radar? Its been over 4 months since the last post and its been even longer since these plans were announced. Very disappointing to spend $1000 on a graphics card and not receive support for basic ML!

---

### 评论 #14 — powderluv (2022-04-01T15:48:46Z)

It's supported in the last rocm release

---

### 评论 #15 — jnordberg (2022-04-19T05:52:31Z)

@powderluv [The docs for v5.1.1](https://docs.amd.com/bundle/ROCm-Getting-Started-Guide-v5.1.1/page/Overview_of_ROCm_Installation.html) doesn't mention the 6900XT being supported, can you confirm if v5.1.1 will work or are you talking about some upcoming release?


---

### 评论 #16 — rubmz (2022-04-19T06:48:25Z)

Stay away from evil! 😈
It took me 2 months and 750 USD loss to get rid of the damn thing. Until AMD go serious on providing drivers for their cutting edge hardware you better check well that the exact model is indeed supported and working.

---

### 评论 #17 — jnordberg (2022-04-19T07:43:06Z)

@rubmz Haha yeah I feel you, I was actually just checking for support one last time before pulling the trigger to sell my card and pick up a Nvidia... hopefully it works now so I don't have to go through with it.

I really hope AMD steps up their ML game, not only with device support but also documentation and ecosystem integration.

---

### 评论 #18 — rubmz (2022-04-19T17:39:56Z)

> @rubmz Haha yeah I feel you, I was actually just checking for support one last time before pulling the trigger to sell my card and pick up a Nvidia... hopefully it works now so I don't have to go through with it.
> 
> I really hope AMD steps up their ML game, not only with device support but also documentation and ecosystem integration.

Yes yes...
While all the NVIDIA card's prices are rocketing high, the XT 6900 's price is going down. Guess AMD got their dev priorities upside down.

---

### 评论 #19 — powderluv (2022-04-19T17:46:27Z)

> @powderluv [The docs for v5.1.1](https://docs.amd.com/bundle/ROCm-Getting-Started-Guide-v5.1.1/page/Overview_of_ROCm_Installation.html) doesn't mention the 6900XT being supported, can you confirm if v5.1.1 will work or are you talking about some upcoming release?

Yes I was able to run the latest ROCm on my 6900XT but your mileage may vary if it isn't listed in the official documentation. I would give it a try. 

---

### 评论 #20 — joaomamede (2022-08-30T00:22:46Z)

If AMD wants to have this go, they can always support opencl and the problem is fixed as well.

---
