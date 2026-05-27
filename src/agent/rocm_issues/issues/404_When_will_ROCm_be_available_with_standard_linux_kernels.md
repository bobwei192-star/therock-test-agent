# When will ROCm be available with standard linux kernels?

> **Issue #404**
> **状态**: closed
> **创建时间**: 2018-05-07T08:41:06Z
> **更新时间**: 2019-01-18T17:35:33Z
> **关闭时间**: 2018-09-16T21:11:38Z
> **作者**: markehammons
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/404

## 描述

Or at the very least, when will amdgpu-pro drivers be more widely available? I'd love to test ROCm on my rx550 with i7-8550u on opensuse-tumbleweed, but it looks like my system wouldn't be compatible and I'm lost on how to build the toolchain or if I could even get stuff set up without a custom kernel.

---

## 评论 (57 条)

### 评论 #1 — markehammons (2018-06-06T08:27:31Z)

Changing the title because I understand what ROCm is a bit more now. My big problem is the reliance on kernel 4.13 is a bit tough for me to deal with as of yet. When will ROCm be a little more kernel version agnostic and support stuff like kernel 4.16 or kernel 4.17, or when will the rock-dkms stuff be mainlined into the linux kernel and ROCm work with a standard linux kernel?

---

### 评论 #2 — gstoner (2018-06-06T13:23:15Z)

By the 4.18 Linux kernel is the first Linux kernel where all the AMDGPU and KFD bit are upstream to support the ROCm userland and make it agonistic as you say. This moment forward you have standard Linux kernel that can support Vega10, FIJI and Polaris GPU's. 

One thing to remember prior to DKMS solution we doing today we bootleg a Linux kernel under Ubuntu.   It how my team internally is running Ubuntu 18.04 right now with ROCm userland. 

RIght now I think you find the ROCm userland will compile in OpenSuSE,  you want to use 4.18 Linux kernel 


---

### 评论 #3 — gstoner (2018-06-06T13:35:39Z)

One thing DKMS is really not ROCm thing nor is the KCL, it how Linux driver team want to target OS when they may need to backpatch kernel.      KCL, Kernel Compatibility Layer is what limit which Kernel are supported.  

Note AMDGPUpro has the same issues since it DKMS based and uses KCL.   It why I am looking forward to upstream Linux support for based driver components needed for ROCm Userland. 

Upstream is a much longer process to get the all core foundation in place.  but we close to closing that chapter in ROCm history. 

---

### 评论 #4 — markehammons (2018-06-06T22:52:45Z)

@gstoner I have a rx550 polaris card. It sounds like kernel 4.17 could possibly support it. How would I determine this? Is there a specific message emitted by amdkfd to look for? Or do I just need to wait for 4.18? If 4.17 will do the job for me right now, then as soon as it's available in tumbleweed I'll compile the rocm 1.8 userspace and get testing.

---

### 评论 #5 — rhlug (2018-06-09T20:24:07Z)

> By the 4.18 Linux kernel is the first Linux kernel where all the AMDGPU and KFD bit are upstream to support the ROCm userland and make it agonistic as you say. This moment forward you have standard Linux kernel that can support Vega10, FIJI and Polaris GPU's.

@gstoner so no way to test that yet?   I compiled   https://cgit.freedesktop.org/~agd5f/linux/log/?h=drm-next-4.18 and installed all the rocm packages, but unless I setup the dkms,  i get nothing from clinfo.


---

### 评论 #6 — markehammons (2018-06-10T19:56:28Z)

@gstoner I've tested with kernel 4.17, and installed rocm-smi, and unfortunately I see no evidence that I can use ROCm with kernel 4.17 without the rock-dkms package (which doesn't work with anything but kernel 4.13)

---

### 评论 #7 — rhlug (2018-06-10T20:30:54Z)

@markehammons thats the conclusion I've come to also.

I am running 6 vegas on amdgpu-pro 18.20-579836 without DKMS however.

