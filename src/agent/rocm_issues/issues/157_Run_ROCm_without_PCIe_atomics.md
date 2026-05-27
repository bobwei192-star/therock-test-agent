# Run ROCm without PCIe atomics?

> **Issue #157**
> **状态**: closed
> **创建时间**: 2017-07-08T12:03:20Z
> **更新时间**: 2023-06-25T00:10:29Z
> **关闭时间**: 2017-07-08T12:44:47Z
> **作者**: Gezine
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/157

## 描述

Hi I am having trouble using ROCm 1.6
My system is
E5-2670v1 + two RX480
CPU itself is using PCIe 3.0, but no PCIe atomics support

I can see two RX480, If I use "rocm-smi -a"
But If I run vector_copy I got "Getting a gpu agent failed."
This is output of "dmesg | grep kfd"
kfd kfd: skipped device 1002:67df, PCI rejects atomics

Is there any solution to run ROCm without PCIe atomics?

Thank you

---

## 评论 (48 条)

### 评论 #1 — gstoner (2017-07-08T12:42:05Z)

This CPU is not supported by ROCm. I added some more info on why we us PCIe Atomics

System Requirements

To use ROCm on your system you need the following:

  *   ROCm Capable CPU and GPU
     *   PCIe Gen 3 Enabled CPU with PCIe Platform Atomics
     *   ROCm enabled GPU’s
        *   Radeon Instinct Family MI25, MI8, MI6
        *   Radeon Vega Frontier Edition
        *   Broader Set of Tested Hardware<https://rocm.github.io/hardware.html>


ROCm is an extension of HSA platform architecture, so it shares the queueing model, memory model, signaling and synchronization protocols. Platform atomics are integral to perform queuing and signaling memory operations where there may be multiple-writers across CPU and GPU agents.

The full list of HSA system architecture platform requirements are here: http://www.hsafoundation.com/html/HSA_Library.htm#SysArch/Topics/01_Overview/list_of_requirements.htm

For ROCm the Platform atomics are used in ROCm in the following ways:

  *   Update HSA queue’s read_dispatch_id: 64bit atomic add used by the command processor on the GPU agent to update the packet ID it processed.
  *   Update HSA queue’s write_dispatch_id: 64bit atomic add used by the CPU and GPU agent to support multi-writer queue insertions.
  *   Update HSA Signals – 64bit atomic ops are used for CPU & GPU synchronization.

The PCIe Platform Atomics are CAS, FetchADD, SWAP

Here is document on PCIe Atomics https://pcisig.com/sites/default/files/specification_documents/ECN_Atomic_Ops_080417.pdf

In ROCm, we also take advantage of PCIe ID based ordering technology for P2P when the GPU originates two writes to two different targets:

  1.  write to another GPU memory,
  2.  then write to system memory to indicate transfer complete.

They are routed off to different ends of the computer but we want to make sure the write to system memory to indicate transfer complete occurs AFTER P2P write to GPU has complete.









---

### 评论 #2 — Gezine (2017-07-08T12:49:18Z)

Oh. Thank you
Seems like I need to change cpu.

Is Xeon E5 v2 supported?
https://software.intel.com/en-us/articles/intel-xeon-processor-e5-2600-v2-product-family-technical-overview#pcie

document says it supports PCIe atomic. But Is ROCm support it?

---

### 评论 #3 — gstoner (2017-07-08T13:18:43Z)

Ivybridge is the first Intel Processor to support PCIe atomics with PCIe Gen3.  We never acquired an Ivybridge system.  Since Haswell already out and OEM vendors we working stopped selling Ivybridge system.   It should work since it meets the requirement, but you need to make sure you're on the PCIe Gen3 slots attached to CPU complex, not off the southbridge.  But you have to be careful you also need motherboard compliant with PCIe Gen3.    

When we started our project Haswell processor was what we have been doing development for ROCm, the primary versions are Xeon E5 v3 -2640, 2660 and 2690.   Now EPYC is out they work great

---

### 评论 #4 — Gezine (2017-07-08T15:55:42Z)

Just tested ROCm with ivybridge intel core i7 3770

Doesn't work.
Having same errors

Is this software limitation?

---

### 评论 #5 — gstoner (2017-07-08T23:30:56Z)

It a hardware limitation of CPU that do not properly support PCIe atomics.,  if you put it into motherboard for Sandybridge you would only get PCIe 2.   Honeslty in need to find Xeon Ivybridge with

