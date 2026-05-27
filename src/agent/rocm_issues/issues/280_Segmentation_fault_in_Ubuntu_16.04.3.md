# Segmentation fault in Ubuntu 16.04.3

> **Issue #280**
> **状态**: closed
> **创建时间**: 2017-12-21T18:49:02Z
> **更新时间**: 2018-06-03T15:26:18Z
> **关闭时间**: 2018-06-03T15:26:18Z
> **作者**: julioauto
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/280

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

**DISCLAIMER**: Yes, I have tried the installation method at https://rocm.github.io/ROCmInstall.html. With multiple kernel versions (4.4, 4.10, 4.11, 4.14.8, 4.15-rc4). Some of them just wouldn't build. Some I'd get the same behavior I'm describing here.

The system is a Ubuntu 16.04.3 with kernel 4.4.0-104-generic. I decided just to go with the default kernel and the normal installation of amdgpu-pro 17.40 after failing miserably to install with rocm-dkms (as stated above). My system has 4 VGAs: 2 Tonga, 1 Hawaii and 1 RX Vega 56.

After installing the 17.40 driver, clinfo works OK but it can only see the first 3 cards, i.e. it doesn't see Vega. Then I add ROCm with "apt install -y rocm-amdgpu-pro" as per http://support.amd.com/en-us/kb-articles/Pages/AMDGPU-PRO-Install.aspx and run clinfo again:

```
root@aaaa:~# clinfo
Segmentation fault (core dumped)

```

On dmesg, what I see is:

```
[ 2086.221499] amdgpu: [powerplay] 
                failed to send pre message 145 ret is 0 
[ 2086.637046] amdgpu: [powerplay] 
                failed to send message 145 ret is 0 
[ 2087.468138] amdgpu: [powerplay] 
      *          failed to send pre message 146 ret is 0 
[ 2087.883676] amdgpu: [powerplay] 
                failed to send message 146 ret is 0 
[ 2087.926991] clinfo[2447]: segfault at 1 ip 00007f3aaecc862d sp 00007fff1fe12d90 error 4 in libhsakmt.so.1.0.0[7f3aaecbb000+15000]
[ 2088.882545] amdgpu: [powerplay] 
                failed to send pre message 145 ret is 0 
[ 2089.298094] amdgpu: [powerplay] 
                failed to send message 145 ret is 0 
[ 2090.129184] amdgpu: [powerplay] 
                failed to send pre message 146 ret is 0 
[ 2090.544809] amdgpu: [powerplay] 
                failed to send message 146 ret is 0 
```

For reference, the relevant bit of my lspci is:

```
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Amethyst XT [Radeon R9 M295X Mac Edition / R9 380X] (rev f1)
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Tonga HDMI Audio [Radeon R9 285/380]
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Amethyst XT [Radeon R9 M295X Mac Edition / R9 380X] (rev f1)
02:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Tonga HDMI Audio [Radeon R9 285/380]
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii XT [Radeon R9 290X]
04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii HDMI Audio
05:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470 (rev c3)
06:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c3)
07:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
```
**EDIT**: I should also note that when ROCm is installed (regardless of installation method) it's making the fan on the GPU at my 1st PCI slot go crazy (like it was under heavy load all the time).
**EDIT 2**: It seems that I only get the crash when the Hawaii card is plugged in. When it is removed, clinfo executes fine, but it only finds 1 Tonga (the one whose fan is going nuts) and none of the other Tongas or Vegas.
**EDIT 3**: I see the 'failed to send message' errors in dmesg anyway, even when clinfo does work without the segfault, and I see them early in dmesg too, when the system is still initializing.

---

## 评论 (20 条)

### 评论 #1 — jamilbk (2017-12-21T18:58:45Z)

According to the [ROCK kernel driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver), they mention it's based on the 4.13 upstream:

> The kernel image is built from a source tree based on the 4.13 upstream

Ubuntu 16.04 provides a mainline 4.13 kernel package: `linux-image-generic-hwe-16.04-edge` -- you may have better luck installing `rocm-dkms` after installing that kernel. Working for me with 4x Vegas.

---

### 评论 #2 — julioauto (2017-12-21T19:38:51Z)

I appreciate the info. I guess I had an outdated apt yesterday when I tried HWE, as it was giving me a 4.10 kernel.

Either way, I just tried it again, got the 4.13.0-21-generic, put ROCm in it, and am getting the same segfault.

---

### 评论 #3 — gstoner (2017-12-21T23:37:40Z)

@julioauto You cannot install ROCm Open Source Driver and AMDGPUpro driver on your system at the same time this will lead to driver failure as you are seeing.      You do not need change out the kernel.   

