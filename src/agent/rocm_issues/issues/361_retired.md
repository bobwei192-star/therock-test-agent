# retired... 

> **Issue #361**
> **状态**: closed
> **创建时间**: 2018-03-15T06:51:33Z
> **更新时间**: 2019-08-10T07:19:24Z
> **关闭时间**: 2018-08-19T16:39:08Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/361

## 描述

*(无描述)*

---

## 评论 (100 条)

### 评论 #1 — earlvanze (2018-04-21T19:13:41Z)

@tekcomm can you upload this elsewhere? MEGA has a 5 GB free transfer limit and I can't download the last 2 GB of the zip file. If this works for me I'd rather pay you the $5 they're charging.

---

### 评论 #2 — earlvanze (2018-04-21T20:06:04Z)

@tekcomm After 12 hours of leaving the MEGA app to sync the file to my computer, I finally got the entirety of the zip file! Thanks! Will flash and try it out now. It would be great to have Version 2 up on your GitHub as well rather than just this thread.

---

### 评论 #3 — BobDodds (2018-04-25T22:50:45Z)

My second time through reading. I will have my own block rippa https://www.meetup.com/Hampton-Roads-Blockheads-A-cryptocurrency-community/photos/28815999/470496043/

---

### 评论 #4 — rhlug (2018-04-26T15:32:11Z)

Only OpenCL that works for me w/ gfx900 is via Mesa/clover.     Using the  fkxamd/drm-next-wip (4.17.0-rc2) with 1.0.6 thunk libs now.   Just need some rocm userland to go with it at this point.


---

### 评论 #5 — Jokooono (2018-04-27T10:43:13Z)

Awesome work on this!
Is there any ETA on your V3? Sounds like exactly what i was looking for! Do you have a tipping address for btc/eth?

---

### 评论 #6 — rhlug (2018-04-27T15:17:26Z)

@tekcomm 
did you get that working on 16.04?   not sure where this clang headers come from.  i installed all llvm-7.0 packages 

```
In file included from llvm/codegen/bitcode.cpp:34:0:
./llvm/codegen.hpp:37:45: fatal error: clang/Frontend/CompilerInstance.h: No such file or directory
```
There are no Frontend headers in llvm-7.0-dev


---

### 评论 #7 — ylyskavets (2018-04-27T16:18:08Z)

> Since I compiled over 2 dozen other packages and included the source and the git and included it. The size limitations of a free github account does not permit it. 

@tekcomm May you try to prepare the image with Ansible or with Docker?

---

### 评论 #8 — earlvanze (2018-04-27T16:34:01Z)

Here's the image modified for 2-core CPUs:
https://github.com/earlvanze/AMD-ROCm-Miner

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1524846836)

On April 27, 2018 at 16:31 GMT, ylyskavets <notifications@github.com> wrote:

Since I compiled over 2 dozen other packages and included the source and the git and included it. The size limitations of a free github account does not permit it.

[@tekcomm](https://github.com/tekcomm) May you try to prepare the image with Ansible or with Docker?

—
You are receiving this because you commented.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-385020265), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3YoGnUL1ja5RB6tK0TqBcuWJhrBljks5ts0fTgaJpZM4Sro0i).

---

### 评论 #9 — 0x90v1 (2018-04-30T04:53:17Z)

Hey tekcomm,
first thanks for your awesome work :) Learning a lot from your stuff that you are sharing with us 👍 

Can't wait for the new recipe from you with the 18.04 :)

greeZ

---

### 评论 #10 — 0x90v1 (2018-04-30T05:00:34Z)

awesome, will reservate some sparetime on weds than :)

---

### 评论 #11 — BobDodds (2018-05-02T00:36:10Z)

Mega says that they will probably fail on our Download. They don't say so, but opening a free cloud storage account on Mega, then Sharing to our mega storage, instead of Download, can then make our Download go all the way through as a Sync.

Sync to local by running the Mega app on target computer where we will burn the flash with the huge dd, once it syncs to here.

Open a free mega account. Download the app. Share the big file over to mega cloud space. The mega app can then be set up locally do Sync the file to here.

I watched the recommended youtube vid of Linux flipping off Nvidia. Next vid on playlist, Linus interview, he defines Good Taste as ripping out, down to the proverbially elegant, yet to Linus simply more efficient, simplicity, like headless rtos rippa here.

---

### 评论 #12 — ghost (2018-05-07T18:50:25Z)

Hello, Could you please send me the v3 so I can test it on my vegas.
Thanks

---

### 评论 #13 — 0x90v1 (2018-05-15T13:38:42Z)

Hey tekcomm, do you have an idea when you can release your new version with the 18.04? ;) Also I'm willing to help you out with testing if you need it :) 

---

### 评论 #14 — puithove (2018-05-17T12:18:04Z)

Any chance you could post this a different way?  Maybe a torrent or something (I would seed it)?  Mega is kind fo a no-go.

---

### 评论 #15 — earlvanze (2018-05-17T12:47:42Z)

I have a version on Google Drive but the 4.13 kernel crashes so I've updated it to 4.16.3+ and will be reuploading an image this weekend. See https://GitHub.com/earlvanze/AMD-ROCm-Miner

[earlvanze/AMD-ROCm-Miner
AMD-ROCm-Miner - Dev userland for usb flash drive with full amd rocm and blockchain support plug and rock.](https://GitHub.com/earlvanze/AMD-ROCm-Miner)

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1526561255)

On May 17, 2018 at 12:18 GMT, Phil Uithoven <notifications@github.com> wrote:

Any chance you could post this a different way? Maybe a torrent or something (I would seed it)? Mega is kind fo a no-go.

—
You are receiving this because you commented.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-389846497), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3YtBC0_GK9jLgQgp_tLcurjunXtw9ks5tzWqAgaJpZM4Sro0i).

---

### 评论 #16 — BobDodds (2018-05-17T17:20:59Z)

The way to use mega is to open a free account, share a file into that rather than download, and then download and run mega's sync app which will download the file to local for free and not get stopped like a direct download probably will.

Edited...sitrep:

Intel Core i3-8100 (8th gen) Processor 4 Cores 3.6GHz  LGA1151 300 Series 65 Watts

MSI Z370 SLI PLUS LGA 1151 (300 Series) Intel Z370 HDMI SATA 6Gb/s USB 3.1 ATX Intel Motherboard - 3 x16 slots and two M.2 x16 module positions, so a total 5 pcie positions at x16.

CORSAIR Vengeance LPX 8GB (1 x 8GB) DDR4 DRAM 2400MHz C16 (PC4-19200) Memory Kit - Black

4 Diamond RX580 GDDR5 8GB cards

KingDian 2.5" 7mm SATA III 6Gb/s Internal Solid State Drive SSD for Desktop PCs Laptop ( 60GB )

Thermaltake Toughpower 1500W 80+ Gold Semi Modular ATX 12V/EPS 12V Power Supply 5 YR Warranty

Update: learning from headless Pi router, wannabe firewall, what need to ssh to rippa v2 headless with remote login from cafe with ac. There's a Russia Hack for Huawei e3372h cell modem, stick a pin in it and burn hacked firmware. My Huawei e3372h-153 was actually a e3372h-510, lobotimized, never mind. Orderred a Netgear LB1120 which offers bridge mode. It's a pretty good router as far as port forwarding, easy way out. iptables can change ttl to look like mobile--not hotspot--tmobile might ban hotspot/tether, and other things, so I want to set Netgear to bridge, grab wan ip and go on Pi with iptables, diy.

---

### 评论 #17 — puithove (2018-05-17T20:21:32Z)

Cool, I'll look for the re-spin this weekend.

---

### 评论 #18 — earlvanze (2018-05-25T18:27:17Z)

It's up on my GitHub fork, by the way. Look for the Google Drive link. Been running stably for days now. https://ethermine.org/miners/0x9eaba219ac4ac28c2c008b3d9968cdbb7c5250f0/dashboard

---

### 评论 #19 — ghost (2018-05-25T18:34:20Z)

@earlvanze does it work with vega?

---

### 评论 #20 — earlvanze (2018-05-25T19:25:52Z)

Good question, I never tried it because I don't have one to test with. The kernel I upgraded to is this: [https://github.com/M-Bab/linux-kernel-amdgpu-binaries](https://www.google.com/url?q=https://github.com/M-Bab/linux-kernel-amdgpu-binaries&sa=D&source=hangouts&ust=1525150968665000&usg=AFQjCNFURudzYx4GZBB53jsbfHvRzZuxCQ) as recommended by @tekcomm. It mentions Vega support. "Among these, is the new display code (previously called "DAL" or "DC") which is required for HDMI audio/sound and Vega/Raven generation display output."

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1527276348)

On May 25, 2018 at 18:34 GMT, abenhamo <notifications@github.com> wrote:

[@earlvanze](https://github.com/earlvanze) does it work with vega?

—
You are receiving this because you were mentioned.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-392144436), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3YgsJ9cj5_DH7tepB30v49PF9dmyaks5t2E6wgaJpZM4Sro0i).

---

### 评论 #21 — puithove (2018-05-25T19:29:01Z)

I downloaded the updated one with 4.16, but have had literally zero time to play with it unfortunately.  Hopefully I'll get a chance to this weekend, and if so I'll be trying it with a Vega Frontier Edition.