We test the stack with the follow CPU as we said in the instructions
When you use the PCIe Gen 3 slot that use the PCIe Root I/O complex that is in Main CPU we support

  *   Xeon E5 v3 ( Haswell) Xeon E5 v4 ( Broadwell),  EPYC processor all support
  *   Core I3, I4, I5 i7,  Xeon E3, in the variants of  Haswell, Broadwell, Skylake, and  Kaby Lake
  *   Ryzen 3,5,7
  *   EPYC
  *   Cavium Thunder X, X2
  *   IBM Power8

One thing you ned

Process that will not work are


  *   Intel Xeon 3000 & 5000
     *   Nehalem  PCIe Gen 2
     *   Intel Westmere  PCIe Gen 2
  *   Intel Xeon V1 SandyBridge PCIe Gen 2
  *   AMD Opeteron  PCIe Gen 2

When I get back from vacation I will see if we can chase down Ivybridge system.

We use Supermicro 1028 GQ -THRT as our main testing server with haswell and broad well Xeons

Greg


On Jul 8, 2017, at 10:55 AM, gezine <notifications@github.com<mailto:notifications@github.com>> wrote:


Just tested ROCm with ivybridge intel core i7 3770

Doesn't work.
Having same errors

Is this software limitation?

—
You are receiving this because you modified the open/close state.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/157#issuecomment-313864407>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duelr6yLoFcg1nAt41R4eGD3PmNPrks5sL6Z_gaJpZM4ORuEv>.



---

### 评论 #6 — P-Tillmann (2017-07-23T16:00:02Z)

I've also tried to get rocm running on an ivy-bridge system (Xeon 1230 v2).
Unfortunatly the vector_copy sample fails with  
"Getting a gpu agent failed."
And "dmesg | grep kfd" outputs
kfd kfd: skipped device 1002:67df, PCI rejects atomics

Under Windows GPU-Z claims i have a pcie-v3 connection.

Is there hope that rocm support will be provided for ivy bridge generation cpus?

---

### 评论 #7 — gstoner (2017-07-23T16:04:23Z)

If that is Xeon E3 Ivybridge it will be missing PCIe Atomics.  

The full list of HSA system architecture platform requirements are here: http://www.hsafoundation.com/html/HSA_Library.htm#SysArch/Topics/01_Overview/list_of_requirements.htm

For ROCm the Platform atomics are used in ROCm in the following ways:

- Update HSA queue’s read_dispatch_id: 64bit atomic add used by the command processor on the GPU agent to update the packet ID it processed.
- Update HSA queue’s write_dispatch_id: 64bit atomic add used by the CPU and GPU agent to support multi-writer queue insertions.
- Update HSA Signals – 64bit atomic ops are used for CPU & GPU synchronization.
- The PCIe Platform Atomics are CAS, FetchADD, SWAP

Here is document on PCIe Atomics https://pcisig.com/sites/default/files/specification_documents/ECN_Atomic_Ops_080417.pdf

In ROCm, we also take advantage of PCIe ID based ordering technology for P2P when the GPU originates two writes to two different targets:  

- write to another GPU memory,
- then write to system memory to indicate transfer complete.


---

### 评论 #8 — P-Tillmann (2017-07-26T15:45:12Z)

Ah a pity,

i didn't knew that Ivybridge doesn't support full PCIe v3 features.

Thanks for sharing this information.

---

### 评论 #9 — iavael (2017-08-25T05:56:39Z)

Well, according to my lspci output Xeon v2 supports some pcie atomics (AtomicOpsCap: 32bit+ 64bit+), but maybe it's not sufficient to HSA needs.

Full lspci output
```
# lspci -s 01:00.0 -vv
01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/580] [1002:67df] (rev e7) (prog-if 00 [VGA controller])
        Subsystem: Micro-Star International Co., Ltd. [MSI] Device 3418
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 38
        Region 0: Memory at e0000000 (64-bit, prefetchable) [size=256M]
        Region 2: Memory at f0000000 (64-bit, prefetchable) [size=2M]
        Region 4: I/O ports at e000 [size=256]
        Region 5: Memory at f7b00000 (32-bit, non-prefetchable) [size=256K]
        Expansion ROM at f7b40000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
                DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 512 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM L1 Enabled; RCB 64 bytes Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 2.5GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
                AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                AtomicOpsCtl: ReqEn-
                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance De-emphasis: -6dB
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                         EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                Address: 00000000fee00418  Data: 0000
        Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150 v2] Advanced Error Reporting
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP+ BadDLLP+ Rollover- Timeout+ NonFatalErr+
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                AERCap: First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
        Capabilities: [200 v1] #15
        Capabilities: [270 v1] #19
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
        Capabilities: [328 v1] Alternative Routing-ID Interpretation (ARI)
                ARICap: MFVC- ACS-, Next Function: 1
                ARICtl: MFVC- ACS-, Function Group: 0
        Capabilities: [370 v1] L1 PM Substates
                L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                          PortCommonModeRestoreTime=0us PortTPowerOnTime=170us
                L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                           T_CommonMode=0us LTR1.2_Threshold=0ns
                L1SubCtl2: T_PwrOn=10us
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
```

