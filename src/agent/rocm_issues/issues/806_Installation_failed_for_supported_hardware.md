# Installation failed for supported hardware

> **Issue #806**
> **状态**: closed
> **创建时间**: 2019-05-29T10:57:07Z
> **更新时间**: 2019-06-10T09:14:52Z
> **关闭时间**: 2019-06-10T09:14:52Z
> **作者**: adbak
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/806

## 描述

I have a notebook HP EliteBook 850 G5 with theoretically supported Intel Core i7 vPro 8th Gen and Radeon RX 550. Unfortunately testing installation with:

> /opt/rocm/bin/rocminfo

results in the following error:

> hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.4/rocminfo/rocminfo.cc. Call returned 4104

In kernel log I have a well known:

> [    2.117230] kfd kfd: skipped device 1002:699f, PCI rejects atomics

however my output for:

> sudo lspci -vvvn

looks like this:

```
01:00.0 0380: 1002:699f (rev c3)
	Subsystem: 103c:83b4
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0
	Interrupt: pin A routed to IRQ 125
	Region 0: Memory at 90000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at a0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at 3000 [size=256]
	Region 5: Memory at ba300000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at ba340000 [disabled] [size=128K]
	Capabilities: [48] Vendor Specific Information: Len=08 <?>
	Capabilities: [50] Power Management version 3
		Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
		Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
	Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
		DevCap:	MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
			ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
		DevCtl:	Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
			RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
			MaxPayload 256 bytes, MaxReadReq 512 bytes
		DevSta:	CorrErr- UncorrErr- FatalErr- UnsuppReq- AuxPwr- TransPend-
		LnkCap:	Port #0, Speed 8GT/s, Width x8, ASPM L1, Exit Latency L0s <64ns, L1 <1us
			ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
		LnkCtl:	ASPM L1 Enabled; RCB 64 bytes Disabled- CommClk+
			ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
		LnkSta:	Speed 8GT/s, Width x2, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
		DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
		DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR+, OBFF Disabled
		LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
			 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
			 Compliance De-emphasis: -6dB
		LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete+, EqualizationPhase1+
			 EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
	Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
		Address: 00000000fee002b8  Data: 0000
	Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
	Capabilities: [270 v1] #19
	Capabilities: [320 v1] Latency Tolerance Reporting
		Max snoop latency: 0ns
		Max no snoop latency: 0ns
	Capabilities: [370 v1] L1 PM Substates
		L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
			  PortCommonModeRestoreTime=0us PortTPowerOnTime=170us
		L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
			   T_CommonMode=0us LTR1.2_Threshold=0ns
		L1SubCtl2: T_PwrOn=10us
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```

so although `LnkSta` informs about the proper PCIe 3.0 speed, the width is lower than in `LnkCap`. Is this a problem or something else entirely? Any ideas how can I fix this?

---

## 评论 (6 条)

### 评论 #1 — JMadgwick (2019-06-01T10:08:41Z)

> PCI rejects atomics