---

### 评论 #22 — earlvanze (2018-05-25T19:30:14Z)

Tekcomm has had more experience with modifying for Vega blockchain support.

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1527276608)

On May 25, 2018 at 19:29 GMT, Phil Uithoven <notifications@github.com> wrote:

I downloaded the updated one with 4.16, but have had literally zero time to play with it unfortunately. Hopefully I'll get a chance to this weekend, and if so I'll be trying it with a Vega Frontier Edition.

—
You are receiving this because you were mentioned.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-392157700), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3YpqBb3tFRxzekIPQYo8nwjPwKm21ks5t2FuDgaJpZM4Sro0i).

---

### 评论 #23 — puithove (2018-05-25T21:55:50Z)

Well, I just started playing with it, but initial thoughts is it doesn't look good for VEGA FE - Claymore says no OpenCL devices available.

lspci says the card is there and driver is loaded:
```
00:05.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 6863
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device 6b76
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```

But clinfo says:
```
root@AMD-rocm-rippa:/opt/rocm/opencl/bin/x86_64# ./clinfo 
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted
```

Just had a few minutes to play, and that time has run out.  Gotta punt for now and put cast-xmr back to work under Windoze.

---

### 评论 #24 — earlvanze (2018-05-26T04:59:17Z)

I tweaked the core clock settings to get better temps and power draws while keeping the same hashrate. Claymore says ~144 MH/s on my first rig, ~142 MH/s on 2nd rig, each with 5 RX580s on an Asus Z270-A Prime and Intel Celeron. Temps all under 60°C and 82-101 Watts per GPU.

Generally the only mods I did in the BIOS are memory straps. Underclocking done in software using rocm-smi. Claymore clock and voltage settings don't seem to actually do anything using the AMD ROCm drivers but ROCm itself can adjust clocks and voltages somewhat automatically. I think memory clocks have to be done in BIOS though.

After tweaking the GPU core clocks using
```
rocm-smi -d gpuid# --setsclk #
```
I modified rc.local to modify/add the following for each card at the bottom of the file, depending on the # I found lowered the clock and power consumption without affecting the hashrate for Ethereum solo mining with Claymore.
```
echo manual > /sys/class/drm/card{gpuid#}/power_dpm_force_performance_level
echo # > /sys/class/drm/card5/pp_dpm_sclk
```

You can see compatible clock settings using ```rocm-smi -s```

I opted to only modify memory straps in the BIOS so I can adjust and modify via software remotely and keep them running stably. I don't wanna have to travel 4+ hours and boot into Windows and mod each of 15 GPUs just to adjust the clocks for each GPU. Software underclocking is much easier and more reliable.

---

### 评论 #25 — earlvanze (2018-05-26T05:30:03Z)

ETH - Total Speed: 144.438 Mh/s, Total Shares: 95(14+26+21+19+15), Rejected: 0(0+0+0+0+0), Time: 00:43 
ETH: GPU0 27.756 Mh/s, GPU1 30.008 Mh/s, GPU2 29.204 Mh/s, GPU3 28.256 Mh/s, GPU4 29.214 Mh/s 
Incorrect ETH shares: none 
 1 minute average ETH total speed: 144.444 Mh/s 
Pool switches: ETH - 0 
Current ETH share target: 0x0000000112e0be82 (diff: 4000MH), epoch 189(2.48GB) 
Current -dcri values: -dcri 20,8,6,12,12 
GPU0 t=54C fan=47%, GPU1 t=54C fan=60%, GPU2 t=55C fan=47%, GPU3 t=55C fan=80%, GPU4 t=55C fan=80%

Fans seem to automatically adjust according to the temperature. I don't have any external cooling at the moment, but tomorrow I will install a 440 CFM heat buster fan and put everything inside a grow tent to isolate the heat and push it somewhere else.

---

### 评论 #26 — gstoner (2018-05-27T17:21:27Z)


Guys we opensource so you can do what you want.

ROCm has no issue with Vega10 running in  a system as the card was designed in x8 or x16. PCIe Gen3 slot,  but miner are using Vega10 in any PCIe slot in the system, with riser ( which can inhibit proper PCIe training )  with substandard PCIe switches.  Motherboards that honestly that barely test if the SBIOS is correct with GPU.    We run tests ( Deep Learning and HPC )  on Xeon based server for 14 to 30 day looking for failure running heavy duty workloads.  


UserLand is ROCm, it sits on the base driver  AMDGPU + KFD + THUNK, this also shipped with AMDGPUpro up until 18.20.  Now AMDGPUpro, Now OpenCL sits on PAL they same base as Vulkan. But it uses the same compiler as it did before with AMDGPUpro as of 17.50.  LLVM HSAIL/SC, not this is the same compiler used on GFX7 and GFX8 GPU with older ORCA base. 

ROCm 1.8 removed the need for PCIe Atomics for only Vega10, we looking for GFX8 IP for future release,  We also drop the need for x8 Lane minimum you can run to your heart content on x1 lane now even PCIe Gen2 with it 20% penalty for the protocol.   If you put GPU direct connected or properly engineered PCIe Switch that has been tested your on your own, we never can guarantee it works  

Remember we pushed to give you more control of Power which has now gone upstream 

On Compiler, there are two compilers now from AMD,   
- HSAIL/SC based Backend  and Open Source Native Code Generator in LLVM 
         - Source for native code generator  https://github.com/llvm-mirror/llvm 
- First, they both share the same 
       - Clang-based Frontend and 
       - Device Libraries https://github.com/RadeonOpenCompute/ROCm-Device-Libs 
They both use LLVM for base compiler technology.  One writes out to IL HSAIL the other drops to full code native generator. 

Also 17:50 was OpenCL rocr with HSAIL/SC compiler. It also had an older version of KFD and THUNK. 

I can look to ship the proprietary compiler with LLVM to HSAIL/SC code generator to be part of the ROCm binary release as package so you can A/B since some time it may be the better compiler for other apps LLVM native will be.  But we working we made a choice to drive to open source components so you could have full visibility into them and also help us improve code generation. 

ROCm does one thing Windows driver does not do it checks out of bound memory references.  App now fails if Kernel is doing out of bound memory reference.  Prior to OpenCL foundation, ORCA and the even newer PAL will just pass these kernel through. 

On HBCC, this is not what is giving the performance lift on Windows, it was a firmware bug that team has been trying to understand.  



---

### 评论 #27 — willietes (2018-05-30T18:57:56Z)

This super news! Do you have a link for the rocm-rippa version 3? I have 18 vega64s busting to try it!!!  

---

### 评论 #28 — sayyiditow (2018-06-03T09:44:56Z)

What is the maximum number of vega GPUs supported on ubuntu + rocm latest + 4.17 kernel? 

---

### 评论 #29 — sayyiditow (2018-06-03T12:28:02Z)

Weird, I cant seem to get go passed 7. Maybe I am total noob. 6 are working perfectly fine, when I add 7 or more, the ubuntu gets stuck at a black screen just before the login. With a cursor like it has hanged, and I have to force shut down. Could it be the pcie speed? Must I use gen3? I tried gen3 and got a hang so went back to gen2. Thanks for the assistance @tekcomm 

---

### 评论 #30 — sayyiditow (2018-06-03T12:28:30Z)

Oh and I followed this to add rocm: https://github.com/RadeonOpenCompute/ROCm

---

### 评论 #31 — gstoner (2018-06-03T12:56:36Z)

@Sayyiditow This thread for custom version of AMDGPU driver that leverage ROCm and other Components that Tekcomm/Doctor developed. 

We now we can hit 14 GPU in Supermicro Server system with standard ROCm.   PCIe Config Space Memory allocated by the system bios become the control point to the upper limit of number of GPU  you can support.   You can see all the memory that allocated in PCIe Config space via LSPCI. 

---

### 评论 #32 — sayyiditow (2018-06-03T14:25:13Z)

Oh I will give it another try with gen3, and check the memory allocated to see if it helps.

---

### 评论 #33 — oaeide (2018-06-05T00:08:42Z)

@tekcomm Is there a download link for V3?

---

### 评论 #34 — willietes (2018-06-05T16:55:30Z)

This constitute as torture. Send me a link :-). 
The FOMO is killing me lol!


---

### 评论 #35 — ghost (2018-06-05T16:57:07Z)

willets, get on earl :)

On Tue, Jun 5, 2018 at 12:55 PM, willietes <notifications@github.com> wrote:

> This constitute as torture. Send me a link :-).
> The FOMO is killing me lol!
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-394783398>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wycEJd4-J47UKYbFffvQ6Nty6t_oks5t5rgbgaJpZM4Sro0i>
> .
>


---

### 评论 #36 — willietes (2018-06-05T17:03:36Z)

Sweet ! thanks a mil

---

### 评论 #37 — willietes (2018-06-05T18:23:54Z)

Ok Cool So I can build the distro with all functionailty myself ?

---

### 评论 #38 — willietes (2018-06-05T18:43:30Z)

> Right now its the great kernel debate.
Interesting what is on the agenda for discussion?

---

### 评论 #39 — 0x90v1 (2018-06-08T19:54:17Z)

hey Doctore, is there a possibility to get the rocm-rippa version 3 already? :) Can't wait for it and exploding, incredible curious # #

