# Vega Frontier Edition idle stats a bit too hot?

> **Issue #403**
> **状态**: closed
> **创建时间**: 2018-05-06T03:32:31Z
> **更新时间**: 2018-10-09T21:08:44Z
> **关闭时间**: 2018-10-09T20:49:56Z
> **作者**: boberfly
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/403

## 描述

Hi all,

I've been checking rocm-smi on the heat/voltage/clock/fan speeds while the card is idle, and from what I see it seems to default at having the clock at max which sets the average temperature to a whopping 79.0c
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  1   79.0c   31.0W    1528Mhz  945Mhz   18.82%   auto      0%       
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```
I'm in Vancouver and it is getting a bit warmer granted, but it seems a little too hot to me... :)

When I run this manually:
```
rocm-smi --setperflevel low
```
I get much better temperatures and average power readouts:
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  1   36.0c   3.0W     852Mhz   167Mhz   12.94%   low       0%       
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```
Do I need to do anything special for it to go into this lower profile without doing this manually every time? I use this card as purely a compute device, the display is handled by a Quadro k2000 so nothing should be taxing it that I know of, no GUI/X11 is being displayed out of it.

Cheers!

---

## 评论 (9 条)

### 评论 #1 — gstoner (2018-05-06T03:36:27Z)

Is this ROCm 1.8  which Distro  which Linux kernel 

---

### 评论 #2 — boberfly (2018-05-06T03:37:55Z)

Yep I'll be more exact:
ROCm 1.8.0 beta
Ubuntu 18.04 LTS
Kernel 4.13 (from Ubuntu 17.10 using rock-dkms 1.8.0 to build the module)

Cheers

---

### 评论 #3 — gstoner (2018-05-06T03:39:23Z)

Thank you... this helps 


---

### 评论 #4 — gstoner (2018-05-06T22:49:03Z)

Ok did you make sure you're using the right firmware package?   

---

### 评论 #5 — boberfly (2018-05-07T00:21:31Z)

