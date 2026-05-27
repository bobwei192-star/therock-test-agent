# hsa api call failure at line 900 on running rocminfo

> **Issue #669**
> **状态**: closed
> **创建时间**: 2019-01-13T09:12:51Z
> **更新时间**: 2019-01-14T16:48:46Z
> **关闭时间**: 2019-01-14T16:48:34Z
> **作者**: benkenobi007
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/669

## 描述

**Description:**

- CPU    : Ryzen 5 2500U
- GPUs  : Radeon RX 560X (PCI 0), Radeon Vega 8 (PCI 4)
- OS     : Deepin 15.8 (Debian unstable)
- Kernel : 4.15.0-29deepin-generic
- Groups : kshitij lp sudo video users netdev lpadmin scanner sambashare
- RoCM installed via apt, as described [here](https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository) .

**Suspected Issue:**
RoCM (or kfd) is not reading PCI 0 and is unable to detect the Polaris 11 dGPU. It goes to PCI 4 and finds the uncompatible Vega 8 iGPU and fails.

**Troubleshooting:**
Below is a list of 9 commands I ran while trying to troubleshoot the issue. I have excluded the non GPU related output of lspci -vvv to keep it as short as possible. Please do tell me if the remaining is required.
1. `dkms status`:

> amdgpu, 2.0-89: added
> bcmwl, 6.30.223.271+bdcom, 4.15.0-29deepin-generic, x86_64: installed
> deepin-anything, 0.0, 4.15.0-29deepin-generic, x86_64: installed
> mincores, 0.2.0, 4.15.0-29deepin-generic, x86_64: installed

2. `lsmod | grep amdgpu:`

> amdgpu               2703360  25
> chash                  16384  1 amdgpu
> i2c_algo_bit           16384  1 amdgpu
> ttm                   102400  1 amdgpu
> drm_kms_helper        172032  1 amdgpu
> drm                   397312  15 amdgpu,ttm,drm_kms_helper

3. `lsmod | grep amdkfd`

> amdkfd                180224  2
> amd_iommu_v2           20480  1 amdkfd

4. `sudo lspci | grep vga`

> (NO OUTPUT)

5. `sudo lspci -vvv`

**RX 560X (recognized as RX 460)**

> 01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 460] (rev c0)
> 	Subsystem: Acer Incorporated [ALI] Baffin [Radeon RX 460/560D / Pro 450/455/460/560]
> 	Physical Slot: 0
> 	Control: I/O- Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
> 	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
> 	Interrupt: pin A routed to IRQ 0
> 	Region 0: Memory at 250000000 (64-bit, prefetchable) [size=256M]
> 	Region 2: Memory at 260000000 (64-bit, prefetchable) [size=2M]
> 	Region 4: I/O ports at <ignored> [disabled]
> 	Region 5: Memory at fef00000 (32-bit, non-prefetchable) [size=256K]
> 	Expansion ROM at fef40000 [disabled] [size=128K]
> 	Capabilities: [48] Vendor Specific Information: Len=08 <?>
> 	Capabilities: [50] Power Management version 3
> 		Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
> 		Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
> 	Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
> 		DevCap:	MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
> 			ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
> 		DevCtl:	Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
> 			RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
> 			MaxPayload 256 bytes, MaxReadReq 512 bytes
> 		DevSta:	CorrErr- UncorrErr- FatalErr- UnsuppReq- AuxPwr- TransPend-
> 		LnkCap:	Port #0, Speed 8GT/s, Width x8, ASPM L1, Exit Latency L0s <64ns, L1 <1us
> 			ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
> 		LnkCtl:	ASPM L1 Enabled; RCB 64 bytes Disabled- CommClk+
> 			ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
> 		LnkSta:	Speed 8GT/s, Width x8, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
> 		DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
> 		DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
> 		LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
> 			 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
> 			 Compliance De-emphasis: -6dB
> 		LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
> 			 EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
> 	Capabilities: [a0] MSI: Enable- Count=1/1 Maskable- 64bit+
> 		Address: 0000000000000000  Data: 0000
> 	Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
> 	Capabilities: [270 v1] # 19
> 	Capabilities: [320 v1] Latency Tolerance Reporting
> 		Max snoop latency: 0ns
> 		Max no snoop latency: 0ns
> 	Kernel modules: amdgpu

**Vega 8**

