# Fixed in ROCm 1.8 - ASROCK Motherboad H270 Second RX570 card fails to run on x4 PCIe Gen3 lane  ...

> **Issue #364**
> **状态**: closed
> **创建时间**: 2018-03-16T23:52:48Z
> **更新时间**: 2018-06-05T20:49:09Z
> **关闭时间**: 2018-06-03T13:17:31Z
> **作者**: chromakey-io
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/364

## 描述

I'm running two cards on a H270 motherboard.  The second card is in a 4x slot.  

I've verified both cards work by switching them into the 16x slot ... and they work fine with other drivers, like the mesa or pro-legacy, simultaneously with this setup.

Any ideas?  I assumed that maybe it would work with degraded features in the 4x slot?  ... but as it is now it doesn't work at all.

---

## 评论 (8 条)

### 评论 #1 — gstoner (2018-03-17T00:00:33Z)

Run sudo lspci -vvvs and sudo lspci -tv


http://rocm-documentation.readthedocs.io/en/latest/Other_Solutions/PCIe-Debug.html#pcie-debug
ROCm Use of Advanced PCIe Features and Overview of How BAR Memory is Used In ROCm Enabled System.

ROCm is an extension of HSA platform architecture, so it shares the queueing model, memory model, signaling and synchronization protocols. Platform atomics are integral to perform queuing and signaling memory operations where there may be multiple-writers across CPU and GPU agents.

The full list of HSA system architecture platform requirements is here: HSA Sys Arch Features<http://www.hsafoundation.com/html/HSA_Library.htm#SysArch/Topics/01_Overview/list_of_requirements.htm>

The ROCm Platform uses the new PCI Express 3.0 (PCIe 3.0) features for Atomic Read-Modify-Write Transactions which extends inter-processor synchronization mechanisms to IO to support the defined set of HSA capbilities needed for queuing and signaling memory operations.

The new PCIe AtomicOps operate as completers for CAS(Compare and Swap), FetchADD, SWAP atomics. The AtomicsOps are initiated by the I/O device which support 32-, 64- and 128-bit operand which target address have to be naturally aligned to operation sizes.

Currently ROCm use this capability as following:

  *   Update HSA queue’s read_dispatch_id: 64bit atomic add used by the command processor on the GPU agent to update the packet ID it processed.
  *   Update HSA queue’s write_dispatch_id: 64bit atomic add used by the CPU and GPU agent to support multi-writer queue insertions.
  *   Update HSA Signals – 64bit atomic ops are used for CPU & GPU synchronization.

The PCIe 3.0 AtomicOp feature allows atomic transactions to be requested by, routed through and completed by PCIe components. Routing and completion does not require software support. Component support for each is detectable via the DEVCAP2 register. Upstream bridges need to have AtomicOp routing enabled or the Atomic Operations will fall even though PCIe endpoint and PCIe I/O Devices has the capability to Atomics Operations.

To do AtomicOp routing capability between two or more Root Ports, each associated Root Port must indicate that capability via the AtomicOp Routing Supported bit in the Device Capabilities 2 register.

If your system has a PCIe Express Switch it needs to support AtomicsOp routing. Again AtomicOp requests are permitted only if a component’s DEVCTL2.ATOMICOP_REQUESTER_ENABLE field is set. These requests can only be serviced if the upstream components support AtomicOp completion and/or routing to a component which does. AtomicOp Routing Support=1 Routing is supported, AtomicOp Routing Support=0 routing is not supported.

Atomic Operation is a Non-Posted transaction supporting 32- and 64-bit address formats, there must be a response for Completion containing the result of the operation. Errors associated with the operation (uncorrectable error accessing the target location or carrying out the Atomic operation) are signaled to the requester by setting the Completion Status field in the completion descriptor, they are set to to Completer Abort (CA) or Unsupported Request (UR).

To understand more about how PCIe Atomic operations work  PCIe Atomics<https://pcisig.com/sites/default/files/specification_documents/ECN_Atomic_Ops_080417.pdf>

Linux Kernel Patch to pci_enable_atomic_request<https://patchwork.kernel.org/patch/7261731/>