---

### 评论 #40 — earlvanze (2018-06-09T16:21:23Z)

That's a super crucial feature. I wonder if it resolves OpenCL hang in
Claymore.

On Sat, Jun 9, 2018, 4:29 AM The Doctor <notifications@github.com> wrote:

> Okay guy please see Earl for Rippa, I am working the last feature :P
> GPU RESET handling :)
> no more crashing even it it does reset it does not matter it will continue
> in within 2 seconds
>
> So when
> [ 5837.283784] [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring gfx timeout,
> last signaled seq=98965, last emitted seq=98966
> [ 5837.283788] amdgpu 0000:06:00.0: GPU reset begin!
> [ 5837.575081] amdgpu 0000:06:00.0: GPU pci config reset
> [ 5837.683712] amdgpu 0000:06:00.0: GPU reset succeeded, trying to resume
> [ 5837.683761] [drm] PCIE GART of 256M enabled (table at
> 0x000000F400000000).
> [ 5837.683790] [drm:amdgpu_device_gpu_recover [amdgpu]] *ERROR* VRAM is
> lost!
> [ 5837.687778] amdgpu: [powerplay] dpm has been enabled
> [ 5837.806938] [drm] UVD and UVD ENC initialized successfully.
> [ 5837.906905] [drm] VCE initialized successfully.
> [ 5838.437076] [drm] recover vram bo from shadow start
> [ 5838.445516] [drm] recover vram bo from shadow done
> [ 5838.445517] [drm] Skip scheduling IBs!
> [ 5838.445537] amdgpu 0000:06:00.0: GPU reset(1) successed!
> Blows up you rig it won't matter :)
> It will continue in less then 1 second
>
>
>
> On Fri, Jun 8, 2018 at 7:41 PM, BobDodds <notifications@github.com> wrote:
>
> > Check this howto, 0x90v1: https://github.com/
> > RadeonOpenCompute/ROCm/issues/361#issuecomment-385870283 <http://url>
> >
> > —
> > You are receiving this because you were mentioned.
> > Reply to this email directly, view it on GitHub
> > <
> https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-395920003
> >,
> > or mute the thread
> > <
> https://github.com/notifications/unsubscribe-auth/AWn0wxXMDYLnHcCZYaE15g5msG2YDr2Zks5t6wutgaJpZM4Sro0i
> >
> > .
> >
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-395951147>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ADj3YuM2HKyTqJAly62kGwh6BWnIMpTvks5t64djgaJpZM4Sro0i>
> .
>


---

### 评论 #41 — plox99 (2018-06-18T05:12:51Z)

Guys how to install .dd image true?
I tried to burn .dd to flash by Rufus, and after that i succefully boot but have a fail in process
> nohup: appending output to 'nohup.out'
https://pp.userapi.com/c849224/v849224084/abdc/A2Mr5dFRFSs.jpg

What I have made not so?

---

### 评论 #42 — earlvanze (2018-06-18T05:18:20Z)

That's not a failure, that's a success and the output is appended to the logfile located at /nohup.out

To view log, type: sudo cat /nohup.out

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1529299094)

On June 18, 2018 at 5:12 GMT, plox99 <notifications@github.com> wrote:

Guys how to install .dd image true?
I tried to burn .dd to flash by Rufus, and after that i succefully boot but have a fail in process

nohup: appending output to 'nohup.out'
https://pp.userapi.com/c849224/v849224084/abdc/A2Mr5dFRFSs.jpg
What I have made not so?

—
You are receiving this because you were mentioned.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-397943728), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3Ygj_rPZP2prsCbvVZUp2vlJlFjyrks5t9zbZgaJpZM4Sro0i).

---

### 评论 #43 — plox99 (2018-06-18T05:21:08Z)

So i just need to wait more? I waiting arout 10 min and nothing changes, its ok?

---

### 评论 #44 — earlvanze (2018-06-18T05:56:14Z)

Nothing is supposed to change. The output is appended to /nohup.out. SSH into the system and cat (read) the file.

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1529301370)

On June 18, 2018 at 5:21 GMT, plox99 <notifications@github.com> wrote:

So i just need to wait more? I waiting arout 10 min and nothing changes, its ok?

—
You are receiving this because you were mentioned.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-397944706), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3Yp6BgcdOTBmzU3SZyNAWupkerFqPks5t9zjIgaJpZM4Sro0i).

---

### 评论 #45 — plox99 (2018-06-18T06:35:25Z)

So, i open it and file is empty

---

### 评论 #46 — plox99 (2018-06-18T06:51:12Z)

Dear Earl, can you write a mini-guide about how to install and boot this rippa?
After downloading zip, unzip it and what to do next.
Something like that? please?

---

### 评论 #47 — earlvanze (2018-06-18T15:02:40Z)

Read the Readme.md on my GitHub fork.

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1529334158)

On June 18, 2018 at 6:51 GMT, plox99 <notifications@github.com> wrote:

Dear Earl, can you write a mini-guide about how to install and boot this rippa?
After downloading zip, unzip it and what to do next.
Something like that? please?

—
You are receiving this because you were mentioned.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-397957917), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3YjGlDm7yELs3VQBo4ZF3hVlRwPKtks5t903kgaJpZM4Sro0i).

---

### 评论 #48 — BobDodds (2018-06-21T01:59:14Z)

["If you're using risers,](https://github.com/earlvanze/AMD-ROCm-Miner/blob/master/README.md) you will not be able to take advantage of PCIe Atomics. Set your motherboard to PCIe Gen 1."

I bought typical risers. Uh-oh. Luckily I've been shot out of several LZ's, still holding my parts, so I could change.

Are [these x16 ribbon cables](https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=x16+ribbon+pcie&rh=i%3Aaps%2Ck%3Ax16+ribbon+pcie) on x16 mbo slots a way to have pcie atomics with a physical jack up(rise)?

M2 m-keys just have usb, though allegedly x16, so still no way pcie3 atomics?

I have 4 RX580 cards, but only 3 x16 slots and one M2 "x16" m-key but that's usb out the m-key.

Earl's fork v2 is [here for download?](https://drive.google.com/open?id=1iel3XKQtI0Z-HPDELonKDxF4gaEYYWDb)
Earl's fork [readme.md?](https://github.com/earlvanze/AMD-ROCm-Miner/blob/master/README.md)

---

### 评论 #49 — BobDodds (2018-06-21T02:12:34Z)

Earl diff: "start-rtlinux.sh was modified from the original image to work on Intel Celeron dual-core CPUs. Note that PCIe Gen3 does not work on Celeron or Pentium CPUs. Your motherboard must be set to PCIe Gen1 or Gen2. If you're using risers, you will not be able to take advantage of PCIe Atomics. Set your motherboard to PCIe Gen 1.", where I have quadcore i3-8100 8th-gen with 8th-gen compatible mbo. So, I compare tekcomm and earl's start-rtlinux.sh to use quadcore.

---

### 评论 #50 — earlvanze (2018-06-21T05:17:54Z)

My i5-7500 test/gaming machine (rig4 branch) is also modified for quad-core.

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1529558268)

On June 21, 2018 at 2:12 GMT, BobDodds <notifications@github.com> wrote:

Earl diff: "start-rtlinux.sh was modified from the original image to work on Intel Celeron dual-core CPUs. Note that PCIe Gen3 does not work on Celeron or Pentium CPUs. Your motherboard must be set to PCIe Gen1 or Gen2. If you're using risers, you will not be able to take advantage of PCIe Atomics. Set your motherboard to PCIe Gen 1.", where I have quadcore i3-8100 8th-gen with 8th-gen compatible mbo. So, I compare tekcomm and earl's start-rtlinux.sh to use quadcore.

—
You are receiving this because you were mentioned.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-398954018), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3YvNwB3-03OCl-_HVt6kTLfPoQbK4ks5t-wEagaJpZM4Sro0i).

---

### 评论 #51 — gstoner (2018-06-21T14:18:14Z)

@tekcomm  I picked up the ASUS B250 and ASROCK H110 Pro as promised.   We let you know how it goes  

---

### 评论 #52 — ghost (2018-06-21T14:28:22Z)

Hey Greg  also on the B250 I found out that if enble mining mode it screws
them up because it enables pci-express one and don't ask me why they did
that I have no idea and causes problems

On Thu, Jun 21, 2018, 9:23 PM Jason Kurtz <tekcommnv@gmail.com> wrote:

> Greg i tried to your email address as a gift card in Newegg and for some
> reason since it's a Google account or something they blocked it. So I order
> the boards locally and I'm sending them out to you next week when my
> business partners in Vegas 6GPU unit and then once I'm done testing the 19
> GPU one I'll send it out
>
> On Thu, Jun 21, 2018, 9:18 PM Gregory Stoner <notifications@github.com>
> wrote:
>
>> @tekcomm <https://github.com/tekcomm> I picked up the ASUS B250 and
>> ASROCK H110 Pro as promised. We let you know how it goes
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-399119761>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0w2KtGNSFUGHXsV1ZJY1Da98D-T20ks5t-6stgaJpZM4Sro0i>
>> .
>>
>


---

### 评论 #53 — BobDodds (2018-06-21T18:01:50Z)

