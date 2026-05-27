# Potential issue with amdgpu/4.0-23 firmware?

> **Issue #1357**
> **状态**: closed
> **创建时间**: 2021-01-09T15:43:52Z
> **更新时间**: 2021-01-09T20:36:44Z
> **关闭时间**: 2021-01-09T20:36:44Z
> **作者**: torehl
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1357

## 描述

Hi,

     installed an AMD Instinct Mi100 in a node on Wednesday. It worked well for a few days. After a reboot today, the firmware download fails when driver loads. Any suggestions? Anyone know of some way to force load of firmware? Is this a known bug?

root@n004:~# uname -ar
Linux n004 4.15.0-130-generic #134-Ubuntu SMP Tue Jan 5 20:46:26 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

[    9.602662] [drm] amdgpu kernel modesetting enabled.
[    9.602665] [drm] amdgpu version: 5.6.19
[    9.602871] amdgpu: Ignoring ACPI CRAT on non-APU system
[    9.602887] amdgpu: Virtual CRAT table created for CPU
[    9.602998] amdgpu: Topology: Add CPU node
[    9.605792] amdgpu 0000:23:00.0: enabling device (0000 -> 0003)
[    9.605889] amdgpu 0000:23:00.0: Trusted Memory Zone (TMZ) feature not supported
[    9.605890] amdgpu 0000:23:00.0: set kernel compute queue number to 8 due to invalid parameter provided by user
[    9.605986] amdgpu 0000:23:00.0: Direct firmware load for amdgpu/arcturus_gpu_info.bin failed with error -2
[    9.605988] amdgpu 0000:23:00.0: Failed to load gpu_info firmware "amdgpu/arcturus_gpu_info.bin"
[    9.605988] amdgpu 0000:23:00.0: Fatal error during GPU init
[    9.605990] amdgpu 0000:23:00.0: amdgpu: finishing device.
[    9.606063] amdgpu: probe of 0000:23:00.0 failed with error -2
[  341.738809] amdgpu: PeerDirect support was initialized successfully

      Seeing adapter with lspci just fine.  No indications in hardware (BMC). All seems ok. 

root@n004:~# lspci -vvv -s 0000:23:00.0
23:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 738c (rev 01)
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device 0c34
	Control: I/O+ Mem+ BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Interrupt: pin A routed to IRQ 43
	NUMA node: 2
	Region 0: Memory at 67800000000 (64-bit, prefetchable) [size=32G]
	Region 2: Memory at 68000000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at 3000 [size=256]
	Region 5: Memory at eb400000 (32-bit, non-prefetchable) [size=512K]
	Expansion ROM at eb480000 [disabled] [size=128K]
	Capabilities: [48] Vendor Specific Information: Len=08 <?>
	Capabilities: [50] Power Management version 3
		Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
		Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
	Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
		DevCap:	MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
			ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
		DevCtl:	Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
			RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
			MaxPayload 256 bytes, MaxReadReq 512 bytes
		DevSta:	CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
		LnkCap:	Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
			ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
		LnkCtl:	ASPM L1 Enabled; RCB 64 bytes Disabled- CommClk+
			ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
		LnkSta:	Speed 16GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
		DevCap2: Completion Timeout: Range ABCD, TimeoutDis+, LTR-, OBFF Not Supported
		DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
		LnkCtl2: Target Link Speed: 16GT/s, EnterCompliance- SpeedDis-
			 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
			 Compliance De-emphasis: -6dB
		LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
			 EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
	Capabilities: [a0] MSI: Enable- Count=1/1 Maskable- 64bit+
		Address: 0000000000000000  Data: 0000
	Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
	Capabilities: [150 v2] Advanced Error Reporting
		UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
		CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
		CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
		AERCap:	First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
	Capabilities: [270 v1] #19
	Capabilities: [2a0 v1] Access Control Services
		ACSCap:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
		ACSCtl:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
	Capabilities: [2c0 v1] Page Request Interface (PRI)
		PRICtl: Enable- Reset-
		PRISta: RF- UPRGI- Stopped+
		Page Request Capacity: 00000100, Page Request Allocation: 00000000
	Capabilities: [2d0 v1] Process Address Space ID (PASID)
		PASIDCap: Exec+ Priv+, Max PASID Width: 10
		PASIDCtl: Enable- Exec- Priv-
	Capabilities: [400 v1] #25
	Capabilities: [410 v1] #26
	Capabilities: [440 v1] #27
	Kernel modules: amdgpu
 
torel@n004:~$ /opt/rocm-4.0.0/opencl/bin/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3212.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
torel@n004:~$ /opt/rocm-4.0.0/bin/rocm-smi 


======================= ROCm System Management Interface =======================
WARNING: No AMD GPUs specified
================================= Concise Info =================================
GPU  Temp  AvgPwr  SCLK  MCLK  Fan  Perf  PwrCap  VRAM%  GPU%  
================================================================================
============================= End of ROCm SMI Log ==============================
torel@n004:~$ 


---

## 评论 (1 条)

### 评论 #1 — torehl (2021-01-09T20:36:44Z)

Had forgotten to reinstall rock-dkms-firmware after kernel upgrade

ii  rock-dkms            1:4.0-23        all             amdgpu driver in DKMS format.
ii  rock-dkms-firmware   1:4.0-23        all             firmware blobs used by amdgpu driver in DKMS 


---
