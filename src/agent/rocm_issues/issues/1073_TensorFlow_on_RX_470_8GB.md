# TensorFlow on RX 470 8GB

> **Issue #1073**
> **状态**: closed
> **创建时间**: 2020-04-04T19:53:04Z
> **更新时间**: 2021-04-05T10:04:29Z
> **关闭时间**: 2021-04-05T10:04:29Z
> **作者**: bimonsubio1984
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1073

## 描述

Hello,

Please let me know:

Does RX 470 8GB card work fine with ROCm? Are there any differences compared to RX 580 except 25% drop in performance? Architectures of RX 470 and RX 580 look almost the same IMHO, though only RX 580 is mentioned as supported on ROCm page.

Except mining I would like to learn and experiment with TensorFlow on RX 470 8GB card, is it possible? Are there any limitations of RX 470 when using with TensorFlow+ROCm compared to RX 580 or may be RX 470 will not work at all (doubtfully)?

---

## 评论 (5 条)

### 评论 #1 — Bengt (2020-04-06T01:57:26Z)

Hi, @bimonsubio1984!

You are probably looking for the tensorflow rocm issue tracker:

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/

The cards you mentioned all use the GFX803 ISA on which Tensorflow runs buggy at best. For more details see:

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479

Personally, I ended up buying Vega GPUs. Those work fine with tensorflow, so maybe do so, too.

---

### 评论 #2 — bimonsubio1984 (2020-04-06T06:48:16Z)

Dear Bengt,

Please suggest which models/manufacturers of Vega are the most problem free, cool, cold and quiet?

As for RX 4xx/5xx cards I guess it was Sapphire Nitro+ ? 

Is Vega 56 OK or need Vega 64?

---

### 评论 #3 — Bengt (2020-04-06T18:39:35Z)

Sorry, I don't know that much about the aftermarket cards. Please do your own research on that.

I trusted Buildzoid with his VRM analysis of the reference Vega 64/56. Since the VRM on those is quite over built, I got a Vega 64 and put it under custom water using a core-only water block as my primary card. the next two are Vega 64 Liquid, which is a bit more noisy and the fourth one is a stock Vega 64 reference blower card, which is noisier still. I have another core-only water block to put on it, but in my experience machine learning rarely hits the cards so hard that the fan kicks up to annoying levels, so I haven't bothered with that. After all, modifying the base plate to fit a core-only water block and all the other mods needed to make this work take about a day, so that time investment needs to pay for itself.

I have no experience with Vega 56 compared to Vega 64 for machine learning. I figured, used Vega 64 would be more financially attractive, because the high-end variant has a more stable resell value. But again, your priorities may be different, so please make up your own mind about that.

You should be able to flash a Vega 64 BIOS onto a Vega 56 card which raises the memory bandwidth to the same levels. So if that limits in your use case, a flashed Vega 56 might be almost as fast as Vega 64.

---

### 评论 #4 — Laser-Cat (2020-05-12T02:59:15Z)

Tf 1.15.2 works with my rx 470 4G card. You may or may not need to meddle with the tensorflow code abit. My workload involves inference with C API and it looks okay to me, not sure about training tho.


---

### 评论 #5 — ROCmSupport (2021-04-05T10:04:29Z)

Thanks @bimonsubio1984 for reaching out.
ROCm does not support gfx8 devices anymore. Please follow our documentation for more details.
Thank you.

---
