# Detecting/Enabling Multi-GPU?

> **Issue #125**
> **状态**: closed
> **创建时间**: 2017-05-31T14:25:28Z
> **更新时间**: 2018-02-10T14:48:40Z
> **关闭时间**: 2017-06-02T09:23:02Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/125

## 描述

Hi folks,

So, I now have two rx480s on 16x lanes, on a board that advertises Crossfire (if that's relevant, probably not). The CPU is an Intel i5, however.

I installed ROCm with rocm-opencl, on Ubuntu 16.04. My system `clinfo` now returns the following:

```
cathal@thinkum:~$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (2410.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx803
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  1.1 (HSA,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Max compute units                               36
  Max clock frequency                             1266MHz
  Device Partition                                (core)
    Max number of sub-devices                     36
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (n/a)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              8589934592 (8GiB)
  Error Correction support                        No
  Max memory allocation                           6442450944 (6GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26591
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max constant buffer size                        6442450944 (6GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.8
  ICD loader Profile                              OpenCL 1.2
	NOTE:	your OpenCL library declares to support OpenCL 1.2,
		but it seems to support up to OpenCL 2.1 too.
```

The ROCm version of `clinfo` returns similar output:

```
cathal@thinkum:~$ /opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (2410.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Device 67df
  Device Topology:				 PCI[ B#1, D#0, F#0 ]
  Max compute units:				 36
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1266Mhz
  Address bits:					 64
  Max memory allocation:			 6442450944
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26591
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 8589934592
  Constant buffer size:				 6442450944
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 6442450944
  Max global variable preferred total size:	 8589934592
  Max read/write image args:			 64
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7f4ac52b2478
  Name:						 gfx803
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 1.1 (HSA,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images 
```

Things generally behave OK; I get similar output on hipCaffe to others, and tests on [tf-Coriander](https://github.com/hughperkins/tf-coriander) are similar in output to my R9 390 using the AMDGPU-pro driver. It's as if I have one GPU only.

However, `lspci` correctly detects two (I think):

```
cathal@thinkum:~$ lspci
00:00.0 Host bridge: Intel Corporation Sky Lake Host Bridge/DRAM Registers (rev 07)
00:01.0 PCI bridge: Intel Corporation Sky Lake PCIe Controller (x16) (rev 07)
00:08.0 System peripheral: Intel Corporation Sky Lake Gaussian Mixture Model
00:14.0 USB controller: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller (rev 31)
00:14.2 Signal processing controller: Intel Corporation Sunrise Point-H Thermal subsystem (rev 31)
00:16.0 Communication controller: Intel Corporation Sunrise Point-H CSME HECI #1 (rev 31)
00:17.0 SATA controller: Intel Corporation Sunrise Point-H SATA controller [AHCI mode] (rev 31)
00:1c.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #5 (rev f1)
00:1f.0 ISA bridge: Intel Corporation Sunrise Point-H LPC Controller (rev 31)
00:1f.2 Memory controller: Intel Corporation Sunrise Point-H PMC (rev 31)
00:1f.3 Audio device: Intel Corporation Sunrise Point-H HD Audio (rev 31)
00:1f.4 SMBus: Intel Corporation Sunrise Point-H SMBus (rev 31)
00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (2) I219-V (rev 31)
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev c7)
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev c7)
02:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
```

How should I go about setting up multi-GPU on ROCm?

To be very clear: I have *not* installed AMDGPU-pro or another AMD/ATI driver, because my understanding is that ROCm includes drivers/kernel-modules etcetera all in the one tree. I've followed the ROCm installation guide from a totally virgin Ubuntu 16.04 install.

---

## 评论 (26 条)

### 评论 #1 — briansp2020 (2017-05-31T21:01:14Z)

See https://github.com/RadeonOpenCompute/ROCm/issues/46#issuecomment-264070476

Does it work with 1 GPU ok even when you have both GPU installed? I took one out because 1.3 did not work at all when I had both GPUs installed. If they have changed it so that ROCm still works with 2 GPU installed, I want to put my other GPU back in.

---

### 评论 #2 — ekondis (2017-06-01T06:05:49Z)

According to my experience I guess that the second slot on your motherboard does not support atomics which is a requirement for ROCm. That is the case for my motherboard as well.

---

### 评论 #3 — ghost (2017-06-01T09:55:06Z)

@ekondis - Do you have any ideas on how to test that theory? If I need a new MoBo I'd better start saving. :)

---

### 评论 #4 — ghost (2017-06-01T10:00:54Z)

Ran `sudo lspci -vv` and pulled out the two VGA-Compatible Controllers, see attached.

Here's the Diff:

```bash
cathal@thinkum:~/Downloads$ diff gpu1 gpu2
1c1
< 01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev c7) (prog-if 00 [VGA controller])
---
> 02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev c7) (prog-if 00 [VGA controller])
4c4
< 	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
---
> 	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
6,11c6,11
< 	Interrupt: pin A routed to IRQ 124
< 	Region 0: Memory at c0000000 (64-bit, prefetchable) [size=256M]
< 	Region 2: Memory at d0000000 (64-bit, prefetchable) [size=2M]
< 	Region 4: I/O ports at e000 [size=256]
< 	Region 5: Memory at dfe00000 (32-bit, non-prefetchable) [size=256K]
< 	Expansion ROM at 000c0000 [disabled] [size=128K]
---
> 	Interrupt: pin A routed to IRQ 125
> 	Region 0: Memory at a0000000 (64-bit, prefetchable) [size=256M]
> 	Region 2: Memory at b0000000 (64-bit, prefetchable) [size=2M]
> 	Region 4: I/O ports at d000 [size=256]
> 	Region 5: Memory at dfd00000 (32-bit, non-prefetchable) [size=256K]
> 	Expansion ROM at dfd40000 [disabled] [size=128K]
20c20
< 			RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
---
> 			RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop+
27c27
< 		LnkSta:	Speed 2.5GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
---
> 		LnkSta:	Speed 2.5GT/s, Width x4, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
34c34
< 			 EqualizationPhase2-, EqualizationPhase3-, LinkEqualizationRequest-
---
> 			 EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
36c36
< 		Address: 00000000fee0400c  Data: 41a1
---
> 		Address: 00000000fee0f00c  Data: 41b1
42c42
< 		CESta:	RxErr- BadTLP- BadDLLP+ Rollover- Timeout- NonFatalErr+
---
> 		CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
53,54c53,54
< 		Max snoop latency: 71680ns
< 		Max no snoop latency: 71680ns
---
> 		Max snoop latency: 3145728ns
> 		Max no snoop latency: 3145728ns
```

[gpu1.txt](https://github.com/RadeonOpenCompute/ROCm/files/1044346/gpu1.txt)
[gpu2.txt](https://github.com/RadeonOpenCompute/ROCm/files/1044347/gpu2.txt)


---

### 评论 #5 — ghost (2017-06-01T10:01:54Z)

Above: I'm concerned at the bit `LnkSta` saying `Width x16` for one, and `Width x4` for the other.. because the motherboard has two x16 PCIe sockets and the cards are plugged into a full-length socket each? Or am I misreading "Width" here?

---

### 评论 #6 — gstoner (2017-06-01T11:02:49Z)

Not all x16 physical link are x16 electrically

Get Outlook for iOS<https://aka.ms/o0ukef>



On Thu, Jun 1, 2017 at 11:02 AM +0100, "Cathal Garvey" <notifications@github.com<mailto:notifications@github.com>> wrote:


Above: I'm concerned at the bit LnkSta saying Width x16 for one, and Width x4 for the other.. because the motherboard has two x16 PCIe sockets and the cards are plugged into a full-length socket each? Or am I misreading "Width" here?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/125#issuecomment-305448380>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuaL8tkxxIWFN8Wrp3eqk-q085Lbhks5r_owTgaJpZM4NrtY2>.


---

### 评论 #7 — ghost (2017-06-01T11:07:35Z)

I know, but the board advertises two 16x ports, so it would be a bit disgraceful if they only meant the physical layout and not the links! :)

It's [this board](https://www.msi.com/Motherboard/B150M-NIGHT-ELF.html#hero-specification) - specs advertise:

```
PCI-Ex16    2
PCI-E Gen   Gen3
PCI-Ex1     2
```

---

### 评论 #8 — briansp2020 (2017-06-01T13:49:02Z)

@gstoner Does B350 based motherboard support atomic on the second PCIe slot? I'm interested in mATX based AM4 board but I can't find any mATX with x370 yet.

---

### 评论 #9 — ekondis (2017-06-01T20:18:19Z)

@cathalgarvey on the specs it mentions "(support x16/x4 mode)". If you take a close look on the 2nd slot you'll probably notice that there are much less electrical contacts compared to the 1st slot, even though both slots have physically the same size

---

### 评论 #10 — gstoner (2017-06-01T22:53:49Z)

I just looked at the Manual for the motherboard.    You have 4 PCIe Slots

1 PCIe x16 slot  that runs at x16 electrically
2 PCie x1 slots
1 PCIe slot that run at x4 electrically

MSI E7979v1.1.pdf
On Jun 1, 2017, at 9:18 PM, Elias <notifications@github.com<mailto:notifications@github.com>> wrote:


@cathalgarvey<https://github.com/cathalgarvey> on the specs it mentions "(support x16/x4 mode)". If you take a close look on the 2nd slot you'll probably notice that there are much less electrical contacts compared to the 1st slot, even though both slots have physically the same size

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/125#issuecomment-305608398>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuT-aFwn9B04UXThpA4UTXTTkQ0E6ks5r_xyNgaJpZM4NrtY2>.



---

### 评论 #11 — gstoner (2017-06-01T22:54:19Z)

I just looked at the Manual for the motherboard.    You have 4 PCIe Slots

1 PCIe x16 slot  that runs at x16 electrically
2 PCie x1 slots
1 PCIe slot that run at x4 electrically

[cid:A3ACD359-841E-4C23-B05B-371C93E7D770]


The spec I saw were  2 PCIe x16 supporting x16 and x4
On Jun 1, 2017, at 12:07 PM, Cathal Garvey <notifications@github.com<mailto:notifications@github.com>> wrote:


I know, but the board advertises two 16x ports, so it would be a bit disgraceful if they only meant the physical layout and not the links! :)

It's this board<https://www.msi.com/Motherboard/B150M-NIGHT-ELF.html#hero-specification> - specs advertise:

PCI-Ex16      2
PCI-E Gen   Gen3
PCI-Ex1        2


—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/125#issuecomment-305462434>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudQSwgv-X6GIUFw5HS4jqJWyleCxks5r_pt4gaJpZM4NrtY2>.



---

### 评论 #12 — gstoner (2017-06-01T22:56:49Z)

The issue you guys are running Core I3/I5/I7 based CPU which have limited number of PCIe lanes.  To get multiple GPU you need I7 Extreme or Xeon based CPU, From AMD Ideal will be Treadripper or EPYC.

Greg
On Jun 1, 2017, at 9:18 PM, Elias <notifications@github.com<mailto:notifications@github.com>> wrote:


@cathalgarvey<https://github.com/cathalgarvey> on the specs it mentions "(support x16/x4 mode)". If you take a close look on the 2nd slot you'll probably notice that there are much less electrical contacts compared to the 1st slot, even though both slots have physically the same size

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/125#issuecomment-305608398>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuT-aFwn9B04UXThpA4UTXTTkQ0E6ks5r_xyNgaJpZM4NrtY2>.



---

### 评论 #13 — ghost (2017-06-02T09:23:02Z)

@ekondis @gstoner Thanks so much for digging into that, my hardware-fu is outdated and I missed that. I'm pretty annoyed that MSI would advertise two 16x rails when one is basically just a 4x with room for unused pins.

Anyways, this may mean a new motherboard, and if I understand correctly, I may also need a new CPU to use both 16x rails, anyway?

The EPYC/ThreadRipper CPUs are of course my dream hardware, but are outside of my price range for now. :)  Any off-hand advice about which Ryzen-generation {AC}PUs would be suitable for multi-GPU use? I can then (more carefully) look into appropriate motherboards to leverage the chip.

I'll close this as it appears to be a hardware limitation on my end.

---

### 评论 #14 — ekondis (2017-06-02T12:55:52Z)

@gstoner wouldn't a motherboard for mainstream 4 core CPUs offering a dual GPU (at x8) mode be supported by ROCm for multigpu?

---

### 评论 #15 — ghost (2017-06-02T13:25:14Z)

I see a lot of options that will spread 8/8 between 2 GPUs. If that would allow me to make full use of both GPUs, that'd be a good outcome for me. With the -4 PCIe lanes I imagine transfer bandwidth to/from the card would suffer, but it would otherwise be fine to use?

---

### 评论 #16 — ekondis (2017-06-03T13:31:37Z)

@cathalgarvey If that x8/x8 configuration is sufficient for ROCm it would be great for regular users. My intuition is that it should work but I haven't confirmed it, though.

---

### 评论 #17 — gstoner (2017-06-03T18:08:40Z)

It is dependent on the workload.   Some workloads need more performance.
On Jun 3, 2017, at 2:31 PM, Elias <notifications@github.com<mailto:notifications@github.com>> wrote:


@cathalgarvey<https://github.com/cathalgarvey> If that x8/x8 configuration is sufficient for ROCm it would be great for regular users. My intuition is that it should work but I haven't confirmed it, though.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/125#issuecomment-305975276>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuVBZ_8cw2hc86j4nEftBbac5gsIrks5sAWA6gaJpZM4NrtY2>.



---

### 评论 #18 — ghost (2017-06-03T21:51:45Z)

So, if I understand correctly:

* A motherboard/CPU combination that provides 8 lanes per GPU would be enough to have both GPUs register as OpenCL devices.
* Transfer Performance would be slower for both, clearly, but they would otherwise be fully functional and would operate internally at full speed.
* For some tasks or projects, a single 16-lane GPU would be preferable to two 8-lane GPUs. I'm imagining this is true mostly of tasks that would need a lot of transfer to/from Host RAM, for example convnets which might need a lot of image transfers during training?
* The above makes it plausible to use a quad-core RYZEN with an 8/8 motherboard to drive 2 GPUs with ROCm.

If the above is correct, then for me it's "question answered". I have an additional "bonus" question I'd be grateful for, though;

* Would a quad-core Intel i5 with an 8/8 motherboard also suffice, or is the i5 series not capable of handling an 8/8 GPU split? If I can reduce my potential purchase to a motherboard, then it's probably something I can do short-term, but if I need to buy a RYZEN CPU then it'll have to wait.

Thanks so much!


---

### 评论 #19 — naibaf7 (2017-09-16T22:19:01Z)

I have a Z97 Extreme6 board (i7-4790K) with a x8/x8 PCIe 3.0 configuration and ROCm 1.6 does NOT work when 2 ROCm compatible GPUs (RX 480, Vega FE) are installed; however, I don't know yet why that is. Maybe because the two PCIe 3.0 ports are in the same IOMMU group and don't have isolation?

Some results of trying to run the system with 2 GPUs:
- "HSA_STATUS_ERROR_OUT_OF_RESOURCES" when running the HIP vector example.
- Segfault for OpenCL "clinfo"
- DMESG: "GPU fault detected: 146 0x00c8480c" -> "VM fault (0x0c, vmid 8) at page 10265, read from 'TC4'"
- UnpinnedCopyEngine () segfault when using GDB on the HIP vector example.

All of these do not occur when only one GPU is present in the system (either RX 480 or Vega FE). ROCm installation works fine.

---

### 评论 #20 — naibaf7 (2017-09-16T22:58:55Z)

I found the issue regarding dual GPU use on Intel chipsets:
Use `intel_iommu=on iommu=pt` as GRUB kernel command line options when IOMMU/VT-d is enabled, do not use `intel_iommu=on` alone, which will cause DMA issues with ROCm. Very important. It is possible `amd_iommu=on iommu=pt` is required on AMD systems, however I don't have the hardware to test this now.

---

### 评论 #21 — rhlug (2017-11-11T15:34:50Z)

@naibaf7 

I tried amd_iommu=on iommu=pt on my a4 board, but i still get only 2 of the 6 cards detected by clinfo.  Even though rocm-smi sees them all.

```
# /opt/rocm/bin/rocm-smi

====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  5   67df   51.0c    58.28W   1235Mhz  2053Mhz  37.65%   manual    10%      N/A      
  3   67df   50.0c    54.107W  1236Mhz  2054Mhz  37.65%   manual    10%      N/A      
  1   67df   49.0c    61.227W  1233Mhz  2021Mhz  37.65%   manual    10%      N/A      
  4   67df   50.0c    61.147W  1237Mhz  2055Mhz  37.65%   manual    10%      N/A      
  2   67df   55.0c    55.13W   1234Mhz  2042Mhz  37.65%   manual    10%      N/A      
  0   67df   44.0c    53.172W  1233Mhz  2051Mhz  37.65%   manual    10%      N/A      
================================================================================
====================           End of ROCm SMI Log          ====================

# lspci | grep VGA
21:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef)
22:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
23:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef)
24:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef)
26:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev cf)
27:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef)


[   10.307274] kfd kfd: Initialized module
[   12.129438] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[   13.536320] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[   15.328276] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[   17.088319] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[   19.754353] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[   19.754498] kfd kfd: Reserved 2 pages for cwsr.
[   19.754528] kfd kfd: added device 1002:67df
[   21.350319] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[   21.350521] kfd kfd: Reserved 2 pages for cwsr.
[   21.350550] kfd kfd: added device 1002:67df

# /opt/rocm/opencl/bin/x86_64/clinfo  | grep -i "Board name"
  Board name:					 Device 67df
  Board name:					 Device 67df

```

All 6 GPUs work fine on windows.  I just want to use them as opencl devices, I dont need PCI atomics.  Is there a way to force kfd to register the device as an opencl device without pci atomics?



---

### 评论 #22 — gstoner (2017-11-11T15:53:08Z)

@rhlug    ROCm stack uses PCIe Atomics aka Atomics Completion for performance optimization.   The Windows Stack is based on different System level userland and Kernel driver your comparing apples and oranges. 

Note we have systems running 8 GPU  when you use proper PCIe Switch that pass Atomic Completors aka PCIe Atomics.   

So you have idea what benefits they provide to us in our program model development 

AtomicOps enable advanced synchronization mechanisms that are particularly useful when there are 15 multiple producers and/or multiple consumers that need to be synchronized in a non-blocking fashion. For example, multiple producers can safely enqueue to a common queue without any explicit locking.
 
AtomicOps also enable lock-free statistics counters, for example where a device can atomically increment a counter, and host software can atomically read and clear the counter.
 
Direct support for the three chosen AtomicOps over PCI Express enables easier migration of existing high-performance SMP applications to systems that use PCI Express as the interconnect to tightly-coupled accelerators, co-processors, or GP-GPUs. For example, a ported application that uses PCI Express-attached accelerators may be able to use the same synchronization algorithms and data structures as the earlier SMP application.
 
An AtomicOp to a given target generally incurs latency comparable to a Memory Read to the same target. Within a single hierarchy, multiple AtomicOps can be “in flight” concurrently. AtomicOps generally create negligible disruption to other PCI Express traffic.
 
Compared to Locked Transactions, AtomicOps provide lower latency, higher scalability, advanced synchronization algorithms, and dramatically less impact to other PCI Express traffic.
 


---

### 评论 #23 — rhlug (2017-11-11T16:26:40Z)

@gstoner so are there pcie switches that you can recommend to try?

---

### 评论 #24 — gstoner (2017-11-11T18:09:49Z)

Broadcomm PCIe Gen3 PCIe switches

- PLX8747,  PLX 8749, PLX 8780, PLX 8764, PLX 8796,  
- PLX 9747, PLX 9749, PLX 9765, PLX9780, PLX9797;   

I really like the Microsemi PCIe Gen3 PCIe switches, 
   
- PM8536 PFX 96xG3, PM8535 PFX 80xG3, PM8534 PFX 64xG3, PM8533 PFX48xG3
- PM8556 PAX 96xG3, PM8555 PAX 80xG3, PM8554 PAX 64xG3, PM8553 PAX 48xG3 
--



---

### 评论 #25 — rhlug (2017-11-12T13:22:44Z)

For retrofitting old motherboards with riser boards, have you any experience with Pericom PI7C9X switches?

---

### 评论 #26 — th0ma7 (2018-02-10T14:48:40Z)

Having a similar problem where only 3 out of 6 cards are being detected by clinfo.
```
$ /opt/rocm/bin/rocm-smi


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  5   39.0c   26.146W  1011Mhz  2052Mhz  21.96%   auto      0%       
  3   60.0c   25.40W   995Mhz   2051Mhz  35.69%   auto      0%       
  1   33.0c   14.255W  214Mhz   2050Mhz  20.0%    auto      0%       
  4   46.0c   27.46W   1011Mhz  2051Mhz  21.96%   auto      0%       
  2   39.0c   14.59W   214Mhz   2052Mhz  34.9%    auto      0%       
  0   39.0c   12.130W  214Mhz   2050Mhz  33.73%   auto      0%       
================================================================================
====================           End of ROCm SMI Log          ====================

```

and clinfo output:
```
$ clinfo 
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP.internal (2545.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 3
  Device Name                                     gfx803
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  2545.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 

```

Using an AMD Ryzen 5 CPU with 4.13 kernel and tried iommu=pt or amd_iommu=on in conjunction with iommu=pt.
```
$ cat /proc/cpuinfo 
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 1
model name	: AMD Ryzen 5 1600X Six-Core Processor
stepping	: 1
...
$ uname -a
Linux th0ma7-miner-01 4.13.0-32-generic #35~16.04.1-Ubuntu SMP Thu Jan 25 10:13:43 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

All cards are being detected properly using amdgpu-pro linux driver with Legacy OpenCL although performance per gpu is lower than when using rocm.
```
$ dpkg -l | grep -i rocm
ii  hsa-ext-rocr-dev                     1.1.7-12-gf0de514                          amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime extensions for ROCm platforms
ii  hsa-rocr-dev                         1.1.7-12-gf0de514                          amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for ROCm platforms
ii  rocm-clang-ocl                       0.2.0-83527dd                              amd64        OpenCL compilation with clang compiler.
ii  rocm-dev                             1.7.60                                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                     0.0.1                                      amd64        Radeon Open Compute - device libraries
ii  rocm-dkms                            1.7.60                                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl                          1.2.0-2017121952                           amd64        OpenCL/ROCm
ii  rocm-opencl-dev                      1.2.0-2017121952                           amd64        OpenCL/ROCm
ii  rocm-smi                             1.0.0-34-g23012d0                          amd64        System Management Interface for ROCm
ii  rocm-utils                           1.7.60                                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                             1.0.7                                      amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool
```

Read that things should evolve significantly using 4.17 which may have rocm built-in for my video adapters along with tons of updates.  In the meantime help would be greatly appreciated.

---
