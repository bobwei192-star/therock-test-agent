# Unable to open /dev/kfd read-write: Cannot allocate memory

> **Issue #1185**
> **状态**: closed
> **创建时间**: 2020-07-27T15:19:45Z
> **更新时间**: 2023-12-19T16:18:21Z
> **关闭时间**: 2023-12-19T16:18:20Z
> **作者**: FahrezaAkmal
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1185

## 描述

I installed rcom on my ubuntu, then I wrote the command `rcominfo` and this happened :
`ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
akuganteng is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.`

---

## 评论 (11 条)

### 评论 #1 — xuhuisheng (2020-07-28T02:40:09Z)

if using RX580, please make sure CPU and motherboard supporting PCIe-Atomics.

---

### 评论 #2 — BrunoLiegiBastonLiegi (2020-07-29T12:40:09Z)

Hi,
I have a similar problem with `/dev/kfd`, I'm trying to install ROCm on a matebook 13 with ryzen 3500u and integrated vega graphics.
Here's the output of `/opt/rocm/bin/rocminfo`

>ROCk module is loaded
Unable to open /dev/kfd read-write: Bad address
andrea is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

`strace /opt/rocm/bin/rocminfo` gives the following (only the relevant part):

>openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 EFAULT (Bad address)
write(1, "\33[31mhsa api call failure at: /s"..., 61hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
) = 61
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -337, SEEK_CUR)                = -1 ESPIPE (Illegal seek)
exit_group(4104)                        = ?
+++ exited with 8 +++

I don't know if this could be of any importance, but in addition to `video` group, I needed to add my user to `render` group.

When I run `/opt/rocm/opencl/bin/clinfo` instead:

>Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3137.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback 


  >Platform Name:                                 AMD Accelerated Parallel Processing
>Number of devices:                               0

it's a bit worrying that the number of devices is 0, but I assume that this might be related to the fact that my gpu is integrated.


---

### 评论 #3 — bfkg (2020-07-30T09:12:44Z)

Similar problem on our system.
```sh
/opt/rocm/bin/rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
root is member of video group
hsa api call failure at: /data/jenkins_workspace/centos_pipeline_job_3.5/rocm-rel-3.5/rocm-3.5-34-20200613/7.5/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
```/opt/rocm/opencl/bin/clinfo``` gives
```sh
 Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3137.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback 


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               0
```
```
03:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 20 (rev 02)
        Region 0: Memory at 30400000000 (64-bit, prefetchable) [size=16G]
        Region 2: Memory at 30200000000 (64-bit, prefetchable) [size=2M]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [64] Express (v2) Legacy Endpoint, MSI 00
                DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
                DevCtl: Report errors: Correctable+ Non-Fatal+ Fatal+ Unsupported-
                        RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 512 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 16GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM Disabled; RCB 64 bytes Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 16GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Range ABCD, TimeoutDis+, LTR+, OBFF Not Supported
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
                UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                AERCap: First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
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
                Page Request Capacity: 00000100, Page Request Allocation: 00000000
        Capabilities: [2d0 v1] Process Address Space ID (PASID)
                PASIDCap: Exec+ Priv+, Max PASID Width: 10
                PASIDCtl: Enable- Exec- Priv-
        Capabilities: [320 v1] Latency Tolerance Reporting
                Max snoop latency: 0ns
                Max no snoop latency: 0ns
        Capabilities: [400 v1] #25
        Capabilities: [410 v1] #26
        Capabilities: [440 v1] #27
        Kernel modules: amdgpu
```
```Model name:            AMD EPYC 7452 32-Core Processor```


---

### 评论 #4 — xuhuisheng (2020-07-30T12:17:34Z)

please ref https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support.
Rocm only supports a few gpu, likes

* Radeon R9 Fury X and Radeon Instinct MI8
* Radeon RX 580 and Radeon Instinct MI6
* Radeon RX Vega 64 and Radeon Instinct MI25
* Radeon Instinct MI50, Radeon Instinct MI60 or AMD Radeon VII

---

### 评论 #5 — bfkg (2020-07-30T12:27:34Z)

I have read about that. We have Radeon Instinct MI50. Only lscpi lists it as Vega20. 
So it should be supported.

---

### 评论 #6 — srinivamd (2020-08-22T16:19:32Z)

Is the user does not 'video' group membership then you could see the error accessing /dev/kfd.
Two things: 1) Does it work when you run using 'sudo'?
2) Add userid to video groups (sudo usermod -a -G video &lt;userid&gt;), logout, log back in and retry.


---

### 评论 #7 — ROCmSupport (2020-12-16T11:59:14Z)

Hi @FahrezaAkmal 
Can you please check with the latest ROCm 3.10 and update me asap.
Thank you.

---

### 评论 #8 — JLT032 (2021-04-25T12:53:22Z)

mount -o remount,exec /dev 

should **temporarily** fix read-write issue with /dev/kfd, now commands and tools using /dev/kfd run normally

https://github.com/RadeonOpenCompute/rocminfo/issues/40

---

### 评论 #9 — tasso (2023-12-19T15:57:25Z)

Is this still an issue?  If not, can we please close it?  Thanks!

---

### 评论 #10 — bfkg (2023-12-19T16:17:01Z)

Sorry. The issue can be closed. Thank you. 

---

### 评论 #11 — tasso (2023-12-19T16:18:20Z)

Thanks for the reply.  Closing issue.

---
