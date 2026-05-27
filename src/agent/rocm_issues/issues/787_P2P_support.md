# P2P support

> **Issue #787**
> **状态**: closed
> **创建时间**: 2019-05-07T13:57:18Z
> **更新时间**: 2023-12-18T18:56:04Z
> **关闭时间**: 2023-12-18T18:56:03Z
> **作者**: FinnStokes
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/787

## 描述

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

---

## 评论 (14 条)

### 评论 #1 — FinnStokes (2019-07-10T18:14:40Z)

We replaced the motherboard we were using with the SuperMicro X11SRA (with Intel Xeon W‑2123 CPU). This motherboard does have the "MMIOH Base" and "MMIO High Size" settings, and using them we were able to get the addresses mapped to the desired ranges, and peer access seems to be working now:
```
$ ./rocm_bandwidth_test
................
............

          RocmBandwidthTest Version: 2.0.1

          Device: 0,  Intel(R) Xeon(R) W-2123 CPU @ 3.60GHz
          Device: 1,  Vega 10 [Radeon PRO WX 8100],  19:0.0
          Device: 2,  Vega 10 [Radeon PRO WX 8100],  67:0.0

          Device Access

          D/D       0         1         2         

          0         1         1         1         

          1         1         1         1         

          2         1         1         1         


          Device Numa Distance

          D/D       0         1         2         

          0         0         20        20        

          1         20        0         40        

          2         20        40        0         


          Unidirectional copy peak bandwidth GB/s

          D/D       0           1           2           

          0         N/A         13.691481   13.668804   

          1         14.285625   388.648245  10.261399   

          2         14.286586   10.261898   389.485083  


          Bdirectional copy peak bandwidth GB/s

          D/D       0           1           2           

          0         N/A         18.476459   18.508231   

          1         17.803980   N/A         18.906259   

          2         17.743369   18.907250   N/A    
```

Perhaps the ASUS X99-E WS/USB 3.1 should be removed from the list of motherboards with sufficient large BAR support. While it does have large BAR support, it lacks the MMIO range options necessary to actually utilise it.

---

### 评论 #2 — emerth (2020-02-19T21:15:59Z)

<...>

I thought I would share my experience in this regard, though I know your work was 1 year ago. Your posts here were helpful in understanding what was going on with my cards.

Using a pair of Radeon VII cards with an X370 Asus Tuf mainboard, the cards would be mapped low with 256 MB windows. The system also had a ConnectX-2 card and a Samsung 960 PCIe3 x4 NVME SSD. 

Removing the ConnectX-2 had no effect, but after removing the Samsung 960 the Radeon VIIs were mapped high with 16GB windows.

I also found that using an Adata PCIe3 x4 NVME SSD (model ASX8200PNP-1TT-C) along with the ConnectX-2 resulted in the Radeon VII cards mapped high with 16GB windows.

Did you ever find a way to do RDMA between GPU memory that did not involve writing custom C Infiniband code?

---

### 评论 #3 — FinnStokes (2020-03-06T10:44:42Z)

Glad to hear my posts have been helpful! We got close but weren't quite able to get there before other projects took priority. By only having a single gpu and a single ConnectX card on each node with the new motherboards we were able to get everything in the correct address ranges to do RDMA, however it turned out that the ConnectX cards we had available didn't properly support infiniband. The next step would have been to get some proper infiniband cards, but by this stage our situation had changed and this project was less of a priority. It has been on the back-burner since then, but we may end up returning to it at some point.

---

### 评论 #4 — huanzhang12 (2020-04-02T06:10:59Z)

I have a AMD X470 motherboard with broken "Above 4G decoding" support. The BIOS maps GPU BAR memories below 4 GB (even "Above 4G decoding" is enabled) and there is no way to find sufficient space to resize the BARs, and p2p does not work on ROCm.