All you need is Ubuntu 16.04 sp2 or sp3 clean install and then follow the direction for the install of ROCm opensource driver. https://rocm.github.io/ROCmInstall.html.     

Greg

---

### 评论 #4 — julioauto (2017-12-21T23:43:22Z)

Shouldn't invoking amdgpu-pro-uninstall and a reboot before installing ROCm
be enough? Between each of my attempts (whether at ROCm or the driver) I
did uninstall everything that made sense to me.

---

### 评论 #5 — julioauto (2017-12-22T18:16:56Z)

OK. So I went and destroyed my system anyway; started from scratch with a clean install of Ubuntu. All I did was apt update; apt-dist upgrade (still keeps me in the branch 4.4 of kernel) and the instructions at ROCmInstall.html.

Same thing. Segfault and all.

Can we start considering that maybe there is a problem here after all?

---

### 评论 #6 — gstoner (2017-12-22T22:18:12Z)

What CPU are you running?  let start there. 

---

### 评论 #7 — gstoner (2017-12-22T22:23:14Z)

Are you using AMD EPYC, RYZEN,  Intel Core xx, or Xeon Processor.   

---

### 评论 #8 — gstoner (2017-12-23T15:58:17Z)

If you're on Ryzen CPU, there was an issue in Linux 4.4 with Ryzen  https://www.phoronix.com/scan.php?page=news_item&px=AMD-Ryzen-Newer-Kernel    ROCm 1.6.4 did not use DKMS, we replaced the whole Linux kernel with 4.11 generic kernel with our bits added for ROCm.   4.11 had the fixes for Ryzen. 

---

### 评论 #9 — gstoner (2017-12-23T18:13:46Z)

If this is Ryzen system also take a look at this https://www.servethehome.com/amd-ryzen-with-ubuntu-here-is-what-you-have-to-do-to-fix-constant-crashes/    

---

### 评论 #10 — gstoner (2017-12-23T18:57:03Z)

Tonga could be the issue why your seeing the system crash, we do some simple triage start with RX Vega 56 system only 

---

### 评论 #11 — julioauto (2017-12-23T19:56:59Z)

Thanks for the information.

I'm pretty sure the CPU is an Intel Celeron G1840 dual core 2.8GHz (Haswell). Unfortunately I don't have access to the machine right now, so I can't confirm. I can do it Tuesday, however, if the CPU still seems to be part of the issue. The motherboard is an ASRock H81 Pro BTC.

I have tried several configurations of the GPUs and then running clinfo. Here's the results I can remember:
- 3x (or 2x or 1x) Tonga + 1x Hawaii + 1x RX Vega 56: segmentation fault
- 3x (or 2x or 1x) Tonga + 1x RX Vega 56: only 1x Tonga identified by clinfo (no crash)
- 1x RX Vega 56: 0 devices identified (no crash)

I don't remember if I tried just Vega + Hawaii, because I'm under the impression that it was the Hawaii causing the segfault.

Other noteworthy observations:
- When I tried with Tongas plugged in, the fan in one of them spins very fast and loud, like it was under heavy load. This behavior begins early in the system initialization - maybe as soon as the driver/device is initialized. This behavior only happens once ROCm is installed (and not when the driver amdgpu-pro is installed, for example).
- When I tried using the Vega to output to a monitor, even when the Vega was by itself, it didn't work. I have more testing to do regarding this (e.g. trying different PCIe slots). When I use a Tonga (the one whose fan spins fast) to output, it works.

**EDIT**: Shouldn't really change anything but the CPU is actually a Celeron G1820.

---

### 评论 #12 — julioauto (2017-12-26T20:52:53Z)

I have rebuilt my system from scratch a couple more times. I have found that one of the Vegas is likely malfunctioning, so I removed it from the system. Here's is its current configuration:
- 1x Vega 56 (this works and is providing my video output)
- 3x Tonga
(I should note that the Hawaii and the Tongas worked fine and were in production until I tried to add the Vegas and this saga began)

When I run rocminfo, it only finds the CPU agent, so no GPU agents.
When I run the clinfo that comes with rocm (/opt/rocm/opencl/bin/x86_64/clinfo), I get:
```
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```
lspci lists all cards correctly. If I plug the Hawaii in I get worse behavior: video output (from Vega) stops working, the segmentation fault mentioned here, etc.

Nothing suspicious in dmesg either, except maybe "amdgpu 0000:05:00.0: Invalid ROM contents". This bus 05 is the one the Vega is attached to. I'm ignoring this message as per [this forum thread](https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/open-source-amd-linux/45819-radeon-0000-01-00-0-invalid-rom-contents), where an apparent driver developer said "You can ignore the "Invalid ROM contents" message. It was due to a change in the rom handling code in the pci subsystem. It's harmless.".

