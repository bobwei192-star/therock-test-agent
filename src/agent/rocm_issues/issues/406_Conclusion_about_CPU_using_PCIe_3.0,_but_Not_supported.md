# Conclusion about CPU using PCIe 3.0, but Not supported

> **Issue #406**
> **状态**: closed
> **创建时间**: 2018-05-08T14:03:41Z
> **更新时间**: 2018-11-27T05:34:50Z
> **关闭时间**: 2018-05-12T12:57:21Z
> **作者**: Gezine
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/406

## 描述

Hi, I opened an issue about PCIe atomics requirements at 2017.july
[https://github.com/RadeonOpenCompute/ROCm/issues/157](https://github.com/RadeonOpenCompute/ROCm/issues/157)

And this is my conclusion about CPU using PCIe 3.0, but Not supported

Not Supported
Ivybridge Core i5,i7
Ivybridge Xeon E3
Sandybridge Xeon E5 V1

Supported
Ivybridge Xeon E5 V2

All tested with my own machines.
Hope It helped.

---

## 评论 (10 条)

### 评论 #1 — boberfly (2018-05-10T18:08:46Z)

I can confirm IvyBridge Xeon E5 v2 works for me also (2x E5-2680v2).

---

### 评论 #2 — gstoner (2018-05-12T04:26:22Z)

@gezine try ROCm 1.8 

---

### 评论 #3 — Gezine (2018-05-12T05:37:49Z)

@gstoner Just installed 1.8, and it still works

Used components
E5 2650 v2
Two RX480 
Ubuntu server 16.04.4, kernel 4.13.0-41

BTW do I really have to uninstall Rocm 1.7 to upgrade to 1.8?
This is so frustrating.

---

### 评论 #4 — Gezine (2018-05-12T06:59:18Z)

Output of rocminfo and clinfo

rocminfo

=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                             
System Endianness:       LITTLE                            

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz
  Vendor Name:             CPU                             
  Feature:                 None specified                  
  Profile:                 FULL_PROFILE                    
  Float Round Mode:        NEAR                            
  Max Queue Number:        0                               
  Queue Min Size:          0                               
  Queue Max Size:          0                               
  Queue Type:              MULTI                           
  Node:                    0                               
  Device Type:             CPU                             
  Cache Info:
    L1:                      32768KB                       
  Chip ID:                 0                               
  Cacheline Size:          64                              
  Max Clock Frequency (MHz):3400                           
  BDFID:                   0                               
  Compute Unit:            16                              
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65916544KB                  
      Allocatable:             TRUE                        
      Alloc Granule:           4KB                         
      Alloc Alignment:         4KB                         
      Acessible by all:        TRUE                        
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65916544KB                  
      Allocatable:             TRUE                        
      Alloc Granule:           4KB                         
      Alloc Alignment:         4KB                         
      Acessible by all:        TRUE                        
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx803                          
  Vendor Name:             AMD                             
  Feature:                 KERNEL_DISPATCH                 
  Profile:                 BASE_PROFILE                    
  Float Round Mode:        NEAR                            
  Max Queue Number:        128                             
  Queue Min Size:          4096                            
  Queue Max Size:          131072                          
  Queue Type:              MULTI                           
  Node:                    1                               
  Device Type:             GPU                             
  Cache Info:
    L1:                      16KB                          
  Chip ID:                 26591                           
  Cacheline Size:          64                              
  Max Clock Frequency (MHz):1266                           
  BDFID:                   512                             
  Compute Unit:            36                              
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE                           
  Wavefront Size:          64                              
  Workgroup Max Size:      1024                            
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                      
    Dim[1]:                  33555456                      
    Dim[2]:                  0                             
  Grid Max Size:           4294967295                      
  Waves Per CU:            40                              
  Max Work-item Per CU:    2560                            
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                    
    Dim[1]:                  4294967295                    
    Dim[2]:                  4294967295                    
  Max number Of fbarriers Per Workgroup:32                 
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8388608KB                   
      Allocatable:             TRUE                        
      Alloc Granule:           4KB                         
      Alloc Alignment:         4KB                         
      Acessible by all:        FALSE                       
    Pool 2
      Segment:                 GROUP                       
      Size:                    64KB                        
      Allocatable:             FALSE                       
      Alloc Granule:           0KB                         
      Alloc Alignment:         0KB                         
      Acessible by all:        FALSE                       
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx803   
      Machine Models:          HSA_MACHINE_MODEL_LARGE     
      Profiles:                HSA_PROFILE_BASE            
      Default Rounding Mode:   NEAR                        
      Default Rounding Mode:   NEAR                        
      Fast f16:                TRUE                        
      Workgroup Max Dimension:
        Dim[0]:                  67109888                  
        Dim[1]:                  1024                      
        Dim[2]:                  16777217                  
      Workgroup Max Size:      1024                        
      Grid Max Dimension:
        x                        4294967295                
        y                        4294967295                
        z                        4294967295                
      Grid Max Size:           4294967295                  
      FBarrier Max Size:       32                          
*******
Agent 3
*******
  Name:                    gfx803                          
  Vendor Name:             AMD                             
  Feature:                 KERNEL_DISPATCH                 
  Profile:                 BASE_PROFILE                    
  Float Round Mode:        NEAR                            
  Max Queue Number:        128                             
  Queue Min Size:          4096                            
  Queue Max Size:          131072                          
  Queue Type:              MULTI                           
  Node:                    2                               
  Device Type:             GPU                             
  Cache Info:
    L1:                      16KB                          
  Chip ID:                 26591                           
  Cacheline Size:          64                              
  Max Clock Frequency (MHz):1266                           
  BDFID:                   768                             
  Compute Unit:            36                              
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE                           
  Wavefront Size:          64                              
  Workgroup Max Size:      1024                            
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                      
    Dim[1]:                  50332672                      
    Dim[2]:                  0                             
  Grid Max Size:           4294967295                      
  Waves Per CU:            40                              
  Max Work-item Per CU:    2560                            
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                    
    Dim[1]:                  4294967295                    
    Dim[2]:                  4294967295                    
  Max number Of fbarriers Per Workgroup:32                 
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8388608KB                   
      Allocatable:             TRUE                        
      Alloc Granule:           4KB                         
      Alloc Alignment:         4KB                         
      Acessible by all:        FALSE                       
    Pool 2
      Segment:                 GROUP                       
      Size:                    64KB                        
      Allocatable:             FALSE                       
      Alloc Granule:           0KB                         
      Alloc Alignment:         0KB                         
      Acessible by all:        FALSE                       
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx803   
      Machine Models:          HSA_MACHINE_MODEL_LARGE     
      Profiles:                HSA_PROFILE_BASE            
      Default Rounding Mode:   NEAR                        
      Default Rounding Mode:   NEAR                        
      Fast f16:                TRUE                        
      Workgroup Max Dimension:
        Dim[0]:                  67109888                  
        Dim[1]:                  1024                      
        Dim[2]:                  16777217                  
      Workgroup Max Size:      1024                        
      Grid Max Dimension:
        x                        4294967295                
        y                        4294967295                
        z                        4294967295                
      Grid Max Size:           4294967295                  
      FBarrier Max Size:       32                          
*** Done ***


clinfo

Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP.internal (2617.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_object_metadata cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               2
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 67df
  Device Topology:                               PCI[ B#2, D#0, F#0 ]
  Max compute units:                             36
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
  Max clock frequency:                           1266Mhz
  Address bits:                                  64
  Max memory allocation:                         7301444403  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26591
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            8589934592  Constant buffer size:                          7301444403  Max number of constant args:                   8
  Local memory type:                             Scratchpad  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          3006477107  Max global variable size:                      7301444403  Max global variable preferred total size:      8589934592  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7efce3265ff0
  Name:                                          gfx803
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2617.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 67df
  Device Topology:                               PCI[ B#3, D#0, F#0 ]
  Max compute units:                             36
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
  Max clock frequency:                           1266Mhz
  Address bits:                                  64
  Max memory allocation:                         7301444403  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26591
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            8589934592  Constant buffer size:                          7301444403  Max number of constant args:                   8
  Local memory type:                             Scratchpad  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          3006477107  Max global variable size:                      7301444403  Max global variable preferred total size:      8589934592  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7efce3265ff0
  Name:                                          gfx803
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2617.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

---

### 评论 #5 — Gezine (2018-05-12T07:01:44Z)

Output of vector_copy

Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
Passed validation.
Freeing kernel argument memory buffer succeeded.
Destroying the signal succeeded.
Destroying the executable succeeded.
Destroying the code object succeeded.
Destroying the queue succeeded.
Freeing in argument memory buffer succeeded.
Freeing out argument memory buffer succeeded.
Shutting down the runtime succeeded.

---

### 评论 #6 — Gezine (2018-05-12T07:11:01Z)

Just compiled hipcaffe and executed samples without any problem.

Is there any other thing to verify?

---

### 评论 #7 — gstoner (2018-05-12T12:57:21Z)

@gezine Unfortanly yes you need to uninstall the driver. It how the Linux team designed the DKMS foundation and how it patch the firmware 

Looks like you good to go.       But love to see you run this https://github.com/RadeonOpenCompute/rocm_bandwidth_test

I am going to close this one up. 

---

### 评论 #8 — Gezine (2018-05-12T14:01:46Z)

@gstoner Just compiled rocm_bandwidth_test and this is result

          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz
          Device: 1,  Device 67df
          Device: 2,  Device 67df

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


          Unidirectional peak bandwidth GB/s

          D/D       0           1           2

          0         N/A         10.175722   9.879670

          1         5.053346    29.020790   N/A

          2         4.910341    N/A         28.803466


          Bdirectional peak bandwidth GB/s

          D/D       0           1           2

          0         N/A         15.702547   15.661749

          1         15.367413   N/A         N/A

          2         15.564688   N/A         N/A


Seems like it worked well.
Two RX480s are connected with Full PCIe 3.0 x16

So are you going to update CPU requirement of ROCm?

---

### 评论 #9 — Avatat (2018-11-22T07:39:57Z)

@gstoner, I'm so happy and surprised because:
PCIe Atomics Operations should work on Ivy Bridge E* CPU, so I chose E5-1650 v2 CPU in HP Z420 workstation. But I was shocked when I can't saw Atomics Operations cap in lspci -vv:
```
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev c7) (prog-if 00 [VGA controller])
        Subsystem: XFX Pine Group Inc. Radeon RX 480
        Physical Slot: 2
        Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
        Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
        Latency: 0, Cache Line Size: 64 bytes
        Interrupt: pin A routed to IRQ 39
        NUMA node: 0
        Region 0: Memory at d0000000 (64-bit, prefetchable) [size=256M]
        Region 2: Memory at e0000000 (64-bit, prefetchable) [size=2M]
        Region 4: I/O ports at c000 [size=256]
        Region 5: Memory at efe00000 (32-bit, non-prefetchable) [size=256K]
        Expansion ROM at efe40000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
                Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
        Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
                DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                        ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                        RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 256 bytes, MaxReadReq 1024 bytes
                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM L1, Exit Latency L0s <64ns, L1 <1us
                        ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                LnkCtl: ASPM Disabled; RCB 64 bytes Disabled- CommClk+
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                LnkSta: Speed 2.5GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR+, OBFF Not Supported
                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                         Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                         Compliance De-emphasis: -6dB
                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                         EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest+
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                Address: 00000000fee07000  Data: 4023
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
In that moment, I just started looking for some GTX 1070, but... I tried install fresh ROCm stack and run some ROCm code and here are the results:
```
# /opt/rocm/bin/rocm-smi


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  0   34c     11.190W  300Mhz   601Mhz   47.84%   auto      0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================
```
```
# /opt/rocm/bin/rocminfo
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0
  Queue Min Size:          0
  Queue Max Size:          0
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768KB
  Chip ID:                 0
  Cacheline Size:          64
  Max Clock Frequency (MHz):3500
  BDFID:                   0
  Compute Unit:            12
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32866292KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32866292KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx803
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26591
  Cacheline Size:          64
  Max Clock Frequency (MHz):1288
  BDFID:                   1280
  Compute Unit:            36
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  83887104
    Dim[2]:                  0
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8388608KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx803
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
*** Done ***
```
```
# /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2679.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Ellesmere [Radeon RX 470/480]
  Device Topology:				 PCI[ B#5, D#0, F#0 ]
  Max compute units:				 36
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1288Mhz
  Address bits:					 64
  Max memory allocation:			 7301444403
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26591
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 8589934592
  Constant buffer size:				 7301444403
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 3006477107
  Max global variable size:			 7301444403
  Max global variable preferred total size:	 8589934592
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f68dcadedf0
  Name:						 gfx803
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0
  Driver version:				 2679.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program
```
```
# /usr/local/bin/rocm_bandwidth_test
......
....

          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz
          Device: 1,  Ellesmere [Radeon RX 470/480]

          Device Access

          D/D       0         1

          0         1         1

          1         1         1


          Device Numa Distance

          D/D       0         1

          0         0         N/A

          1         20        0


          Unidirectional peak bandwidth GB/s

          D/D       0           1

          0         N/A         10.013300

          1         4.839133    54.063786


          Bdirectional peak bandwidth GB/s

          D/D       0           1

          0         N/A         14.282987

          1         14.406123   N/A
```

Tomorrow, my fiancee will try run some deeplearning stuff there and we will see if it really work! :)

My question is: how is it possible, that ROCm works on that setup without Atomic Operations in lspci output?

---

### 评论 #10 — jlgreathouse (2018-11-27T05:34:50Z)

Older versions of lspci do not display whether your CPU supports PCIe atomics or not. It was added to that tool in [December, 2016](https://github.com/pciutils/pciutils/commit/ad4315739e81e77f06f775efbf8e13699746b3ff). So you will likely need [version 3.5.3 or above](https://github.com/pciutils/pciutils/releases) to properly display PCIe 3.0 atomics capabilities. Ubuntu 18.04 comes with 3.5.2, as an example.

In addition, note that the capability you will want to look for is not in the VGA device, but rather in the PCIe root complex that your GPU is connected through. For example, likely in 00:00.0 for your root complex, and any bridges between it and your GPU (which you can see mapped out with `lspci -t`)

I believe that Ivy Bridge E Xeons (but not the original Ivy Bridge desktop processors) have PCIe 3.0 atomics. I'm not sure if this is available across the entire product line, however.

---