So it can't hurt to enable or permit pcie3, but is absolutely wrong to assume that Mining Mode is a magic mountain mantra moses word to the wise from anonymous hierarchy.

How about that about x16 usb risers, just for kids? Instead, use the ribbon cables(https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=x16+ribbon+pcie&rh=i%3Aaps%2Ck%3Ax16+ribbon+pcie) be better there? (or just leave cards in mobo slots? if ppl assume that they are using risers for cooling by a rack of fans, tekcomm has described his cooling setup relying on ducting more than fans,"Power usage is 24/ monitor and is at 97.5 watts per card for a total of 195 per 3gpu + 145 Complete system. for about 440w. There are now external powered items and only a [ram air intake with no moving parts that allows the boards to need no external cooling](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-373915974). Which of course like a cuda under glass, keeps all the gpus at 20 degrees above ambient with no external fans."

---

### 评论 #54 — BobDodds (2018-06-22T05:17:56Z)

So 3 [Amfeltec](http://amfeltec.com/) hose boards connect 12 backplanes to 3 mobo x16 slots, and I could be running 48 gpu's. Most of us will settle for 19 gpu's or less with the [$120-$140 mobo](https://amzn.to/2lsTuDa) though, judging by the hose board price. His [accent on host board sounds like hose board](https://youtu.be/Vm9mFtSq2sg) in the vid.

Amfeltec does actually use ribbon cables a lot in their products, but to each hose board, Amfeltec uses four cat6 ethernet cables for four pci express backplane clusters, each backplane clusterring four gpu's, four clusters of four, per hose board. Cat6, like any ethernet cable, has twisted pairs for noise reduction and that's why the gpu's can be ten feet away from the 3 hose boards on the motherboard.

---

### 评论 #55 — 0x90v1 (2018-06-22T18:11:51Z)

good a ugly error during the boot process with for GPU's. Three are working fine. Checkout the following error messages that I got: https://i.imgur.com/ZlILuKq.png

Somebody know's why? I also get the same with the IMG from earl so far. Hopefully u guys can help me :) thanks

---

### 评论 #56 — earlvanze (2018-06-22T19:23:21Z)

Amdgpu is the module referenced looks like a hardware or BIOS straps issue causing a driver or kernel fault.

[Earl Co - Contact Using Hop](http://GetHop.com/?_hmid=1529695395)

On June 22, 2018 at 18:11 GMT, 0x90v1 <notifications@github.com> wrote:

good a ugly error during the boot process with for GPU's. Three are working fine. Checkout the following error messages that I got: https://i.imgur.com/ttxsilP.png

Somebody know's why? I also get the same with the IMG from earl so far. Hopefully u guys can help me :) thanks

—
You are receiving this because you were mentioned.
Reply to this email directly, [view it on GitHub](https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-399531430), or [mute the thread](https://github.com/notifications/unsubscribe-auth/ADj3Yte6shIyd-5rBT2z-k_j31r4nGpMks5t_TNsgaJpZM4Sro0i).

---

### 评论 #57 — 0x90v1 (2018-06-22T20:00:38Z)

seems to be a problem with kernel 4.15. With 4.14 everything is working. But will go now for 18.04 first instad of 16.04. Thanks earl for your super fast replay :D

---

### 评论 #58 — earlvanze (2018-06-22T21:32:30Z)

My image is 4.16.3+ which shouldn’t have that issue. I haven’t gotten to do @tekcomm’s newest v3 image though.

> On Jun 22, 2018, at 4:00 PM, 0x90v1 <notifications@github.com> wrote:
> 
> seems to be a problem with kernel 4.15. With 4.14 everything is working. But will go now for 18.04 first instad of 16.04. Thanks eral for your super fast replay :D
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-399565494>, or mute the thread <https://github.com/notifications/unsubscribe-auth/ADj3YlTVezwCgG_GbZCGz2Wx_eWYidjdks5t_UzrgaJpZM4Sro0i>.
> 



---

### 评论 #59 — 0x90v1 (2018-06-22T21:46:00Z)

Just tried your image, same problem there also with 4.17 kernels.

---

### 评论 #60 — 0x90v1 (2018-06-23T14:48:15Z)

ah somebody figured out how to reset the GPU which crashed because of overclocking and the following dmesg: [  611.818778] amdgpu: [powerplay]
                failed to send message 5c ret is 0


---

### 评论 #61 — CMcCullough41 (2018-06-24T01:10:50Z)

Hey guys, does anyone know where I can find the 4.16.0-996-lowlatency kernel images and headers? Checked the linked repo and can't find it anywhere... haven't been able to compile rocm successfully for multiple vegas on the other low-latency kernels I've tried!

---

### 评论 #62 — vampyrus (2018-06-26T23:04:27Z)

is V3 available for DL ?

---

### 评论 #63 — ghost (2018-06-26T23:11:59Z)

I just fixed the problems for bab's with his kernel and added virtio
support and kvm qemu virtualbox passthrough. Currently Its in the oven
baking and I will help ya install it via skype. The vega support is only
available via a third party who has the keys to sign the ati bios's :)

On Wed, Jun 27, 2018 at 7:04 AM, vampyrus <notifications@github.com> wrote:

> is V3 available for DL ?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-400490328>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w2GBPjwxUMy9Puq0GpGXB90AiebYks5uAr4AgaJpZM4Sro0i>
> .
>


---

### 评论 #64 — ghost (2018-06-26T23:24:44Z)

 I just fixed the kernel today for babs
https://github.com/M-Bab/linux-kernel-amdgpu-binaries/issues/60

On Wed, Jun 27, 2018 at 7:11 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> I just fixed the problems for bab's with his kernel and added virtio
> support and kvm qemu virtualbox passthrough. Currently Its in the oven
> baking and I will help ya install it via skype. The vega support is only
> available via a third party who has the keys to sign the ati bios's :)
>
> On Wed, Jun 27, 2018 at 7:04 AM, vampyrus <notifications@github.com>
> wrote:
>
>> is V3 available for DL ?
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-400490328>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0w2GBPjwxUMy9Puq0GpGXB90AiebYks5uAr4AgaJpZM4Sro0i>
>> .
>>
>
>


---

### 评论 #65 — ghost (2018-06-26T23:32:00Z)

    0.744247] iommu: Adding device 0000:01:00.0 to group 1
[    0.744250] iommu: Adding device 0000:01:00.1 to group 1
[    0.744278] iommu: Adding device 0000:07:00.0 to group 12
[    0.744303] iommu: Adding device 0000:07:00.1 to group 12
:)
I busy adding back the stuff to allow for some fun gcn3 stuff.


On Wed, Jun 27, 2018 at 7:24 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:

>  I just fixed the kernel today for babs
> https://github.com/M-Bab/linux-kernel-amdgpu-binaries/issues/60
>
> On Wed, Jun 27, 2018 at 7:11 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:
>
>> I just fixed the problems for bab's with his kernel and added virtio
>> support and kvm qemu virtualbox passthrough. Currently Its in the oven
>> baking and I will help ya install it via skype. The vega support is only
>> available via a third party who has the keys to sign the ati bios's :)
>>
>> On Wed, Jun 27, 2018 at 7:04 AM, vampyrus <notifications@github.com>
>> wrote:
>>
>>> is V3 available for DL ?
>>>
>>> —
>>> You are receiving this because you were mentioned.
>>> Reply to this email directly, view it on GitHub
>>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-400490328>,
>>> or mute the thread
>>> <https://github.com/notifications/unsubscribe-auth/AWn0w2GBPjwxUMy9Puq0GpGXB90AiebYks5uAr4AgaJpZM4Sro0i>
>>> .
>>>
>>
>>
>


---

### 评论 #66 — ghost (2018-06-26T23:37:00Z)

Current Hashrate for 2x 570 102.0 Mh/s eth

On Wed, Jun 27, 2018 at 7:31 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:

>     0.744247] iommu: Adding device 0000:01:00.0 to group 1
> [    0.744250] iommu: Adding device 0000:01:00.1 to group 1
> [    0.744278] iommu: Adding device 0000:07:00.0 to group 12
> [    0.744303] iommu: Adding device 0000:07:00.1 to group 12
> :)
> I busy adding back the stuff to allow for some fun gcn3 stuff.
>
>
> On Wed, Jun 27, 2018 at 7:24 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:
>
>>  I just fixed the kernel today for babs
>> https://github.com/M-Bab/linux-kernel-amdgpu-binaries/issues/60
>>
>> On Wed, Jun 27, 2018 at 7:11 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:
>>
>>> I just fixed the problems for bab's with his kernel and added virtio
>>> support and kvm qemu virtualbox passthrough. Currently Its in the oven
>>> baking and I will help ya install it via skype. The vega support is only
>>> available via a third party who has the keys to sign the ati bios's :)
>>>
>>> On Wed, Jun 27, 2018 at 7:04 AM, vampyrus <notifications@github.com>
>>> wrote:
>>>
>>>> is V3 available for DL ?
>>>>
>>>> —
>>>> You are receiving this because you were mentioned.
>>>> Reply to this email directly, view it on GitHub
>>>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-400490328>,
>>>> or mute the thread
>>>> <https://github.com/notifications/unsubscribe-auth/AWn0w2GBPjwxUMy9Puq0GpGXB90AiebYks5uAr4AgaJpZM4Sro0i>
>>>> .
>>>>
>>>
>>>
>>
>


