# Information Request - high numbers of GPUs support 

> **Issue #295**
> **状态**: closed
> **创建时间**: 2018-01-02T03:53:34Z
> **更新时间**: 2020-11-18T11:33:38Z
> **关闭时间**: 2020-11-18T11:33:38Z
> **作者**: AirSquirrels
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/295

## 描述

I’m using ROCm and am looking to achieve more than 13 GPUs running on one system. I believe the main issues are not in ROCm but with the system BIOS, however I believe @gstoner has 

---

## 评论 (11 条)

### 评论 #1 — AirSquirrels (2018-01-02T03:58:26Z)

For some reason I can’t edit the original issue, but it was submitted prematurely. I believe that @gstoner may have some insight into the limitations. What I have observed is that the actual BAR allocations would seem to be fine and not exceed memory space even on 39 bit (512G) consumer systems (we are of course dealing with above 4G decoding). I have also observed that the GPU limit does not seem to exist when using cards that have the PCI Device Class of 3D Controller vs. VGA compatible. Can you provide any clarification regarding what resource limits are being hit? I considered legacy VGA space in the 0x3b0-0x3bb etc. or an issue with legacy Video Bios option Roms, but he issues are hit even when using UEFI BIOS loads which should not have those limits. 

---

### 评论 #2 — rhlug (2018-01-04T23:50:40Z)

@AirSquirrels what are you using to switch 13 GPUs and provide PCI Atomics to them?

---

### 评论 #3 — AirSquirrels (2018-01-04T23:55:47Z)

Using ASMedia PCIe switches, devices are connected to 1x PCIe as I don’t need bandwidth for my applications. This issue would seem to be pre-atomic support though, as it results in BIOS not posting. I understand the bootstrap process, however I am working to remove the resource constraints preventing larger card counts. 

---

### 评论 #4 — VincentSC (2018-01-06T13:02:16Z)

Maybe ask the FASTRA-team how they did it? http://fastra.ua.ac.be/en/index.html

---

### 评论 #5 — AirSquirrels (2018-01-06T15:08:26Z)

From the article it looks like they only did 8 cards, which is below the number I can achieve. I am guessing the number of people in the world actually fully familiar with early x86/64 boot and PCIe resource allocation in this context must be quite small. 

---

### 评论 #6 — VincentSC (2018-01-06T15:44:54Z)

In FASTRA-II they had 13 GPUs. One different GPU for booting and 12 for compute. The custom BIOS had a hard-coded ID for which GPU to use for the monitor-output. See also https://www.pcworld.com/article/184648/fastra_ii_supercomputer.html
So no worries - all you're trying now, already has been done 9 years ago. :)

Also checked PCIe-splitters? For example http://amfeltec.com/products/gpu-oriented-cluster/

---

### 评论 #7 — AirSquirrels (2018-01-06T15:51:02Z)

I’m not sure you read my inquiry fully. I already have 13 GPUs running. There is already a lot of custom work done to enable that. My issue is 13 seems to be the limit, and the FASTRA team also stopped there, but that limit doesn’t apply for 3D controller pci class devices vs VGA compatible devices. The reason seems to be related resources needed by either the expansion ROM on the VGA devices or other legacy VGA centric resources. AMD is in a position to know this information more than I am. I have been involved in HPC with GPU clusters for many years, I’m well aware of the regular commercial hardware and PCIe switches, etc. 

---

### 评论 #8 — gstoner (2018-01-15T15:43:25Z)

@AirSquirrels  What GPU are you running Consumer RX Series.    What your hitting most likely is PCIe Config space memory limitation,  But I need a little more info.   

Remember GPU have BAR region they reserve system memory inside the System Memory 4GB range, inside this PCIe is give a limited range.  We have to have all these BAR mapped in that range. 

Linux limit for PCIe device is 127 devices,  but there are other limits we have work through with the System BIOS and PCIe. 



---

### 评论 #9 — AirSquirrels (2018-01-15T16:00:48Z)

Thanks for the reply.

I have observed this limit with at least two consumer grade cards. RX Fury X, and Polaris RX 570/580s. Both show identical BAR resource usage. My Vega system is the same in 64 bit range, but requires 512K in 32 bit non-prefetchable space.

For the 32bit BAR, size is 256K + expansion BAR at 128K, plus losses for alignment. Here's an example from a system with 1 NVIDIA GPU with 16MB in 32 bit at f6000000, +  Region 5: I/O ports at e000 [size=128] + 	[virtual] Expansion ROM at f7000000 [disabled] [size=512K]. Below are the 12 AMD cards BARs in 32 bit space. They appear to be utilizing 1MB each after alignment. In this system, the NVIDIA card alone is using 16MB of 32 bit bar space, suggesting we are not out of such space since I can replace this with an AMD card and still be at the limit (add a 14th AMD card and the system will not POST). This is a 39bit v-addr CPU. 

`	Region 5: Memory at f7c00000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7b00000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7400000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7300000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7200000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7100000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7a00000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7900000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7800000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7700000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7600000 (32-bit, non-prefetchable) [size=256K]
	Region 5: Memory at f7500000 (32-bit, non-prefetchable) [size=256K]
....
	Expansion ROM at f7c40000 [disabled] [size=128K]
	Expansion ROM at f7b40000 [disabled] [size=128K]
	Expansion ROM at f7440000 [disabled] [size=128K]
	Expansion ROM at f7340000 [disabled] [size=128K]
	Expansion ROM at f7240000 [disabled] [size=128K]
	Expansion ROM at f7140000 [disabled] [size=128K]
	Expansion ROM at f7a40000 [disabled] [size=128K]
	Expansion ROM at f7940000 [disabled] [size=128K]
	Expansion ROM at f7840000 [disabled] [size=128K]
	Expansion ROM at f7740000 [disabled] [size=128K]
	Expansion ROM at f7640000 [disabled] [size=128K]
	Expansion ROM at f7540000 [disabled] [size=128K]

       < 64 bit BARs>
	Region 0: Memory at 2fe0000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2fc0000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2ee0000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2ec0000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2ea0000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2e80000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2fa0000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2f80000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2f60000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2f40000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2f20000000 (64-bit, prefetchable) [size=256M]
	Region 0: Memory at 2f00000000 (64-bit, prefetchable) [size=256M]

	Region 2: Memory at 2ff0000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2fd0000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2ef0000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2ed0000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2eb0000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2e90000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2fb0000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2f90000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2f70000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2f50000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2f30000000 (64-bit, prefetchable) [size=2M]
	Region 2: Memory at 2f10000000 (64-bit, prefetchable) [size=2M]
`

With a non-VGA compatible accelerator card (NV branded in this case), I still see 16MB used in 32 bit space, yet the system is happy with 20+ of them. The only difference I see is no Expansion ROM on the "3D Controller" PCI class devices. 

---

### 评论 #10 — okrasit (2018-01-25T17:52:34Z)

@AirSquirrels Try without loading the vbios on boot?

---

### 评论 #11 — ROCmSupport (2020-11-18T11:28:57Z)

Thanks @AirSquirrels 
As its very old issue, and no updates for the last 2 years, this issue is going to be closed.
Request to open a new ticket, if you found any.
Thank you.

---