```
# uname -a
Linux rig30 4.17.0-rc2-180424-fkxamd #1 SMP PREEMPT Wed Apr 25 17:53:26 CDT 2018 x86_64 x86_64 x86_64 GNU/Linux

# dkms status

# clinfo | egrep -e "(Device|Driver) (Name|Board|Version)"
  Device Name                                     gfx900
  Device Version                                  OpenCL 1.2 AMD-APP (2633.3)
  Driver Version                                  2633.3 (PAL,HSAIL)
  Device Board Name (AMD)                         Radeon RX Vega
  Device Name                                     gfx900
  Device Version                                  OpenCL 1.2 AMD-APP (2633.3)
  Driver Version                                  2633.3 (PAL,HSAIL)
  Device Board Name (AMD)                         Radeon RX Vega
  Device Name                                     gfx900
  Device Version                                  OpenCL 1.2 AMD-APP (2633.3)
  Driver Version                                  2633.3 (PAL,HSAIL)
  Device Board Name (AMD)                         Radeon RX Vega
  Device Name                                     gfx900
  Device Version                                  OpenCL 1.2 AMD-APP (2633.3)
  Driver Version                                  2633.3 (PAL,HSAIL)
  Device Board Name (AMD)                         Radeon RX Vega
  Device Name                                     gfx900
  Device Version                                  OpenCL 1.2 AMD-APP (2633.3)
  Driver Version                                  2633.3 (PAL,HSAIL)
  Device Board Name (AMD)                         Radeon RX Vega
  Device Name                                     gfx900
  Device Version                                  OpenCL 1.2 AMD-APP (2633.3)
  Driver Version                                  2633.3 (PAL,HSAIL)
  Device Board Name (AMD)                         Radeon RX Vega
```

---

### 评论 #8 — gstoner (2018-06-11T13:18:37Z)

4.18 Linux kernel has the key feature you guys want 

amdgpu:
Vega 20 support
VEGAM support (Kabylake-G)
preOS scanout buffer reservation
power management gfxoff support for raven
SR-IOV fixes
**Vega10 power profiles and clock voltage control**
Scatter/gather display support on CZ/ST

amdkfd:
**GFX9 dGPU support**
**Userptr memory mapping**

---

### 评论 #9 — rhlug (2018-06-11T14:13:29Z)

@gstoner I built the drm-next-4.19-wip kernel, and there is no clinfo output without rocm dkms installed.    So are those pieces not in drm-next-4.19-wip yet?

---

### 评论 #10 — gstoner (2018-06-11T15:56:12Z)

@rhlug We have to look at the Thunk it most likely where the mismatch is happing 

---

### 评论 #11 — rhlug (2018-06-11T16:00:20Z)

can that make rocm 1.9 or is it too late?

---

### 评论 #12 — gstoner (2018-06-11T16:01:08Z)

I will talk to the Linux driver team 

Greg



---

### 评论 #13 — rhlug (2018-06-11T19:48:33Z)

Or if rocm-dkms in 1.9 works, and doesnt break powerplay, i dont mind using it at all.   But disconnecting from dkms would be ideal.

---

### 评论 #14 — gstoner (2018-06-11T23:13:11Z)

@rhlug  Yes, I am not DKMS fan.  Let me see what we can get out of the team for 1.9

---

### 评论 #15 — shimmervoid (2018-06-12T00:20:31Z)

A ROCm kernel maybe? 4.17 variant like 4.11 will be 💯 

---

### 评论 #16 — rhlug (2018-06-12T04:53:19Z)

@shimmervoid  that doesnt necessarily fix any problems with powerplay if you still have to load a dkms with issues against that rocm 4.17 kernel.  The dkms overloads the kernels powerplay with the dkms powerplay (ie amdgpu-1.8-151/amd/powerplay/hwmgr/vega10_*).     So you potentially replace a good powerplay (ie 4.17rc2) with a broken one (ie rocm-dkms 1.8-151).   And if you dont load a dkms,  and you dont have an update thunk like greg mentions, you have no opencl devices detected at all.