There are also a number of papers which talk about these new capabilities:

  *   Atomic Read Modify Write Primitives by Intel<https://www.intel.es/content/dam/doc/white-paper/atomic-read-modify-write-primitives-i-o-devices-paper.pdf>
  *   PCI express 3 Accelerator Whitepaper by Intel<https://www.intel.sg/content/dam/doc/white-paper/pci-express3-accelerator-white-paper.pdf>
  *   Intel PCIe Generation 3 Hotchips Paper<https://www.hotchips.org/wp-content/uploads/hc_archives/hc21/1_sun/HC21.23.1.SystemInterconnectTutorial-Epub/HC21.23.131.Ajanovic-Intel-PCIeGen3.pdf>
  *   PCIe Generation 4 Base Specification includes Atomics Operation<http://composter.com.ua/documents/PCI_Express_Base_Specification_Revision_4.0.Ver.0.3.pdf>

Other I/O devices with PCIe Atomics support

  *   Mellanox ConnectX-5 InfiniBand Card<http://www.mellanox.com/related-docs/prod_adapter_cards/PB_ConnectX-5_VPI_Card.pdf>
  *   Cray Aries Interconnect<http://www.hoti.org/hoti20/slides/Bob_Alverson.pdf>
  *   Xilinx PCIe Ultrascale Whitepaper<https://www.xilinx.com/support/documentation/white_papers/wp464-PCIe-ultrascale.pdf>
  *   Xilinx 7 Series Devices<https://www.xilinx.com/support/documentation/ip_documentation/pcie_7x/v3_1/pg054-7series-pcie.pdf>

Future bus technology with richer I/O Atomics Operation Support

  *   GenZ<http://genzconsortium.org/faq/gen-z-technology/#33>

New PCIe Endpoints with support beyond AMD Ryzen and EPIC CPU; Intel Haswell or newer CPU’s with PCIe Generation 3.0 support.

  *   Mellanox Bluefield SOC<http://www.mellanox.com/related-docs/npu-multicore-processors/PB_Bluefield_SoC.pdf>
  *   Cavium Thunder X2<http://www.cavium.com/ThunderX2_ARM_Processors.html>

In ROCm, we also take advantage of PCIe ID based ordering technology for P2P when the GPU originates two writes to two different targets:

  1.  write to another GPU memory,
  2.  then write to system memory to indicate transfer complete.

They are routed off to different ends of the computer but we want to make sure the write to system memory to indicate transfer complete occurs AFTER P2P write to GPU has complete.

Good Paper on Understanding PCIe Generation 3 Throughput<https://www.altera.com/en_US/pdfs/literature/an/an690.pdf>



---

### 评论 #2 — chromakey-io (2018-03-17T00:11:45Z)

root@miner-desktop:/home/miner# dmesg | grep kfd
[    0.783518] kfd kfd: Initialized module
[    1.576913] kfd kfd: Allocated 3969056 bytes on gart
[    1.576986] kfd kfd: Reserved 2 pages for cwsr.
[    1.577002] kfd kfd: added device 1002:67df
[    3.394728] kfd kfd: skipped device 1002:67df, PCI rejects atomics

PCIe Atomics failed to load, which I'm going to guess is due to the cheap asrock h270 motherboard I have ... so I'll assume that's the issue.  Going to grab a proper workstation motherboard next week ...

Thanks again!!

Here's the lspci output though:

root@miner-desktop:/home/miner# lspci -tv
-[0000:00]-+-00.0  Intel Corporation Device 590f
           +-01.0-[01]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-02.0  Intel Corporation Device 5912
           +-14.0  Intel Corporation Device a2af
           +-14.2  Intel Corporation Device a2b1
           +-16.0  Intel Corporation Device a2ba
           +-17.0  Intel Corporation Device a282
           +-1c.0-[02]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-1f.0  Intel Corporation Device a2c4
           +-1f.2  Intel Corporation Device a2a1
           +-1f.3  Intel Corporation Device a2f0
           +-1f.4  Intel Corporation Device a2a3
           \-1f.6  Intel Corporation Ethernet Connection (2) I219-V