CPU: Xeon E3-1275 V2
MoBo: ASUS P8C WS
GPU: Radeon RX 580 (in PCIe 3.0 slot)

---

### 评论 #10 — andreychernyshev (2018-02-09T20:54:00Z)

hi 
i have working one with : 
DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
			 AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR+, OBFF Disabled
			 AtomicOpsCtl: ReqEn+



---

### 评论 #11 — luncht1me (2018-02-24T20:08:22Z)

I'd love a way to have OpenCL detect my VEGA56s that are plugged into pcie 2.0 slots...
Althought ROCM-SMI detects them, OpenCL won't register them as devices on Ubuntu 16.04.

ie: rocm-smi and lspci | grep 'VGA' show 3 devices, but clinfo only shows the one connected via pcie 3.0 slot. The other two are on pci-e risers connected to pcie 2.0.

---

### 评论 #12 — Spudz76 (2018-03-11T17:02:37Z)

I find it interesting most of these stacks are all assumptive of moving lots of data to and from the card.

Mining moves a couple bytes literally, mostly chews the GPU, definitely doesn't NEED atomics nor even DMA really and definitely works fine on single lane (when the driver doesn't try to enforce "OMG GAMING BRO" performance).  Similar to how the driver assumes you'll be using a GPU for display and not just brainwork, and it's nearly impossible to ignore the display ports and audio junk (don't init what you aren't going to use - best practice?)

---

### 评论 #13 — rhlug (2018-03-11T19:10:33Z)

One of several reasons why mining w/ Vega on linux is still not worth the hassle

1) PCI atomics required for opencl, restricting usable slots on legacy hardware.
2) Modifying clocks and/or voltages is difficult at best.
3) Cryptonight performance not on par with windows.

If you are mining ethash, and only have 2 or 3 vegas, you might be able to get away with it on basic hardware that we've all used in the past.   If you want to splurge on x399 board, then 4 Vegas is doable.

I set up one vega rig (and its currently running win10) because of the issues mentioned above, and it will be the only one unless something changes in usability.   Its too bad they lock out the bios, and provide no software on linux to make it usable for mining.   May be moving onto Volta if it ever gets released.



---

### 评论 #14 — gstoner (2018-03-11T19:43:01Z)

When we started develop on ROCm the use case was HPC applications and Deep Learning. Both ran on servers which Xeon v3 or newer we had to compliant.   Both need bandwidth. Hence x16 optimization   What hear issue are is we want to use cheapest oldest posibile hardware. Volta will not be that.  

We are looking into the Cryptonight issue.  It firmware issue internal firmware team needs to solve

Soon you do not need atomic on Vega and ROCm.   This removes pcie gen 3 restriction.   

Minning is new use case they looking at.  Amdgpupro is going to use opencl on pal which will give you what your asking for. Version 18.10. It goes back to older compiler used under windows as well 



---

### 评论 #15 — dfad44 (2018-03-11T20:55:34Z)

@rhlug I run quad vega-fes on x399. I mine cryptonight and my issue is the inconsistent performance. The hashrates declared on xmr-stak is inaccurate. Typically, the miner declares between, 6500 - 7000 h/s and on poolside will report between 5000 - 14,000 h/s. I have to confess i got the best performance using rocm kfd kernel (somewhat stable hashrates). There has been some type of regression since it was moved to dkms or maybe the 4.13 kernel. I sincerely hope it can be rectified. I've decided to wait till kernel 4.17 to know if i made the right choice going with rocm.

---

### 评论 #16 — luncht1me (2018-03-11T21:17:46Z)

Thats exciting about the change in atomics for linux :) Ive found linux is
easier to manage larger mining servers with.

On Sun, Mar 11, 2018, 1:55 PM dfad44, <notifications@github.com> wrote:

> @rhlug <https://github.com/rhlug> I run quad vega-fes on x399. I mine
> cryptonight and my issue is the inconsistent performance. The hashrates
> declared on xmr-stak is inaccurate. Typically, the miner declares between,
> 6500 - 7000 h/s and on poolside will report between 5000 - 14,000 h/s. I
> have to confess i got the best performance using rocm kfd kernel (somewhat
> stable hashrates). There has been some type of regression since it was
> moved to dkms or maybe the 4.13 kernel. I sincerely hope it can be
> rectified. I've decided to wait till kernel 4.17 to know if i made the
> right choice going with rocm.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/157#issuecomment-372148327>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ADQw9KmUiIbqDUN0SfZzuF1u2pehpvKNks5tdY9JgaJpZM4ORuEv>
> .
>


