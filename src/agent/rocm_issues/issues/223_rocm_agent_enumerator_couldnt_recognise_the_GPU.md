# rocm_agent_enumerator couldnt recognise the GPU

> **Issue #223**
> **状态**: closed
> **创建时间**: 2017-10-10T11:18:06Z
> **更新时间**: 2018-02-01T14:01:35Z
> **关闭时间**: 2017-10-24T09:29:05Z
> **作者**: psn9
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/223

## 描述

Hi , 

I am trying to run **_/opt/rocm/bin/rocm_agent_enumerator -t GPU_**  and getting the following output : 

**gfx000**

No GPU is being specified. I have tried updating the rocm driver but of no use.

**command** : uname -a 
**output** : Linux prasanth 4.11.0-kfd-compute-rocm-rel-1.6-148 #1 SMP Wed Aug 23 12:00:35 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux

**command** : /opt/rocm/hcc/bin/hcc --version
**output** : 
HCC clang version 6.0.0  (based on HCC 1.0.17373-bd1f35c-c639ce0-e4adac0 )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/hcc/bin

**command** : lspci -v | grep -i amd
**output** : 
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca) (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Radeon R9 FURY X / NANO
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8

Any inputs ?

---

## 评论 (14 条)

### 评论 #1 — rhlug (2017-10-10T17:04:38Z)

With an RX470 (custom bios) and a RX Vega 56 installed, kfd doesnt detect the RX470.   If I take the Vega out of the system, my RX470 works just fine by itself.

$ /opt/rocm/bin/rocm_agent_enumerator -t GPU 
gfx000
gfx900

$ lspci | grep VGA
26:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
29:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c3)

Here is dmesg with RX470 load failure and Vega56 load success.

[   12.206462] amdgpu 0000:26:00.0: amdgpu_init failed
[   12.314626] [drm] amdgpu: ttm finalized
[   12.314682] amdgpu 0000:26:00.0: Fatal error during GPU init
[   12.314741] [drm] amdgpu: finishing device.
[   12.315117] amdgpu: probe of 0000:26:00.0 failed with error -22
...
...
[   13.426862] kfd kfd: Allocated 3969056 bytes on gart for device 1002:687f
[   13.427797] kfd kfd: Reserved 2 pages for cwsr.
[   13.428086] kfd kfd: added device 1002:687f
[   13.428346] [drm] Initialized amdgpu 3.18.0 20150101 for 0000:29:00.0 on minor 0


Here is with just RX470

$ /opt/rocm/bin/rocm_agent_enumerator -t GPU 
gfx000
gfx803

$ lspci | grep VGA
26:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)

dmesg

[    3.073351] fbcon: amdgpudrmfb (fb0) is primary device
[    3.124616] amdgpu 0000:26:00.0: fb0: amdgpudrmfb frame buffer device
[    3.141330] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[    3.141557] kfd kfd: Reserved 2 pages for cwsr.
[    3.141607] kfd kfd: added device 1002:67df
[    3.141630] [drm] Initialized amdgpu 3.18.0 20150101 for 0000:26:00.0 on minor 0


Thoughts?


---

### 评论 #2 — fxkamd (2017-10-13T19:39:53Z)

amdgpu driver initialization fails. Can you provide full dmesg output?

---

### 评论 #3 — fxkamd (2017-10-13T19:42:43Z)

Also, do we have two different issues reported on this thread? @prasanth09 has a single Fiji NANO card. @rhlug has a combination of Vega10 and Polaris10.

---

### 评论 #4 — rhlug (2017-10-13T20:42:42Z)

@fxkamd its possible they are different issues.   I'll have to set things back up to generate that full dmesg.

---

### 评论 #5 — gstoner (2017-10-17T12:43:37Z)

@rhlug can you update to ROCm 1.6.4 which was released last night let us know if you continue to see the issue,  we want to trace this down 

---

### 评论 #6 — rhlug (2017-10-17T14:14:22Z)

@gstoner I will get this setup today and tested.

Update 1 -

