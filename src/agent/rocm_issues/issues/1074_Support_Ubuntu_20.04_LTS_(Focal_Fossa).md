# Support Ubuntu 20.04 LTS (Focal Fossa)

> **Issue #1074**
> **状态**: closed
> **创建时间**: 2020-04-06T01:49:31Z
> **更新时间**: 2020-10-25T15:56:21Z
> **关闭时间**: 2020-08-23T18:07:44Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1074

## 描述

ROCm should support Ubuntu 20.04 since it is the next release with long-term support (LTS) of this Linux distribution, following the currently-supported 16.04 and 18.04 LTS. The Ubuntu 20.04 Beta has just come out, so now is a good time to start testing with that version, before it gets released on April 23rd:

https://wiki.ubuntu.com/FocalFossa/ReleaseSchedule

---

## 评论 (54 条)

### 评论 #1 — Danny3 (2020-04-09T12:01:32Z)

This would be great and very much needed.
Also it would be amazing if the installer would not break if we manually update the kernel to the current one (5.6).

---

### 评论 #2 — Bengt (2020-04-17T02:26:16Z)

The release candidate should have been out by now:

http://releases.ubuntu.com/20.04/

---

### 评论 #3 — witeko (2020-04-17T10:51:32Z)

@Bengt I think since yesterday You can now install rocm in ubuntu 20.04

---

### 评论 #4 — witeko (2020-04-19T05:55:15Z)

@han-minhee you can install the rocm. Some things work (like rocm smi), some things don't (like tensorflow). 

---

### 评论 #5 — witeko (2020-04-19T13:42:23Z)

@han-minhee i dont know whats the root cause, tensorflow doesnt build, the whl package from pypi "crashes" (produces errors) when using.
If You can provide sth easy to check (if it works), I can check it for You. :)

---

### 评论 #6 — Bengt (2020-04-20T10:16:35Z)

@witeko You can avoid building TensorFlow yourself by using a wheel package of tensorflow-rocm:

https://pypi.org/project/tensorflow-rocm/#files

To verify ROCm can run TensorFlow  as intended, please run a simple payload like this one:

https://gist.github.com/Bengt/c5d5c45506339f234f6d7a9a13d23ba3

---

### 评论 #7 — witeko (2020-04-20T23:01:56Z)

@Bengt first you need to install libncurses5 (6 is not enough) [not listed in: https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-install-basic.md]
After that I get:
2020-04-21 00:50:14.817784: E tensorflow/stream_executor/rocm/rocm_driver.cc:975] could not retrieve ROCM device count: HIP_ERROR_NoDevice

rocm-smi seems to be working fine.



---

### 评论 #8 — Bengt (2020-04-21T13:32:33Z)

@witeko Thanks for testing this. Interesting to know that the rocm driver does not recognise the GPUs, although rocm-smi has no issues with that.

---

### 评论 #9 — Goddard (2020-04-23T22:41:10Z)

This will land in http://repo.radeon.com/rocm/apt/debian focal Release  soon?

---

### 评论 #10 — witeko (2020-04-24T20:07:21Z)

Seems like you can run tensorflow using docker in 20.04
@Bengt 

---

### 评论 #11 — agners (2020-04-26T13:18:31Z)

Probably expected, but just wanted to note: Installing the xenial packages currently fails when trying to install `rocm-dkms`:

```
/var/lib/dkms/amdgpu/3.3-19/build/amd/amdgpu/../backport/kcl_mmu_notifier.c:7:32: error: dereferencing pointer to incomplete type ‘struct mmu_notifier_mm’
    7 |  spin_lock(&mm->mmu_notifier_mm->lock);
      |                                ^~
make[2]: *** [scripts/Makefile.build:265: 
```

---

### 评论 #12 — chaoji90 (2020-05-10T04:36:40Z)