And when I say powerplay, I actually mean just pp_table, because most of it works (sclk/mclk levels, overdrive, etc)... but only way to undervolt is via pp_table, and thats where it currently has issues.

@gstoner i'll be happy to test any beta if you need.


---

### 评论 #17 — securitizones (2018-06-23T21:56:51Z)

when is rocm-dkms 1.9 being released

---

### 评论 #18 — justxi (2018-07-01T09:48:49Z)

With the mainline kernel 4.18.0-rc2, WIP Thunk branch ("fxkamd/drm-next-wip") and 1.8.x branches of ROCR-Runtime and ROCm-OpenCL-Runtime I get the following results:

    rocm_agent_enumerator reports my Radeon 560 (gfx803)
    clinfo reports expected information about this card

Examples:

    "HelloWorld" from "OpenCL Programming Guide" reports "Executed succesfully"
    "vector_copy" reports "... succeeded"
    "saxpy" reports "0 errors"

Tested on Gentoo Linux (Ryzen 7 1800x, Radeon 560).


---

### 评论 #19 — saitam757 (2018-07-03T22:29:42Z)

@justxi : Thanks for your hints. I followed your steps on Manjaro (kernel 4.18.0-rc2) as well as on Solus (kernel 4.17.2). Checkout of ROCT-Thunk-Interface branch ("fxkamd/drm-next-wip") and 1.8.x branch of ROCR Runtime. When compiling ROCR Runtime I got the error that _HSA_ENGINE_VERSION uCodeEngineVersions_ in _hsakmttypes.h_ was not defined. I did some ugly merges of _hsakmttypes.h_ and _topology.c_ with master of ROCT-Thunk-Interface to get this typedef and finally I got ROCR compiled. I tested vector_copy sample with result:
`Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
`
**Segmentation Fault**

Did you face similar problems ? My plan is to get at least the ROCm-docker container to run. Do you know what else besides ROCT-Thunk-Interface and ROCR is needed ? When I start the container and run _rocminfo_ I get:
`hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
`


---

### 评论 #20 — securitizones (2018-07-04T16:48:27Z)

Is there no way to patch the rocm 1.8 code and build locally so we can replace with a patched fixed version.i don't mind if that's the case.if so has anyone got the patched code or how to find it

---

### 评论 #21 — ghost (2018-07-09T22:43:43Z)

I put 18.04 bionic with version of rocm 1.8.2 up That I have working with the 4.16 with the kfd, I replaced the dkms package in the rocm installer with a dummy package and it is working on the live cd. I also patched CodeXL's pwrdriver so it also works.

---

### 评论 #22 — arigit (2018-07-11T15:39:28Z)

+1 for support on standard kernels. 
Looking forward to seeing Fedora 28 and above working with ROCm for OpenCL acceleration of darktable and gimp. Still resorting to manually extracting the opencl bits of amdgpu-pro to get opencl to work with my RX560 (luckily, at least this method still works)


---

### 评论 #23 — ghost (2018-07-11T15:43:55Z)

You will be looking forward to that for a very very very long time. Here is
a quote from mine to the ceo of redhat from awhile ago.
https://fishbowl.pastiche.org/2003/10/27/redhat_can_bite_my_shiny_metal_ass/

On Wed, Jul 11, 2018 at 11:39 PM, Ari <notifications@github.com> wrote:

> +1 for support on standard kernels.
> Looking forward to seeing Fedora 28 and above working with ROCm for OpenCL
> acceleration of darktable and gimp. Still resorting to manually extracting
> the opencl bits of amdgpu-pro to get opencl to work with my RX560 (luckily,
> at least this method still works)
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/404#issuecomment-404215499>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wx1wAYSmy7vjCi4PlhJDok3dDjyDks5uFhw3gaJpZM4T0nD6>
> .
>


---

### 评论 #24 — ghost (2018-07-11T15:48:11Z)

So, I will happily provide a tar.gz for you to test. There will be no rpms
from me.