So at first, I added my rx470 in the x8 slot.   On bootup, the kernel got into some exit_to_usermode_loop, and never would boot.   So I moved the rx470 beside my rxvega in the 2nd x16 slot.   Now I'm booting and both detecting.

```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  1   67df   30.0c    26.0W    301Mhz   2021Mhz  37.65%   auto      0%       N/A      
  0   687f   56.0c    91.0W    1312Mhz  928Mhz   73.73%   manual    0%       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================

./rocm_agent_enumerator -t GPU
gfx000
gfx803
gfx900
```

Update 2 - 
Still working through scenarios.

1) rxvega56 in x16 slot 1,  rx470 in x16 slot 2 =  boots and kfd detects both
2) rxvega56 in x16 slot 1,  rx570 in x16 slot 2 = also works fine
3) rxvega56 in x16 slot 1,  rx470 in x8 =  Errors during boot, timeouts and loops.
4) rxvega56 in x16 slot 1,  rx470 in x1 =  Seems to boot, vega blows off like normal, then black screen.  OS is non-responsive, cannot ping host.
5) rxvega56 in x16 slot 1,  rx470 in x16 slot 2, rx570 in x1 (via extender) = same fate as 4)

I need to test rx470 in x16 and rx570 in x8 (or x1) to rule out the vega being the cause of the failed boot ups.   Also need to determine if this is all just MSI x370 A4 w/ Ryzen 1700 related.







---

### 评论 #7 — psn9 (2017-10-24T09:29:05Z)

I updated to latest ROCm and the issue is fixed. I am closing this issue now.

---

### 评论 #8 — rhlug (2017-10-24T18:59:00Z)

Thats fine, I'll spin off a new BZ once I get the time and all the details sorted.

---

### 评论 #9 — VincentSC (2018-01-31T13:40:06Z)

Seems this discussion is better than #281 for the "GPU not recognised problem"
Second GPU in slot 4, /opt/rocm/bin/rocm_agent_enumerator gives:
> gfx000
gfx900

Second GPU in slot 3, /opt/rocm/bin/rocm_agent_enumerator gives:
> gfx000
gfx803
gfx900

---

### 评论 #10 — psn9 (2018-01-31T14:14:07Z)

But what I did in this case was just updatting ROCm. I was using Rocm 1.5 I suppose and upgrading it to 1.6.4 resolved the issue. 

Now in 1.7 , I end up with "No device" error.
And additionally , in ROCM 1.7 case , the rocm_agent_enumerator is able to recognise GPU unlike the case in this issue. I have mentioned it in this [comment](https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-361578737) in #281 .

---

### 评论 #11 — VincentSC (2018-01-31T14:54:26Z)

Possibly ROCm 1.7 reintroduced the problem with PCIx8? The list of VGA-devices from `sudo lspci -vv | grep 'LnkCap\|AMD'` here:
````
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca) (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Radeon R9 FURY X / NANO
		LnkCap:	Port #0, Speed 8GT/s, Width x16, ASPM not supported, Exit Latency L0s <64ns, L1 <1us
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon Vega Frontier Edition] (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon Vega Frontier Edition]
		LnkCap:	Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
````

When at port 4, that one would have had a Width of x8. So if somebody from the ROCm-team could please test with a GPU on a x8 port, to see if this is indeed a problem?

---

### 评论 #12 — gstoner (2018-01-31T19:30:31Z)

What linux kernel version are you on, it might be the issue 

---

### 评论 #13 — psn9 (2018-02-01T04:37:07Z)

Hello @gstoner , 

Can you point me to the right Linux kernel version ie., the output of `uname -a` of your PC where Rocm 1.7 runs fine ? 

---

### 评论 #14 — gstoner (2018-02-01T14:01:35Z)

Step one start with clean ubuntu 16.04 release. We have it running on stock 4.4 kernel and 4.10 kernel.   You have to follow these instructions exactly https://rocm.github.io/ROCmInstall.html.  If your on Intel based  you can use the 4.4, Only Ryzen do  need update Kernel 4.10 in 16.04.3. Soon they will release 4.13 but you want to wait for this one with newer 1.7.1 update we will be releasing. 

---