I got this when I tried to use the tf
2020-05-10 12:24:20.926812: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-05-10 12:24:20.982479: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:03:00.0 name: Vega 10 XL/XT [Radeon RX Vega 56/64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.59GHz coreCount: 56 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-05-10 12:24:21.020605: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-10 12:24:21.021757: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-10 12:24:21.024344: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-10 12:24:21.024556: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-10 12:24:21.024624: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-10 12:24:21.024894: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX
2020-05-10 12:24:21.031167: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3411120000 Hz
2020-05-10 12:24:21.031533: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x86a0570 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-10 12:24:21.031555: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-05-10 12:24:21.032908: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x8708d60 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-05-10 12:24:21.032932: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Vega 10 XL/XT [Radeon RX Vega 56/64], AMDGPU ISA version: gfx900
2020-05-10 12:24:21.033075: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:03:00.0 name: Vega 10 XL/XT [Radeon RX Vega 56/64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.59GHz coreCount: 56 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-05-10 12:24:21.033109: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-10 12:24:21.033125: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-10 12:24:21.033140: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-10 12:24:21.033153: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-10 12:24:21.033188: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-10 12:24:21.033206: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-05-10 12:24:21.033214: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2020-05-10 12:24:21.033220: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2020-05-10 12:24:21.033282: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7444 MB memory) -> physical GPU (device: 0, name: Vega 10 XL/XT [Radeon RX Vega 56/64], pci bus id: 0000:03:00.0)
2020-05-10 12:24:27.770244: E tensorflow/stream_executor/rocm/rocm_event.cc:28] Error polling for event status: failed to query event: hipError_t(600)
2020-05-10 12:24:27.770282: F tensorflow/core/common_runtime/gpu/gpu_event_mgr.cc:273] Unexpected Event status: 1


---

### 评论 #13 — chaoji90 (2020-05-10T04:37:52Z)

Nothing seemed wrong with rocm.
rocminfo and clinfo both work fine.


---

### 评论 #14 — bastibe (2020-05-11T11:54:32Z)

Indeed, rocm now seems to work on my Kubuntu 20.04 Vega M GH install as well, but didn't last week.

---

### 评论 #15 — showlabor (2020-05-11T19:54:28Z)

> 2020-05-10 12:24:27.770244: E tensorflow/stream_executor/rocm/rocm_event.cc:28] Error polling for event status: failed to query event: hipError_t(600)
> 2020-05-10 12:24:27.770282: F tensorflow/core/common_runtime/gpu/gpu_event_mgr.cc:273] Unexpected Event status: 1

I'm trying to get tensorflow-rocm working on Fedora 32 with a RX580 card. I'm getting the same error with any example or getting started tutorial. The simplest way I have found to trigger it is to use tf.divide(x, y).


---

### 评论 #16 — Szalacinski (2020-05-11T21:10:17Z)

Same issue here.

This may just be a HIP/TF issue, because OpenCL applications like Luxmark 4 seem to work just fine.

Edit: Blender also doesn't work, and causes severe graphical corruption in Gnome.

```
2020-05-11 15:59:47.946973: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-05-11 15:59:48.023615: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:05:00.0 name: Vega 10 XTX [Radeon Vega Frontier Edition]     ROCm AMD GPU ISA: gfx900
coreClock: 1.6GHz coreCount: 64 deviceMemorySize: 15.98GiB deviceMemoryBandwidth: -1B/s
2020-05-11 15:59:48.076894: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-11 15:59:48.078867: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-11 15:59:48.082346: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-11 15:59:48.082654: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-11 15:59:48.082764: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-11 15:59:48.083216: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX
2020-05-11 15:59:48.098908: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 2100085000 Hz
2020-05-11 15:59:48.100206: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5d78d90 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-11 15:59:48.100237: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-05-11 15:59:48.102324: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5de1cb0 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-05-11 15:59:48.102361: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Vega 10 XTX [Radeon Vega Frontier Edition], AMDGPU ISA version: gfx900
2020-05-11 15:59:48.102602: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:05:00.0 name: Vega 10 XTX [Radeon Vega Frontier Edition]     ROCm AMD GPU ISA: gfx900
coreClock: 1.6GHz coreCount: 64 deviceMemorySize: 15.98GiB deviceMemoryBandwidth: -1B/s
2020-05-11 15:59:48.102648: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-11 15:59:48.102677: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-11 15:59:48.102703: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-11 15:59:48.102729: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-11 15:59:48.102801: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-11 15:59:48.102830: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-05-11 15:59:48.102847: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2020-05-11 15:59:48.102863: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2020-05-11 15:59:48.102988: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 15145 MB memory) -> physical GPU (device: 0, name: Vega 10 XTX [Radeon Vega Frontier Edition], pci bus id: 0000:05:00.0)
2020-05-11 16:00:01.563183: E tensorflow/stream_executor/rocm/rocm_event.cc:28] Error polling for event status: failed to query event: hipError_t(600)
2020-05-11 16:00:01.563273: F tensorflow/core/common_runtime/gpu/gpu_event_mgr.cc:273] Unexpected Event status: 1
```