> 04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Raven Bridge [Radeon Vega Series / Radeon Vega Mobile Series] (rev c4) (prog-if 00 [VGA controller])
> 	Subsystem: Acer Incorporated [ALI] Raven Bridge [Radeon Vega Series / Radeon Vega Mobile Series]
> 	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
> 	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
> 	Latency: 0, Cache Line Size: 64 bytes
> 	Interrupt: pin A routed to IRQ 42
> 	Region 0: Memory at 270000000 (64-bit, prefetchable) [size=256M]
> 	Region 2: Memory at 268000000 (64-bit, prefetchable) [size=2M]
> 	Region 4: I/O ports at 0000
> 	Region 5: Memory at ff600000 (32-bit, non-prefetchable) [size=512K]
> 	Capabilities: [48] Vendor Specific Information: Len=08 <?>
> 	Capabilities: [50] Power Management version 3
> 		Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
> 		Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
> 	Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
> 		DevCap:	MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
> 			ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset+
> 		DevCtl:	Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
> 			RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+ FLReset-
> 			MaxPayload 128 bytes, MaxReadReq 512 bytes
> 		DevSta:	CorrErr- UncorrErr- FatalErr- UnsuppReq- AuxPwr- TransPend-
> 		LnkCap:	Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
> 			ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
> 		LnkCtl:	ASPM L0s L1 Enabled; RCB 64 bytes Disabled- CommClk+
> 			ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
> 		LnkSta:	Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
> 		DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
> 		DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR+, OBFF Disabled
> 		LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
> 			 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
> 			 Compliance De-emphasis: -6dB
> 		LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
> 			 EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
> 	Capabilities: [a0] MSI: Enable+ Count=1/4 Maskable- 64bit+
> 		Address: 00000000fee04000  Data: 4024
> 	Capabilities: [c0] MSI-X: Enable- Count=3 Masked-
> 		Vector table: BAR=5 offset=00042000
> 		PBA: BAR=5 offset=00043000
> 	Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
> 	Capabilities: [200 v1] # 15
> 	Capabilities: [270 v1] # 19
> 	Capabilities: [2a0 v1] Access Control Services
> 		ACSCap:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
> 		ACSCtl:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
> 	Capabilities: [2b0 v1] Address Translation Service (ATS)
> 		ATSCap:	Invalidate Queue Depth: 00
> 		ATSCtl:	Enable+, Smallest Translation Unit: 00
> 	Capabilities: [2c0 v1] Page Request Interface (PRI)
> 		PRICtl: Enable- Reset-
> 		PRISta: RF- UPRGI- Stopped+
> 		Page Request Capacity: 00000020, Page Request Allocation: 00000000
> 	Capabilities: [2d0 v1] Process Address Space ID (PASID)
> 		PASIDCap: Exec+ Priv+, Max PASID Width: 10
> 		PASIDCtl: Enable- Exec- Priv-
> 	Capabilities: [320 v1] Latency Tolerance Reporting
> 		Max snoop latency: 0ns
> 		Max no snoop latency: 0ns
> 	Kernel driver in use: amdgpu
> 	Kernel modules: amdgpu

6. `sudo lspci -tv`

> -[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD] Device 15d0
>            +-00.2  Advanced Micro Devices, Inc. [AMD] Device 15d1
>            +-01.0  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge
>            +-01.1-[01]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 460]
>            +-01.6-[02]--+-00.0  Realtek Semiconductor Co., Ltd. RTL8411B PCI Express Card Reader
>            |            \-00.1  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
>            +-01.7-[03]----00.0  Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter
>            +-08.0  Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge
>            +-08.1-[04]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Raven Bridge [Radeon Vega Series / Radeon Vega Mobile Series]
>            |            +-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device 15de
>            |            +-00.2  Advanced Micro Devices, Inc. [AMD] Device 15df
>            |            +-00.3  Advanced Micro Devices, Inc. [AMD] Device 15e0
>            |            +-00.4  Advanced Micro Devices, Inc. [AMD] Device 15e1
>            |            \-00.6  Advanced Micro Devices, Inc. [AMD] Device 15e3
>            +-08.2-[05]----00.0  Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode]
>            +-14.0  Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller
>            +-14.3  Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge
>            +-18.0  Advanced Micro Devices, Inc. [AMD] Device 15e8
>            +-18.1  Advanced Micro Devices, Inc. [AMD] Device 15e9
>            +-18.2  Advanced Micro Devices, Inc. [AMD] Device 15ea
>            +-18.3  Advanced Micro Devices, Inc. [AMD] Device 15eb
>            +-18.4  Advanced Micro Devices, Inc. [AMD] Device 15ec
>            +-18.5  Advanced Micro Devices, Inc. [AMD] Device 15ed
>            +-18.6  Advanced Micro Devices, Inc. [AMD] Device 15ee
>            \-18.7  Advanced Micro Devices, Inc. [AMD] Device 15ef