---

### 评论 #67 — CMcCullough41 (2018-06-27T00:22:09Z)

No way... that speed is unreal. How stable is it?

---

### 评论 #68 — ghost (2018-06-27T01:20:52Z)

There are known knowns. There are unknown knowns and there are known
unknowns and unknown unknowns.
Heres some fun stuff to read. If you look hard enough, and long enough you
will find the known unknowns.

https://developer.amd.com/wordpress/media/2017/08/Vega_Shader_ISA_28July2017.pdf
<https://www.google.com/url?q=https://developer.amd.com/wordpress/media/2017/08/Vega_Shader_ISA_28July2017.pdf&sa=D&source=hangouts&ust=1530148327952000&usg=AFQjCNGn9QocSNUdqxP8xhY2VRIt8TZFgQ>
https://developer.amd.com/wordpress/media/2012/10/GL3_WhitePaper.pdf
<https://www.google.com/url?q=https://developer.amd.com/wordpress/media/2012/10/GL3_WhitePaper.pdf&sa=D&source=hangouts&ust=1530148327952000&usg=AFQjCNGoiwtq-MvnN1SeMuHasoxH5uHa8A>
http://developer.amd.com/wordpress/media/2012/10/opencl-1.2.pdf
<https://www.google.com/url?q=http://developer.amd.com/wordpress/media/2012/10/opencl-1.2.pdf&sa=D&source=hangouts&ust=1530148327952000&usg=AFQjCNEFR27KDaUm1Rk20roamcgqSl2YZA>
http://ed25519.cr.yp.to/software.html
<https://www.google.com/url?q=http://ed25519.cr.yp.to/software.html&sa=D&source=hangouts&ust=1530148327952000&usg=AFQjCNHA3QD8tLul0TsxivGfnjhBrU0CEg>
http://cr.yp.to/ecdh/curve25519-20060209.pdf
<https://www.google.com/url?q=http://cr.yp.to/ecdh/curve25519-20060209.pdf&sa=D&source=hangouts&ust=1530148327952000&usg=AFQjCNFJVH28Odw--bU6UhodKd8nSirJhA>
http://developer.amd.com/wordpress/media/2017/04/Clang-the-C-C-Compiler-
<https://www.google.com/url?q=http://developer.amd.com/wordpress/media/2017/04/Clang-the-C-C-Compiler-&sa=D&source=hangouts&ust=1530148327952000&usg=AFQjCNGSGphTmgRxgTUtnewcdmMRCU8pcg>
—-AOCC-LLVM-1.pdf
https://developer.amd.com/wordpress/media/2013/12/AMD_OpenCL_Programming_Optimization_Guide.pdf
<https://www.google.com/url?q=https://developer.amd.com/wordpress/media/2013/12/AMD_OpenCL_Programming_Optimization_Guide.pdf&sa=D&source=hangouts&ust=1530148327953000&usg=AFQjCNG-NUO-6ZpZ4omaIhKvspOoGqXZkA>
http://developer.amd.com/wordpress/media/2013/12/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf
<https://www.google.com/url?q=http://developer.amd.com/wordpress/media/2013/12/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf&sa=D&source=hangouts&ust=1530148327953000&usg=AFQjCNF09Q9gGZZFLa_C9woaviQ_x_ZOQA>
http://developer.amd.com/wordpress/media/2013/12/AMD_OpenCL_Programming_User_Guide2.pdf
<https://www.google.com/url?q=http://developer.amd.com/wordpress/media/2013/12/AMD_OpenCL_Programming_User_Guide2.pdf&sa=D&source=hangouts&ust=1530148327953000&usg=AFQjCNF4NrDdV9QXDPXmL-1POIx_zDEjlw>
https://support.amd.com/en-us/kb-articles/pages/how-to-enable-amd-freesync-in-linux.aspx'
<https://www.google.com/url?q=https://support.amd.com/en-us/kb-articles/pages/how-to-enable-amd-freesync-in-linux.aspx%27&sa=D&source=hangouts&ust=1530148327953000&usg=AFQjCNFdPIKcNxNQanK4MnN_0R9B0QRiGg>
https://developer.amd.com/wordpress/media/2012/10/Dark_Secrets_of_shader_Dev-Mojo.pdf
<https://www.google.com/url?q=https://developer.amd.com/wordpress/media/2012/10/Dark_Secrets_of_shader_Dev-Mojo.pdf&sa=D&source=hangouts&ust=1530148327953000&usg=AFQjCNHTEjuQAhrGXdKFkC5y9jlGSS6_qA>
https://gpuopen.com/archive/app-kernel-analyzer/
<https://www.google.com/url?q=https://gpuopen.com/archive/app-kernel-analyzer/&sa=D&source=hangouts&ust=1530148327953000&usg=AFQjCNE_3x2OmVd5s6GYZ1wZzs-4S50LZQ>
https://wiki.archlinux.org/index.php/ATI#Driver_options
<https://www.google.com/url?q=https://wiki.archlinux.org/index.php/ATI%23Driver_options&sa=D&source=hangouts&ust=1530148327953000&usg=AFQjCNHcN7rIBTjYDfadgw6PoiE6l6LCWQ>
https://developer.amd.com/resources/developer-guides-manuals/
<https://www.google.com/url?q=https://developer.amd.com/resources/developer-guides-manuals/&sa=D&source=hangouts&ust=1530148327954000&usg=AFQjCNHidVlyL-iJaxwh_GFsMD_lrGi3XQ>
https://developer.amd.com/wordpress/media/2012/10/asiacrypt2007.pdf
<https://www.google.com/url?q=https://developer.amd.com/wordpress/media/2012/10/asiacrypt2007.pdf&sa=D&source=hangouts&ust=1530148327954000&usg=AFQjCNFkITDOjHSmWHfgha34a2r1eBCV-w>
http://developer.amd.com/wordpress/media/2013/10/R6xx_R7xx_3D.pdf
<https://www.google.com/url?q=http://developer.amd.com/wordpress/media/2013/10/R6xx_R7xx_3D.pdf&sa=D&source=hangouts&ust=1530148327954000&usg=AFQjCNF9cBcgHM5qzhenoJWcv6Qer7rZEw>
https://developer.amd.com/wordpress/media/2012/10/42589_rv630_rrg_1.01o.pdf
<https://www.google.com/url?q=https://developer.amd.com/wordpress/media/2012/10/42589_rv630_rrg_1.01o.pdf&sa=D&source=hangouts&ust=1530148327954000&usg=AFQjCNE4dSxQEoJk3Wa-anOvkwMQi5-HUw>
http://developer.amd.com/wordpress/media/2013/05/GCNPerformanceTweets.pdf
<https://www.google.com/url?q=http://developer.amd.com/wordpress/media/2013/05/GCNPerformanceTweets.pdf&sa=D&source=hangouts&ust=1530148327954000&usg=AFQjCNE4qGnzBU6YWevDks7psjrW1egtjg>





On Wed, Jun 27, 2018 at 8:22 AM, CMcCullough41 <notifications@github.com>
wrote:

> No way... that speed is unreal. How stable is it?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-400503634>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wzjJZkYHS6iuq1iLVscDfDypBLWxks5uAtA1gaJpZM4Sro0i>
> .
>


---

### 评论 #69 — puithove (2018-06-27T10:48:25Z)

That's an insane hashrate for 570s. I have several that could use that kind of upgrade.

---

### 评论 #70 — ghost (2018-06-29T23:58:46Z)

Uploading  Now
*********************-Rippa CodeX V(egas) 3**********************

