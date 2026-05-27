# ROCm RX VEGA hash rates for Cryptonight (linux vs windows)

> **Issue #325**
> **状态**: closed
> **创建时间**: 2018-02-03T23:44:51Z
> **更新时间**: 2021-01-05T09:52:18Z
> **关闭时间**: 2021-01-05T09:52:18Z
> **作者**: rhlug
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/325

## 描述

Going to start a new issue in hopes to find a solution to the performance of cryptonight mining on linux under ROCm, as we continue to lag behind the windows aug 23rd blockchain drivers by 35%.

### 

GPUs - RX Vega 64

Running Aug 23 blockchain drivers on windows, I see 1900h cryptonight, and 39Mh ethash.
Running ROCm 1.7 on ubuntu, I see 1250h cryptonight, and 39Mh ethash.

So the fact that I can get like rates on ethash means the opencl stack is just as good as windows.

I gave windows 64GB of virtual memory and ubuntu 64GB of swap. Tested amdkfd.noretry 1 and 0.

Any other recommendations on things to try?


---

## 评论 (100 条)

### 评论 #1 — todxx (2018-02-04T07:05:49Z)

If I remember correctly, to hit the 1900+h/s with cryptonight in windows it required doing a hot re-initialization of the GPUs.  I remember people were initially doing this by enabling or disabling HBCC which seemed to cause re-initialization of the GPU.  

Without the re-initialization, I believe performance is pretty similar to the linux rocm stack.  This seems to suggest that the windows initialization procedures at boot and for hot reset are different somehow.  I would love to get some clarity into what the difference is that is causing this performance delta.  

A 50% performance increase running the exact same code is impressive.

---

### 评论 #2 — rhlug (2018-02-04T17:50:32Z)

@todxx  its nothing with hbcc.  just reloading the driver with a disable/enable in device manager is all it takes.  No way to do that in linux.  Neither modprobe -r or rmmod/insmod will allow amdgpu or amdkfd to be removed/reloaded.

---

### 评论 #3 — ob7 (2018-02-05T03:30:41Z)

Can whatever it is Windows is toggling when reinitializing the gpus be accomplished with a bios mod?

---

### 评论 #4 — todxx (2018-02-05T04:58:02Z)

@rhlug I don't think it has to do just with reloading the driver.  I think the way windows reloads the driver for a hot reset is somehow different than how it loads on boot.  But I'm just guessing here.

@ob7 I believe the bios on Vega requires to be signed and therefore is not moddable.  In either case, without knowing what is being changed, it will be difficult to reproduce.

---

### 评论 #5 — akostadinov (2018-02-15T23:15:48Z)

Perhaps you can try to disable module on boot and only manually load it before running the compute program. My suspicion though is that on windows, the card is getting used by something during the whole boot process and resources are not released completely. The reload perhaps allows for releasing all needless resources on the card.
If you load linux module before running computing, that might be the same. e.g. would prevent X to ever try to use the card. If this helps, then x/wayland may need to be configured to never touch the cards.

btw what are you using to tune card cooling and speed on linux? It seems proper underclocking is always needed for good results.

---

### 评论 #6 — lsimplify (2018-02-18T04:14:51Z)

@rhlug Did you achieve 1900h cryptonight _without_ overclocking the memory frequency on Windows? Because as far as I know overclocking the memory is required to get a hashrate like 1900h/s. (Am I wrong?)

---

### 评论 #7 — 949f45ac (2018-02-18T10:47:25Z)

@lsimplify You can only achieve 1900 H/s on Windows with overclocking sure enough, but even without OC a Vega is at >1500 H/s after the disable/enable toggle. On Linux it’s less than 1200 H/s without OC, and maybe ~1300 with.

@akostadinov You can simply let a Vega run compute jobs on a headless system, forgoing X completely. It doesn’t change anything, sadly.
>the card is getting used by something during the whole boot process and resources are not released completely.

