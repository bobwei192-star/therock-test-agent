# Q: What is status of ROCm on RX 5700/XT?

> **Issue #819**
> **状态**: closed
> **创建时间**: 2019-06-12T01:01:10Z
> **更新时间**: 2020-05-21T08:42:49Z
> **关闭时间**: 2019-06-17T15:24:07Z
> **作者**: emerth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/819

## 描述

Hello!

What is the status of ROCm on the new RX 5700 & RX 5700XT video cards?

Thanks!

And thanks for making ROCm!

---

## 评论 (17 条)

### 评论 #1 — emerth (2019-06-17T15:19:07Z)

Hi Kent, I don't have the IDs. All I have is pci.ids also. It' OK, we will learn more when the cards hit the shelves.

---

### 评论 #2 — kentrussell (2019-06-17T15:24:07Z)

ROCm doesn't have support for the RX5700 series of cards yet, but since the cards aren't being released until July 7th (https://www.amd.com/en/products/graphics/amd-radeon-rx-5700 under "General") , that's not a concern. Keep watching for support for these GPUs via https://github.com/RadeonOpenCompute/ROCm#supported-gpus . Once we support it, we'll add it to the list :)

---

### 评论 #3 — oscarbg (2019-08-06T05:41:55Z)

would be nice to know what expected version ROCM 2.7? ROCM 3.x?

---

### 评论 #4 — tmielika (2019-09-14T19:09:52Z)

No support yet?

---

### 评论 #5 — kentrussell (2019-09-16T11:30:23Z)

Sorry, I should've updated this previously. We have full compute support for Navi10 (Radeon 5700 and 5700XT) as of 2.7. We don't have **display** capabilities yet (in 2.7 or 2.8) due to some issues with the display code, so we had to disable display to allow the GPU to work with our ROCm stack. We are aiming to get full display support for Navi10 to go with the already-present full compute capabilities in the 2.9 release. 

---

### 评论 #6 — emerth (2019-09-16T16:34:17Z)

Hi Kent, thanks for the update. 

Just to verify my understanding: an RX 5700/XT will run compute jobs under ROCm but cannot yet produce video output; thus I could use 5700/XT in a headless compute machine or install a different card alongside a 5700/XT if video out is required.

Is this correct?

---

### 评论 #7 — kentrussell (2019-09-16T17:13:41Z)

I should clarify that **_initial_** support is in the kernel for RX5700/XT. I don't know what the status is on the runtime and OCL, and we haven't officially said that it's supported yet (so there may be some bugs still), but I was speaking specifically from the kernel/firmware perspective, 

I should have said that first. Sorry for any confusion that I may have caused. Right now, I don't have  the official timeline for RX5700 support. While the parts are in the kernel (ROCk/SMI), there is likely still some debugging to take place for the kernel driver, and the runtime and official ROCm support isn't confirmed as of yet but definitely isn't there yet. But feel free to try things out and let us know about any bugs that you might find, it will help us to get things working sooner :)

---

### 评论 #8 — emerth (2019-09-16T21:05:33Z)

OK, that's cool. Thanks for the details, Kent. Are the ROCm devs aiming for RX5800/RX5800 launch day support, by any chance? I know that for compute the 5700 would be OK, but really at this point a VII or Vega 64 makes more sense. I'm guessing "big Navi" will be more powerful for FP32 at least.

---

### 评论 #9 — kentrussell (2019-09-18T22:07:45Z)

I don't have any specifics unfortunately. Plus, they likely wouldn't want to give out firm deadlines in case things slip, or if we push the date up and release things earlier. We've always got to consider the amount of work that it takes to get the basic (amdgpu) support in the kernel, then the compute kernel (amdkfd) support, and ironing out those bugs as the runtime is brought up, then finally getting to performance testing instead of just basic functionality, which always makes it tougher than giving basic Display or kernel functionality, which tends to come along pretty early on.

I'd love to give you an answer, but all I can say is to watch the "Supported Hardware" listing in the ROCm documentation. Anything outside of that list is considered to be _unsupported_. But bear in mind that some things might just not be confirmed. The kernel will have support for new chips pretty quickly, since that gets brought in by the amdgpu and amdkfd components. The thunk (ROCT)  is usually pretty quick to follow along there (and is usually pretty stable unless some new hardware features need to be considered), and the SMI is just a layer to interface with the sysfs files, so that's under kernel support. But once you get beyond that, you're looking at the runtime, which is where support for the hardware gets dicier. So even if something isn't in the "Supported Hardware" list, it may have some limited functionality. And since it's all open-sourced, we always invite help from the ROCm community to help to bring these ASICs along.

---

### 评论 #10 — anthqiu (2019-10-19T08:56:27Z)

Are there any further update on supporing navi cards? I'm really looking foward to run some computation on my RX 5700~

---

### 评论 #11 — omerferhatt (2019-10-30T14:30:46Z)

Is there any update about RX 5700XT ROCm driver

---

### 评论 #12 — soutzis (2020-05-20T21:41:52Z)

I understand that over the past year or so, there has been some fuss about Navi10 support in ROCm. While we can see that it is not yet officially supported, is there an estimate? I purchased this card a month ago with the intention on working on ML projects, as well as gaming, but I (wrongly) assumed that almost a year after the launch of RX 5700/XT the support would already be there. However, if support is expected in the coming ~2 months, then I would keep this card. If you could also let us know that support won't be here for a year or so (or never?!?), then I would return it to get a more suitable alternative (e.g. Radeon VII).
So, is there any chance you'll let us know about your plans regarding RX 5700 XT and ROCm? Is anybody working on it? Is the card's architecture inherently unsuitable for deep learning?

---

### 评论 #13 — Degerz (2020-05-21T07:23:42Z)

@soutzis I recommend you acquiring a Radeon VII or even better which is the Radeon Instinct MI100 (gfx908) ...

There's no telling when AMD's ML libraries or their HCC compiler will support GFX10/RDNA's instruction encoding. A lot of AMD's ML libraries use hand optimized assembly that's only compatible with GFX8/GFX9 GPUs ... 

---

### 评论 #14 — soutzis (2020-05-21T07:29:57Z)

@Degerz Thanks. I will give the GFX10 1-2 more months, otherwise I will have to go back to NVidia. The black screen driver issues haven't helped me love this card much so far.

---

### 评论 #15 — Degerz (2020-05-21T08:07:20Z)

@soutzis I don't think waiting will be necessary ... 

AMD doesn't plan on adding GFX10 support for their HCC [compiler](https://github.com/RadeonOpenCompute/hcc/blob/clang_tot_upgrade/CMakeLists.txt) until maybe after 2022 ? That's assuming that AMD's strategy will change and they go back to reconverging and maintaining a single unified family of architectures again ...

I imagine that their next generation CDNA 2 GPU will be based on gfx910. The safest bet IMO so far is the MI100 in which you can expect 5 years of quality support from AMD with the entire software stack but the next best thing is a Radeon VII if you're looking for the best possible support out of a regular consumer GPU ...

---

### 评论 #16 — soutzis (2020-05-21T08:12:38Z)

@Degerz I see. Thanks for your insight. 
Hopefully, I hope that in time everything will go well for AMD, so they can hire more people to work on software.

---

### 评论 #17 — Degerz (2020-05-21T08:42:48Z)

@soutzis TBH, AMD's software support for more HW is contingent on their strategy rather than the size of their software team ... 

AMD could drop supporting GFX9 GPUs altogether tomorrow and start redeveloping their entire software stack based around GFX10 GPUs with lower performance than they had originally envisioned ... 

Or they could maintain and release new products based on the GFX9 architecture so that they can avoid rewriting huge parts of their software stack and they can optimize their HW design for even better performance on compute applications compared to GFX10 based HW. I can see why AMD would vastly prefer this path even though the community here wouldn't like it. I do wish that if AMD were committing to this route that they would at least release some cheap compute accelerator SKUs under $1000 so that there could still be a widespread option to do work or develop on their platform ...

If the worst comes to pass then the community could just add HCC compiler support for GFX10 GPUs and start porting AMD's ML libraries if they want to get either Tensorflow or PyTorch up and running since all of this is open source ...

---