---

### 评论 #17 — gstoner (2018-03-11T21:59:07Z)

@luncht1me It really is not exciting about losing PCIe Atomic/Atomic Completor support,  we lose a lot of performance optimization for GPU Computing.   But I understand the Miners who just care about their use case this is exciting. 

---

### 评论 #18 — luncht1me (2018-03-11T22:07:33Z)

Im sure theres a way to have it work both ways. Pci slot is 3.0+? Enable
atomics for that gpu. It isnt? Dont enable it, but still allow it to be an
openCL device available for use. Atomics doesnt have to be axed at all.

On Sun, Mar 11, 2018, 2:59 PM Gregory Stoner, <notifications@github.com>
wrote:

> @luncht1me <https://github.com/luncht1me> It really is not exciting about
> losing PCIe Atomic/Atomic Completor support, we lose a lot of performance
> optimization for GPU Computing. But I understand the Miners who just care
> about their use case this is exciting.
>
> —
> You are receiving this because you were mentioned.
>
>
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/157#issuecomment-372153308>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ADQw9C8-cTy51om5qcuF14S2Uyf28MfMks5tdZ4ugaJpZM4ORuEv>
> .
>


---

### 评论 #19 — gstoner (2018-03-11T22:24:11Z)

@luncht1me With AMDGPUpro stack you will not have to use the ROCm foundation at All,  You will get OpenCL with out PCIe Atomics support in 18.10, it does not leverage ROCm driver foundation.  You get every you want, but it is not open source.   Note the issue  rhlug is seeing could also be still there since Window Driver uses different kernel driver foundation that AMDGPU uses.  

---

### 评论 #20 — briansp2020 (2018-03-11T23:55:46Z)

@gstoner 
Will ROCm stop using atomic for all configuration? It seems counter productive if that will result in performance hit for those that do have the supported hardware.

---

### 评论 #21 — luncht1me (2018-03-12T00:04:48Z)

Thanks for the info, that's what's exciting!
I arrived here because of amdgpupro and my own digging into why things
weren't working. I think they were using rocm in their driver package or
something. Keep up the good work <3

On Mar 11, 2018 3:24 PM, "Gregory Stoner" <notifications@github.com> wrote:

> @luncht1me <https://github.com/luncht1me> With AMDGPUpro stack you will
> not have to use the ROCm foundation at All, You will get OpenCL with out
> PCIe Atomics support in 18.10, it does not leverage ROCm driver foundation.
> You get every you want, but it is not open source. Note the issue rhlug is
> seeing could also be still there since Window Driver uses different kernel
> driver foundation that AMDGPU uses.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/157#issuecomment-372155067>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ADQw9Be__4IM4nBLt-6Ac6DPwU21ibevks5tdaQOgaJpZM4ORuEv>
> .
>


---

### 评论 #22 — gstoner (2018-03-12T00:45:03Z)