The author of the original [Vega mining guide on reddit](https://www.reddit.com/r/MoneroMining/comments/74hjqn/monero_and_vega_the_definitive_guide/) writes that it has something to do with a power saving feature, but doesn’t give any specifics on how he’s reached that conclusion:
>The blockchain Beta driver has some sort of a bug (i see it as a feature) that when you restart the GPU device some sort of power saving feature (i see it as a bug) doesn't get activated. Therefore, by restarting your GPU device it will hash higher.

---

### 评论 #8 — akostadinov (2018-02-19T17:34:27Z)

@949f45ac , this might be what author **thinks** but it is not necessarily true as well it is driver dependent. I for one had very unstable setup with the plain blockchain driver. Then updated only the driver with a newer one from pro-series driver (leaving the rest to be from the blockchain driver. Setup is much more stable. The interesting thing is that I have to

1. run under/overclock utility
1. disable/enable device

This is the best I have so far. If I run the underclock utility after disable/enable, then card sucks much more power for some reason. Until we have stable linux drivers upstreamed situation will be crap it seems. IMO it is still worth trying to avoid loading rocm until just before compute software is to be run. I can't try though because mainboard is incompatible :/  I decided to wait until linux drivers stabilize and there is better statistics which mainboards are supported.

---

### 评论 #9 — 949f45ac (2018-02-27T07:56:18Z)

@tekcomm What you write is true for the RX 400 / 500 series. However, it seems that Vega memory overclocks just fine with `rocm-smi` alone. Hash rate goes up, and you achieve numbers mostly similar to those on Windows *without the device toggle.* But if you do the device toggle on Windows, you get another +30%.

I personally believe it would be very nice if we got control over all the remaining DPM features on Vega. Looking into vega10_hwmgr.h in the kernel driver, we see this:
```c
enum {
        GNLD_DPM_PREFETCHER = 0,
        GNLD_DPM_GFXCLK,
        GNLD_DPM_UCLK,
        GNLD_DPM_SOCCLK,
        GNLD_DPM_UVD,
        GNLD_DPM_VCE,
        GNLD_ULV,
        GNLD_DPM_MP0CLK,
        GNLD_DPM_LINK,
        GNLD_DPM_DCEFCLK,
// goes on with non-DPM features
```
So there’s the graphics clock (GFXCLK), the memory clock (UCLK), but also apparently the SoC clock and something related to the Prefetcher.

When I profile a Cryptonight miner on Vega with RCP, I see `MemUnitStalled` 30% upwards. On the normal RX series this is only a few percent. Possibly this is related to having HBM2 memory, which may have higher bandwidth, but clocks much lower.

Another thing I notice is that the main loop in Cryptonight, which is iterated over 500k times doing two random 16 byte fetches and two random 16 byte reads, actually has a `FetchSize` 4 times the expected amount and a `WriteSize` double. I believe this _might_ be prefetch logic reading +3 ahead on every read and queueing one write to the predicted location, then one write to the actual one. Now maybe if we could tune the prefetcher differently, this could increase performance, is my wild speculation.

---

### 评论 #10 — todxx (2018-02-27T08:58:20Z)

@949f45ac I think you might be onto something there.  A misbehaving prefetcher could cause a perf hit like this, and your data seems to back it up.

I'd be curious to see what happens if the 3 lines starting [here](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/powerplay/hwmgr/vega10_hwmgr.c#L2273) are changed/removed to disable the prefetcher smu feature.

It would be nice to get some input from the devs on what the GNLD_DPM_PREFETCHER feature actually controls before playing Vega roulette.

---

### 评论 #11 — todxx (2018-02-27T10:11:36Z)

@tekcomm I've made the changes and have a build going.  However, I'm not sure if I need to do anything to make it play nice with roc-dkms.  I'm not familiar with how dkms works.  I guess I'll just try a normal kernel install and hope for the best.

---

### 评论 #12 — todxx (2018-02-27T12:20:32Z)

Disabling the feature had no effect.  Cryptonight still running around 1200.

---

### 评论 #13 — 949f45ac (2018-02-27T19:08:48Z)

@todxx I already tried simply disabling `GNLD_DPM_PREFETCHER` -- then I realised that what this does is probably only to disable *the DPM* for Prefetcher, ie. the driver is telling the card: "I have no intent of setting power levels for prefetcher myself."

What we actually want, though, is try different manual overrides to prefetcher power level. For this we’d need the driver extended to expose a file to sysfs like `/sys/class/drm/card0/device/pp_dpm_sclk` (which is what rocm-smi uses when you call `--setsclk`). I thought about trying my hand at it, but I didn’t really understand where the driver was getting information about possible sclk states from, to begin with -- not straightforward from the card, I think. (I believe it might get some voltage information from the card and use that to calculate clocks.) So I suppose that some knowledge of the hardware internals is needed.

---

### 评论 #14 — gstoner (2018-02-27T19:11:59Z)

This is correct, the GNLD_DPM_PREFETCHER has nothing to do with instruction cache or Data Cache prefetcher.  



---

### 评论 #15 — 949f45ac (2018-02-27T19:47:05Z)

@gstoner So is it possible, in principle, to control power state of Vega memory prefetcher from the driver?

We are talking about a compute kernel that goes through a loop 2^19 times, doing 2 reads with a write-back each, in every iteration.
In simplified terms:
```c
uint a, b;
uint128_t pad[131072];
for (int i = 0; i < 524288; i++) {
  data = pad[a];
  data = hash1(data);
  pad[a] = data;
  b = newBfromData(data);

  data = pad[b];
  data = hash2(data);
  pad[b] = data;
  a = newAfromData(data);
}
```
The memory prefetcher seems to be pointlessly reading ahead after each of these random reads, and also scheduling every write to a wrong location at first – possibly worsening performance. Do you think modifying the prefetcher’s power state could help? Or do you have another idea on how to improve performance?

---

### 评论 #16 — gstoner (2018-03-02T23:03:44Z)

@rhlug  Can you try the beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2  It support 4.13 Linux kernel 

---

### 评论 #17 — todxx (2018-03-03T20:22:51Z)

I tested this out since I was testing another bug with the 1.7.1 beta 4.  There seems to be no difference in cryptonight performance, though I did not profile to check fetch behaviour.

---

### 评论 #18 — CthulhuVRN (2018-03-03T20:35:06Z)

@gstoner I made clean installation of Ubuntu 16.04.4, ROCm 1.7.1b4. CryptoNight algo gives me up to 1200 H/s. Same miner but Windows gives me up to 1900 H/s.

```
~> cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.4 LTS"

~> uname -a
Linux dahlia 4.13.0-36-generic #40~16.04.1-Ubuntu SMP Fri Feb 16 23:25:58 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

~> cat /etc/default/grub
...
GRUB_CMDLINE_LINUX_DEFAULT="splash quiet amdgpu.vm_fragment_size=9"
...
```

The card is ref Vega 56.

---

### 评论 #19 — gstoner (2018-03-03T21:56:49Z)

Thanks, I am talking with the SMU team about delta.  We will soon have a new ROCm profiling foundation available with trace and perf counter support. It is a massive update on what we had in the past.    Also working on Debugger that will show the PC, VGPR, SGPR, Support Breakpoints and Runcontrol etc.   

It would great in the short run if we can get someone to profile the base driver with  Perf and eBPF now we have DKMS based install. 

Here is a rough outline of the  API of the New Profiler Foundation.  

Returned API status:
-	hsa_status_t - HSA status codes are used from hsa.h header

Info API:
-	rocprofiler_info_kind_t - profiling info kind
-	rocprofiler_info_query_t - profiling info query
-	rocprofiler_info_data_t - profiling info data
-	rocprofiler_iterate_info - iterate over the info for a given info kind 
-	rocprofiler_query_info - iterate over the info for a given info query

Context API:
-	rocprofiler_t - profiling context handle
-	rocprofiler_feature_kind_t - profiling feature kind
-	rocprofiler_feature_parameter_t - profiling feature parameter
-	rocprofiler_data_kind_t - profiling data kind
-	rocprofiler_data_t - profiling data
-	rocprofiler_feature_t - profiling feature
-	rocprofiler_mode_t - profiling modes
-	rocprofiler_properties_t - profiler properties
-	rocprofiler_open - open new profiling context
-	rocprofiler_close - close profiling context and release all allocated resources
-	rocprofiler_group_count - return profiling groups count
-	rocprofiler_get_group - return profiling group for a given index
-	rocprofiler_get_metrics - method for calculating the metrics data
-	rocprofiler_iterate_trace_data - method for iterating output trace data instances

Sampling API:
-	rocprofiler_start - start profiling
-	rocprofiler_stop - stop profiling
-	rocprofiler_read - read profiling data to the profiling features objects
-	rocprofiler_get_data - wait for profiling data
Group versions of start/stop/read/get_data methods:
o	rocprofiler_group_start
o	rocprofiler_group_stop
o	rocprofiler_group_read
o	rocprofiler_group_get_data

Intercepting API:
-	rocprofiler_callback_t - profiling callback type
-	rocprofiler_callback_data_t - profiling callback data type
-	rocprofiler_set_dispatch_callback - adding kernel dispatch callback
-	rocprofiler_remove_dispatch_callback - removing kernel dispatch callback

Returning the error string method:
-	rocprofiler_error_string - method for returning the API error string


---

### 评论 #20 — CthulhuVRN (2018-03-05T10:50:15Z)

@gstoner provide some instructions, and I will try to do all my best (-:

---

### 评论 #21 — gurupras (2018-04-03T03:49:46Z)

Is there any  update on this?

---

### 评论 #22 — 949f45ac (2018-04-09T06:51:28Z)

Apparently with the new Windows driver release 18.3.4 the cryptonight performance bugs on Windows are completely fixed, i.e. you don’t even have to toggle your cards off/on anymore to achieve great performance.

@gstoner  Maybe you could talk to the team building the Windows drivers and find out what fix they put into this release and get it done in the Linux drivers too? That’d be wonderful. [Release notes](https://support.amd.com/en-us/kb-articles/Pages/Radeon-Software-Adrenalin-Edition-18.3.4-Release-Notes.aspx) for 18.3.4 simply state
>Fixed Issues:
>- Some blockchain workloads may experience lower performance than expected when compared to previous Radeon Software releases.

---

### 评论 #23 — CthulhuVRN (2018-04-22T16:07:37Z)

Still no updates?

---

### 评论 #24 — briansp2020 (2018-04-22T17:12:40Z)

What is the unrolling bug you are talking about? Do you have link to more information? Just curious.

---

### 评论 #25 — akostadinov (2018-04-22T18:55:15Z)

Is there a reproducer program. I'm seeing lock-ups here with a frontier edition. But also can be the driver vs older mobo and cpu.

---

### 评论 #26 — Mandrewoid (2018-04-23T01:03:47Z)

@tekcomm would that be why my Vega FE does this? https://i.imgur.com/xTDxroL.jpg
it works fine until I put it under 100% load, even under windows after about  2 minutes full load it does that

---

### 评论 #27 — uentity (2018-05-03T11:25:38Z)

Maybe some light is shed on magic Windows HBCC driver switch?
I'm having the same issue as topic starter.

---

### 评论 #28 — uentity (2018-05-03T11:55:18Z)

@tekcomm so, problem can be solved with ROM modification? Can you suggest any references for finding such mods?

---

### 评论 #29 — szogun1987 (2018-05-04T11:06:42Z)

New version of AMDGPU-PRO (18.10) have been released. On Windows 18.x version doesn't require HBCC switch for high hashrates. Maybe Linux version doesn't require it also. Unfortunately for some reason I cannot extract version I download. So I cannot check it.

---

### 评论 #30 — uentity (2018-05-04T11:51:12Z)

@szogun1987 no, 18.10 doesn't solve this issue.

---

### 评论 #31 — sayyiditow (2018-05-10T10:45:57Z)

Looks like we are still out of luck here for ubuntu vega CN hash to reach same speed as on windows? Damn, I wish I could use linux.

---

### 评论 #32 — cryptonote-social (2018-05-16T14:54:51Z)

Perhaps we can start a bounty for whoever gets Vegas to perform well in stock linux distros?

---

### 评论 #33 — 949f45ac (2018-05-16T18:54:01Z)

You just need enough to bribe some guy on the Windows driver team into telling you what the secret sauce is. ;)

---

### 评论 #34 — ghost (2018-05-17T09:43:53Z)

Anyways good luck I'll be back in 3 days after I finish watching the paint
dry


On Thu, May 17, 2018, 4:35 PM Jason Kurtz <tekcommnv@gmail.com> wrote:

>
> On May 17, 2018 1:55 AM, "dur" <notifications@github.com> wrote:
>
> You just need enough to bribe some guy on the Windows driver team into
> telling you what the secret sauce is. ;)
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/325#issuecomment-389627700>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w_hrpdJiJlonRWtTjY11PkgUxUbQks5tzHYFgaJpZM4R4X68>
> .
>
> It would have to be a good Bounty since Whoever has it running would be
> making more then selling it. Since it's worth .1 to one Bitcoin for every
> 3.92 to 57 days.
>


---

### 评论 #35 — sayyiditow (2018-05-21T04:21:26Z)

Any updates on this?

---

### 评论 #36 — Blazin64 (2018-05-25T19:42:42Z)

If I'm understanding what @tekcomm said to @uentity correctly, all it takes is a rom modification to get full cryptonight hashing performance out of Vega on Linux?

---

### 评论 #37 — Blazin64 (2018-05-26T22:00:59Z)

@tekcomm I sent you a couple of emails. Think you could take a look at them? :)

So, does anybody know if these OpenCL patches will be mainline or ROCM only? A lot of people are having a hard time with Vega, so I hope it will be mainline. That way everyone wins, ROCM or not.

---

### 评论 #38 — Zarkoob (2018-06-04T11:27:34Z)

@tekcomm I'm having issues where linux my cards are hashing at 710H/s on cryptonight but windows it's 840H/s. I don't have Vega I have RX580. Is the compute option not turned on?

---

### 评论 #39 — rhlug (2018-06-04T22:34:18Z)

Just finished testing Cryptonight and Cryptonight-heavy on Ubuntu 18.04 with those amdgpu-pro 18.20 drivers.   Cryptonight-heavy does around 1100h/s on my vega 56s, Cryptonight v7 gives me ZERO hashes.  Never finds any results.  I compiled both xmr-stak and xmrig-amd.   I'm assuming something goes wrong during kernel compilation.   I'll check a cryptonight-lite to see how it fares.

---

### 评论 #40 — Zarkoob (2018-06-05T08:18:04Z)

Here is where I get so far:
https://i.imgur.com/njwBz0u.png

I'm not able to change any other straps I don't think. (I was able to flash the cards using ATIflash in windows with Polaris editor 1.6 and the "ezclick method". The cards are all XFX RX580 but all have oddly different memory manufacturers. Some Micron, Samsung, others Samsung /hynix/ Samsung. It's odd. The highest of the list is Samsung. Again windows they all hash the same at 820-840.

The cards in Linux run hotter. (same total power use at 1300 watts)
Windows the cards all hash **EXACTLY the same**. However I can only get 5 cards going max in windows. The CPU in windows hashes at a dwarf of what Linux does. So I guess that's a plus? 

---

### 评论 #41 — rhlug (2018-06-05T14:18:14Z)

@tekcomm I'm running latest stak.  
```
# ./xmr-stak -v
Version: xmr-stak 2.4.4 c0ab173
```

With bionic 18.04 + 18.20 pro drivers, cryptonight v7 doesnt do shit on gfx900. 



---

### 评论 #42 — rhlug (2018-06-05T17:13:12Z)

@tekcomm your compiling stak against mesa ocl?

---

### 评论 #43 — rhlug (2018-06-05T17:52:25Z)

are you positive its linked against libMesaOpenCL.so.1?

```
# ldd libxmrstak_opencl_backend.so  | grep OpenCL
	libMesaOpenCL.so.1 => /usr/lib/x86_64-linux-gnu/libMesaOpenCL.so.1 (0x00007f1eaddf6000)

# ./xmr-stak  -c config.txt --amd amd.txt -C pool.txt
[snip]
[2018-06-05 17:43:30] : Compiling code and initializing GPUs. This will take a while...
./xmr-stak: symbol lookup error: ./libxmrstak_opencl_backend.so: undefined symbol: clGetPlatformIDs
```

Is there some secret, because I only see AMD/NVIDIA on man

```
# ./xmr-stak --openCLVendor MESA
[2018-06-05 17:51:41] : '--openCLVendor' must be 'AMD' or 'NVIDIA'
```

---

### 评论 #44 — rhlug (2018-06-05T20:35:03Z)

Can you check what its linked against?

```
# ldd libxmrstak_opencl_backend.so  | grep OpenCL
```

I've setup xmr-stak against mesa in the past, and actually had it detecting my vegas, only to segfault during kernel compilation.  Now I dont even get past GPU detection.

OS: Ubuntu 18.04
MESA: mesa-opencl-icd:amd64                    18.2~git1806050730.1ac443~oibaf~b
STAK:  Version: xmr-stak 2.4.4 c0ab173

I think older stak didnt have --openCLVendor, and used to give warning about it detecting my GPUs under mesa, which was ocl 1.1.  I probably posted about it on the interwebs somewhere... I forget.


---

### 评论 #45 — rhlug (2018-06-05T21:07:58Z)

There is no clGetPlatformIDs() in libMesaOpenCL.so, which explains why xmr-stak barfs on that call.   
I dont see how you can successfully link against Mesa OCL given this fact.

```
# objdump -Tx /usr/lib/x86_64-linux-gnu/libMesaOpenCL.so*  | grep clGetPlatformIDs
#

# objdump -Tx /opt/rocm-backup/opencl/lib/x86_64/libOpenCL.so.1  | grep clGetPlatformIDs
00000000000034e0 g    DF .text	00000000000000e2  OPENCL_1.0  clGetPlatformIDs

# objdump -Tx /opt/amdgpu-pro/lib/x86_64-linux-gnu/libOpenCL.so.1  | grep clGetPlatformIDs
0000000000002f10 g    DF .text	00000000000000e2  OPENCL_1.0  clGetPlatformIDs
```

But I'd love to be proved wrong.


---

### 评论 #46 — rhlug (2018-06-06T21:49:38Z)

@tekcomm  i give zero shits about polaris cards on linux.   the only thing that matters to me at this point is solving the vega riddle on linux.   i have cryptonight-heavy solved, 1300h/s on vega56 right now.   Based on those hashrates, I should be able to get 1800-1900 on cryptonightv7, but trying to run cryptonightv7 against 18.20 drivers results in 

```
[   73.116566] amdgpu 0000:03:00.0: [gfxhub] VMC page fault (src_id:0 ring:24 vmid:5 pasid:32769)
[   73.116571] amdgpu 0000:03:00.0:   at page 0x0000000304dfd000 from 27
[   73.116574] amdgpu 0000:03:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x00501030
[   86.306453] amdgpu 0000:03:00.0: [gfxhub] VMC page fault (src_id:0 ring:24 vmid:5 pasid:32769)
[   86.306458] amdgpu 0000:03:00.0:   at page 0x0000000304dfc000 from 27
[   86.306461] amdgpu 0000:03:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x00501030
```

From what I gather, a regression in llvm may have carried over into these drivers.   Although it may just be kernel dependant.  I've got to try something newer than rc2 I suspect.

```
https://bugzilla.redhat.com/show_bug.cgi?id=1562946
```

More to come...


---

### 评论 #47 — rhlug (2018-06-06T22:07:02Z)

And let me clarify a bit more.  I've ran my Vegas under ethminer with Mesa 18.2 / LLVM 6 / Ubuntu 16.04 since November.     I have also had working cryptonight and variants working on my Vegas at lack luster speeds (1200+ cn7).  None of that matters...    

The issue at task here is what the subject says 
```
ROCm RX VEGA hash rates for Cryptonight (linux vs windows)
```

My goal is to get 1400-1500 cn-heavy and 1900+ cn7 on linux, to be on par with windows, because I despise windows.  Right now, the closest I've been is with the 18.20 drivers getting 1300 on heavy.    But cant get cn7 going on it.   

Hoping rocm 1.9 is the answer too all the problems.

---

### 评论 #48 — gstoner (2018-06-06T22:30:20Z)

We did not drop the ball.  OpenCL 2.0 was for Integrated Graphics not a DGPU.   Also blame Apple, NVIDIA, at the time they did not Invest in 2.0 so we had stayed with what the Commercial application used 
 
In Catalyst with OpenCL  2.0 you had load of fun. 
- PIPES - with a work in progress  spec 
- Device Enqueue - that realy did not work 
- SVM with Fine Grain Memory Access - APU Only 
- SVM with Coarse Grain Memory - Access where when you add more then one 1 GPU the total 4 GB of Memory you can access via your kernel is now 4 GB/n per GPU you add into your system.   Aka 4 GPU each gpu can access only 1 GB of memory if you enable SVM. 
- Deferred memory allocation where you have to throw away the result from your first run 
- PCIe Subsystem that had I/O bandwidth performance latency issues 

With ROCm we have OpenCL 2.0 Kernel support now with OpenCL 1.2 host API 

The only thing we missing right now in the current OpenCL stack for ROCm is Device Enqueue and it coming.   Plus you now can use Coarse Grain SVM you do no have limits on Catalyst for memory allocation. 

With SVM you do not have Catalyst issue 

---

### 评论 #49 — gstoner (2018-06-06T23:14:23Z)

@tekcomm Yes, the SVM thing was dumb in the catalyst driver.     

 I ask to get one of these ASUS 19 GPU motherboards, so we can do testing with it.   Also asked the Linux team to put it in there CI environment. See if we can get to break their firmware and driver.

We have the new Vega in the Lab, it is much better GPU.    Vega10 would be a big dark subject in my memoirs if ever write a book.  Vega next driver running and the stack is up.  I can not wait for it to get into the wild much better animal.  

---

### 评论 #50 — Zarkoob (2018-06-06T23:17:05Z)

Doc, Good luck trying the 19 board! Tell me how it is cuz my Asrock H110 ports are so close that they cross talk :( such garbage 

---

### 评论 #51 — gstoner (2018-06-06T23:17:45Z)

@tekcomm On Vega10 have you tried this.   

If you Plan to Run with X11 - we are seeing X freezes under load.   

ROCm 1.8.1 a kernel parameter noretry has been set to 1 to improve overall system performance. However, it has been proven to bring instability to graphics driver shipped with Ubuntu. This is an ongoing issue and we are looking into it.

Before that, please try to apply this change by changing noretry bit to 0.

echo 0 | sudo tee /sys/module/amdkfd/parameters/noretry
Files under /sys won't be preserved after reboot so you'll need to do it every time.

One way to keep noretry=0 is to change /etc/modprobe.d/amdkfd.conf and make it be:

options amdkfd noretry=0

Once it's done, run sudo update-initramfs -u. Reboot and verify /sys/module/amdkfd/parameters/noretry stays as 0.


---

### 评论 #52 — Zarkoob (2018-06-06T23:37:06Z)

Hah I’ll just settle for a “stargate”.  But Doc the board looks a beaut. Tell me how it goes. They placed the usb connectors on board for the risers right? Looks like they spaced them far enough for less cross talk! Woo hoo. 

---

### 评论 #53 — Zarkoob (2018-06-06T23:42:05Z)

For a stargate? Ok! 

---

### 评论 #54 — rhlug (2018-06-07T00:53:36Z)

> Your really gonna hate me but, I get 2200 on cn7 on linux with 2x2 2 570's
and 2 560's

@tekcomm remember, i said i dont care about polaris?   I have plenty of 570's runing cn7 @ 985h/s and  cnheavy @ 715h/s.   if i wanted to redo bios with newer straps i could squeeze some more... but too lazy.

btw, drm-tip/2018-06-06/ was not the answer for VM_L2_PROTECTION_FAULT_STATUS.  So must be in the 18.20 driver... more waiting.  






---

### 评论 #55 — rhlug (2018-06-07T01:52:29Z)

> rhlug, I did not see the opencl 2x extensions on kronos till this feb.

you're right, just checked my eth tx's, they started in march.   i was mining monero on winblows from oct->feb.


---

### 评论 #56 — rhlug (2018-06-07T14:04:47Z)

Heavy rates on linux...   

Vega56 8gb, cryptonight-heavy.

```
GPU #0
-----------------------------------------------------------------------------------------
Totals (AMD):  1237.1 1236.5 1233.1 H/s
-----------------------------------------------------------------------------------------
GPU #1
-----------------------------------------------------------------------------------------
Totals (AMD):  1253.6 1253.9 1247.4 H/s
-----------------------------------------------------------------------------------------
GPU #2
-----------------------------------------------------------------------------------------
Totals (AMD):  1264.5 1264.1 1263.9 H/s
-----------------------------------------------------------------------------------------
GPU #3
-----------------------------------------------------------------------------------------
Totals (AMD):  1237.5 1237.0 1244.7 H/s
-----------------------------------------------------------------------------------------
Speed (ALL GPU): 4992.7  Shares (ALL GPU): 
```


RX 580 8GB, cryptonight-heavy

```
GPU #0
-----------------------------------------------------------------------------------------
Totals (AMD):  1020.6 1037.8 1042.0 H/s
-----------------------------------------------------------------------------------------
GPU #1
-----------------------------------------------------------------------------------------
Totals (AMD):  1040.3 1037.9 1025.4 H/s
-----------------------------------------------------------------------------------------
GPU #2
-----------------------------------------------------------------------------------------
Totals (AMD):  1021.9 1041.5 1035.0 H/s
-----------------------------------------------------------------------------------------
GPU #3
-----------------------------------------------------------------------------------------
Totals (AMD):  1013.5 1095.1 1045.6 H/s
-----------------------------------------------------------------------------------------
GPU #4
-----------------------------------------------------------------------------------------
Totals (AMD):  1021.0 1033.6 1045.1 H/s
-----------------------------------------------------------------------------------------
```


RX 570 4GB, cryptonight-heavy

```
GPU #0
-----------------------------------------------------------------------------------------
Totals (AMD):   774.7  774.8  775.1 H/s
-----------------------------------------------------------------------------------------
GPU #1
-----------------------------------------------------------------------------------------
Totals (AMD):   787.4  787.3  787.4 H/s
-----------------------------------------------------------------------------------------
GPU #2
-----------------------------------------------------------------------------------------
Totals (AMD):   788.5  788.5  788.5 H/s
-----------------------------------------------------------------------------------------
GPU #3
-----------------------------------------------------------------------------------------
Totals (AMD):   787.9  786.9  786.2 H/s
-----------------------------------------------------------------------------------------
GPU #4
-----------------------------------------------------------------------------------------
Totals (AMD):   786.5  786.3  786.1 H/s
-----------------------------------------------------------------------------------------
GPU #5
-----------------------------------------------------------------------------------------
Totals (AMD):   785.4  785.0  785.3 H/s
-----------------------------------------------------------------------------------------
```

So polaris rates on par with windows, and vega lacking just a bit, but not bad.



---

### 评论 #57 — rhlug (2018-06-07T14:27:59Z)

> Need to test the new rocm like greg suggested

My vegas want 4.17rc2+, but rocm 1.8.1 isnt dkms friendly there.     Once its dkms independant, it will be so much easier.


---

### 评论 #58 — gurupras (2018-06-07T15:00:41Z)

Apart from the straps/bios mods (on Polaris), can share the process of
reproducing this with the rest of us?

On Thu, Jun 7, 2018 at 10:28 AM, rhlug <notifications@github.com> wrote:

> Need to test the new rocm like greg suggested
>
> My vegas want 4.17rc2+, but rocm 1.8.1 isnt dkms friendly there. Once its
> dkms independant, it will be so much easier.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/325#issuecomment-395441016>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ACzB1zysY2jAfHkuhnO3g_4cg9Ah8yS3ks5t6Th0gaJpZM4R4X68>
> .
>


---

### 评论 #59 — rhlug (2018-06-10T20:18:41Z)

@gurupras 

reproducing what exactly?   my polaris and vega platforms are completely different.



---

### 评论 #60 — gurupras (2018-06-10T20:27:53Z)

The steps to reproduce vega cryptoknight-heavy hashrates on Linux. Not sure
if I can really help, but maybe enough stupid people trying things will
help out?

On Sun, Jun 10, 2018 at 4:18 PM, rhlug <notifications@github.com> wrote:

> @gurupras <https://github.com/gurupras>
>
> reproducing what exactly? my polaris and vega platforms are completely
> different.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/325#issuecomment-396078973>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ACzB12nyveabHRi8de_QtmNsF4ITY7gkks5t7X8ngaJpZM4R4X68>
> .
>


---

### 评论 #61 — rhlug (2018-06-10T20:39:43Z)

@gurupras 

pretty simple.

* install ubuntu 18.04
* replace kernel with one of them we have talked about on Issue #404 (if you want working powerplay
* install amdgpu pro 18.20
* install xmr-stak 2.4.4.
* replace pp_tables to adjust sclk, mclk, and voltage, then start miner

On my reference 56s, I see pretty much same hashrates with 56 bios @ 1405mhz/955mhz/900mv as 64 bios @ 1405mhz/1095mhz/900mv

Probably some tighter timings on the 56 bios.


---

### 评论 #62 — rhlug (2018-06-11T03:37:57Z)

Got a couple new 64's to test.   Conservative clocks, power save pp_table

```
# gpus
 ID       Name  Sclk  Mclk Volts Watts  Temp   Fan
============================================================
  0   rxvega64  1309  1053   900   104    53   36%
  1   rxvega64  1331  1053   900   106    56   36%
============================================================
  2                                210
```

Vega 64 Heavy rates

```
# watchrates
MINING xhv
GPU #0
-----------------------------------------------------------------------------------------
Totals (ALL):   1335.9 1335.4 1335.6 H/s
-----------------------------------------------------------------------------------------
GPU #1
-----------------------------------------------------------------------------------------
Totals (ALL):   1288.6 1305.7 1317.0 H/s
-----------------------------------------------------------------------------------------
Speed (ALL GPU): 2624.5 
```

I think I can push these 1400-1450 with higher clocks and maybe a bit more voltage.



---

### 评论 #63 — uentity (2018-06-12T08:48:09Z)

Do somebody have any success in launching `xmr-stak` with `cryptonight7` algo on top of ROCm stack? Despite that my Vega 64 is now successfully detected (thanks to weakened PCIe atomics requirement in 1.8) miner is actually not mining anything (no single valid result).

There are no errors, OpenCL code compiles fine, but it's resulting size is less than 300 Kb and it produces no useful work. For comparison, size of "valid" compiled OpenCL binary is ~ 3 Mb (compiled using amdgpu-pro stack and working fine).

---

### 评论 #64 — 949f45ac (2018-06-12T11:12:49Z)

@uentity Just tested and it actually failed for me as well, on a Vega56. On a RX470, interestingly enough, it works, _but only if_ the OpenCL kernel is loaded from cache. On a clean run (deleted ~/.openclcache), it will compile the kernel, but then also stall at 0 H/s. On Vega it stalls even if the kernel was loaded from cache.

I’m going to shamelessly recommend using [my own project](https://github.com/949f45ac/xmr-stak-hip) to mine cn7 on Vega+ROCm combo, for the time being, if anyone desperately wants to.

---

### 评论 #65 — 949f45ac (2018-06-12T12:32:01Z)

@uentity Oh, I forget: Of course you have to `export HSA_ENABLE_SDMA=0` beforehand, to be able to actually run the Vega via something other than PCIe3.0x8-16. It does work with the normal `xmr-stak` then. Cf. issue #430.

---

### 评论 #66 — uentity (2018-06-13T05:47:28Z)

@949f45ac thanks for information! Will try it today.

BTW, did I get you right that `export HSA_ENABLE_SDMA=0` should fix upstream `xmr-stak` too?
Actually my Vega is sitting in PCIe3.0x8 slot (but atomics are missing), so theoretically I don't need this setting. But practice is always a little bit different ;-)

---

### 评论 #67 — gstoner (2018-06-13T13:25:03Z)

@uentity if you have slot that does not support atomics you need to set export HSA_ENABLE_SDMA=0

---

### 评论 #68 — uentity (2018-06-13T16:04:46Z)

@gstoner @949f45ac setting `HSA_ENABLE_SDMA=0` did some help: `xmr-stak` shows "normal" hashrate, not zero, and GPU temperature rises telling that it actually computing something.

But! It still cannot find any valid result. Seems like it computing trash and no answer is correct.

---

### 评论 #69 — rhlug (2018-06-13T19:09:27Z)

@uentity  also, dont waste your time trying amdgpu-pro 18.20.   xmr-stak reports 0 h/s on all gpu, and any opencl calls hang indefinitely after that.  i have to sysrq-trigger to reboot.   cryptonight-heavy works fine w/ 18.20.

---

### 评论 #70 — gstoner (2018-06-13T19:11:29Z)

@rhlug on XMR-STACK, do you think this is Compiler or Runtime issue.    We had worked on XMR in the past on LC. 

---

### 评论 #71 — rhlug (2018-06-13T19:49:59Z)

@gstoner  i havent been able to get to the bottom of it, but I havent spent alot of time on it yet.   i did test cryptonight-v7 with llvm/clang v5, v6, v7 packages, and from what I could tell, the resulting compiled kernels nearly the same, so I'm leaning toward runtime.   I'm going to build xmrig-amd and sgminer-gm when I get a chance and see if they suffer similar fates.


---

### 评论 #72 — rhlug (2018-06-15T20:53:02Z)

Cryptonight-heavy worked fine with xmrig-amd.

Cryptonightv7 exhibits similar behavior to xmr-stak under 18.20 drivers.  zero hashrate, future opencl interaction hangs.



---

### 评论 #73 — gstoner (2018-06-16T01:14:49Z)

@rhlug we have compiler optimization in for SGminer https://reviews.llvm.org/D48246 for performance 

---

### 评论 #74 — Joe-Lapetoire (2018-06-21T18:18:28Z)

An old bench when i had tried a vega 64 : 
XMRIG-AMD - 2 THREAD (INTENSITY: 2032 / WORKSIZE: 8) - SCLK 1630MHZ - MCLK 1105MHZ - FAN 75% (FAN = 175) - AMD 17.50 + ROCM
=> 1380 H/s @ 145w

You don't do better H/rate actually ?

---

### 评论 #75 — pacf531 (2018-09-15T02:07:16Z)

So just a report, I installed rocm 1.9 (on Linux kernel 4.18.7 without rock-dkms, using upstream vanilla interface, not sure if it makes a difference) to do a comparison to see if the performance difference has been fixed. At stock settings(mostly except for a maxed power limit of 220W on each OS) on a Vega Frontier Edition, I did a benchmark run of the compiled latest dev source code of xmr-stak, which lasts 60 seconds.

Windows 10
[2018-09-14 18:49:58] : Benchmark Thread 0 amd: 923.1 H/S
[2018-09-14 18:49:58] : Benchmark Thread 1 amd: 939.6 H/S
[2018-09-14 18:49:58] : Benchmark Total: 1862.7 H/S

Linux
[2018-09-14 18:54:42] : Benchmark Thread 0 amd: 615.2 H/S
[2018-09-14 18:54:42] : Benchmark Thread 1 amd: 600.1 H/S
[2018-09-14 18:54:42] : Benchmark Total: 1215.3 H/S

Seems like the performance difference has yet to be resolved yet, unless I did something terribly wrong.

---

### 评论 #76 — ob7 (2018-09-21T06:13:17Z)

someone is getting close, 4 vegas running at 7000 hashes:
https://www.reddit.com/r/MoneroMining/comments/9bq42w/vega_mining_guide_for_linuxubuntu_is_here/

It's not using rocm though, but still some good info there.

---

### 评论 #77 — CthulhuVRN (2018-09-21T09:33:38Z)

@ob7, if you get a closer look you'll see it's only "max" jump, but average is about 3000 H/s only.

---

### 评论 #78 — pacf531 (2018-09-24T07:24:37Z)

Copied over from xmr-stak issue about ROCm invalid results, which still hold true, but performance figures from 15 minute hashing tests with GPU-only. I updated to start using amd-drm-staging-next which is around 4.19 rc1 and 100% fans since for some reason, fan control is broken for my Vega Frontier edition so high temperatures essentially will crash the card.

Windows 10 Adrenalin 18.5.1 stock clocks with 100% fans

> HASHRATE REPORT - AMD
> | ID | 10s | 60s | 15m | ID | 10s | 60s | 15m |
> | 0 | 943.3 | 942.8 | 942.4 | 1 | 941.9 | 942.2 | 942.3 |
> Totals (AMD): 1885.2 1885.0 1884.7 H/s
> 
> RESULT REPORT
> Difficulty : 57180
> Good results : 49 / 49 (100.0 %)
> Avg result time : 19.4 sec

Windows 10 Adrenalin 18.5.1 Custom Powerplay with 100% fans

> HASHRATE REPORT - AMD
> | ID | 10s | 60s | 15m | ID | 10s | 60s | 15m |
> | 0 | 1079.2 | 1081.7 | 1084.8 | 1 | 1089.9 | 1086.8 | 1084.6 |
> Totals (AMD): 2169.2 2168.5 2169.4 H/s
> 
> RESULT REPORT
> Difficulty : 71430
> Good results : 53 / 53 (100.0 %)
> Avg result time : 17.8 sec

Linux ROCm 1.9 with amd-staging-drm-next (~Linux 4.19 rc1+) stock
with Wayland desktop and custom Powerplay with 100% fans

> HASHRATE REPORT - AMD
> | ID | 10s | 60s | 15m | ID | 10s | 60s | 15m |
> | 0 | 944.1 | 945.0 | 944.1 | 1 | 947.6 | 945.3 | 944.1 |
> Totals (AMD): 1891.7 1890.4 1888.2 H/s
> 
> RESULT REPORT
> Difficulty : 43380
> Good results : 49 / 57 (86.0 %)
> Avg result time : 19.9 sec
> 
> Error details:
> | Count | Error text | Last seen |
> | 8 | AMD Invalid Result GPU ID 0 | 2018-09-23 17:01:39 |

Linux ROCm 1.9 with amd-staging-drm-next (~Linux 4.19 rc1+)
with Wayland desktop and custom Powerplay with 100% fans

> HASHRATE REPORT - AMD
> | ID | 10s | 60s | 15m | ID | 10s | 60s | 15m |
> | 0 | 1089.9 | 1093.1 | 1094.0 | 1 | 1096.0 | 1093.4 | 1094.4 |
> Totals (AMD): 2185.9 2186.5 2188.4 H/s
> 
> Totals (ALL): 2185.9 2186.5 2188.4 H/s
> Highest: 2195.1 H/s
> 
> RESULT REPORT
> Difficulty : 60960
> Good results : 39 / 46 (84.8 %)
> Avg result time : 24.2 sec
> 
> Error details:
> | Count | Error text | Last seen |
> | 7 | AMD Invalid Result GPU ID 0 | 2018-09-23 16:31:19 |

So the main difference this time is installing rock-dkms as there seems to be something inside it that is causing the performance parity jump. I read somewhere that there was some improved copying semantics or something included that hasn't been included in upstream Linux yet, but would be nice to know. On the other hand, even though hashing is on par now if not better than Windows, the invalid results drag the hashrate down, although even with this deficit, it is way better than the 33% difference without rock-dkms. Since I am only one user, it would be nice to see if someone else can confirm similar results to mine and to see if this issue can finally be closed or not despite the invalid results situation.

---

### 评论 #79 — uentity (2018-09-24T18:55:39Z)

Hi, @pacf531 

I'm back to this ROCm theme after a long period of time. And I actually can confirm your results: with Vega64 + ROCm 1.9 + rock-dkms on kernel 4.15 (for some reason dkms modules won't compile for kernels v. 4.17+, missing `vga_switcheroo_...(smth)`) I'm getting `~1850 H/s`.
And I also experience invalid results.

What is interesting is that I have three Polaris GPUs on same machine in the same environment and they ALSO produce errors! Ratio is about 80% of good results and 20% of errors.
Hence, errors probably aren't caused by ROCm code itself, but by `rock-dkms` modules and/or `xmr-stak` itself (because Polaris cards aren't using ROCm but they do use the same AMDKFD modules from `rock-dkms`). So it's still an open question.

I see you also use `xmr-stak` so a couple of questions.
1) Did you notice any dependency between errors count and tuning params of `xmr-stack` AMD backend?
2) What settings for Vega GPU threads do you use?

