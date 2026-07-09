# P2P support

- **Issue #:** 787
- **State:** closed
- **Created:** 2019-05-07T13:57:18Z
- **Updated:** 2023-12-18T18:56:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/787

I am having trouble getting P2P communication to work. I think it is an issue with the large BAR address space. My setup is as follows:
- ASUS X99-E WS/USB 3.1
- Intel Core i7-6900K
- 2x Radeon Pro WX 8200 (in slots 1 and 5)

This motherboard is listed as a [system that AMD has tested](https://gpuopen.com/radeon-open-compute-new-era-heterogeneous-in-hpc-ultrascale-computing-the-boltzmann-initiative-delivering-new-opportunities-in-gpu-computing-research/) which has large BAR support. The GPUs seem to support large BAR and after enabling "Above 4G Decoding" in the BIOS, they seem to have their address spaces fully mapped:
```
$ sudo lspci -vv
...
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon PRO WX 8100] (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 32 bytes
	Interrupt: pin A routed to IRQ 67
	NUMA node: 0
	Region 0: Memory at 380400000000 (64-bit, prefetchable) [size=8G]
	Region 2: Memory at 380300000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at fb800000 (32-bit, non-prefetchable) [size=512K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: [48] Vendor Specific Information: Len=08 <?>
	Capabilities: [50] Power Management version 3
		Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
		Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
	Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
		DevCap:	MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
			ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
		DevCtl:	Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
			RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
			MaxPayload 256 bytes, MaxReadReq 512 bytes
		DevSta:	CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
		LnkCap:	Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
			ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
		LnkCtl:	ASPM Disabled; RCB 64 bytes Disabled- CommClk+
			ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
		LnkSta:	Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
		DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
		DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
		LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
			 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
			 Compliance De-emphasis: -6dB
		LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
			 EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
	Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
		Address: 00000000fee05000  Data: 4023
	Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
	Capabilities: [150 v2] Advanced Error Reporting
		UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
		CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
		CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
		AERCap:	First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
	Capabilities: [200 v1] #15
	Capabilities: [270 v1] #19
	Capabilities: [2a0 v1] Access Control Services
		ACSCap:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
		ACSCtl:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
	Capabilities: [2b0 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable-, Smallest Translation Unit: 00
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
...
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon PRO WX 8100] (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Vega
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 32 bytes
	Interrupt: pin A routed to IRQ 61
	NUMA node: 0
	Region 0: Memory at 380000000000 (64-bit, prefetchable) [size=8G]
	Region 2: Memory at 380200000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at d000 [size=256]
	Region 5: Memory at fb500000 (32-bit, non-prefetchable) [size=512K]
	Expansion ROM at fb580000 [disabled] [size=128K]
	Capabilities: [48] Vendor Specific Information: Len=08 <?>
	Capabilities: [50] Power Management version 3
		Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
		Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
	Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
		DevCap:	MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
			ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
		DevCtl:	Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
			RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
			MaxPayload 256 bytes, MaxReadReq 512 bytes
		DevSta:	CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
		LnkCap:	Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
			ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
		LnkCtl:	ASPM Disabled; RCB 64 bytes Disabled- CommClk+
			ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
		LnkSta:	Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
		DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
		DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
		LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
			 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
			 Compliance De-emphasis: -6dB
		LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
			 EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
	Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
		Address: 00000000fee01000  Data: 4023
	Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
	Capabilities: [150 v2] Advanced Error Reporting
		UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
		CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
		CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
		AERCap:	First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
	Capabilities: [200 v1] #15
	Capabilities: [270 v1] #19
	Capabilities: [2a0 v1] Access Control Services
		ACSCap:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
		ACSCtl:	SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
	Capabilities: [2b0 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable-, Smallest Translation Unit: 00
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
...
```

I am running Ubuntu 18.04 (kernel 4.15.0-48-generic) and have installed `rocm-dkms` 2.3-14 from repo.radeon.com

Despite the apparently successful large BAR mapping, and sharing a PCIe root complex, the two GPUs do not show up as peers. For example:
```
$ ./rocm_bandwidth_test 
............
........

          RocmBandwidthTest Version: 2.0.1

          Device: 0,  Intel(R) Core(TM) i7-6900K CPU @ 3.20GHz
          Device: 1,  Vega 10 [Radeon PRO WX 8100],  0d:0.0
          Device: 2,  Vega 10 [Radeon PRO WX 8100],  07:0.0

          Device Access

          D/D       0         1         2         

          0         1         1         1         

          1         1         1         0         

          2         1         0         1         


          Device Numa Distance

          D/D       0         1         2         

          0         0         N/A       N/A       

          1         20        0         N/A       

          2         20        N/A       0         


          Unidirectional copy peak bandwidth GB/s

          D/D       0           1           2           

          0         N/A         13.377405   13.366351   

          1         14.310061   404.438375  N/A         

          2         14.309640   N/A         389.988691  


          Bdirectional copy peak bandwidth GB/s

          D/D       0           1           2           

          0         N/A         25.912159   25.915931   

          1         25.938865   N/A         N/A         

          2         25.936705   N/A         N/A         

$ cd ~/test_cl_amd_copy_buffer_p2p
$ ./test_p2p 
Searching for platforms...
    Using platform: AMD Accelerated Parallel Processing
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #0: 0
PCIe Topology of device 0: d:0.0
Searching for devices...
    Using device: gfx900
Number of P2P devices that can be seen from device #1: 0
PCIe Topology of device 1: 7:0.0
Device 0 and device 1 are not P2P neighbors
They cannot be used to test P2P transfers.
Exiting!
```
(The latter test is https://github.com/jlgreathouse/test_cl_amd_copy_buffer_p2p)

I think the issue might be related to the address range. Region 0 of `0d:00.0` is mapped to `0x380000000000 = 61572651155456 > 2^44`, and similar for `07:00.0`. If this is the problem, I suppose I need to change the equivalent of the "MMIOH Base" and "MMIO High Size" settings discussed in the [explanation of large BAR](https://rocm.github.io/ROCmPCIeFeatures.html#bar-memory-overview) to get it in the right range. However, I can't find those settings in the ASUS BIOS. If I am correct in these assumptions but you have had success with this setup internally (as I understand the motherboard is used in one of your test configurations), how did you resolve this issue?