Hey @gstoner I'm not too sure on how to check this exactly. Digging a bit into the kernel I use I might possibly be using the ones found in:
```
/lib/firmware/4.13.0-38-generic/amdgpu/
```
I don't know where to check exactly on firmware but my dmesg has some interesting stuff:
```
[    2.883907] kfd kfd: Initialized module
[    2.884071] checking generic (b0000000 260000) vs hw (d0000000 10000000)
[    2.884097] amdgpu 0000:06:00.0: enabling device (0106 -> 0107)
[    2.884202] [drm] initializing kernel modesetting (VEGA10 0x1002:0x6863 0x1002:0x6B76 0x00).
[    2.884208] [drm] register mmio base: 0xEF100000
[    2.884208] [drm] register mmio size: 524288
[    2.884213] [drm] add ip block number 0 <soc15_common>
[    2.884214] [drm] add ip block number 1 <gmc_v9_0>
[    2.884214] [drm] add ip block number 2 <vega10_ih>
[    2.884215] [drm] add ip block number 3 <psp>
[    2.884215] [drm] add ip block number 4 <amdgpu_powerplay>
[    2.884216] [drm] add ip block number 5 <dm>
[    2.884216] [drm] add ip block number 6 <gfx_v9_0>
[    2.884217] [drm] add ip block number 7 <sdma_v4_0>
[    2.884218] [drm] add ip block number 8 <uvd_v7_0>
[    2.884218] [drm] add ip block number 9 <vce_v4_0>
[    2.884244] [drm] probing gen 2 caps for device 1022:1471 = 700d03/e
[    2.884245] [drm] probing mlw for device 1022:1471 = 700d03
[    2.884251] [drm] UVD is enabled in VM mode
[    2.884251] [drm] UVD ENC is enabled in VM mode
[    2.884252] [drm] VCE enabled in VM mode
[    2.884274] ATOM BIOS: 113-D0501100-109
[    2.884294] [drm] vm size is 256 GB, 3 levels, block size is 9-bit, fragment size is 9-bit
[    2.884298] amdgpu 0000:06:00.0: VRAM: 16368M 0x000000F400000000 - 0x000000F7FEFFFFFF (16368M used)
[    2.884300] amdgpu 0000:06:00.0: GTT: 256M 0x000000F800000000 - 0x000000F80FFFFFFF
[    2.884303] [drm] Detected VRAM RAM=16368M, BAR=256M
[    2.884304] [drm] RAM width 2048bits HBM
[    2.884373] [TTM] Zone  kernel: Available graphics memory: 61772647 kiB
[    2.884373] [TTM] Initializing pool allocator
[    2.884376] [TTM] Initializing DMA pool allocator
[    2.884399] [drm] amdgpu: 16368M of VRAM memory ready
[    2.884400] [drm] amdgpu: 64346M of GTT memory ready.
[    2.884410] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    2.884477] [drm] PCIE GART of 256M enabled (table at 0x000000F400800000).
[    2.885622] [drm] use_doorbell being set to: [true]
[    2.885655] [drm] use_doorbell being set to: [true]
[    2.885807] [drm] Found UVD firmware Version: 1.50 Family ID: 17
[    2.885810] [drm] PSP loading UVD firmware
[    2.886074] [drm] Found VCE firmware Version: 53.19 Binary ID: 4
[    2.886078] [drm] PSP loading VCE firmware
```
For the Vega card via lspci:
```
sudo lspci -vvv
```
```
04:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470 (prog-if 00 [Normal decode])
        Physical Slot: 5
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 26
        NUMA node: 0
        Region 0: Memory at ef200000 (32-bit, non-prefetchable) [size=16K]
        Bus: primary=04, secondary=05, subordinate=06, sec-latency=0
        I/O behind bridge: 0000b000-0000bfff
        Memory behind bridge: ef100000-ef1fffff
        Prefetchable memory behind bridge: 00000000d0000000-00000000e01fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Upstream Port, MSI 00
                DevCap: MaxPayload 512 bytes, PhantFunc 0
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ SlotPowerLimit 75.000W
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 1024 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L1, Exit Latency L0s <512ns, L1 <64us
                        ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM Disabled; Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance De-emphasis: -6dB
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                         EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
        Capabilities: [a0] MSI: Enable- Count=1/1 Maskable- 64bit+
                Address: 0000000000000000  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                AERCap: First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
        Capabilities: [270 v1] #19
        Capabilities: [320 v1] Latency Tolerance Reporting
                Max snoop latency: 0ns
                Max no snoop latency: 0ns
        Capabilities: [370 v1] L1 PM Substates
                L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                          PortCommonModeRestoreTime=250us PortTPowerOnTime=170us
                L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                           T_CommonMode=0us LTR1.2_Threshold=0ns
                L1SubCtl2: T_PwrOn=10us
        Kernel driver in use: pcieport
        Kernel modules: shpchp

05:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471 (prog-if 00 [Normal decode])
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 26
        NUMA node: 0
        Bus: primary=05, secondary=06, subordinate=06, sec-latency=0
        I/O behind bridge: 0000b000-0000bfff
        Memory behind bridge: ef100000-ef1fffff
        Prefetchable memory behind bridge: 00000000d0000000-00000000e01fffff
        Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
        BridgeCtl: Parity- SERR+ NoISA- VGA- MAbort- >Reset- FastB2B-
                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Downstream Port (Slot-), MSI 00
                DevCap: MaxPayload 512 bytes, PhantFunc 0
                        ExtTag+ RBE+
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 1024 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM- Surprise- LLActRep+ BwNot+ ASPMOptComp+
                LnkCtl: ASPM Disabled; Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported ARIFwd-
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled ARIFwd-
                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-, Selectable De-emphasis: -3.5dB
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance De-emphasis: -6dB
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                         EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
        Capabilities: [a0] MSI: Enable- Count=1/1 Maskable- 64bit+
                Address: 0000000000000000  Data: 0000
        Capabilities: [c0] Subsystem: Advanced Micro Devices, Inc. [AMD] Device 1471
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                AERCap: First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
        Capabilities: [270 v1] #19
        Capabilities: [2a0 v1] Access Control Services
                ACSCap: SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: pcieport
        Kernel modules: shpchp

06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition] (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition]
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 39
        NUMA node: 0
        Region 0: Memory at d0000000 (64-bit, prefetchable) [size=256M]
        Region 2: Memory at e0000000 (64-bit, prefetchable) [size=2M]
        Region 4: I/O ports at b000 [size=256]
        Region 5: Memory at ef100000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at ef180000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
                DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 1024 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM Disabled; RCB 64 bytes Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance De-emphasis: -6dB
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                         EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                Address: 00000000fee00498  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                AERCap: First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
        Capabilities: [200 v1] #15
        Capabilities: [270 v1] #19
        Capabilities: [2a0 v1] Access Control Services
                ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Capabilities: [2b0 v1] Address Translation Service (ATS)
                ATSCap: Invalidate Queue Depth: 00
                ATSCtl: Enable-, Smallest Translation Unit: 00
        Capabilities: [2c0 v1] Page Request Interface (PRI)
                PRICtl: Enable- Reset-
                PRISta: RF- UPRGI- Stopped+
                Page Request Capacity: 00000020, Page Request Allocation: 00000000
        Capabilities: [2d0 v1] Process Address Space ID (PASID)
                PASIDCap: Exec+ Priv+, Max PASID Width: 10
                PASIDCtl: Enable- Exec- Priv-
        Capabilities: [320 v1] Latency Tolerance Reporting
                Max snoop latency: 0ns
                Max no snoop latency: 0ns
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu

06:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
        Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin B routed to IRQ 62
        NUMA node: 0
        Region 0: Memory at ef1a0000 (32-bit, non-prefetchable) [size=16K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Endpoint, MSI 00
                DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset- SlotPowerLimit 0.000W
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 1024 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM Disabled; RCB 64 bytes Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete-, EqualizationPhase1-
                         EqualizationPhase2-, EqualizationPhase3-, LinkEqualizationRequest-
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                Address: 00000000fee00718  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                AERCap: First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
        Capabilities: [2a0 v1] Access Control Services
                ACSCap: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
```
Does the ROCm 1.8.0 beta come with firmware itself? I can force install it somehow but I don't know which deb package has them.