All this behavior is exactly the same whether I have the Tongas plugged in or not, i.e. the Vega all by itself.

Note: while doing some superficial debugging, I noticed that clinfo unsuccessfully tries to load libamdoclcl64.so (probably coming from NullDevice::initCompiler at [rocdevice.cpp](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/cc77105f58e5096ff81afe4d1992c6bde3545fff/runtime/device/rocm/rocdevice.cpp#L200)) shortly before exiting. I'm not sure this is an issue, but the double 'cl' seemed weird to me. In any case, this library isn't there.

**In the meantime**: does anybody know of any way to get this system to work? I don't care if it's with ROCm or not. I just need Vega + Tonga + Hawaii + OpenCL to work. This machine worked great and now has been pulled off production ever since I tried adding the Vegas to it.

---

### 评论 #13 — gstoner (2017-12-27T15:44:15Z)

Try the AMDGPUpro driver 17.50  http://support.amd.com/en-us/kb-articles/Pages/Installation-Instructions-for-amdgpu-Graphics-Stacks.aspx 

---

### 评论 #14 — robolivable (2017-12-29T05:01:56Z)

I was getting an issue somewhat related to this due to a missing dependency. Installing development libraries for `libnuma` solved my issue:

    sudo apt-get install libnuma-dev

It also may be worth mentioning that I'm running Ubuntu Server 16.04.3, which doesn't seem to ship with these files.

---

### 评论 #15 — spozi (2017-12-29T15:00:22Z)

I have similar problem. My CPU is Haswell 4790 with RX Vega 64.

---

### 评论 #16 — fxkamd (2017-12-29T18:27:35Z)

@robolivable : libnuma-dev is only needed if you are going to compile the Thunk. At runtime it depends on libnuma1.

@julioauto : Do you have a complete kernel log? The powerplay messages indicate that the SMU is hanging. Something must have gone wrong before that to get the hardware into a bad state. A complete kernel log may hold a clue. The segfault in clinfo is probably some initialization problem. I doubt it's related to the SMU hang. Can you get more info (a backtrace) by running it in gdb?

---

### 评论 #17 — julioauto (2017-12-29T18:53:16Z)

@fxkamd I'll see if I can get you something next week. At this point, the system seems to behave weirder and weirder to me, so I'm suspecting hardware issues. I can't pinpoint exactly what, nor be sure if it was there from the start or if it was caused by all my fiddling with the hardware this past week, but it's in a strange state. I'll keep you posted if I make any progress or find anything interesting.

---

### 评论 #18 — julioauto (2018-01-04T16:29:09Z)

Hi, all.

I thought I would touch base again with some information that, while probably not relevant to the ROCm team, might be useful for people that might be facing the same issues as I am.

Long story short, I stopped trying ROCm and turned to the AMD drivers. Nothing really worked:
- Drivers 17.40 and 17.50 will make clinfo crash if I have all my GPUs plugged in and won't crash if I remove the Hawaii (but won't identify the Vega either, so they aren't very helpful)
- The latest driver on _Windows_ will identify all GPUs correctly, but the application I want to run (hashcat) crashes in some very specific use cases unless the Vega is removed. It's easy to blame it on the application code but this application is pretty mature and the CL code should be the same across all platforms, so I'm inclined to believe that the Windows driver, although in better shape, isn't yet 100% functional for Vega.
- In the end I reverted to amdgpu-pro 16.40, which works just flawlessly for hashcat on Linux - albeit not seeing (and being unable to use) the Vega, of course.

I read that my motherboard can be somewhat unstable or exhibit strange behavior once there are more than 3 or 4 GPUs plugged in, so I can definitely believe that maybe my hardware is provoking part of the issue. But the fact is that, for the same hardware, 16.40 supports it just fine (except for Vega, of course) while 17.{40,50} and ROCm don't. The Windows drivers also do a better job, close to perfect, so there's definitely a software component to this problem.

I know this doesn't bring any answers but, as I said, it may be useful for someone. I still want to make use of the Vega on my motherboard, but at this point I've exhausted my options and all I can do is expect it to work with the next driver (and/or ROCm) release.
 
P.S.: Do I understand it right that ROCm only works with PCIe 3? That is, it means that it should never work with my MB considering all 6 slots are PCIe 2.0?

---

### 评论 #19 — VincentSC (2018-01-05T10:12:24Z)

See https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-355328679 what to do

---

### 评论 #20 — julioauto (2018-01-05T14:24:55Z)

Thanks, @VincentSC , but this will not solve my issue, however. As per my reports above, I'm doing clean installs of Ubuntu 16.04 between attempts - I tried switching to Windows, even. Anyway, fresh installs every time.

---