I was able to get P2P working by (1) booting the kernel with "pci=nocrs" option which reassign PCI root complex memory resource, and (2) patching and rebuilding the amdgpu driver code: [amdgpu_device.c](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/05883f12fbdf011852ba919ff27c945d6501c4bb/drivers/gpu/drm/amd/amdgpu/amdgpu_device.c#L920) Remove this condition `res->start > 0x100000000ull`; this condition prevents the driver from attempting reallocating BAR memory. I use the `rocm-dkms` package so the source can be easily found at `/usr/src/amdgpu-*/amd/amdgpu/amdgpu_device.c`.

With these tricks applied it seems "above 4G decoding" in BIOS is not necessary to enable P2P support, and I guess the issues @FinnStokes @emerth had can be workaround similarly as well. As a reference, my `rocm-bandwidth-test` results look like this:

```
          RocmBandwidthTest Version: 2.3.11

          Launch Command is: rocm-bandwidth-test (rocm_bandwidth -a + rocm_bandwidth -A)


          Device: 0,  AMD Ryzen 7 2700X Eight-Core Processor
          Device: 1,  Ellesmere [Radeon RX 470/480/570/570X/580/580X/590],  01:0.0
          Device: 2,  Vega 20 [Radeon VII],  29:0.0
          Device: 3,  Ellesmere [Radeon RX 470/480/570/570X/580/580X/590],  2a:0.0
          Device: 4,  Vega 20 [Radeon VII],  2d:0.0

          Inter-Device Access

          D/D       0         1         2         3         4         

          0         1         1         1         1         1         

          1         1         1         1         1         1         

          2         1         1         1         1         1         

          3         1         1         1         1         1         

          4         1         1         1         1         1         


          Inter-Device Numa Distance

          D/D       0         1         2         3         4         

          0         0         20        20        20        20        

          1         20        0         40        40        40        

          2         20        40        0         40        40        

          3         20        40        40        0         40        

          4         20        40        40        40        0         


          Unidirectional copy peak bandwidth GB/s

          D/D       0           1           2           3           4           

          0         N/A         2.770479    3.578846    2.771179    7.157202    

          1         2.836541    202.427799  2.628326    2.630832    2.631393    

          2         3.574820    3.574880    589.090226  3.574881    3.574820    

          3         2.834477    2.630607    2.628035    205.050932  2.630706    

          4         7.163805    3.580771    3.578511    3.581689    587.440106  


          Bdirectional copy peak bandwidth GB/s

          D/D       0           1           2           3           4           

          0         N/A         4.314801    5.919565    4.326627    13.049600   

          1         4.314801    N/A         5.042996    4.972801    5.151355    

          2         5.919565    5.042996    N/A         3.509641    5.614854    

          3         4.326627    4.972801    3.509641    N/A         3.406554    

          4         13.049600   5.151355    5.614854    3.406554    N/A         
```

The bandwidth are within expectation since the 4 GPUs run at x4/x4/x4/x8 configuration.

---

### 评论 #5 — emerth (2020-04-02T13:48:40Z)

Hi Huan,

Thanks! I will give this a try in the next few days.
 
> I was able to get P2P working by (1) booting the kernel with "pci=nocrs" option which reassign PCI root complex memory resource, and (2) patching and rebuilding the amdgpu driver code: [amdgpu_device.c](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/05883f12fbdf011852ba919ff27c945d6501c4bb/drivers/gpu/drm/amd/amdgpu/amdgpu_device.c#L920) Remove this condition `res->start > 0x100000000ull`; this condition prevents the driver from attempting reallocating BAR memory. I use the `rocm-dkms` package so the source can be easily found at `/usr/src/amdgpu-*/amd/amdgpu/amdgpu_device.c`.
> 


---

### 评论 #6 — huanzhang12 (2020-04-07T23:06:51Z)

@emerth Sounds great! I was also able to get large BAR working on a B350 motherboard using this trick as well. If the trick also works for you, I will submit a patch to the kernel driver to get that `res->start > 0x100000000ull` condition removed, so that people can apply this trick more easily.

---

### 评论 #7 — YumingChang02 (2022-12-15T02:28:04Z)

There seems to have no mentioning of navi or navi2 in documents, is this supported only on vega/cdna cards?

---

### 评论 #8 — emerth (2022-12-15T18:50:59Z)

Yuming: do you mean P2P and BAR and RDMA, or ROCm generally?

I cannot speak to P2P/BAR/RDMA because I have no Navi cards.

ROCm support for Navi 1 and Nava 2 is limited. OpenCL works, but HIP does not work for Navi1. HIP works on some Navi 2 based "workstation cards". I have never found anyone that said HIP worked for them on a consumer/gaming Navi 2 card.

________________________________
From: YuMingChang ***@***.***>
Sent: December 15, 2022 2:28 AM
To: RadeonOpenCompute/ROCm ***@***.***>
Cc: emerth ***@***.***>; Mention ***@***.***>
Subject: Re: [RadeonOpenCompute/ROCm] P2P support (#787)


There seems to have no mentioning of navi or navi2 in documents, is this supported only on vega/cdna cards?

—
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/787#issuecomment-1352475778>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AKXG4Y7ZK3SBUIFQZI4OHA3WNJ64BANCNFSM4HLJDJ5A>.
You are receiving this because you were mentioned.Message ID: ***@***.***>


---

### 评论 #9 — YumingChang02 (2022-12-16T01:28:44Z)

emerth: I mean P2P / RDMA on Navi2 cards,
Overwriting HSA_OVERRIDE_GFX_VERSION to 10.3.0 ( corresponding Navi workstation card id ), I can run rocm pytorch on my 6700xts, just wondering which features are brought along from vega.

---

### 评论 #10 — emerth (2022-12-17T04:51:13Z)

Excellent! I did not know this kind of thing worked. What kind of image rate do you get training something like Googlenet (assuming you train Googlenet)?
________________________________
From: YuMingChang ***@***.***>
Sent: December 16, 2022 1:28 AM
To: RadeonOpenCompute/ROCm ***@***.***>
Cc: emerth ***@***.***>; Mention ***@***.***>
Subject: Re: [RadeonOpenCompute/ROCm] P2P support (#787)


emerth: I mean P2P / RDMA on Navi2 cards,
Overwriting HSA_OVERRIDE_GFX_VERSION to 10.3.0 ( corresponding Navi workstation card id ), I can run rocm pytorch on my 6700xts, just wondering which features are brought along from vega.

—
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/787#issuecomment-1354050572>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AKXG4YYBKX6DXGAYN2UKPDDWNPAVNANCNFSM4HLJDJ5A>.
You are receiving this because you were mentioned.Message ID: ***@***.***>


---

### 评论 #11 — YumingChang02 (2022-12-17T15:01:33Z)

I've tried resnet50, if you'd want to see googlenet results, i can give it a shot, but there seems to be some optimization issues, as i openned an issue here https://github.com/ROCmSoftwarePlatform/pytorch/issues/1147

```
System:
  Host: X99-TF-8 Kernel: 6.0.12-arch1-1 arch: x86_64 bits: 64 compiler: gcc v: 12.2.0
    Console: pty pts/4 Distro: Arch Linux
Machine:
  Type: Desktop System: HUANANZHI product: N/A v: N/A serial: <superuser required>
  Mobo: HUANANZHI model: X99-TF-Q GAMING v: V1.2 serial: <superuser required>
    UEFI: American Megatrends v: 5.11 date: 07/06/2022
CPU:
  Info: 12-core model: Intel Xeon E5-2673 v3 bits: 64 type: MT MCP arch: Haswell rev: 2 cache:                                                                                                                                                                                   L1: 768 KiB L2: 3 MiB L3: 30 MiB
  Speed (MHz): avg: 1891 high: 3100 min/max: 1200/3100 cores: 1: 2642 2: 1428 3: 2395 4: 1197
    5: 2694 6: 1800 7: 3100 8: 1197 9: 1200 10: 3100 11: 1197 12: 2694 13: 2400 14: 1200 15: 2394
    16: 1200 17: 1200 18: 2694 19: 2396 20: 1200 21: 1197 22: 2476 23: 1200 24: 1200
    bogomips: 114965
  Flags: avx avx2 ht lm nx pae sse sse2 sse3 sse4_1 sse4_2 ssse3 vmx
Graphics:
  Device-1: AMD Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M] vendor: Micro-Star MSI
    driver: amdgpu v: kernel arch: RDNA-2 bus-ID: 05:00.0
  Device-2: AMD Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M] vendor: Micro-Star MSI
    driver: amdgpu v: kernel arch: RDNA-2 bus-ID: 09:00.0
  Device-3: AMD Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M] vendor: Micro-Star MSI
    driver: amdgpu v: kernel arch: RDNA-2 bus-ID: 0c:00.0
```
# note that these cards are running on x4 only ( i am using pcie bifrucation, splitting x16 to x4x4x4x4

```
markchang@X99-TF-8 ~ [1]> docker run -it -e HSA_OVERRIDE_GFX_VERSION=10.3.0 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host -v /srv/Dataset:/Dataset:ro -v /home/markchang/main.py:/main.py rocm/pytorch:latest python /main.py -a resnet50 -b 300 -j8 -p100 /Dataset/ILSVRC2012
=> creating model 'resnet50'
Epoch: [0][   1/4271]   Time 155.944 (155.944)  Data  4.888 ( 4.888)    Loss 7.1376e+00 (7.1376e+00)    Acc@1   0.00 (  0.00)   Acc@5   0.33 (  0.33)
Epoch: [0][ 101/4271]   Time  0.947 ( 2.476)    Data  0.000 ( 0.049)    Loss 6.9035e+00 (7.2136e+00)    Acc@1   0.00 (  0.13)   Acc@5   0.33 (  0.60)
Epoch: [0][ 201/4271]   Time  1.006 ( 1.715)    Data  0.000 ( 0.027)    Loss 6.8930e+00 (7.0610e+00)    Acc@1   0.00 (  0.13)   Acc@5   0.67 (  0.63)
Epoch: [0][ 301/4271]   Time  0.949 ( 1.459)    Data  0.000 ( 0.020)    Loss 6.8559e+00 (7.0014e+00)    Acc@1   0.00 (  0.15)   Acc@5   1.33 (  0.71)
Epoch: [0][ 401/4271]   Time  0.942 ( 1.331)    Data  0.000 ( 0.016)    Loss 6.8265e+00 (6.9623e+00)    Acc@1   0.00 (  0.17)   Acc@5   2.00 (  0.81)
Epoch: [0][ 501/4271]   Time  0.939 ( 1.254)    Data  0.000 ( 0.014)    Loss 6.7476e+00 (6.9258e+00)    Acc@1   0.33 (  0.19)   Acc@5   0.33 (  0.90)
Epoch: [0][ 601/4271]   Time  0.941 ( 1.203)    Data  0.000 ( 0.012)    Loss 6.6629e+00 (6.8915e+00)    Acc@1   0.33 (  0.22)   Acc@5   2.33 (  1.02)
Epoch: [0][ 701/4271]   Time  0.945 ( 1.166)    Data  0.000 ( 0.011)    Loss 6.6552e+00 (6.8589e+00)    Acc@1   0.00 (  0.26)   Acc@5   1.67 (  1.18)
Epoch: [0][ 801/4271]   Time  0.953 ( 1.139)    Data  0.000 ( 0.011)    Loss 6.6480e+00 (6.8267e+00)    Acc@1   1.00 (  0.31)   Acc@5   1.67 (  1.34)
Epoch: [0][ 901/4271]   Time  0.947 ( 1.117)    Data  0.000 ( 0.010)    Loss 6.4222e+00 (6.7927e+00)    Acc@1   1.33 (  0.36)   Acc@5   3.00 (  1.55)
Epoch: [0][1001/4271]   Time  0.941 ( 1.100)    Data  0.000 ( 0.009)    Loss 6.3638e+00 (6.7553e+00)    Acc@1   1.00 (  0.43)   Acc@5   4.00 (  1.78)
Epoch: [0][1101/4271]   Time  0.947 ( 1.086)    Data  0.000 ( 0.009)    Loss 6.2487e+00 (6.7144e+00)    Acc@1   1.33 (  0.50)   Acc@5   4.00 (  2.05)
Epoch: [0][1201/4271]   Time  0.940 ( 1.075)    Data  0.000 ( 0.009)    Loss 6.1317e+00 (6.6698e+00)    Acc@1   1.67 (  0.59)   Acc@5   7.67 (  2.37)
```

---

### 评论 #12 — emerth (2022-12-20T17:11:17Z)

Thanks Yuming, much appreciated. Good to know there is an alternative to the CUDA Mafia ;-)

---

### 评论 #13 — tasso (2023-12-12T20:07:12Z)

Is this still an issue? If not, can we please close it? Thanks!

---

### 评论 #14 — tasso (2023-12-18T18:56:03Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request. If this is still an issue, please file a new ticket and we will be more than happy to investigate it. Thanks!

---