Xubuntu 18.04 Bionic
Live memory based system / OpenGL Dev Environment / Playland 
Latest X
Amd CodeXL & Pwr kernel module
Latest vega patches & Firmware
Latest AMDGPU Updates & Patches
Chrome Apps
![screenshot_2018-06-29_23-45-20](https://user-images.githubusercontent.com/23721155/42119109-54afa462-7bf8-11e8-860b-e4ab8b1c1d39.png)

Steam
Other Extras: 
Latest firmware & kernel patches 
Dual OpenGL 4.5, Mesa 18.2, AMDPRO OpenGL 2.1 1.2 Vulkan, Clover MesaGL
Linux xubuntu 4.16.15-amd (Custom Kernel)
The Doctor

---

### 评论 #71 — ghost (2018-06-30T05:23:53Z)

Here is Version 3 (Mesa Only Stable)
Xubuntu 18.04 Bionic
Live memory based system / OpenGL Stable Environment / Playland
Latest X
Amd CodeXL & Pwr kernel module
Latest vega patches & Firmware
Latest AMDGPU Updates & Patches
https://drive.google.com/open?id=1u4Yka0YjRBtyyeHBfkpFpKSCcBCFq8RS

Here is Version 3 (Mesa Edge)

Here is Version 3 (AMDGPUPRO/Mesa Stable) 
To add ROCM

#!/bin/bash
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'

sudo apt-get update
sudo apt-get install libnuma-dev
sudo apt-get install rocm-dkms rocm-opencl-dev
dkms remove amdgpu/1.8-151 --all
￼￼update-initramfs -u
##########END Update Scrit#################


Here is Version 3 (AMDGPUPRO/Mesa Edge)


---

### 评论 #72 — heavyarms2112 (2018-06-30T17:46:42Z)

@tekcomm is v3 both polaris and vega friendly? and supports undervolting and clocks adjustments?



---

### 评论 #73 — ghost (2018-06-30T18:41:27Z)

Yes, Im releasing 6 versions, They are all the patched up till the last week
OpenCL MESA    STABLE/EDGE
AmdGPUPro/MESA
AmdGPUPro

These include a kernel with all the recent patches in the last two weeks &
Firmware

On Sun, Jul 1, 2018 at 1:46 AM, heavyarms2112 <notifications@github.com>
wrote:

> @tekcomm <https://github.com/tekcomm> is v3 both polaris and vega
> friendly? and supports undervolting and clocks adjustments?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401556069>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w6vvbAO8uEgb4YpOFxtV2JXFl9GYks5uB7mHgaJpZM4Sro0i>
> .
>


---

### 评论 #74 — ghost (2018-06-30T18:42:49Z)

These are dev versions with a custom kernel module I built & patched to
work with the latest CodeXL

On Sun, Jul 1, 2018 at 2:41 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> Yes, Im releasing 6 versions, They are all the patched up till the last
> week
> OpenCL MESA    STABLE/EDGE
> AmdGPUPro/MESA
> AmdGPUPro
>
> These include a kernel with all the recent patches in the last two weeks &
> Firmware
>
> On Sun, Jul 1, 2018 at 1:46 AM, heavyarms2112 <notifications@github.com>
> wrote:
>
>> @tekcomm <https://github.com/tekcomm> is v3 both polaris and vega
>> friendly? and supports undervolting and clocks adjustments?
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401556069>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0w6vvbAO8uEgb4YpOFxtV2JXFl9GYks5uB7mHgaJpZM4Sro0i>
>> .
>>
>
>


---

### 评论 #75 — heavyarms2112 (2018-06-30T19:52:59Z)

@tekcomm so need to wait for the amdgpu-pro driver patched version of rippa v3?

---

### 评论 #76 — ghost (2018-06-30T20:26:46Z)

:) Or you can install it and it will install with all the features to
another drive. Then install to taste :)


On Sun, Jul 1, 2018 at 3:53 AM, heavyarms2112 <notifications@github.com>
wrote:

> @tekcomm <https://github.com/tekcomm> so need to wait for the amdgpu-pro
> driver patched version of rippa v3?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401562665>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w13MSeJv5Q3pReteKDun1VnTfpUJks5uB9cfgaJpZM4Sro0i>
> .
>


---

### 评论 #77 — heavyarms2112 (2018-06-30T21:35:18Z)

So which amdgpu pro drivers for undervolting Vegas?  18.20?  Should I install that?

---

### 评论 #78 — ghost (2018-07-01T04:27:13Z)

email me ill send ya the pp tables :_

On Sun, Jul 1, 2018 at 5:35 AM, heavyarms2112 <notifications@github.com>
wrote:

> So which amdgpu pro drivers for undervolting Vegas? 18.20? Should I
> install that?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401567666>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w4V2xtblVrb-SLgOaYgMBYNHw_Vhks5uB-8agaJpZM4Sro0i>
> .
>


---

### 评论 #79 — ghost (2018-07-01T09:04:59Z)

*next part is compiling xmr-stak miner with AMD support*

*1) Download AMD APP SDK*

Download SDK installer AMD-APP-SDKInstaller-v3.0.130.136-GA-linux64.tar.bz2
<https://excellmedia.dl.sourceforge.net/project/nicehashsgminerv5viptools/APP%20SDK%20A%20Complete%20Development%20Platform/AMD%20APP%20SDK%203.0%20for%2064-bit%20Linux/AMD-APP-SDKInstaller-v3.0.130.136-GA-linux64.tar.bz2>

*2) Unpack SDK installer tar.bz2 package*
> tar jxf AMD-APP-SDKInstaller-v3.0.130.136-GA-linux64.tar.bz2

*3) Run extracted SDK*
> ./AMD-APP-SDK-v3.0.130.136-GA-linux64.sh

By default, SDK will be installed in /opt/AMDAPPSDK-3.0 directory.

*4) Set AMDAPPSDKROOT environment variable*
> export AMDAPPSDKROOT=/opt/AMDAPPSDK-3.0

After AMD APP SDK is installed, set AMDAPPSDKROOT environment variable for
“cmake” to find SDK when xmr-stak will be compiled.

*5) Install needed tools to compile xmr-stak*
>apt-get install  install gcc gcc-c++ hwloc-devel libmicrohttpd-devel libstdc++-static
make libssl1.0-dev cmake git 

*6) Get xmr-stak from Git repository*
> git clone https://github.com/fireice-uk/xmr-stak.git

*7) Create build directory inside cloned xmr-stak source code*
> cd xmr-stak
> mkdir build
> cd build

*8) Run cmake*
> cmake .. -DCUDA_ENABLE=OFF
-DOpenCL_LIBRARY=/opt/amdgpu-pro/lib64/libOpenCL.so

*9) Run make and make install*
> make
> make install

*10) Start xmr-stak*
> bin/xmr-stak

Finally, set large page support to get better results with “sysctl -w
vm.nr_hugepages=128” command. For permanent settings add
“vm.nr_hugepages=128” to the /etc/sysctl.conf file:
vm.nr_hugepages=128


On Sun, Jul 1, 2018 at 4:27 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> email me ill send ya the pp tables :_
>
> On Sun, Jul 1, 2018 at 5:35 AM, heavyarms2112 <notifications@github.com>
> wrote:
>
>> So which amdgpu pro drivers for undervolting Vegas? 18.20? Should I
>> install that?
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401567666>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0w4V2xtblVrb-SLgOaYgMBYNHw_Vhks5uB-8agaJpZM4Sro0i>
>> .
>>
>
>


---

### 评论 #80 — ghost (2018-07-01T11:12:49Z)

To answer your question b4 your ask does this work on this.
���������������������������������������������������������������ͻ
�           Claymore's CryptoNote AMD GPU Miner v11.3            �
����������������������������������������������������������������ͼ

XMR: 6 pools are specified
Main Monero pool is xmr-eu1.nanopool.org:14433
At least 16 GB of Virtual Memory is required for multi-GPU systems
Make sure you defined GPU_MAX_ALLOC_PERCENT 100
Be careful with overclocking, use default clocks for first tests
Press "s" for current statistics, "0".."9" to turn on/off cards, "r" to reload pools
OpenCL initializing...
AMD Cards available: 4 
GPU #0: Baffin (Radeon RX 560 Series), 3988 MB available, 16 compute units (pci bus 1:0:0)
GPU #0 recognized as Radeon RX 460/560
GPU #1: Ellesmere (Radeon RX 570 Series), 8178 MB available, 32 compute units (pci bus 3:0:0)
GPU #1 recognized as Radeon RX 470/570
GPU #2: Baffin (Radeon RX 560 Series), 4082 MB available, 16 compute units (pci bus 4:0:0)
GPU #2 recognized as Radeon RX 460/560
GPU #3: Ellesmere (Radeon RX 570 Series), 8178 MB available, 32 compute units (pci bus 6:0:0)
GPU #3 recognized as Radeon RX 470/570
POOL version
GPU #0 algorithm ASM, -h 416, -dmem 1 (Memory used: 1704MB)
GPU #1 algorithm ASM, -h 1024, -dmem 1 (Memory used: 4198MB)
GPU #2 algorithm ASM, -h 416, -dmem 1 (Memory used: 1704MB)
GPU #3 algorithm ASM, -h 1024, -dmem 1 (Memory used: 4198MB)
Total cards: 4 
AMD ADL library not found.
XMR: Stratum - connecting to 'xmr-eu1.nanopool.org' <92.222.180.119> port 14433
"-allpools" option is set, default pools can be used for devfee, check "Readme" file for details.
Watchdog enabled
Remote management (READ-ONLY MODE) is enabled on port 3333

SSL/TLS encryption is enabled
XMR: Stratum - Connected (xmr-eu1.nanopool.org:14433) (SSL/TLS)

CLAYMORE WORKS@@@@@



./xmr-stak 
-------------------------------------------------------------------
xmr-stak 2.4.5 b3f79de

Brought to you by fireice_uk and psychocrypt under GPLv3.
Based on CPU mining code by wolf9466 (heavily optimized by fireice_uk).
Based on OpenCL mining code by wolf9466.

Configurable dev donation level is set to 0.0%