On Wed, Jul 11, 2018 at 11:43 PM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> You will be looking forward to that for a very very very long time. Here
> is a quote from mine to the ceo of redhat from awhile ago.
> https://fishbowl.pastiche.org/2003/10/27/redhat_can_bite_my_
> shiny_metal_ass/
>
> On Wed, Jul 11, 2018 at 11:39 PM, Ari <notifications@github.com> wrote:
>
>> +1 for support on standard kernels.
>> Looking forward to seeing Fedora 28 and above working with ROCm for
>> OpenCL acceleration of darktable and gimp. Still resorting to manually
>> extracting the opencl bits of amdgpu-pro to get opencl to work with my
>> RX560 (luckily, at least this method still works)
>>
>> —
>> You are receiving this because you commented.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/404#issuecomment-404215499>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0wx1wAYSmy7vjCi4PlhJDok3dDjyDks5uFhw3gaJpZM4T0nD6>
>> .
>>
>
>


---

### 评论 #25 — arigit (2018-07-11T16:04:40Z)

lol. No RPMs would be fine - building rocm should be OK, as long as there is no need to build a custom kernel and assuming other dependencies can be met by installing standard fedora packages. 
Fedora 28 is already on 4.17.3 and I guess 4.18 will be coming as well. 


---

### 评论 #26 — ghost (2018-07-11T16:09:32Z)

Wait a sec, your running on the 4.17 branch? I have had and alot of other
people to a serious issues with the 4.17 and 4.18 kernels. I went as far as
to merge everything back into the 4.16 branch.

On Thu, Jul 12, 2018 at 12:04 AM, Ari <notifications@github.com> wrote:

> lol. No RPMs would be fine - building rocm should be OK, as long as there
> is no need to build a custom kernel and assuming other dependencies can be
> met by installing standard fedora packages.
> Fedora 28 is already on 4.17.3 and I guess 4.18 will be coming as well.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/404#issuecomment-404224319>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wwflw0Z1z-iW91ydiJPALHr5XC2Vks5uFiIdgaJpZM4T0nD6>
> .
>


---

### 评论 #27 — arigit (2018-07-11T16:35:56Z)

Running 17.3, fedora's current kernel, but not ROCm. To get openCL working in my workstation I manually extracted the libraries from an older amdgpu-pro rpm binary, and customized darktable/gimp launch scripts to load the libraries, like so

env LD_LIBRARY_PATH=$LD_LIBRARY_PATH_OPENCL darktable

This works (500% acceleration on darktable) but it's so ugly and the opencl libraries are old. Also I would like to have a normal opencl integration with my desktop so other apps can find it and use it without having to customize launchers.

I had/have some hope that with 4.17 or 4.18 I could move away from amdgpu-pro to ROCm. It seems I'll have to wait for 4.19?

---

### 评论 #28 — markehammons (2018-07-14T23:05:53Z)

with kernel 4.18-rc4, i'm getting the following:

```[    5.178854] amdgpu 0000:02:00.0: kfd not supported on this ASIC```

I assumed the rx550 was a supported GPU. Is this not the case? This is the output from lspci:

```Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X] (rev c0)```

---

### 评论 #29 — ghost (2018-07-15T00:31:48Z)

rtfm

On Sun, Jul 15, 2018 at 7:05 AM, Mark Hammons <notifications@github.com>
wrote:

> with kernel 4.18-rc4, i'm getting the following:
>
> [ 5.178854] amdgpu 0000:02:00.0: kfd not supported on this ASIC
>
> I assumed the rx550 was a supported GPU. Is this not the case? This is the
> output from lspci:
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/404#issuecomment-405055419>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w1Ehk1OG75gHcWpDuVZysHfCToF6ks5uGnlUgaJpZM4T0nD6>
> .
>


---

### 评论 #30 — markehammons (2018-07-15T01:27:49Z)

Thanks. I looked at the manual and it looks like it says polaris cards are supported, but it's not particularly clear at the moment. I assumed since my card was a polaris card that it was supported, but I guess there's a manual page elsewhere where it says it's not