The RX 550 is a Polaris 12 chip and [requires support for atomics](https://github.com/RadeonOpenCompute/ROCm#supported-gpus).
Your Laptop should support atomics, they have been supported since Haswell. The only thing I can think of is that the BIOS is configured strangely (atomics disabled) or a PCIe bridge is used (doesn't seem likely it would use one).
[This issue has a lot of conversation about it](https://github.com/RadeonOpenCompute/ROCm/issues/157#issuecomment-324830593). You should be seeing an _AtomicOpsCap_ line and similar in your lspci output.
I would [check the BIOS](http://h10032.www1.hp.com/ctg/Manual/c06114605) and set the graphics to dedicated only and maybe try disabling power management and setting PCIe to always Gen 3.
If this laptop has switchable graphics it could be that when booting they are in a low power state that doesn't expose the atomics or doesn't expose them generally because of poorly implemented power saving.
You could try contacting HP and asking them, but I doubt the normal support channels will know anything about PCIe atomics.

---

### 评论 #2 — adbak (2019-06-03T10:31:43Z)

@JMadgwick thank you very much for your time. What you write seems very reasonable. But unfortunately my BIOS doesn't offer such fancy options like setting PCIe to always Gen 3 (as described in the mentioned whitepaper). To be honest it offers very little. Updating BIOS to the newest version didn't help either.

---

### 评论 #3 — adbak (2019-06-06T14:12:40Z)

@JMadgwick I'm intrigued by this `PCIe bridge` issue. What does it exactly mean and how to check for it? My outputs for `lspci` and `lspci -t` respectively look like this:

```
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 08)
00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620 (rev 07)
00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 08)
00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
00:15.1 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 (rev 21)
00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
00:16.3 Serial controller: Intel Corporation Device 9d3d (rev 21)
00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
00:1c.3 PCI bridge: Intel Corporation Device 9d13 (rev f1)
00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
00:1f.0 ISA bridge: Intel Corporation Intel(R) 100 Series Chipset Family LPC Controller/eSPI Controller - 9D4E (rev 21)
00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (4) I219-LM (rev 21)
01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X] (rev c3)
02:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)
03:00.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
04:00.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
04:01.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
04:02.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
05:00.0 System peripheral: Intel Corporation JHL6340 Thunderbolt 3 NHI (C step) [Alpine Ridge 2C 2016] (rev 02)
3b:00.0 USB controller: Intel Corporation Device 15db (rev 02)
3c:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981
```

and 

```
-[0000:00]-+-00.0
           +-02.0
           +-04.0
           +-14.0
           +-14.2
           +-15.0
           +-15.1
           +-16.0
           +-16.3
           +-1c.0-[01]----00.0
           +-1c.3-[02]----00.0
           +-1c.4-[03-3b]----00.0-[04-3b]--+-00.0-[05]----00.0
           |                               +-01.0-[06-3a]--
           |                               \-02.0-[3b]----00.0
           +-1d.0-[3c]----00.0
           +-1f.0
           +-1f.2
           +-1f.3
           +-1f.4
           \-1f.6
```

Does it mean I have a bridge (between which components?) that doesn't support atomics?

---

### 评论 #4 — JMadgwick (2019-06-06T15:06:07Z)

I'm not an expert but from the looks of it your GPU _might_ be connected to the chipset (and not the CPU directly).
The output for `lspci` on my system is below. In my system I have a so called "processor PCI Express Root Port" (00:01.0) this connects to the GPU (03:00._X_). This is a desktop and I know that the GPU is in the slot which connects directly to the CPU. All the other PCIe slots are connected to the Chipset and these show as "Series Chipset Family PCI Express Root Port".

I notice that your output is missing a 00:01.0 entry and the GPU is connected to "Sunrise Point-LP PCI Express Root Port" (00:1c.0) instead. ["Sunrise Point" is the name of the chipset](https://en.wikipedia.org/wiki/Platform_Controller_Hub#Sunrise_Point). It seems odd that the GPU seems to not be connected to the CPU directly.

I notice in your earlier post that the GPU has "LnkSta: Speed 8GT/s, Width x2". Does this increase under load? I believe the RX 550 has a maximum of x8 lanes (not x16) so this value should change (potentially to the LnkCap x8 value) when the GPU is loaded. [This chipset does support PCIe 3.0](https://ark.intel.com/content/www/us/en/ark/products/90583/mobile-intel-qm170-chipset.html) but I don't know if it supports atomics. It would seem to me that it should, somewhere Intel might have an engineering manual that goes into more detail.

From what I can tell (not an expert). Either:
1. Your GPU is connected to the chipset (not directly to the CPU), and
a. the chipset doesn't support atomics, or
b. the chipset does support atomics but they are disabled or not working due to decisions made by HP
2. Your GPU is in fact connected directly to the CPU (less likely) but atomics are not working because of HP

I think that generally the bridges which the devs warn about are those from other companies and not the ones built into the motherboard. For instance PCIe expansion breakout boxes which have multiplexing chips. However if I'm right in the assumptions I've made above then there are potentially many laptops which are incompatible because of the way the GPU has been connected.
_Note that my system doesn't support Atomics anyway, this shouldn't matter as far as determining how the devices are connected._

```
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v2/Ivy Bridge DRAM Controller (rev 09)
00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port (rev 09)
00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04)
00:16.0 Communication controller: Intel Corporation 7 Series/C216 Chipset Family MEI Controller #1 (rev 04)
00:1a.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #2 (rev 04)
00:1b.0 Audio device: Intel Corporation 7 Series/C216 Chipset Family High Definition Audio Controller (rev 04)
00:1c.0 PCI bridge: Intel Corporation 7 Series/C216 Chipset Family PCI Express Root Port 1 (rev c4)
00:1c.1 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 2 (rev c4)
00:1c.3 PCI bridge: Intel Corporation 82801 PCI Bridge (rev c4)
00:1c.4 PCI bridge: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 5 (rev c4)
00:1d.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #1 (rev 04)
00:1f.0 ISA bridge: Intel Corporation Z77 Express Chipset LPC Controller (rev 04)
00:1f.2 SATA controller: Intel Corporation 7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode] (rev 04)
00:1f.3 SMBus: Intel Corporation 7 Series/C216 Chipset Family SMBus Controller (rev 04)
01:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Device 14a0 (rev c1)
02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Device 14a1
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 20 [Radeon VII] (rev c1)
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Vega 20 HDMI Audio [Radeon VII]
05:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 06)
06:00.0 PCI bridge: ASMedia Technology Inc. ASM1083/1085 PCIe to PCI Bridge (rev 03)
07:01.0 FireWire (IEEE 1394): Texas Instruments TSB43AB23 IEEE-1394a-2000 Controller (PHY/Link)
08:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981
```


```
-[0000:00]-+-00.0
           +-01.0-[01-03]----00.0-[02-03]----00.0-[03]--+-00.0
           |                                            \-00.1
           +-14.0
           +-16.0
           +-1a.0
           +-1b.0
           +-1c.0-[04]--
           +-1c.1-[05]----00.0
           +-1c.3-[06-07]----00.0-[07]----01.0
           +-1c.4-[08]----00.0
           +-1d.0
           +-1f.0
           +-1f.2
           \-1f.3
```

---

### 评论 #5 — adbak (2019-06-07T10:31:57Z)

> I notice in your earlier post that the GPU has "LnkSta: Speed 8GT/s, Width x2". Does this increase under load?

The speed indeed can increase, sometimes after reboot I get `2.5GT/s` in `lspci` output and only after some time it changes to `8GT/s`, but the width always remains `x2`.

---

### 评论 #6 — JMadgwick (2019-06-07T10:44:44Z)

> the width always remains `x2`

In that case it is probably only connected with x2 lanes although it can support x8 it looks like HP has designed to use only x2. I don't think you are going to be able to get Rocm to work unfortunately. It seems HP is to blame here because of how they have designed this laptop. If they had done it differently then it _should_ be possible to use Rocm on a laptop with this GPU.

---