You can use following keys to display reports:
'h' - hashrate
'r' - results
'c' - connection
-------------------------------------------------------------------
[2018-07-01 19:10:04] : Mining coin: cryptonight_v7
[2018-07-01 19:10:04] : Compiling code and initializing GPUs. This will take a while...
[2018-07-01 19:10:04] : Device 0 work size 8 / 32.
[2018-07-01 19:10:04] : OpenCL device 0 - Load precompiled code from file /root/.openclcache/25c9ee14088ae044ef65203b1b41605dc1d2b2319c72e20658859f82ddc22945.openclbin
[2018-07-01 19:10:04] : Device 1 work size 8 / 32.
[2018-07-01 19:10:04] : OpenCL device 1 - Load precompiled code from file /root/.openclcache/eb683d98bc2a21477104f1d4668b569d2406c2c0f6880c8913830edca43cda34.openclbin
[2018-07-01 19:10:04] : Device 2 work size 8 / 32.
[2018-07-01 19:10:05] : OpenCL device 2 - Load precompiled code from file /root/.openclcache/25c9ee14088ae044ef65203b1b41605dc1d2b2319c72e20658859f82ddc22945.openclbin
[2018-07-01 19:10:05] : Device 3 work size 8 / 32.
[2018-07-01 19:10:05] : OpenCL device 3 - Load precompiled code from file /root/.openclcache/eb683d98bc2a21477104f1d4668b569d2406c2c0f6880c8913830edca43cda34.openclbin
[2018-07-01 19:10:05] : Starting AMD GPU (OpenCL) thread 0, no affinity.
[2018-07-01 19:10:05] : Starting AMD GPU (OpenCL) thread 1, no affinity.
[2018-07-01 19:10:05] : Starting AMD GPU (OpenCL) thread 2, no affinity.
[2018-07-01 19:10:05] : Starting AMD GPU (OpenCL) thread 3, no affinity.
[2018-07-01 19:10:05] : Starting 1x thread, affinity: 0.
[2018-07-01 19:10:05] : hwloc: memory pinned
[2018-07-01 19:10:05] : Starting 1x thread, affinity: 1.
[2018-07-01 19:10:05] : hwloc: memory pinned
[2018-07-01 19:10:05] : Starting 1x thread, affinity: 2.
[2018-07-01 19:10:05] : hwloc: memory pinned
[2018-07-01 19:10:05] : Starting 1x thread, affinity: 3.
[2018-07-01 19:10:05] : hwloc: memory pinned

XMR-STACK Works @@@@@@@@@@@@@@@@@


etc.......
Good night from the Mad man in the blue box ;)

---

### 评论 #81 — ghost (2018-07-01T15:34:10Z)

Attached is the installer for nicehashminer tdd miner claymore etc etc etc.
This will install the min requirements for them
#!/bin/bash
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'

sudo apt-get update
sudo apt-get install libnuma-dev
sudo apt-get install rocm-dkms rocm-opencl-dev
dkms remove amdgpu/1.8-151 --all
￼￼update-initramfs -u
##########END Update Scrit#################


---

### 评论 #82 — heavyarms2112 (2018-07-01T16:13:26Z)

Hi Tekcomm,

So I've been trying to undervolt vegas using rocm 1.8 and wasn't able to do
so.
Thanks again.

EDIT:  I am not sure how to email you directly :|

[image: Mailtrack]
<https://mailtrack.io?utm_source=gmail&utm_medium=signature&utm_campaign=signaturevirality5&>
Sender
notified by
Mailtrack
<https://mailtrack.io?utm_source=gmail&utm_medium=signature&utm_campaign=signaturevirality5&>
01/07/18,
12:07:03

On Sun, Jul 1, 2018 at 12:27 AM, The Doctor <notifications@github.com>
wrote:

> email me ill send ya the pp tables :_
>
> On Sun, Jul 1, 2018 at 5:35 AM, heavyarms2112 <notifications@github.com>
> wrote:
>
> > So which amdgpu pro drivers for undervolting Vegas? 18.20? Should I
> > install that?
> >
> > —
> > You are receiving this because you were mentioned.
> > Reply to this email directly, view it on GitHub
> > <https://github.com/RadeonOpenCompute/ROCm/issues/
> 361#issuecomment-401567666>,
> > or mute the thread
> > <https://github.com/notifications/unsubscribe-auth/AWn0w4V2xtblVrb-
> SLgOaYgMBYNHw_Vhks5uB-8agaJpZM4Sro0i>
>
> > .
> >
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401582184>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AJpaZr-3x8m9lbEHyxfMwFVIfzM8RY_vks5uCE-mgaJpZM4Sro0i>
> .
>


---

### 评论 #83 — ghost (2018-07-01T16:52:42Z)

That was not possible tilll early june with the ppmask patch


---

### 评论 #84 — rhlug (2018-07-01T19:21:45Z)

@tekcomm your cryptonight_v7 on xmr-stak output shows xmr-stak loads, but does it find any results?  let it run for a few minutes, and press "r"

this is cryptonight-heavy output on xmr-stak
```
RESULT REPORT
Difficulty       : 655820
Good results     : 3 / 3 (100.0 %)
Avg result time  : 89.0 sec
Pool-side hashes : 674613
```

But cryptonight-v7 its always 0 / 0 (0.0%)


---

### 评论 #85 — BobDodds (2018-07-01T19:37:07Z)

"Watchdog enabled"
--but not for long if we've been reading?

"At least 16 GB of Virtual Memory is required for multi-GPU systems
Make sure you defined GPU_MAX_ALLOC_PERCENT 100
Be careful with overclocking, use default clocks for first tests"
--I made 28GB VM on ssd, but only 8gigs ram, for quadcore gen8 with 4 rx580s.

"-allpools" option is set, default pools can be used for devfee, check "Readme" file for details.


---

### 评论 #86 — ghost (2018-07-01T20:18:13Z)

grub nmi_watchdog=0 :)

On Mon, Jul 2, 2018 at 3:37 AM, BobDodds <notifications@github.com> wrote:

> "Watchdog enabled"
> --but not for long if we've been reading?
>
> "At least 16 GB of Virtual Memory is required for multi-GPU systems
> Make sure you defined GPU_MAX_ALLOC_PERCENT 100
> Be careful with overclocking, use default clocks for first tests"
> --I made 28GB VM on ssd, but only 8gigs ram, for quadcore gen8 with 4
> rx580s.
>
> "-allpools" option is set, default pools can be used for devfee, check
> "Readme" file for details.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401628140>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wzTJcPRFYyrDXHUcAGPdlQKtMuziks5uCSTmgaJpZM4Sro0i>
> .
>


---

### 评论 #87 — ghost (2018-07-01T21:55:26Z)

My thoughts on watchdogs

"The watchdog is a waste, It needs to be stuck with the cat in Schrodinger
box.
The processor state is always forced to full, cstate 1 idle & idle=poll"


On Mon, Jul 2, 2018 at 4:18 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> grub nmi_watchdog=0 :)
>
> On Mon, Jul 2, 2018 at 3:37 AM, BobDodds <notifications@github.com> wrote:
>
>> "Watchdog enabled"
>> --but not for long if we've been reading?
>>
>> "At least 16 GB of Virtual Memory is required for multi-GPU systems
>> Make sure you defined GPU_MAX_ALLOC_PERCENT 100
>> Be careful with overclocking, use default clocks for first tests"
>> --I made 28GB VM on ssd, but only 8gigs ram, for quadcore gen8 with 4
>> rx580s.
>>
>> "-allpools" option is set, default pools can be used for devfee, check
>> "Readme" file for details.
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401628140>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0wzTJcPRFYyrDXHUcAGPdlQKtMuziks5uCSTmgaJpZM4Sro0i>
>> .
>>
>
>


---

### 评论 #88 — BobDodds (2018-07-02T01:40:57Z)

grub, another thing Refind is not going to do better. isorespin guy Linuxium is one of many who were talking about grub2 as fossil, when I really needed to mount Ubuntu iso file from a uefi, to install linux, and it wasn't happening with Refind--cute though but did not refind its ass. Ooh, I actually had to learn grub cli, woohoo, cli not fossilized compared to no cli. So we can assure 100% already with:
cstate 1 idle & idle=poll
as well as start to clear out wastes of time with:
grub nmi_watchdog=0

Linuxium's work is great, helps lots of people, Refind didn't do it for me like grub.

---

### 评论 #89 — ghost (2018-07-02T04:48:48Z)

Ohhh I had to learn how to load programs from a tape :), I have worked with
linuxiuan on projects for a long time and the reason we loved the shit out
of refind was how easy we could shim those god dam 32bit / 64bit franken
tablets and give the tablets a touch interface. Otherwise Ill use grub.
Otherwise I don't give a shit I still have 512 in the boot loader :P

On Mon, Jul 2, 2018 at 9:41 AM, BobDodds <notifications@github.com> wrote:

> grub, another thing Refind is not going to do better. isorespin guy
> Linuxium is one of many who were talking about grub2 as fossil, when I
> really needed to mount Ubuntu iso file from a uefi, to install linux, and
> it wasn't happening with Refind--cute though but did not refind its ass.
> Ooh, I actually had to learn grub cli, woohoo, cli not fossilized compared
> to no cli. So we can assure 100% already with:
> cstate 1 idle & idle=poll
> as well as start to clear out wastes of time with:
> grub nmi_watchdog=0
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401649874>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w2Ew2O3CiADzqUL66VnjqrFCZrQ8ks5uCXotgaJpZM4Sro0i>
> .
>


---

### 评论 #90 — ghost (2018-07-02T04:52:06Z)

its intel_idle.max_cstate=1 and your learn that dam fast be cause otherwise
u spent two cpu gens with nothing but crashes :)