No.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Brian <notifications@github.com>
Sent: Sunday, March 11, 2018 5:55:47 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Run ROCm without PCIe atomics? (#157)


@gstoner<https://github.com/gstoner>
Will ROCm stop using atomic for all configuration? It seems counter productive if that will result in performance hit for those that do have the supported hardware.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/157#issuecomment-372161243>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYWbNswa-nrMg5MHCLeHNf4pNahTks5tdbmDgaJpZM4ORuEv>.


---

### 评论 #23 — rhlug (2018-03-12T01:27:18Z)

@gstoner Thanks for the update.  Thats great news.  Glad to hear there is some eyes on cryptonight optimization.   Its not about being cheap per say, but more-so about being able to ROI the gear before they EOL or the rise in hashing difficulty obsoletes them.

If I could buy server-class gear with xeons and pci atomics support across 12 GPUs for same as 2x 6GPU desktop-class rigs, I would definitely do that.  But there is about a $6k gap, and that makes ROI alot harder.



---

### 评论 #24 — dfad44 (2018-03-12T15:40:05Z)

@rhlug I understand how you feel. However if you believe that this endeavor is worth it and this market is here to stay, it would be worthwhile in the end. After watching https://www.youtube.com/watch?v=k3aGaxcYCxw I was completely sold on Mr. Stoners passion for the prospects of hpc and believe me when I say I know nothing of it. I've spent my savings and I don't regret it. If anything, I gained knowledge learning this stuff.

---

### 评论 #25 — gstoner (2018-03-12T23:45:59Z)

@rhlug  I get the ROI part of it on mining. I used to run Major VFX houses Rendering farm, you have CapEx and OpeEx you have to watch.  In the long run, OpEX dominates your costs.   We are finally getting more resource on the team.   One thing on CapEx you will start seeing more Cloud service with ROCm. 

---

### 评论 #26 — dfad44 (2018-03-13T00:21:19Z)

@gstoner with some algorithm optimization, prosumer can be alive and well. There should be enough room to exist side by side with enterprise. Collectively, we are also enterprise. I hope your team can give us something before summer.

---

### 评论 #27 — Spudz76 (2018-03-13T15:23:47Z)

You see though, "cheapest oldest posibile hardware" is generally what works best on Linux since developers pretty much get the software working right just about at the EOL... latest hardware on Linux is shooting yourself in the foot.

Hawaii core cards still ripping 30MH here, can't get a Fiji or Ellesmere to get anywhere close (because of the drivers, obviously).

---

### 评论 #28 — gstoner (2018-03-13T16:44:42Z)

There diminishing return on HPC and Deep Learning.   I get why everyone wants this. But even Haswell is now 5 years old when PCI atomics first showed.  It is about 1.5 billion CPU with PCI atomic support



---

### 评论 #29 — gstoner (2018-03-13T16:46:08Z)

Hawaii does not need pci atomics on ROCm.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Tony Butler <notifications@github.com>
Sent: Tuesday, March 13, 2018 10:23:54 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Run ROCm without PCIe atomics? (#157)


You see though, "cheapest oldest posibile hardware" is generally what works best on Linux since developers pretty much get the software working right just about at the EOL... latest hardware on Linux is shooting yourself in the foot.

Hawaii core cards still ripping 30MH here, can't get a Fiji or Ellesmere to get anywhere close (because of the drivers, obviously).

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/157#issuecomment-372704401>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuZbFY0mTQUz7KklwdwWkDxI3imewks5td-SFgaJpZM4ORuEv>.


---

### 评论 #30 — Spudz76 (2018-03-13T17:30:37Z)

Generally using H81 based boards which run very low TDP processors.  Many low TDP Intels do not have extended features (Atomics, AES-NI, etc) even if they are brand new, to save power and transistor count and complexity.

I don't recall anything refusing to boot without TCQ on SATA.  It's a extension and should be treated as such, don't panic just deal with it missing for whatever reason ("old" hardware or just turned off because I wanted to).

I turn off all KVM/VT-d/Virtualization as well since I'm not using it.  If you had used those just because it was easier it would also break 6+ GPU installs or PCIe bridges beyond bridges beyond bridges (PCIe expansion/mux boards).

I have never gotten ROCm to work on anything including Hawaii.  Segfaults at best, if it finds the platform at all.  Same software runs against Intel/nVidia OpenCL albeit slow as tortoises at least it works.

Also stuff you say about ROCm vs AMDGPU-PRO does not match what the AMDGPU-PRO people seem to claim (target is merging the two and going open source completely / AMDGPU-PRO will be retired).  This is the only reason I care about ROCm at all, if it will replace AMDGPU-PRO then we have to ensure it works with mining now.  Atomics will break current use cases.  We also use x1 and no more.  That is all.

---

### 评论 #31 — gstoner (2018-03-13T18:31:33Z)

@Spudz76

I am sorry you have hard time getting anything working for your use case.   ROCm started on very specific set of use cases when we started.   We always target Xeon based Processor first  including Pseudo Xeon I7 Extreme Edition + core i3, i5, and i7.  We also support LargeBar P2P and P2P via RDMA which is not your use case.   

Core linux driver is common between the AMDGPU, AMDGPUpro and ROCm enabeld AMDGPU driver.  Some of the issue are seeing are in the base driver.    AMDGPU adds KFD and Thunk to enable HSA based stack you can see the requirements  http://www.hsafoundation.com/html_spec111/HSA_Library.htm  So we can support more then OpenCL 

Our main testing is on   ( we test with Fiji Nano, S9150 Hawaii, MI25 ) 
Intel Xeon E5 v3 or newer CPU 

- SuperMicro SYS-1019 
- SuperMicro SYS-1029 
- SuperMicro SYS-1028GQ -TRT 
- SuperMicro SYS-4028GR-TRT 
- SuperMicro SYS-4028GR-TRT2 

EPYC 
Invetec P47  EPYC based 

Intel i7 extreme edition ASUS x99 based 
Core i5 &. i7 with Z-97 based Motherboard 

Threadripper 

Ryzen 
- Note MSI has SBIOS issue which is why you need newer version of Linux 

I get you care about Mining use case only PCIe x1 Lane on the H81 2013 era Chip set and using only PCIe gen 2 via PCIe x1,  also you want to source  lowest possible cost PCIe Switch.  

What your really asking for your use case is stripped down stack that just runs OpenCL, Windows driver OpenCL run on one of two foundation Pre GFX9 is Orca which been around since Catalyst drivers.  For GFX9 runs on PAL Platform Abstraction Layer.    

For AMDGPUpro 18.10 and newer OpenCL will be  running on PAL.  PAL is the same user driver foundation used by the Vulcan driver. It will also move back to using same compiler as the Windows Stack,    LLVM to HSAIL to SC compiler aka the shader compiler.  Note Linux and Windows driver will not have same base Kernel driver architecture. 














---

### 评论 #32 — gstoner (2018-03-13T18:36:46Z)

@Spudz76   We also see if we can source H81 motherboards.  Also if you give your exact linux kernel config we can added to our testing profile.  Also need to know the exact GPU's and AIB vendor your using to build the test case.   Please also include the exact application you are running a care about.  
 Also include instruction on how your run the application.   Also any special configs Like voltage, clocks changes since we need to understand if your under driving the GPU which can also drive instability 

---

### 评论 #33 — Spudz76 (2018-03-20T16:07:55Z)

I have reverted to Ubuntu 14 and kernel 3.x with fglrx 13, which ironically is mining on a HD5570 right now, a Redwood card that would not work with any other stack at all.   I tried Windows7 and six different driver revisions, which never showed OpenCL because apparently you have to have a display (or dummy plug) actually connected to any GPU you want to **calculate** upon (so dumb, as to be nearly infuriating).  I tried various other Linux 4.x kernel distros as basis and never got results either, similar failure points or unavailable old source files.

Basically it seems like the best practice for mining specifically is to obtain the oldest working version of the entire OS as if it were a time warp and it's 2005 (or whenever the hardware target was made) again, and then everything works perfectly other than being susceptible to thousands of exploits (hope the LAN is secure enough...)  And then shift that OS compiler stack up to GCC 5 as some mining software compilation requires it, side-install CMake manually since nothing works with v2 anymore and v3 is not available on antique OS releases, etc, etc, etc.

Also these OS components and driver revisions are getting VERY difficult to find it would be very cool if AMD/ATI could ensure all old versions are available.  For example you can't find the old Stream SDK 2.1/2.3 versions anywhere ever since the rename to APP-SDK, however you must have the old Stream SDK to be able to do things on old cores, and thanks to AMD stranglehold on IP / nobody mirrors their files only links back to the same old URL / whatever is on the main web site is what exists / APP-SDK 2,9 doesn't work for what I was trying...

---

### 评论 #34 — Spudz76 (2018-03-20T16:32:09Z)

Hawaii still works on Ubuntu 16 but now I'm wondering if it would be more optimal on this time-warp stack.  Unfortunately I think I have to roll back even more (Xorg is too new in the final Ubuntu 14) in order to make that work properly.  I do have one Hawaii that almost works but chokes on one ring/IB test and I sort of suspect the old driver / fglrx might work around that IMO minor error and use the card OK (via the other 9 lanes that DO still work).  Every other radeon/amdgpu/amdgpu-pro stack just finds the bad lane and quits.  I had hoped Windows might also work around bad single IB however I don't have any dummy plugs nor the gumption to tear down one of my working LCDs and drag it down into the basement/crypt just to find out it probably doesn't.  Or, some other bad coder decided feature Z shouldn't work unless you have headphones hooked up, for who knows why apparently just trolling.

This is like if an Intel CPU refused to boot unless you had the iGPU inside it hooked up to something.  Sorry but graphical output and even Xorg should not be necessary to compute on a GPU, much less to be able to control a GPU (clocks, fans, temps tend to be inaccessible without firing up Xorg... on both GPU vendors... which is insane).

---

### 评论 #35 — Spudz76 (2018-03-20T16:47:43Z)

The H81 stack is just Ubuntu 16 server from the latest install ISO.
Then manually install the older 4.10 kernel (linux-image-extra-4.10....) and headers.
Then install either 17.40 or 17.50 (either one basically works the same for Hawaiis).  If you use rocm option with 17.50 it won't work / hits the atomics error / needs 'legacy' OpenCL.  Also 'headless' doesn't actually work, you need most of the libraries it skips, even when "as headless as possible given bad assumptions that everyone has a head and runs Xorg and..."  or maybe that's just to obtain all the -dev packages so as to compile OpenCL stuff.

You can run the 17.50 on the stock kernel 4.13 whatever but 17.40 doesn't build on anything newer than 4.10 / thus I just run 4.10 for both.

The main client software is xmr-stak from the dev branch of fireice-uk github repo.  I have not developed a local proxy for the cryptonight coins yet so I prefer to have CPU + all various GPUs running in as few instances of xmr-stak as possible so it can divide up the nonce ranges appropriately for varied speed devices (better than having 100 things connected out to the Internet).  This is why I am trying to run say Redwood garbage along with GCN stuff along with old GTX 550Ti and such as well all in one box (regardless of CPU/atomics capabilities).  If the card eats 40w but gives me the output of a couple CPUs (58H/s) then I'm overall making progress.  No reason to toss the Redwood in the trash where it otherwise belongs.  Kind of 'green mining' instead of robbing the gamers of all the new GPUs.

---

### 评论 #36 — wrt54gl (2018-03-22T14:42:16Z)

@gstoner 
> Soon you do not need atomic on Vega and ROCm. This removes pcie gen 3 restriction.

That is good news for me. I have a rig with a prime Z370A and an I3-8100 cpu. Right now I can run 2 vega 56 on it with rocm amd very impressed with the performance. I would like to run 9. Let me know If I can help with testing.

---

### 评论 #37 — Sumenia (2018-03-22T14:58:30Z)

@wrt54gl I wonder how many Hashrate you get ? 🤔

---

### 评论 #38 — wrt54gl (2018-03-22T15:30:49Z)

@Sumenia 
39.76 mh/s per card. All I did was put a 19% overclock on the memory. Seems very stable. Using msi airboost which don't overclock as well as some.

---

### 评论 #39 — nguha (2018-04-19T23:19:02Z)

> Soon you do not need atomic on Vega and ROCm. This removes pcie gen 3 restriction.
> You will get OpenCL with out PCIe Atomics support in 18.10

Both great news. Specially the support on the open-source ROCm.

@gstoner Can you give us an ETA for any of these two?

---

### 评论 #40 — boberfly (2018-04-24T04:51:49Z)

Just to post on my E5-2680v2 using kernel 4.17 Ubuntu 18.04 I get this on a dmesg |grep kfd
[    2.789921] kfd kfd: Initialized module

Currently I can't get ROCm/OpenCL to work but I think it's something else, still investigating...

@gstoner you might be able to change the minimum spec for Xeon CPUs to E5-2600v2 on the main page, provided that kfd report is an accurate indicator.

---

### 评论 #41 — cmal (2020-09-13T16:51:25Z)

@gstoner I have an Intel Core i7 3770K CPU, which is ivy-bridge(Haswell is 4xxx). Clearly PCIe 3.0 is supported by this CPU and my motherboard. But it seems AtomicOps are not supported(which is a PCIe 3.0 spec).

```
$ dmesg|grep kfd
[    4.123886] kfd kfd: amdgpu: skipped device 1002:67df, PCI rejects atomics
```
Are there other methods to make tensorflow using my GPU(RX580) without PCIe AtomicOps?

---

### 评论 #42 — Mushoz (2021-05-26T07:51:02Z)

Would it be possible to get OpenCL support without AtomicOps on 6xxx hardware as well? Currently, only the GPU connected to the CPU is being used for mining, and the GPU connected via the chipset (b550) is completely ignored. I don't think see why this should be a hard requirement given with how little bandwidth mining actually uses.

---

### 评论 #43 — blackmennewstyle (2021-09-22T09:44:28Z)

> Would it be possible to get OpenCL support without AtomicOps on 6xxx hardware as well? Currently, only the GPU connected to the CPU is being used for mining, and the GPU connected via the chipset (b550) is completely ignored. I don't think see why this should be a hard requirement given with how little bandwidth mining actually uses.

Debian based distros like HiveOS manage to bypass the PCIE 3.0 atomics restrictions for new GPUs like the RX 6000 GPUs which all use the AMDGPU with OpenCL ROCR which is based on ROCM. It will be interesting to know how they manage to do it, looking at their GUI, it says AMDGPU version 20.40, which is a version which uses OpenCL PAL. They definitely did some drivers customization. 

---

### 评论 #44 — kaiwangyu (2022-01-25T08:38:52Z)

> @gstoner I have an Intel Core i7 3770K CPU, which is ivy-bridge(Haswell is 4xxx). Clearly PCIe 3.0 is supported by this CPU and my motherboard. But it seems AtomicOps are not supported(which is a PCIe 3.0 spec).
> 
> ```
> $ dmesg|grep kfd
> [    4.123886] kfd kfd: amdgpu: skipped device 1002:67df, PCI rejects atomics
> ```
> 
> Are there other methods to make tensorflow using my GPU(RX580) without PCIe AtomicOps?

Same issue's here with the same CPU,  did you fixed it?

---

### 评论 #45 — Spudz76 (2022-01-25T18:43:04Z)

AMDGPU-Pro drivers at least up to 20.40 didn't need atomics anywhere on anything.

---

### 评论 #46 — Espionage724 (2022-07-17T13:01:14Z)

I have a RX 6600 XT in a computer with a Phenom II X4 CPU and PCI-E 2.0. It's running Fedora 36 with ROCm OpenCL from default repos (it was added relatively recently).

OpenCL through ROCm seems to work fine even though `amdgpu` reports no `PCIE atomic ops` support.

I get these in `dmesg`:

```
[espionage724@Oak ~]$ dmesg | grep atomic
[    0.286970] DMA: preallocated 1024 KiB GFP_KERNEL pool for atomic allocations
[    0.286977] DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.286984] DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.850468] atomic64_test: passed for x86-64 platform with CX8 and with SSE
[    2.759942] amdgpu 0000:05:00.0: amdgpu: PCIE atomic ops is not supported
```
```
[espionage724@Oak ~]$ dmesg | grep kfd
[   16.743909] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[   16.818223] kfd kfd: amdgpu: added device 1002:73ff
```

`rocminfo`:

```
[espionage724@Oak ~]$ sudo rocminfo
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Phenom(tm) II X4 965 Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Phenom(tm) II X4 965 Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      65536(0x10000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3400
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            4
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    8131580(0x7c13fc) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    8131580(0x7c13fc) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8131580(0x7c13fc) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1032
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon RX 6600 XT
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      2048(0x800) KB
    L3:                      32768(0x8000) KB
  Chip ID:                 29695(0x73ff)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2900
  BDFID:                   1280
  Internal Node ID:        1
  Compute Unit:            32
  SIMDs per CU:            2
  Shader Engines:          4
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8372224(0x7fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1032
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```

`rocm-clinfo`:

```
[espionage724@Oak ~]$ rocm-clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3452.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    AMD Radeon RX 6600 XT
  Device Topology:                               PCI[ B#5, D#0, F#0 ]
  Max compute units:                             16
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           2900Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183768
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            16384
  Max image 3D height:                           16384
  Max image 3D depth:                            8192
  Max samplers within kernel:                    29695
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            8573157376
  Constant buffer size:                          7287183768
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216472
  Max global variable size:                      7287183768
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     32
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7f8c96dee008
  Name:                                          gfx1032
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                3452.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program
```

`clinfo`:

```
[espionage724@Oak ~]$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3452.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx1032
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0
  Driver Version                                  3452.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0
  Device Type                                     GPU
  Device Board Name (AMD)                         AMD Radeon RX 6600 XT
  Device PCI-e ID (AMD)                           0x73ff
  Device Topology (AMD)                           PCI-E, 0000:05:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               16
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                32
  SIMD instruction width (AMD)                    1
  Max clock frequency                             2900MHz
  Graphics IP (AMD)                               10.3
  Device Partition                                (core)
    Max number of sub-devices                     16
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple (kernel)     32
  Wavefront width (AMD)                           32
  Preferred / native vector sizes
    char                                                 4 / 4
    short                                                2 / 2
    int                                                  1 / 1
    long                                                 1 / 1
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
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
  Address bits                                    64, Little-Endian
  Global memory size                              8573157376 (7.984GiB)
  Global free memory (AMD)                        8372224 (7.984GiB) 8372224 (7.984GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7287183768 (6.787GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    7287183768 (6.787GiB)
  Preferred total size of global vars             8573157376 (7.984GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             29695
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 8192 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             16384x16384x8192 pixels
    Max number of read image args                 128
    Max number of write image args                8
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    16
  Max pipe packet size                            2992216472 (2.787GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        7287183768 (6.787GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                262144 (256KiB)
    Max size                                      8388608 (8MiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             16
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx1032
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx1032
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx1032

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.3.1
  ICD loader Profile                              OpenCL 3.0
```

---

### 评论 #47 — xuhuisheng (2022-07-17T22:20:15Z)

Good news, navi21 with recent firmware didn't need PCOe atomics any more.

---

### 评论 #48 — wxianxin (2023-06-25T00:10:29Z)

> Good news, navi21 with recent firmware didn't need PCOe atomics any more.

I am running on a system that doesn't support PCIE atomics, ROCM & Pytorch run without error but all the number will become NaN.

---
