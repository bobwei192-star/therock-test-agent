# Does ROCm support Tonga?

> **Issue #509**
> **状态**: closed
> **创建时间**: 2018-08-22T19:25:03Z
> **更新时间**: 2019-03-15T09:33:15Z
> **关闭时间**: 2019-03-15T09:32:39Z
> **作者**: JMadgwick
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/509

## 标签

- **Question** (颜色: #cc317c)

## 描述

I'm writing about ROCm in the context of GPU compute languages and putting together tables of GPUs and the degree of support.
It says [here](https://llvm.org/docs/AMDGPUUsage.html#processors) that there is support for Tonga (R9 285, R9 385, R9 380 and some FirePros). But I can't find any mention of this on the ROCm github. Is Tonga actually supported?
As far as the level of support goes, am I right that because the tensorflow port only supports gfx803, 900 and 906(whats that?) anything older than gfx803 lacks instructions and so is only experimental like the support for Hawaii?

---

## 评论 (23 条)

### 评论 #1 — jlgreathouse (2018-08-22T21:58:29Z)

We should support Tonga. It has support in the [KFD](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.8.x/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L269), is enumerated by [rocm_agent_enumerator](https://github.com/RadeonOpenCompute/rocminfo/blob/0b5ccf90fa8824fde9b8f889e0904f89234ed3c3/rocm_agent_enumerator#L19), and (as you point out) it is supported in LLVM (which we use as the base for our kernel compilers for HIP, HCC, and OpenCL).

That said, I don't have a Tonga GPU on hand to verify this at the moment -- sorry, my desk is pretty full with the systems for Hawaii, Polaris 10, Fiji, and Vega 10. :)  I can try finding one and testing it, but it may be a while before I can do so.

It may be the case that our HCC/HIP compiler does not target gfx802 by default. In that case, you can force it to target gfx802, as [described on this page](https://github.com/RadeonOpenCompute/hcc/wiki#compiling-for-different-gpu-architectures), by setting `--amdgpu-target=gfx802`

I believe that our MIOpen framework does not include support for optimized (e.g. hand-written) kernels for gfx802. That said, so long as HIP and the OpenCL compilers properly target gfx802, MIOpen (and TensorFlow built with MIOpen) should work. Emphasis on "should", because I don't think this is a target we rigorously test.

---

### 评论 #2 — Sixkplus (2018-08-23T14:02:18Z)

I'm wondering whether ROCm can be used on R9 380/380X?

It seems that 380/380X are Antigua XT/Pro(Tonga XT/Pro)

So, according to your answer, it's still not supported, right?

A little shame  : (.

By the way, have you test the compatibility for Hawaii? I'm also curious whether 290(X)/390(X) are supported.

---

### 评论 #3 — gstoner (2018-08-23T14:16:21Z)

The shame was when we trying to bring that hardware there was hardware bug we could not work around for ROCm stack. Fiji base GPU was the first real GPU we supported with ROCm.   FIJI has the Most Development and testing time on it.  Then RX480/RX470, Vega10 cards. 

The shame was Minner drove the price sky high on Polaris cards, since originally we also supported RX480 and RX470,  should be starting to get those card for the small money.  

Now if you can find used FIji Nano for Compute that will blow the doors it @  8.19 TFlops and we saw up to 8 GB HBM  470 GB/s memory bandwidth off it and less power.   a Tonga ( 285)  was 3.2 flops 2 GB of memory  176 GB/s  of memory bandwidth peak.  

For Tonga, we really recommend the AMDGPUpro driver which fully support since it use more limited foundation via ORCA with OpenCL.

---

### 评论 #4 — jlgreathouse (2018-08-23T14:17:11Z)

Hi @Sixkplus 

I believe the answer to your question about the Radeon R9 380/380X GPUs should be identical to the response above -- as far as the ROCm stack is concerned, Tonga is Tonga. In other words, It should be supported in ROCm, (again, I haven't tested this myself recently), but our MIOpen framework may not have hand-optimized kernels in place for it.

As for Hawaii: Support for Hawaii (gfx7) is experimental. I do have one at my desk, and it does work for all the tests I run on it. That said, I don't think MIOpen is built to work on Hawaii.

---

### 评论 #5 — Sixkplus (2018-08-24T02:38:46Z)

THX, @jlgreathouse 
I think it's better for you guys to list the supported GPUs in a clearer way on ROCm website. Now, it seems that the supported devices mentioned on [this page](https://rocm.github.io/ROCmInstall.html) are more about CPUs and PCIE ports. 




---

### 评论 #6 — JMadgwick (2018-08-27T18:02:06Z)

A user [here](https://github.com/RadeonOpenCompute/hcc/issues/810) couldn't get Tonga working. I can also confirm that Tonga is not supported (at least by HCC). This is easily confirmed by trying to target Tonga with `--amdgpu-target=gfx802` when compiling.
The result is:
`clang-8: warning: -amdgpu-target argument 'gfx802' is not recognized; using gfx803 instead [-Winvalid-command-line-argument]`
If it can't be targeted then I don't see how it can be supported.

As was pointed out on that other issue, [this](https://github.com/RadeonOpenCompute/hcc-clang-upgrade/blob/be6eeeeffb62557a79a6b559b7b633fb29e5d8e4/lib/Driver/ToolChains/Hcc.cpp#L311) seems to be the conclusive list of supported GPUs for HCC. Even though LLVM lists others.
Hawaii, Fiji and Vega. **Nothing else**. Documentation should be clearer as it looks like its all there in the code.

---

### 评论 #7 — gstoner (2018-08-30T04:26:25Z)

@JMadgwick are you using Tonga because Polaris was too much money  I see your student.  Due Bitcoin craze on GPUs

---

### 评论 #8 — rkothako (2018-08-31T03:58:48Z)

Hi @jlgreathouse 
We may need to make **clear** the documentation with list of asics supported.
Looks like still some confusion is there and so we need to address it.
Please update the Rocm wiki.
Thank you.

---

### 评论 #9 — ruc98 (2018-09-14T10:26:53Z)

I have this GPU: Sun XT [Radeon HD 8670A/8670M/8690M / R5 M330 / M430 / R7 M520].
Do you think ROCm supports my GPU?

---

### 评论 #10 — kentrussell (2018-09-14T12:16:41Z)

@Rahulchakwate ROCm doesn't support GFX6, which is what Sun XT is. 
@rkothako There is a description at https://rocm.github.io/ROCmInstall.html discussing supported GFX versions but it's not blatantly listed out. This could probably be clarified

---

### 评论 #11 — JMadgwick (2018-09-14T12:49:56Z)

It's not as simple as GFX7,8,9 is supported. If you try to use something other than [gfx701,gfx803, gfx900,gfx906](https://github.com/RadeonOpenCompute/hcc-clang-upgrade/blob/clang_tot_upgrade/lib/Driver/ToolChains/Hcc.cpp#L229) then you can't compile anything as those are the only valid targets in HCC. I put together a quick list of what was supported when writing on [my blog](http://madgwick.xyz/quick-look-at-compute-languages.php). I don't think it's too much to ask to have a small table on the readme with a conclusive list of exactly what is supported.

---

### 评论 #12 — kentrussell (2018-09-14T13:21:35Z)

I don't disagree. I oversimplified for the GFX6 issue, but I agree with you there. 

Regarding HCC's support and lack of support for gfx802 (Tonga), their documentation clearly lists gfx802 as an option (and no Vega*). There have been discussions explicitly discussing documentation updating, so I'll make sure that this is brought up as a friendly reminder for teams to actually update their documentation to be current and accurate (it's why we dropped the README.md from ROCK, since it wasn't providing any useful information beyond what ROCm documentation provides)

As for the supported list for rocm.github.io, that's an issue all unto itself. It's doable, but it's complicated due to different components supporting different hardware. ROCK/ROCT/ROCR supports the GFX7/8/9 APUs (Kaveri/Carrizo/Raven) and GFX7/8/9 GPUs (Hawaii, Tonga, Polaris10, Polaris11, Fiji, Vega10, Vega12, Vega20), while HCC doesn't support any APUs and only supports Hawaii, Fiji, Polaris10, Vega10 and Vega20, while HIP supports Carrizo, but not Kaveri or Raven. It might be worth trying a greatest-common-denominator approach, but that might exclude some use-cases. e.g. If you have a Raven and only want to run OpenCL, you'd be fine, but our supported list wouldn't have that. It's something that could definitely use clarification though.

---

### 评论 #13 — jlgreathouse (2018-09-14T15:49:16Z)

@JMadgwick Your request is appreciated, and I agree. We are working to get together an officially sanctioned list of exactly what we support and what parts should work but are not officially supported.

As @kentrussell describes -- the situation is a bit more complex than just a simple table. Especially because there are components that _should_ work with particular devices, but which ROCm will not claim official support for, and which are no longer actively tested. In addition, there are some products with "supported" ASICs but where we do not support particular boards due to platform limitations.

---

### 评论 #14 — JMadgwick (2018-09-15T16:42:56Z)

@jlgreathouse The updated documentation is far better, hopefully by explicitly mentioning all the supported and some of the not so obviously unsupported chips, this sort of issue will stop coming up.
Even earlier today (before the readme was updated) there was a confused user posting on the [Phoronix forums](https://www.phoronix.com/forums/forum/phoronix/latest-phoronix-articles/1047471-amd-rocm-1-9-available-with-vega-20-support-plus-upstream-kernel-compatibility?p=1047489#post1047489) asking if Tonga was supported after reading the [Phoronix news post about ROCm 1.9 release](https://www.phoronix.com/scan.php?page=news_item&px=AMD-ROCm-1.9-Released).

My only question now is am I right in thinking that[ this pull request](https://github.com/RadeonOpenCompute/hcc-clang-upgrade/pull/149) adds support for Tonga (and others) to HCC and thus in future, if it is merged, ROCm will be closer to experimentally supporting Tonga? Or is this unrelated and Tonga support is something which will never be added?

I think this and the other Tonga related issue on the HCC repo could be closed now as the answer has been found and is now included in the documentation.

---

### 评论 #15 — jlgreathouse (2018-09-15T18:41:15Z)

Hi @JMadgwick 

You can find more information about our Tonga support/non-support in the [more detailed hardware page at rocm.github.io](https://rocm.github.io/hardware.html).

In particular, there is a bug in the Thunk that prevents Tonga from running in a stable manner. As such, the HCC compiler group decided to remove support for gfx802, since not only was it not on our official to-support list, but they were unable to test any of their changes since they could not run applications in a stable manner.

Because many of our projects rely on HCC, other projects also removed support for gfx802 since they couldn't compile for it. This includes HIP and most of our libraries.

That said, we have a patchset under test internally right now since this GitHub issue piqued some interest. I've been able to run Tonga on ROCm 1.8 over a bunch of test applications after applying these patches. We need to port it to 1.9, and then maybe we can post it here so that anyone who uses Tonga can try to build their own "custom" ROCm that may work with their GPU. That's why I've left this issue open -- and it's also one of the benefits of open source code, IMO. :)

Longer term, I don't know if that patchset would make it into all of the projects. Because ROCm does not officially support Tonga, some projects may want to avoid adding support for it to avoid polling their code or adding complexity. I can't speak for them at this time. But yes, if all of these patches were accepted, we would likely move Tonga into the "not officially supported, but should work" category, like Hawaii.

---

### 评论 #16 — jlgreathouse (2018-09-15T18:43:59Z)

With respect to that Phoronix question (I'll try to reply directly there if I have time) -- I'll note that even if we  got Tonga working, it would still require PCIe atomics. This is a requirement on all gfx8 GPUs, including Tonga, Fiji, Polaris 10, and Polaris 11. That user is asking about running Tonga on an FX CPU over PCIe 2.0. Even with the patches I describe above, that setup would not work.

---

### 评论 #17 — timdorohin (2018-09-20T00:14:46Z)

When GFX7 support appeared, i started to wonder about GFX6 support. Is it possible (in theory)?

---

### 评论 #18 — jlgreathouse (2018-09-20T00:20:38Z)

AMD has no plans to add gfx6 support into the ROCm software stack. gfx6 hardware is lacking some fundamental internal mechanisms we need for our software to interface to the GPU. Getting "ROCm" working on gfx6 would involve enough changes that it wouldn't be "ROCm" anymore.

---

### 评论 #19 — smokhov (2019-02-27T17:43:37Z)

@jlgreathouse -- where we can find your patchset you've been working on? We'd like to have it tested in our environment.

---

### 评论 #20 — smokhov (2019-02-27T17:45:00Z)

... also from #720 -- anyone has a list of existing, popular or not, frameworks, libraries, or tools, outside of ROCc that work with Tonga FirePro S7100X GPUs? We have 5 we'd like to get them used.

---

### 评论 #21 — JMadgwick (2019-02-27T18:04:44Z)

> ... also from #720 -- anyone has a list of existing, popular or not, frameworks, libraries, or tools, outside of ROCc that work with Tonga FirePro S7100X GPUs? We have 5 we'd like to get them used.

As far as I know you can use anything that supports OpenCL and you can get that working without needing ROCm. [Just use the closed source AMD drivers instead of ROCm (they do support Tonga).](https://www.amd.com/en/support/professional-graphics/firepro/firepro-s-series/firepro-s7100x)
With working OpenCL you [might be able to use this guide](https://developer.codeplay.com/computecppce/latest/getting-started-with-tensorflow) to install an OpenCL SYCL based version of **Tensorflow**. I haven't tried it but it looks like it's relatively current. Might be better than Nothing?

Edit: This method is not viable. See closing comment.


---

### 评论 #22 — smokhov (2019-02-27T18:09:44Z)

@JMadgwick -- thanks! I'll have a look. And @jlgreathouse -- would also like to test that patchset if possible if you guys posted it somewhere.

---

### 评论 #23 — JMadgwick (2019-03-15T09:32:39Z)

I've been researching this a bit more and so please ignore my last comment. That SYCL based Tensorflow I linked requires [SPIR which is no longer/was never supported by AMD](https://community.amd.com/thread/232093) and no longer exists in current drivers.
So if your GPU configuration is not **fully** supported by ROCm then you cannot and will almost certainly never be able to use Tensorflow on your GPU.

### With the exception of Tonga(_gfx802_) all AMD GPUs since 2015 are supported by ROCm and will work with Tensorflow and everything else ROCm offers.
Hawaii GPUs from 2013 were _experimentally_ supported but this never included support for any of the machine learning components and as of [Rocm 2.0 Hawaii no longer works correctly if at all](https://github.com/RadeonOpenCompute/ROCm/issues/691).

Therefore:
Does ROCm support Tonga? **No**
Will ROCm support Tonga? This issue has been around for 6 months and there is no news. Tonga is now 5 years old and no longer in production on sale so. **It does not seem likely** it will ever be supported so this issue should now be closed as the question has been _implicitly_ answered.

---