---

### 评论 #17 — chaoji90 (2020-05-12T08:31:37Z)

> > 2020-05-10 12:24:27.770244: E tensorflow/stream_executor/rocm/rocm_event.cc:28] Error polling for event status: failed to query event: hipError_t(600)
> > 2020-05-10 12:24:27.770282: F tensorflow/core/common_runtime/gpu/gpu_event_mgr.cc:273] Unexpected Event status: 1
> 
> I'm trying to get tensorflow-rocm working on Fedora 32 with a RX580 card. I'm getting the same error with any example or getting started tutorial. The simplest way I have found to trigger it is to use tf.divide(x, y).

I changed back to 19.10 with the kernel version 5.3, then everything worked fine. But I cannot confirm ed if it was the problem with kernel.

---

### 评论 #18 — showlabor (2020-05-12T09:27:04Z)

On my Fedora 32 system using a 5.3.0 kernel does not make any difference. Tried with both the kernel module and the rocm-dkms module. 

---

### 评论 #19 — BloodyIron (2020-05-25T00:23:36Z)

Really getting fed up with ROCM taking months to work on major Ubuntu releases. That's literally why the beta program is there, so devs can test and release on-time. Like the #1 reason I'm not upgrading from 19.10 to 20.04 is because I need OpenCL for DaVinci Resolve and upgrading to 20.04 breaks that.

Get with it AMD!

---

### 评论 #20 — witeko (2020-05-25T09:18:32Z)

@BloodyIron https://www.youtube.com/watch?v=efKjfBkjPlM

---

### 评论 #21 — Goddard (2020-05-25T14:36:45Z)

> @BloodyIron https://www.youtube.com/watch?v=efKjfBkjPlM

It only works if you have 1 opencl agent.  If you have more it fails.  Also many things crash when using opencl with DaVinci Resolve right now.  The person in the video doesn't show any operations either.  Just because the little green check box shows up doesn't mean it works.

The first point release has already been released.  That means all Ubuntu LTS systems can be upgraded to the next LTS.  I expect many more people will run into compatibility issues because of the slow updating.

I hope AMD keeps up the good work, but I must admit these updates should be faster in my humble opinion.

Anyone who uses Ubuntu as their workstation and wants to work on machine learning tasks it is impossible right now.

---

### 评论 #22 — BloodyIron (2020-05-25T14:44:12Z)

I don't get it, the video shows effectively what looks like the normal steps to get up and running, but when I check the readme.md for this repo it only reports Ubuntu 18.04 and Linux 5.3, but not 5.4. So it _looks_ like the repo he used (the normal ones?) serves up the necessary aspects for Linux 5.4, so is it just that the readme.md is out of date or what?

I don't see what he did that's special. Am I missing something here?

Also, what do you mean @Goddard about that only works if you have 1 opencl agent? Are his steps special? And I'm not even sure what you mean by "opencl agent", what's that all about?