lspci -vv -s 02:00.0
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef) (prog-if 00 [VGA controller])
        Subsystem: Tul Corporation / PowerColor Device 2379
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 129
        Region 0: Memory at 2fe0000000 (64-bit, prefetchable) [size=256M]
        Region 2: Memory at 2ff0000000 (64-bit, prefetchable) [size=2M]
        Region 4: I/O ports at d000 [size=256]
        Region 5: Memory at df000000 (32-bit, non-prefetchable) [size=256K]
        Expansion ROM at df040000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
                DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 512 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM+ Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM L1 Enabled; RCB 64 bytes Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 2.5GT/s, Width x4, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR+, OBFF Disabled
                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance De-emphasis: -6dB
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                         EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                Address: 00000000fee002d8  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                AERCap: First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
        Capabilities: [200 v1] #15
        Capabilities: [270 v1] #19
        Capabilities: [2b0 v1] Address Translation Service (ATS)
                ATSCap: Invalidate Queue Depth: 00
                ATSCtl: Enable-, Smallest Translation Unit: 00
        Capabilities: [2c0 v1] #13
        Capabilities: [2d0 v1] #1b
        Capabilities: [320 v1] Latency Tolerance Reporting
                Max snoop latency: 3145728ns
                Max no snoop latency: 3145728ns
        Capabilities: [328 v1] Alternative Routing-ID Interpretation (ARI)
                ARICap: MFVC- ACS-, Next Function: 1
                ARICtl: MFVC- ACS-, Function Group: 0
        Capabilities: [370 v1] L1 PM Substates
                L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                          PortCommonModeRestoreTime=0us PortTPowerOnTime=170us
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu

root@miner-desktop:/home/miner# lspci -vv -s 01:00.0
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev ef) (prog-if 00 [VGA controller])
        Subsystem: Tul Corporation / PowerColor Device 2379
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 126
        Region 0: Memory at c0000000 (64-bit, prefetchable) [size=256M]
        Region 2: Memory at d0000000 (64-bit, prefetchable) [size=2M]
        Region 4: I/O ports at e000 [size=256]
        Region 5: Memory at df100000 (32-bit, non-prefetchable) [size=256K]
        Expansion ROM at 000c0000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
                DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 512 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM+ Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM L1 Enabled; RCB 64 bytes Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 2.5GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR+, OBFF Disabled
                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance De-emphasis: -6dB
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                         EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                Address: 00000000fee00298  Data: 0000
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
        Capabilities: [2b0 v1] Address Translation Service (ATS)
                ATSCap: Invalidate Queue Depth: 00
                ATSCtl: Enable-, Smallest Translation Unit: 00
        Capabilities: [2c0 v1] #13
        Capabilities: [2d0 v1] #1b
        Capabilities: [320 v1] Latency Tolerance Reporting
                Max snoop latency: 71680ns
                Max no snoop latency: 71680ns
        Capabilities: [328 v1] Alternative Routing-ID Interpretation (ARI)
                ARICap: MFVC- ACS-, Next Function: 1
                ARICtl: MFVC- ACS-, Function Group: 0
        Capabilities: [370 v1] L1 PM Substates
                L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                          PortCommonModeRestoreTime=0us PortTPowerOnTime=170us
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu

---

### 评论 #3 — Mandrewoid (2018-03-17T04:14:19Z)

hey @kevin You're probably going to want to find a motherboard that will run the GPU's in x8 x8 mode. It should say either in the manual or even on the box. Any SLI-capable motherboard would be able to do this, for example.

---

### 评论 #4 — gstoner (2018-03-17T13:13:10Z)

I saw what they are doing  2 x PCI Express 3.0 x16 Slots (PCIE2: x16 mode; PCIE4: x4 mode) 
i need to get one of these board is and see how they messing up x4 PCIe Gen3 lane 

---

### 评论 #5 — chromakey-io (2018-03-17T22:56:43Z)

It's an ASRock H270m Pro4 .... bought it cause it had the slots positioned to allow 2 16x cards + a 1x ... and it has dual m.2 slots ... and it was cheap :)

---

### 评论 #6 — gstoner (2018-05-05T14:29:47Z)

We released ROCM 1.8 Beta http://repo.radeon.com/rocm/misc/beta_1.8.0/  which Linux driver team put in the restriction on the number lanes of PCIe needed to be supported. It was x8, this restriction has been removed.  This was not PCIe Atomics issue.   But for Vega10 only we removed this restriction as well for now.   We are looking at addressing this in the future release for FIJI and Polaris since it involves microcode changes.      You also pick up REHL/Centos 7.4 support in this beta. 

---

### 评论 #7 — akostadinov (2018-06-05T20:43:34Z)

@gstoner , in 1.8 you removed both - the atomics restriction as well the number of lanes restriction for Vega? So now Vega can run on any motherboard, correct?

Asking so when I try to install at least I know there is a chance for it to work.

---

### 评论 #8 — gstoner (2018-06-05T20:48:41Z)

@akostadinov In 1.8 it was removed for only Vega10, but in 1.8.1 we found an issue in SDMA without PCI Atomics, but we give you the option to turn off SDMA support and not have PCIe atomics.   The team is working with SDMA firmware for a fix for this. 

---