7. `sudo lspci -n`

> 00:00.0 0600: 1022:15d0
> 00:00.2 0806: 1022:15d1
> 00:01.0 0600: 1022:1452
> 00:01.1 0604: 1022:15d3
> 00:01.6 0604: 1022:15d3
> 00:01.7 0604: 1022:15d3
> 00:08.0 0600: 1022:1452
> 00:08.1 0604: 1022:15db
> 00:08.2 0604: 1022:15dc
> 00:14.0 0c05: 1022:790b (rev 61)
> 00:14.3 0601: 1022:790e (rev 51)
> 00:18.0 0600: 1022:15e8
> 00:18.1 0600: 1022:15e9
> 00:18.2 0600: 1022:15ea
> 00:18.3 0600: 1022:15eb
> 00:18.4 0600: 1022:15ec
> 00:18.5 0600: 1022:15ed
> 00:18.6 0600: 1022:15ee
> 00:18.7 0600: 1022:15ef
> 01:00.0 0380: 1002:67ef (rev c0)
> 02:00.0 ff00: 10ec:5287 (rev 01)
> 02:00.1 0200: 10ec:8168 (rev 12)
> 03:00.0 0280: 168c:003e (rev 32)
> 04:00.0 0300: 1002:15dd (rev c4)
> 04:00.1 0403: 1002:15de
> 04:00.2 1080: 1022:15df
> 04:00.3 0c03: 1022:15e0
> 04:00.4 0c03: 1022:15e1
> 04:00.6 0403: 1022:15e3
> 05:00.0 0106: 1022:7901 (rev 61)

8. `dmesg | grep kfd` (run after rocminfo error)

> [    2.590715] kfd kfd: Initialized module
> [    2.946817] Modules linked in: amdkfd amd_iommu_v2 amdgpu(+) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc chash aesni_intel i2c_algo_bit ttm aes_x86_64 crypto_simd rtsx_pci_sdmmc drm_kms_helper glue_helper syscopyarea cryptd sysfillrect sysimgblt psmouse ahci fb_sys_fops i2c_piix4 r8169 libahci drm rtsx_pci mii i2c_hid(+) video hid wmi
> [    3.534711] amdgpu 0000:04:00.0: kfd not supported on this ASIC

9. Running `clinfo` as root gives:
> ERROR: clGetPlatformIDs(-1001)


---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-01-14T16:48:34Z)

Hi @benkenobi007 

At this time, ROCm is [known not to work](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66) with a dGPU + iGPU setup, as you are trying to run right now.

If you would like to use your dGPU in ROCm, at the moment you will likely need to disable the iGPU in your system BIOS. Using the iGPU in ROCm will require disabling or removing the dGPU. As noted in the issue report I linked above, we are working on this. There is a patch in that ticket you can try that should at least make the GPUs visible to `rocminfo`, though memory allocation is still not working and as such you cannot use the GPUs for computational workloads yet. However, at this time, your setup is not fully supported.

I am going to close this ticket for now and recommend that you keep an eye on [that issue](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66). I prefer to not to have multiple duplicates of the same root issue.

I will note that the reason you see `[ 3.534711] amdgpu 0000:04:00.0: kfd not supported on this ASIC` with regards to your integrated GPU (rather than the errors shown in that issue above) is that appears you are not loading the ROCm 2.0 drivers. However, the ROCm 2.0 GPU driver, has combined `amdkfd` into `amdgpu`. As such, you should not see any output from `lsmod | grep amdkfd`.

Looking at the output of `dkms status`, I see `amdgpu, 2.0-89: added`. This means that the amdgpu driver that is part of ROCm has neither been "built" nor has it been "installed". This is likely because our .deb driver is not guaranteed to work with the version of Debian that you are using. Our .deb files are only tested to work on Ubuntu 16.04 and 18.04 at this time. If you decide to upgrade to a 4.17 or later kernel, you should be able to use the upstream `amdgpu` driver [to run ROCm user-level software with your dGPU](https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md#rocm-support-in-upstream-linux-kernels) (assuming you have disabled your iGPU). 

---