When you say many things crash with opencl with DaVinci Resolve, do you mean in Ubuntu 20.04, or the latest ROCM drivers that I myself would be using right now? (I'm on Ubuntu 19.10) I haven't used DaVinci Resolve too hard in recent days, I'm trying to keep it operational for upcoming stuff.

---

### 评论 #23 — Goddard (2020-05-25T14:59:36Z)

The guy in the video does nothing special.  He just follows the documentation.

In Ubuntu you can install debs for a different version.  That is all that is happening here.

Official support for Ubuntu 20.04 hasn't landed yet and if you installed with the method they guy shows in the video you would be disappointed because many things do not work properly.  

By multiple agents I mean more then 1 graphics card, or using CPU and GPU at once.

---

### 评论 #24 — BloodyIron (2020-06-11T00:49:35Z)

So it's now June, and 20.04 has been out for several months now. WHEN will this support 20.04? I haven't seen any responses to this issue.

---

### 评论 #25 — BloodyIron (2020-07-06T18:49:49Z)

Okay now it's JULY and still no 20.04 support. I'm now going to seriously consider switching to nVidia for my next GPU if this kind of garbage LTS support continues. 20.04 support should have been ready for at LEAST release date of Ubuntu 20.04. Having to wait so long for something related to actual productivity purposes is unacceptable. Get it together AMD.

---

### 评论 #26 — bastibe (2020-07-07T06:53:06Z)

It works just fine as is on my 20.04. Have you tried installing it on yours?

---

### 评论 #27 — Bengt (2020-07-07T09:40:04Z)

@bastibe Thanks for your testing. It is great that ROCm can run under Ubuntu 20.04. However, I would rather have an official word of support from AMD, because I trust the software provider to validate more thoroughly than any end user ever could. I actually think it is a good sign that AMD has not yet declared Ubuntu 20.04 support, because that hints at them working on remaining issues, that we don't know about. I would like these issues to be fixed, before I migrate to a new operating system. I would be reinstalling my workstation operating system with 2 years of modifications and configurations in it, so this transition comes at a sizable time cost for me.

---

### 评论 #28 — BloodyIron (2020-07-07T12:58:18Z)

> It works just fine as is on my 20.04. Have you tried installing it on yours?

I'm staying on 19.10 until I see official support or conclusive evidence it works properly out of the box. I've seen it working for some, but inconsistently, and I am not about to break my working setup on a possibility. Thanks friend, but I need to be absolutely certain.

---

### 评论 #29 — BloodyIron (2020-07-20T13:54:40Z)

So... AMD has said nothing about Ubuntu 20.04 support for ROCM so far as I can find. Has anyone heard anything from them on this matter? Still cannot upgrade to 20.04 as a result of this blocker.

---

### 评论 #30 — selroc (2020-07-20T13:59:59Z)

Probably you have another issue there because I am running ROCm with Ubuntu Focal Fossa and it installed fine from the repo.


---

### 评论 #31 — BloodyIron (2020-07-20T14:02:18Z)

Are you able to get DaVinci Resolve to actually use the OpenCL in that mode? Because every method I've explored thus-far for 20.04 ROCm as is, is incomplete and does not do that. So I'd love to hear your results.

---

### 评论 #32 — BloodyIron (2020-07-20T14:02:45Z)

I'd also like to add that AMD does not list 20.04 as supported, which means they probably won't fix issues that we find with ROCm on 20.04 at this time.

---

### 评论 #33 — Szalacinski (2020-07-20T19:00:42Z)

It seems that OpenCL is the real problem for me on 20.04, although I don't know if the same issues are present on 18.04.  It seems to be issues with specific OpenCL code, to where programs like Luxmark 4 and Darktable don't crash, but programs like Luxmark 3, DaVinci Resolve, and Blender do crash.

---

### 评论 #34 — BloodyIron (2020-07-20T19:27:33Z)

Yeah like, 19.10 is formally EOL now for Ubuntu, so... Really need 20.04 support here.

---

### 评论 #35 — Bengt (2020-08-01T19:55:03Z)

Ubuntu's first point release is set to release in less than a week:

https://wiki.ubuntu.com/FocalFossa/ReleaseSchedule

Also, Adrenalin is now supporting Ubuntu 20.04:

https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-20-30

Maybe ROCm could follow soon?

---

### 评论 #36 — BloodyIron (2020-08-01T20:14:16Z)

Ugh this is so frustrating. 19.10 is now out of support and I can't even upgrade to 20.04 because ROCM doesn't support it!!! SOMEHOW. This should have worked DAY ONE.

---

### 评论 #37 — Bengt (2020-08-02T17:06:46Z)

@BloodyIron, I feel your frustration, but I don't see you case. Ubuntu 19.10 is not supported by the latest 3.5 ROCm release:

https://github.com/RadeonOpenCompute/ROCm#Supported-Operating-Systems-and-Documentation-Updates

So how is upgrading from Ubuntu 19.10 to 20.04 a supported use case? Was Ubuntu 19.10 ever a supported operating system?

---

### 评论 #38 — xuhuisheng (2020-08-02T17:40:57Z)

ubuntu-18.04.4 using the same kernel (5.3) of ubuntu-19.10.
18.04.5 will using linux-5.4 as 20.04.
So we couldnot upgrade to 18.04.5, since ROCm cannot support linux-5.4, I am afraid.

---

### 评论 #39 — Bengt (2020-08-02T18:45:05Z)

@xuhuisheng this issue is about supporting Ubuntu 20.04, please keep discussion about 18.04.5 in issue #1187.

---

### 评论 #40 — acai66 (2020-08-02T23:40:54Z)

> ubuntu-18.04.4 using the same kernel (5.3) of ubuntu-19.10.
> 18.04.5 will using linux-5.4 as 20.04.
> So we couldnot upgrade to 18.04.5, since ROCm cannot support linux-5.4, I am afraid.

I've reinstalled ubuntu, and rocm works under linux5.4. **DO NOT upgrade linux version to 5.4 if you are using 5.3 now**
![image](https://user-images.githubusercontent.com/37766207/89134916-a712f880-d55b-11ea-81a1-c69fc7e175b6.png)

I've compiled Pytorch with ROCM support, you can find whl files [here](https://github.com/acai66/Pytorch_ROCm_whl/releases), it works fine, here is a test about running yolov5 with Pytorch1.7.
![image](https://user-images.githubusercontent.com/37766207/89134969-5d76dd80-d55c-11ea-9872-2b25d3e73335.png)


---

### 评论 #41 — ghost (2020-08-12T15:39:11Z)

first time 
tensorflow works well
but now 
![image](https://user-images.githubusercontent.com/35652426/90035939-00fe8580-dcf5-11ea-9bd8-6d00cf84af4d.png)



---

### 评论 #42 — xuhuisheng (2020-08-19T05:17:47Z)

Good news. ROCm-3.7.0 will support ubuntu-20.04 officially. 
ref : https://github.com/Rmalavally/ROCm/commit/ac464aff1b5fd956fe9c4abad76d7364d69415c3
But the kernel of ubuntu-20.04 is 5.4.0 not 5.3.0. @Rmalavally 

---

### 评论 #43 — H-Ribeiro (2020-08-19T13:27:09Z)

> Good news. ROCm-3.7.0 will support ubuntu-20.04 officially.
> ref : [Rmalavally@ac464af](https://github.com/Rmalavally/ROCm/commit/ac464aff1b5fd956fe9c4abad76d7364d69415c3)
> But the kernel of ubuntu-20.04 is 5.4.0 not 5.3.0. @Rmalavally

Great news!
Question: When is ROCm-3.7.0 due to be released?

---

### 评论 #44 — BloodyIron (2020-08-19T13:30:43Z)

> Good news. ROCm-3.7.0 will support ubuntu-20.04 officially.
> ref : [Rmalavally@ac464af](https://github.com/Rmalavally/ROCm/commit/ac464aff1b5fd956fe9c4abad76d7364d69415c3)
> But the kernel of ubuntu-20.04 is 5.4.0 not 5.3.0. @Rmalavally

The syntax of that link suggests the 5.3 might be specifically for 18.04, as it comes after 18.04, and they may just be implying that the kernel included in 20.04 is supported. I really don't see how they could claim support for 20.04 without the base 5.4 kernel included.

Also, about fucking time!

---

### 评论 #45 — xuhuisheng (2020-08-19T15:42:30Z)

About the release schedule of ROCm.  It seems like the team will release a version every month. But the monthly version may not be the public release, Like the 3.6Beta maybe released in the middle of July. https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/releases/tag/3.6Beta,

We could find the release time from here: http://repo.radeon.com/rocm/apt/

```
rocm 3.0 2019-12 public release
rocm 3.1 2020-2  public release
rocm 3.2 2020-3 (no version in github)
rocm 3.3 2020-4 public release
rocm 3.4 2020-5 (no version in github)
rocm 3.5 2020-6 public release
rocm 3.6 2020-7 beta
rocm 3.7 2020-8 (internel or public?)
```

So I guess, if we couldnot see the 3.7.0 before September, Then we have to wait for 3.8.0 or a later version.
In my opinion, rocm-3.7.0 is most likely a public version. :D

---

### 评论 #46 — Bengt (2020-08-23T18:07:44Z)

Since Friday's release of ROCm 3.7, Ubuntu 20.04 is now a supported operating system.

For reference:

- [Release notes on OS support](https://rocmdocs.amd.com/en/latest/Current_Release_Notes/Current-Release-Notes.html#supported-operating-systems)
- [Commit announcing the support](https://github.com/RadeonOpenCompute/ROCm_Documentation/commit/738f79196f1067f30c4cac4f5f970463a5f51b87#diff-53f25b7d87cfbcc6fd211b71d801283c)

Since adding the support sorts out this issue, I am closing it.

---

### 评论 #47 — BloodyIron (2020-08-24T01:43:38Z)

W00t! \o/

---

### 评论 #48 — jmsjr (2020-08-24T04:14:04Z)

> Since Friday's release of ROCm 3.7, Ubuntu 20.04 is now a supported operating system.
> 
> For reference:
> 
> * [Release notes on OS support](https://rocmdocs.amd.com/en/latest/Current_Release_Notes/Current-Release-Notes.html#supported-operating-systems)
> * [Commit announcing the support](https://github.com/RadeonOpenCompute/ROCm_Documentation/commit/738f79196f1067f30c4cac4f5f970463a5f51b87#diff-53f25b7d87cfbcc6fd211b71d801283c)
> 
> Since adding the support sorts out this issue, I am closing it.

But why is the installation guide still referring to xenial : https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html :

> wget -q -O - http://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
> echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list 

.. and there does not seem to be a focal directory on the repo:

http://repo.radeon.com/rocm/apt/debian/dists/ only shows:

> ..
> xenial  20-Aug-2020 19:21






---

### 评论 #49 — Bengt (2020-08-24T05:38:10Z)

@jmsjr This issue was about AMD committing to support Ubuntu 20.04. Since there is some official support now, any future issue can just assume this support commitment. The points you raise seem like bugs, so please file an issue each, referencing this issue. 

---

### 评论 #50 — rkothako (2020-08-24T06:33:58Z)

@jmsjr 
This issue is already notified internally and will be fixed in ROCm 3.8.

xenial is the space name here which points to all packages in ROCm repo. Actually there is no issue w.r.to functionality front.
As ROCm dropped official support of Ubuntu 16.04, we have plans to change the space name to "focal" instead of "xenial".
Next release will have this change.

---

### 评论 #51 — xuhuisheng (2020-08-24T06:48:15Z)

@rkothako Sounds like ROCm-3.8.0 will be a public version. It is appreciate if there is a project roadmap. Maybe you could show us  more information for furture. Thanks

---

### 评论 #52 — jmsjr (2020-08-24T09:30:55Z)

> @jmsjr
> This issue is already notified internally and will be fixed in ROCm 3.8.
> 
> xenial is the space name here which points to all packages in ROCm repo. Actually there is no issue w.r.to functionality front.
> As ROCm dropped official support of Ubuntu 16.04, we have plans to change the space name to "focal" instead of "xenial".
> Next release will have this change.

Thanks @rkothako . I take this to mean that Ubuntu 20.04 users can safely use the "xenial" distribution in the AMD repo for ROCm 3.7.





---

### 评论 #53 — BloodyIron (2020-08-24T14:02:50Z)

> @jmsjr
> This issue is already notified internally and will be fixed in ROCm 3.8.
> 
> xenial is the space name here which points to all packages in ROCm repo. Actually there is no issue w.r.to functionality front.
> As ROCm dropped official support of Ubuntu 16.04, we have plans to change the space name to "focal" instead of "xenial".
> Next release will have this change.

Is there any way we can get public-facing roadmaps in the near future? The amount of time it took to get 20.04 support has been exceptionally frustrating, and so far as I am aware, I saw no outward-facing communications from AMD as to "when-ish" it would happen, etc.

---

### 评论 #54 — Bengt (2020-10-25T15:56:21Z)

For future reference, ROCm supported Ubuntu 20.04 LTS on August 19th, 2020.
That was almost exactly 4 months after the release of Ubuntu 20.04 LTS on April 23, 2020.

---