Cheers

---

### 评论 #6 — boberfly (2018-05-07T00:38:36Z)

Doing a quick checksum on vega10_uvd.bin SHA256:
```
519382f062481d5b189a14235f51ec7fbe56830564e5d42cf1d2aee126e51a37
```
vega10_vce.bin SHA256:
```
044f312bdcab9bdb8ef4403127606efc8ec0c3e3a205f1853c175db2b39591f8
```

---

### 评论 #7 — gstoner (2018-05-12T04:27:25Z)

Sorry I was traveling this week.  We released ROCm 1.8 official release this week. 

---

### 评论 #8 — jlgreathouse (2018-10-09T18:21:19Z)

Hi @boberfly 

With the recent release of ROCm 1.9.1, do you still see this issue? I just checked one of our test boxes with a Vega Frontier Edition, and I see it idling as expected.

If you still see the issue, I can hopefully walk you through some steps to either alleviate or root cause the issue.

---

### 评论 #9 — boberfly (2018-10-09T20:49:56Z)

@jlgreathouse hi Joseph, actually I think this isn't a problem now for awhile, I do monitor temperatures from time to time and artificially limit it but I think it's because of infinite looped apps like indigo render or blender cycles. Killing them restores power/temps that are idling correctly without the artificial limit.

I think we can safely close this issue then. Cheers!

---