---

### 评论 #80 — pacf531 (2018-09-25T05:12:19Z)

1.) I didn't do that in depth of testing with kernel versions after reinstalling ROCm because I essentially ran out of time during the weekend, but I will be retesting this weekend to see if there is and to see if with a lower kernel version the dkms error has any impact but I doubt it from your report. The issue is already being tracked in #473.

2.) I use the following for my Vega FE:

```
  { "index" : 0,
    "intensity" : 2024, "worksize" : 8,
    "affine_to_cpu" : 1, "strided_index" : 2, "mem_chunk" : 18,
    "unroll" : 8, "comp_mode" : false
  },
  { "index" : 0,
    "intensity" : 2024, "worksize" : 8,
    "affine_to_cpu" : 3, "strided_index" : 2, "mem_chunk" : 18,
    "unroll" : 8, "comp_mode" : false
  },
```
Running at 1422 core, 1150 memory clocks at 950 mV got me the hashrates I mentioned.

PS: I should mention this is not the best efficiency configuration as this uses anywhere from 15-30 more watts, but IMO it is worth it for me for the extra hashrate.

---

### 评论 #81 — ob7 (2018-09-29T18:30:18Z)

@pacf531 how do I set the clock speeds and mV?

---

### 评论 #82 — gurupras (2018-09-29T18:41:33Z)