---

### 评论 #31 — ghost (2018-07-15T01:38:59Z)

#361 you can see polaris 10, amd 11 working


On Sun, Jul 15, 2018 at 9:27 AM, Mark Hammons <notifications@github.com>
wrote:

> Thanks. I looked at the manual and it looks like it says polaris cards are
> supported, but it's not particularly clear at the moment.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/404#issuecomment-405060812>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w-QamyvAu8tQX6JcJa7quNG4CNN-ks5uGpqZgaJpZM4T0nD6>
> .
>


---

### 评论 #32 — ghost (2018-07-15T11:28:58Z)

The 550 will work fine, In fact it will an can work more then fine it can xfire, at the current time with 550's and even across to the radeon drivers. I have both the amdgpu and the radeon drivers running at the same time being virtualized :)

---

### 评论 #33 — ghost (2018-07-15T12:01:17Z)

Here is a nice shot of the bios editor running  

https://www.techpowerup.com/download/techpowerup-radeon-bios-editor/
To use the bios editor just apt-get wine, Here is the latest void you warranty and get your cards working 
WINEARCH=win32 winetricks vb6run
WINEARCH=win32 wine RBE_128.exe
![screenshot_2018-07-15_19-46-37](https://user-images.githubusercontent.com/23721155/42733761-cc19d158-8869-11e8-9cb3-2a9f83011687.png)



---

### 评论 #34 — markehammons (2018-07-15T12:48:32Z)

I'm a little lost. So it will work fine with polaris 12 cards? In that case what am I doing wrong that KFD is rejecting my card? Is there anything different between an rx 550 and a mobile rx550?

---

### 评论 #35 — justxi (2018-07-18T13:28:56Z)

@saitam757 No I had not such problems.

---

### 评论 #36 — johnbridgman (2018-07-29T16:37:32Z)

I'll check the code, but my recollection was that RX550 was not supported in the ROCm stack. 

AFAIK the bigger issue you are running into re: running upstream kernels is that the user/kernel interface for upstream is a bit different, so you need a modified thunk as well. Felix published a tree at the same time he pushed the kernel code - I'll see if I can find it and if not check with Felix on Monday.

---

### 评论 #37 — ghost (2018-07-29T17:20:06Z)

gfx804 for the 550

On Mon, Jul 30, 2018 at 12:37 AM, johnbridgman <notifications@github.com>
wrote:

> I'll check the code, but my recollection was that RX550 was not supported
> in the ROCm stack.
>
> AFAIK the bigger issue you are running into re: running upstream kernels
> is that the user/kernel interface for upstream is a bit different, so you
> need a modified thunk as well. Felix published a tree at the same time he
> pushed the kernel code - I'll see if I can find it and if not check with
> Felix on Monday.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/404#issuecomment-408689596>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w09PAObKp1I6mdydfyo0FTb3SGkoks5uLeTPgaJpZM4T0nD6>
> .
>


---

### 评论 #38 — johnbridgman (2018-07-29T17:53:13Z)

Felix's WIP thunk stack is here:

https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/fxkamd/drm-next-wip

I confirmed that the commits to align with upstream IOCTLs are there, however I have not tested this against upstream kernel code myself. 

---

### 评论 #39 — arigit (2018-07-30T18:24:08Z)

FWIW there is some activity on the Fedora / rawhide front, the rocm-runtime package was accepted for Fedora 29:

https://src.fedoraproject.org/rpms/rocm-runtime

I guess that implies that Fedora's kernel now has the required bits. I do notice though the release of ROCM they are currently building is 1.6 rather than 1.8



---

### 评论 #40 — lsr0 (2018-08-29T19:48:58Z)

Tested some HC/C++AMP samples on ~stock (4.18.5-arch1-1-ARCH) with the fxkamd/drm-next-wip branch on an RX480. They seem to work, pass their CPU verify step.

The OpenCL runtime, on the other hand, is segfaulting somewhere between `clIcdGetPlatformIDsKHR()` and `__gthread_create`, am rebuilding with symbols to find out more (though it complains about missing `libhsa-amd-aqlprofile64.so.1` at runtime).

---

### 评论 #41 — alexfrolov (2018-09-14T12:47:49Z)

Hi!

I am trying to use amd-staging-drm-next branch to work with amdkfd (built into amdgpu) for the AMD Instinct MI25 device.

As a first step I compiled libhsakmt 1.8.x and tried to run kfdtest. But it produces lots of failures (see below).
Here are the results:

...
[==========] 76 tests from 14 test cases ran. (80250 ms total)
[  PASSED  ] 39 tests.
[  FAILED  ] 37 tests, listed below:
[  FAILED  ] KFDEvictTest.QueueTest
[  FAILED  ] KFDGraphicsInterop.RegisterGraphicsHandle
[  FAILED  ] KFDIPCTest.BasicTest
[  FAILED  ] KFDIPCTest.CrossMemoryAttachTest
[  FAILED  ] KFDIPCTest.CMABasicTest
[  FAILED  ] KFDLocalMemoryTest.BasicTest
[  FAILED  ] KFDLocalMemoryTest.VerifyContentsAfterUnmapAndMap
[  FAILED  ] KFDLocalMemoryTest.CheckZeroInitializationVram
[  FAILED  ] KFDMemoryTest.MapUnmapToNodes
[  FAILED  ] KFDMemoryTest.MemoryRegisterSamePtr
[  FAILED  ] KFDMemoryTest.FlatScratchAccess
[  FAILED  ] KFDMemoryTest.MMBench
[  FAILED  ] KFDMemoryTest.QueryPointerInfo
[  FAILED  ] KFDMemoryTest.PtraceAccessInvisibleVram
[  FAILED  ] KFDMemoryTest.SignalHandling
[  FAILED  ] KFDQMTest.CreateCpQueue
[  FAILED  ] KFDQMTest.CreateMultipleSdmaQueues
[  FAILED  ] KFDQMTest.SdmaConcurrentCopies
[  FAILED  ] KFDQMTest.CreateMultipleCpQueues
[  FAILED  ] KFDQMTest.DisableSdmaQueueByUpdateWithNullAddress
[  FAILED  ] KFDQMTest.DisableCpQueueByUpdateWithZeroPercentage
[  FAILED  ] KFDQMTest.OverSubscribeCpQueues
[  FAILED  ] KFDQMTest.BasicCuMaskingEven
[  FAILED  ] KFDQMTest.QueuePriorityOnDifferentPipe
[  FAILED  ] KFDQMTest.QueuePriorityOnSamePipe
[  FAILED  ] KFDQMTest.EmptyDispatch
[  FAILED  ] KFDQMTest.SimpleWriteDispatch
[  FAILED  ] KFDQMTest.MultipleCpQueuesStressDispatch
[  FAILED  ] KFDQMTest.CpuWriteCoherence
[  FAILED  ] KFDQMTest.CreateAqlCpQueue
[  FAILED  ] KFDQMTest.QueueLatency
[  FAILED  ] KFDQMTest.CpQueueWraparound
[  FAILED  ] KFDQMTest.SdmaQueueWraparound
[  FAILED  ] KFDQMTest.Atomics
[  FAILED  ] KFDQMTest.P2PTest
[  FAILED  ] KFDQMTest.SdmaEventInterrupt
[  FAILED  ] KFDTopologyTest.BasicTest

Does it mean that current amdkfd from the kernel cant be used with libhsakmt 1.8.x? or I am doing something wrong...
Thank you!

Best,
   Alexander

---

### 评论 #42 — jlgreathouse (2018-09-14T15:41:42Z)

We are planning on releasing ROCm 1.9 very soon (today, I think) which will update all of this. The Thunk and amdkfd are tightly coupled, so changes in the KFD can affect how the Thunk interacts. I would not expect that the Thunk for 1.8 would work with the latest KFD (roughly for 1.9).

There is a roc-1.9.x branch in the ROCt (Thunk -- libhsakmt) github tracker; you can try building that, perhaps.

---

### 评论 #43 — jlgreathouse (2018-09-14T22:38:59Z)

ROCm 1.9.0 was just released and should allow ROCm to work with the upstream kernel. See [README.md](https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md) for more information.

---

### 评论 #44 — markehammons (2018-09-16T07:36:02Z)

This is great, but apparently I still can't test it cause my card is not supported.

Apparently Lexa cards have no kfd support yet.

---

### 评论 #45 — jlgreathouse (2018-09-16T21:11:38Z)

Hi @markehammons 

Polaris 12 (Lexa) is not currently on our [list of supported GPUs](https://rocm.github.io/hardware.html). We are focusing most of our official development efforts on our more powerful GPUs, such as Polaris 10, Vega 10, and upcoming chips. While I appreciate the desire to use GPUs such as Polaris 12 with the ROCm stack, our team must focus our limited amount of resources where we think they will have the most impact.

That isn't to say that we don't want to get Polaris 12 working in ROCm -- only that at this time we do not offer official support for it. I can't tell you anything about if such support would be added in the future. Your request has been heard, however.

That said, I'm going to close this specific issue because I believe, with the release of ROCm 1.9.0, this software should work with standard (upstream) Linux kernels.

---

### 评论 #46 — arigit (2018-09-17T18:16:01Z)

Question for those using Ubuntu 18.01LTS (stock kernel 4.15). Does installing rocm 1.9 require replacing the distro kernel with a patched one like in prior rocm releases?  
(as opposed to only having to use dkms to build a single kernel driver (kfd?) which would be ok)
Card - RX560. 
Some ppl refer to kernel 4.17 and above as a requirement - which is not really part of stock ubuntu so a bit confused on whether 1.9 can be taken to production systems where stock kernel is needed


 

---

### 评论 #47 — jlgreathouse (2018-09-17T18:46:11Z)

I may be misunderstanding your question, but I believe our current release just rebuilds a custom amdgpu/amdkfd/amdkcl module using DKMS. We do not require a custom kernel anymore, like we did back in the ROCm 1.6 days. This was also true for ROCm 1.7 and 1.8, so I hope I'm understanding your question correctly.

You can choose to use the ROCm user-level code with upstream kernels 4.17 and above. In this case, you don't need to install any kernel-level changes. However, if you *want* to install rock-dkms (our custom modules, described in the paragraph above), then you will get more features that you may find interesting.

Basically, ROCK includes our most up-to-date changes, most of which we are trying to get upstreamed into the Linux kernel. Because upstreaming takes time, we release these new features into ROCK while we wait. This is especially useful for folks who don't want to run bleeding-edge kernels that are outside of their distro's stock kernel list.

So yes, you should be able to run ROCm 1.9 with a stock Ubuntu kernel. For example, I'm running it on Ubuntu 18.04.1 LTS with 4.15.0-34-generic right  now.
```
jlgreathouse@test-polaris10:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.1 LTS
Release:        18.04
Codename:       bionic
jlgreathouse@test-polaris10:~$ uname -a
Linux test-polaris10 4.15.0-34-generic #37-Ubuntu SMP Mon Aug 27 15:21:48 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
jlgreathouse@test-polaris10:~$ dkms status
amdgpu, 1.9-211, 4.15.0-34-generic, x86_64: installed
```

---

### 评论 #48 — arigit (2018-09-17T19:01:10Z)

@jlgreathouse thanks for the fast response. Indeed you got the question right, I see I was assuming wrongly that the patched kernel was still needed as of 1.8.

Question - I see via dkms you had a new amdgpu driver built, does this change OpenGL (in addition to enabling OpenCL) in any way with respect to the distro-provided amdgpu driver? ( i.e. any risk of app compatibility issues)

If  the answer is yes, would doing this for and OpenCL-only install:

> sudo apt-get install dkms rock-dkms rocm-opencl

... eliminate that risk?



---

### 评论 #49 — jlgreathouse (2018-09-17T19:08:30Z)

Hi @arigit 

I can't speak much towards app compatibility issues with respect to OpenGL. I suppose I should ping @kentrussell to get the driver team's feedback on this question.

However, it *is* the case that ROCK is essentially a replacement `amdgpu` and `amdkfd` compared to the versions that ship with your distro. We do not claim to keep up-to-date with any backported patches that your distro brings into their version of these drivers -- though our versions might be newer than what comes with your distro.

Doing the commands you listed would not eliminate this risk, as `rock-dkms` is the new amdgpu module under discussion. Installing `rock-dkms` creates the new amdgpu under DKMS. However, on stock Ubuntu 18.04.1 with kernel 4.15.0-xx, you need `rock-dkms` to use ROCm. As you noted earlier, stock Ubuntu 18.04.1 does not come with the required 4.17+ kernel needed for ROCm to work without a custom driver.

---

### 评论 #50 — arigit (2018-09-17T19:27:56Z)

@jlgreathouse understood 100%, thanks for the clarity. For the prod environment I will wait a few more months for the next distro release and jump to rocm at that point

---

### 评论 #51 — ernestoriv7 (2018-09-20T02:52:13Z)

Hi, I want to install ROCm in ubuntu 18.04 running the latest kernel (upstream). Reading the documentation I see that I should not install the rock-dkms package. How can I install ROCm without installing that package?

---

### 评论 #52 — jlgreathouse (2018-09-20T03:44:44Z)

[This post](https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/open-source-amd-linux/1047471-amd-rocm-1-9-available-with-vega-20-support-plus-upstream-kernel-compatibility?p=1047548#post1047548) may help you do that.

---

### 评论 #53 — ernestoriv7 (2018-09-20T14:59:15Z)

Great, thanks!

---

### 评论 #54 — jlgreathouse (2018-12-22T00:40:34Z)

@markehammons I've switched up the tags because, as of the 2.0 release, "Polaris 12" should be be enabled in ROCm. I just sat down and tested a batch of OpenCL, HCC, and HIP applications with a Polaris 12 board, and things appear to be working as expected.

Note that you will need to be on a distro that supports our rock-dkms driver to have this support, since the last bit that needed to be in place was a driver change. Support for this is also in the amd-staging-next drivers, but will not hit upstream Linux until post-4.20.

OpenSUSE support is not yet official. However, you might try to keep an eye on the new [Experimental ROC](https://github.com/RadeonOpenCompute/Experimental_ROC) repo, which includes build and install scripts for a variety of distros, including ones that AMD does not officially support. I would like to get OpenSUSE working (or get the community's help to get OpenSUSE working).

---

### 评论 #55 — saitam757 (2019-01-18T16:59:34Z)

@markehammons I'm eager to get ROCm to run on OpenSUSE. Maybe I can give it try. Currently I'm using the compute stack inside a docker container but a "native" support would be nice.
When this came to my mind some days ago (and I found this post) I read a little bit about the Open Build Service. Now I want to try get get ROCm to compile there. My question is, wouldn't it be a nice solution to get ROCm to run on all major distributions ? As far as I read, libraries for Debian, OpenSUSE, Fedora, and Arch could be created. I have to admit I don't have any experiences with the Open Build Service and maybe there are some drawbacks I don't know. Best, Matthias. 

---

### 评论 #56 — saitam757 (2019-01-18T17:08:16Z)

@jlgreathouse Sorry, write my previous post to the wrong person. (-: Please see my post here: 

https://github.com/RadeonOpenCompute/ROCm/issues/404#issuecomment-455615945

---

### 评论 #57 — FelixSchwarz (2019-01-18T17:35:33Z)

Just a short heads-up due to the lack of a better place: Tom Stellard is currently packaging ROCm 2.0 for Fedora but it will take some more time (packaging the whole eco system is quite a challenge, need to remove some hard coded paths etc).

---