On Mon, Jul 2, 2018 at 12:48 PM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> Ohhh I had to learn how to load programs from a tape :), I have worked
> with linuxiuan on projects for a long time and the reason we loved the shit
> out of refind was how easy we could shim those god dam 32bit / 64bit
> franken tablets and give the tablets a touch interface. Otherwise Ill use
> grub. Otherwise I don't give a shit I still have 512 in the boot loader :P
>
> On Mon, Jul 2, 2018 at 9:41 AM, BobDodds <notifications@github.com> wrote:
>
>> grub, another thing Refind is not going to do better. isorespin guy
>> Linuxium is one of many who were talking about grub2 as fossil, when I
>> really needed to mount Ubuntu iso file from a uefi, to install linux, and
>> it wasn't happening with Refind--cute though but did not refind its ass.
>> Ooh, I actually had to learn grub cli, woohoo, cli not fossilized compared
>> to no cli. So we can assure 100% already with:
>> cstate 1 idle & idle=poll
>> as well as start to clear out wastes of time with:
>> grub nmi_watchdog=0
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401649874>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0w2Ew2O3CiADzqUL66VnjqrFCZrQ8ks5uCXotgaJpZM4Sro0i>
>> .
>>
>
>


---

### 评论 #91 — BobDodds (2018-07-03T01:04:57Z)

I was looking at Linuxium site when mainline kernel did not have the drivers for frankenstein Cherry Trail(64-bit) and Bay Trail(32-bit) yet. I had a Cherry Trail 2-in-1 11.9" screen, keyboard detachable, worked with Ubuntu touch screen. Drivers were coming from others for wifi, ethernet, bt, Broadcom Realtek.

I installed Linuxium's 64-bit Cherry Trail isorespin of Ubuntu, by letting InsydeH20 bios put me in position to boot grub, and then use grub2 commandline to boot Linuxium's iso. Once installed, it would boot Ubuntu from power on.

My rig mobo bios allows turning off uefi, no EFI vfat partition, no signed kernel. The 2-in-1 would only allow turning off the signed kernel check.

---

### 评论 #92 — ghost (2018-07-03T03:49:35Z)

I knew it you are jr bob dobbs :P
V4 Will run steam games faster then windows :)
V3 I am gearing more toward Dev/Program/Debug
V2 Is geared for Crypto/Cloud

On Tue, Jul 3, 2018 at 9:05 AM, BobDodds <notifications@github.com> wrote:

> I was looking at Linuxium site when mainline kernel did not have the
> drivers for Cherry Trail(64-bit) and Bay Trail(32-bit) yet. I had a Cherry
> Trail 2-in-1 11.9" screen, keyboard detachable, worked with Ubuntu touch
> screen.
>
> I installed Linuxium's 64-bit Cherry Trail isorespin of Ubuntu, by letting
> InsydeH20 bios put me in position to boot grub, and then use grub2
> commandline to boot Linuxium's iso. Once installed, it would boot Ubuntu
> from power on.
>
> My rig mobo bios allows turning off uefi, no EFI vfat partition, no signed
> kernel. The 2-in-1 would only allow turning off the signed kernel check.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-401981880>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w_xqPVPSGsu-Wng3daIKr7erRLVRks5uCsM-gaJpZM4Sro0i>
> .
>


---

### 评论 #93 — securitizones (2018-07-03T09:01:14Z)

Whats in the V2 thats more geared towards Crypto/Mining thats not in V3. Just i'd like to run one kernel for mining and development.

---

### 评论 #94 — ghost (2018-07-03T09:22:38Z)

V2, is a Ferrari F1
Stripped of all services and configured for faster boots and no user
interface. Stripped down for speed and stability Ubuntu 16. Exceeds US Gov
standards on security with a optional RTOS interface the Navy Uses. Created
by the Motorola Teacher/Developer who created the code for the DCX DVR
systems (Comcast AOL etc etc Cableboxs. The Doctor).


V3, is a Rolls Royce
Xubuntu based with custom kernel patched with latest amdgpu firmware and
patches for Vegas with AMD's Developer platform CodeXL for coding and
realtime GPU profiling. I personally updated and rewrote the kernel driver
to support it. In other words CodeXL can profile all your gpus on V2. While
it disassembles the Claymore kernel and when combined with the AMD Compiler
recompile the code for better support using OpenCL. Then you can use the
kernel on V2 of Rippa for full Vega support.

On Tue, Jul 3, 2018 at 9:01 AM, securitizones <notifications@github.com>
wrote:

> Whats in the V2 thats more geared towards Crypto/Mining thats not in V3.
> Just i'd like to run one kernel for mining and development.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-402065521>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wwGcnlyP3Ph4uPuSW0xnrIP79CORks5uCzLggaJpZM4Sro0i>
> .
>


---

### 评论 #95 — securitizones (2018-07-03T09:34:04Z)

thanks
Ive booted up V3 and i have 2 vega 64s on there and when i start CodeXL is says i dont have a supported MAD GPU. any ideas. 
Also i want to undervolt the vegas. Can i do that on the V3 kernel ?
sorry little unsure what to use for general mining and development. need to get up to speed with what youve built.


---

### 评论 #96 — ghost (2018-07-03T10:02:41Z)

Yes you can change the voltages on vega by using the PP tables. Heres a
quick vid of whats new. Once your done just run the kernel and firmware on
the headless V2 :)
Heres a vid of Whats new.
https://youtu.be/qsDAimkuYpc

On Tue, Jul 3, 2018 at 9:34 AM, securitizones <notifications@github.com>
wrote:

> thanks
> Ive booted up V3 and i have 2 vega 64s on there and when i start CodeXL is
> says i dont have a supported MAD GPU. any ideas.
> Also i want to undervolt the vegas. Can i do that on the V3 kernel ?
> sorry little unsure what to use for general mining and development. need
> to get up to speed with what youve built.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-402078277>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w9HLPcp20vbqSWGu0VdUNVkn3Wx7ks5uCzqdgaJpZM4Sro0i>
> .
>


---

### 评论 #97 — securitizones (2018-07-03T10:20:48Z)

Do you have any scripts to chnage the pptables fro vega64. I would really appreciate it. 
Sorry to be a pain

---

### 评论 #98 — ghost (2018-07-03T10:30:13Z)

add me google hangouts tekcommnv AT gmail.com

On Tue, Jul 3, 2018 at 10:20 AM, securitizones <notifications@github.com>
wrote:

> Do you have any scripts to chnage the pptables fro vega64. I would really
> appreciate it.
> Sorry to be a pain
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/361#issuecomment-402095270>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w1EosCu-18tyoIThBq_vQIFovNOuks5uC0WGgaJpZM4Sro0i>
> .
>


---

### 评论 #99 — ghost (2018-07-04T06:21:06Z)

Cryptonight V7
Working...

HASHRATE REPORT - AMD
| ID |    10s |    60s |    15m | ID |    10s |    60s |    15m |
|  0 |  285.6 |  290.4 |   (na) |  1 |  337.3 |  338.2 |   (na) |
|  2 |  296.6 |  296.6 |   (na) |  3 |  340.4 |  344.8 |   (na) |
Totals (AMD):  1259.9 1270.1    0.0 H/s
-----------------------------------------------------------------
Totals (ALL):   1435.8 1473.4    0.0 H/s
Highest:  1523.0 H/s

tdx is now working too
[2018-07-04 06:16:47] Pool lyra2z.usa.nicehash.com share accepted.
[2018-07-04 06:16:56] Pool lyra2z.usa.nicehash.com share accepted.
[2018-07-04 06:16:57] Pool lyra2z.usa.nicehash.com share accepted.
[2018-07-04 06:17:06] Stats GPU 0 - lyra2z: 2.182Mh/s (2.750Mh/s)  
[2018-07-04 06:17:06] Stats GPU 1 - lyra2z: 2.152Mh/s (2.744Mh/s)  
[2018-07-04 06:17:06] Stats Total - lyra2z: 4.334Mh/s (5.494Mh/s)  
I spent the last couple days writing a monster installer for them.


Ill be uploading the next three parts over the week Ill be in and out of the hospital all week.
Donations, coffee, tea,
BTC: 3GVotAvf4PD9xJ7TSxQrZ38cZoSsBWuHC3
LTC: LbmeaZt8oxLuExphJn419C3nGjjj4q19wd
ETH: 0xf10d05cf2751dcea29e060b75bd47c038fd2abc8




---

### 评论 #100 — chromakey-io (2018-07-05T03:17:59Z)

Hey tekcomm ... I was hoping to try out your whole setup targeting the RX570's.

I just upgraded with a new thread ripper board .. but am having some issues getting the atomics support to be recognized (though that was on RHEL so who knows).  

Aany-who.  I downloaded your version 3 (mesa) yesterday and tried to get things going.  Unfortunately, I get an error with ethminer:

OpenCL kernel: Stable kernel
  ✘  20:16:20|cl-0    |  Build info: <unknown>:0:0: in function ethash_calculate_dag_item void (i32, %union.compute_hash_share addrspace(1)*, %union.compute_hash_share addrspace(1)*, i32): unsupported initializer for address space

  ✘  20:16:20|cl-0    |  OpenCL Error: clEnqueueWriteBuffer: CL_INVALID_MEM_OBJECT (-38)


I also tried to install the ROCM drivers as instructed in this thread ... but didn't seem to have much luck there either.  Does this kernel have that stuff built in?  Either way (with or without dkms modules) rocminfo fails :(

---