@ob7 I'm sure there is a sane way of doing it, but one way I've found is to configure the softpptables on Windows and copy over the hex string without the commas into Linux. Once you have this, you can just convert this to binary and write it to `/sys/class/drm/cardX/device/pp_table`.

I vaguely recall that there were structs into which the data can be deconstructed into. I'd really appreciate it if someone can provide a reference to this or an existing library to use.

Here's a sample Golang program to achieve this. This is what I use with my Sapphire Vega64.  
**Use this at your own risk!!**


```
package main

import (
        "encoding/hex"
        "io/ioutil"
        "os"
        "log"
)

const CustomPPTable = `B6020801005C00E1060000EE2B00001B004800000080A90300F04902008E0008000000000000000000000000000002015C004F02460294009E01BE0028017A008C00BC0100000000720200009000A8026D0143019701F0490200710202020000000000000800000000000000050007000300050000000000000001082003840384038403840384038E0393030101890301018403000860EA00000040190100018038010002DC4A010003905F01000400770100059091010006C0D40100070108D04C01000000800000000000001C83010001000000000000000070A7010002000000000000000088BC010003000000000000000038C1010004000000000000000088D5010005000000000100000070D9010006000000000100000000260200070000000001000000000560EA00000040190100008038010000DC4A010000905F0100000008286E0000002CC9000001F80B0100028038010003905F010004F491010005D0B0010006C0D401000700086C39000000245E000001FC85000002ACBC00000334D0000004686E0100050897010006ECA30100070001683C01000001043C41000000000050C300000000008038010002000038C101000400000108009885000040B5000060EA000050C300000180BB000060EA0000940B010050C300000200E10000940B01004019010050C300000378FF0000401901008826010050C300000440190100803801008038010050C300000580380100DC4A0100DC4A010050C30000060077010000770100905F010050C300000790910100909101000077010050C300000118000000000000000BE412600960094B000A0054039001900190019001900190019001000000000002043107DC00DC00DC0090010000590069004A004A005F007300730064004000909297609600905500000000000000000000000000000000000202D4300000021060EA00000210`

func main() {
        b, err := hex.DecodeString(CustomPPTable)
        if err != nil {
                log.Fatalf("Failed to decode string: %v", err)
        }
        //ioutil.WriteFile("pp", b, 0664) // Uncomment this line if you want to write the output to a file
        file := os.Args[1]
        if err := ioutil.WriteFile(file, b, 0666); err != nil {
                log.Fatalf("Failed to write pp_table file: %v", err)
        }
}
```
To run it, you just:
```
    go build
    sudo ./pptable /sys/class/drm/cardX/device/pp_table; #Writing this file needs elevated privileges
```

---

### 评论 #83 — 949f45ac (2018-10-02T12:28:34Z)

So, all of you guys who got the normal OpenCL miner running at good speed on Linux now (albeit with errors), maybe you’d like to try the HIP-based miner I created? Potentially it does not have bad results (newer compiler, I believe), but possibly it is also slower or does not work at all or whatever. On ROCm 1.8.2 with kernel 4.15.0-33 it does the normal old low linux hashrate, but a bit more stable than the OpenCL miner.
On ROCm 1.9 I haven’t even been able to reproduce your results with the OpenCL miner, and sadly I’m a bit short on time right now. So maybe give it a shot?
https://github.com/949f45ac/xmr-stak-hip

---

### 评论 #84 — shimmervoid (2018-10-02T14:30:20Z)

@949f45ac I revisited your miner and able to hit upward of 1800 per thread on rocm 1.9 exluding tweaks as that might have been relevant to dkms (correct me if I'm wrong). I'm still learning these things. However problem [#1](https://github.com/949f45ac/xmr-stak-hip/issues/1) still plagues me as shown below. 

    root@cr-1:~/xmr-stak-hip/build/bin# uname -ar
    Linux cr-1 4.19.0-rc6-awesomeness #1 SMP Mon Oct 1 12:01:45 CDT 2018 x86_64 x86_64 x86_64 GNU/Linux

    HASHRATE REPORT
    | ID |  10s |  60s |  15m | ID |  10s |  60s |  15m |
    |  0 | (na) | 1794.3 | (na) |  1 | 1806.0 | 1805.2 | (na) |
    |  2 | 1806.5 | 1805.4 | (na) |  3 | 1806.5 | 1805.4 | (na) |
    -----------------------------------------------------
    Totals:   (na) 7210.3 (na) H/s
    Highest:  7212.8 H/s

Cheers,


---

### 评论 #85 — gstoner (2018-10-02T14:38:38Z)

Anyway you can track the rail voltage during the test,    Also can you use  rocm_smi_lib https://github.com/RadeonOpenCompute/rocm_smi_lib to track temp and clocks as you run the app

---

### 评论 #86 — 949f45ac (2018-10-02T15:02:30Z)

@shimmervoid Does it also have invalid results? Or is it stalling too soon to tell? If it doesn’t have invalid results, I could quickly rush a "simple version" that doesn’t have the complicated optimization that is probably causing the hang-ups. That’d still be a fine linux miner.

---

### 评论 #87 — shimmervoid (2018-10-02T15:05:50Z)

@gstoner I wish I understood how to use all the tools, One day though.

@949f45ac No invalids, got max of 8 results before malfunction. If you can seperate that branch on your repo, much gratitude.

---

### 评论 #88 — gurupras (2018-10-02T15:23:17Z)

@949f45ac @pacf531 Could you kindly elaborate on the setup so that I and others may try to reproduce results? Specifically: What distro and whether you had to make any other custom modifications?

---

### 评论 #89 — 949f45ac (2018-10-02T15:31:15Z)

@shimmervoid Try branch `tweaks` that I just pushed, please, possibly I forgot to commit some bug fix. `master` was stalling for me as well on 1.9, but version I just pushed keeps on trucking. Still no big hashrate on my machine, sadly. :)

---

### 评论 #90 — shimmervoid (2018-10-02T16:06:53Z)

@949f45ac you win the internet today in my world. 

    RESULT REPORT
    Difficulty       : 198638
    Good results     : 37 / 37 (100.0 %)
    Avg result time  : 28.0 sec
    Pool-side hashes : 6869984

    Top 10 best results found:
    |  0 |          7631493 |  1 |          4208637 |
    |  2 |          1263111 |  3 |          1209828 |
    |  4 |          1100450 |  5 |           908331 |
    |  6 |           728169 |  7 |           516094 |
    |  8 |           494310 |  9 |           493261 |

    Error details:
    Yay! No errors.

    HASHRATE REPORT
    | ID |  10s |  60s |  15m | ID |  10s |  60s |  15m |
    |  0 | 1831.6 | 1830.6 | 1830.4 |  1 | 1831.6 | 1832.5 | 1832.7 |
    |  2 | 1838.4 | 1837.4 | 1837.2 |  3 | 1833.9 | 1834.9 | 1835.3 |
    -----------------------------------------------------
    Totals:   7335.5 7335.4 7335.7 H/s
    Highest:  7343.8 H/s


---

### 评论 #91 — uentity (2018-10-02T18:33:58Z)

So, no errors on `xmr-stak-hip`? Hmm... Will surely give it a try! I checked out repo a long time ago but something went wrong I don't remember what exactly )

But does it really look like an errors are caused by upstream `xmr-stak` implementation? Or unhappy interaction between particular `xmr-stak` OpenCL code and `rock-dkms` driver?

---

### 评论 #92 — 949f45ac (2018-10-02T18:52:29Z)

Ok I’ve got it running fast now as well, vital info was in this issue: https://github.com/fireice-uk/xmr-stak/issues/1797
The key is to use latest amdgpu-pro on 4.15 (not sure which part exactly, --opencl=pal --headless does the job), then you can either use OpenCL binary compiled with OLDER amdgpu-pro or you can use `xmr-stak-hip`
Simply because the OpenCL compiler shipped with latest amdgpu-pro is bugged
And you have to use/install ROCm of course, not sure for what exactly in the case of OpenCL miners

edit: Alternatively, take kernel 4.18+ and install rocm without dkms, but make sure to add the kfd rule!!

---

### 评论 #93 — gstoner (2018-10-02T19:13:01Z)

Sounds like the fastest is AMDGPUpro base driver + rocr enabled OpenCL with HSAIL/SC enabled compiler    PAL enabled OpenCL runtime is being bypased 

---

### 评论 #94 — ddobreff (2018-10-02T22:40:45Z)

This is amazing, why didn't you do it over current xmr-stak dev? Probably separate branch hcc-hip?

---

### 评论 #95 — pacf531 (2018-10-06T20:15:13Z)

I realized now the reason why I have it hashing at that high of a hashrate was some amdgpu pro remnants and the binary not being up to date. Changing all of that, I get back to the previous results. The whole hybrid install + using a custom fork is way too much for me personally, so I probably will wait for the time being until ROCm itself is more stable. xmr-stak fixed the invalid shares issue now in their dev branch which ROCm is somehow messing up the opencl code there, which is probably good enough for now for anyone that wants to run the hybrid setup with vanilla xmr-stak.

@ob7 Yeah sorry, stuff came up but what @gurupras said was true, you could modify the voltages with with the new sysfs pp_od_clk_voltage but it saner and safer just to use soft powerplay tables and modify the pp_table instead which has been in the Linux kenel since 4.4, I found quite a few quirks with state switching and memory speed behavior using the first method.

I got a bit fed up with manual command line conversion of powerplay tables and needing to do the stripping manually so I made a quick CLI utility to convert Windows .reg files to a .bin file for applying to Linux, you can find it in my repositories.

---

### 评论 #96 — ddobreff (2018-10-07T11:43:14Z)

The custom soft pp table method will work for Vega on 4.18 but it will cause sdma failure on pre Vega, some patch broke soft pp table after mainline 4.17, even first 4.18-rc1 has the bug.

---

### 评论 #97 — 949f45ac (2018-10-07T16:12:37Z)

@ddobreff I didn’t do it on unified `xmr-stak` because cmake gave me enough of a hassle already.
I’ve quickly hacked together a version on top of xmrig now: https://github.com/949f45ac/xmrig-HIP
That’ll give you some of the more modern features like pool-failover and algo-switching (only cn/1, msr, xtl yet, so it works on moneroocean).
A v8 version may or may not come; won’t be at all trivial to build.

#### Also an update to my last post
You don’t need amdgpu-pro, 4.18+ kernel does indeed work fine. Only make sure you don’t forget adding the kdf rule (like I did): https://github.com/RadeonOpenCompute/ROCm/#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels

---

### 评论 #98 — shimmervoid (2018-10-07T17:19:12Z)

@949f45ac  Nicely done with xmrig. Keep the fire burning with HIP. Build it and they will come. Heterogeneous baby!

    | THREAD | GPU | 10s H/s | 60s H/s | 15m H/s | NAME
    |      0 |   0 |  1825.8 |  1826.9 |  1826.9 | Vega 10 XTX [Radeon Vega Frontier Edition]
    |      1 |   1 |  1825.0 |  1824.0 |  1824.0 | Vega 10 XTX [Radeon Vega Frontier Edition]
    |      2 |   2 |  1825.5 |  1827.0 |  1827.0 | Vega 10 XTX [Radeon Vega Frontier Edition]
    |      3 |   3 |  1835.1 |  1833.8 |  1831.7 | Vega 10 XTX [Radeon Vega Frontier Edition]
    [2018-10-07 12:10:20] speed 10s/60s/15m 7311.6 7311.8 7309.8 H/s max 7322.0 H/s



---

### 评论 #99 — ddobreff (2018-10-07T19:17:21Z)

Excellent again, but what I meant is that hip/hcc requires pci atomics to work and unfortunately disabling only works for Vega, so RX a.k.a Polaris series will not work unless they are on pcie gen.3 also pp_table editing for Polaris is broken in 4.18 and thats where hip/hcc is fully supported in kgd/kfd.

---

### 评论 #100 — uentity (2018-10-07T19:51:06Z)

I can confirm that latest update of `xmr-stak` fixes errors on Vega + ROCm 1.9.
But errors still remain on Polaris cards (rx 480/580). Tried both with amdgpu 18.30 and rocm kernel modules.

BTW, with latest `rock-dkms` update (1.9-224) I'm getting `< 900 H/s` on Vega 64, whilst with prev version and with 18,30 the hashrate is as expected `~ 1850 H/s`.

---
