# clinfo segfaults with rocm-2.7

> **Issue #880**
> **状态**: closed
> **创建时间**: 2019-08-29T00:18:55Z
> **更新时间**: 2023-12-19T00:32:27Z
> **关闭时间**: 2023-12-18T22:25:49Z
> **作者**: FireBurn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/880

## 描述

Running clinfo segfaults:

```
fireburn@axion ~ $ gdb clinfo
GNU gdb (Gentoo 8.3 vanilla) 8.3
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://bugs.gentoo.org/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from clinfo...
(No debugging symbols found in clinfo)
(gdb) start
Function "main" not defined.
Make breakpoint pending on future shared library load? (y or [n]) y
Temporary breakpoint 1 (main) pending.
Starting program: /usr/bin/clinfo 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
[New Thread 0x7fffefd22700 (LWP 12339)]

Thread 1 "clinfo" hit Temporary breakpoint 1, 0x00007ffff5a516d0 in lld::elf::LinkerDriver::main(llvm::ArrayRef<char const*>)@plt () from /usr/lib/llvm/roc/lib/liblldELF.so.9roc
(gdb) bt
#0  0x00007ffff5a516d0 in lld::elf::LinkerDriver::main(llvm::ArrayRef<char const*>)@plt () from /usr/lib/llvm/roc/lib/liblldELF.so.9roc
#1  0x00007ffff5a7d5c6 in lld::elf::link(llvm::ArrayRef<char const*>, bool, llvm::raw_ostream&) () from /usr/lib/llvm/roc/lib/liblldELF.so.9roc
#2  0x00007ffff7284a27 in COMGR::linkWithLLD(llvm::ArrayRef<char const*>, llvm::raw_ostream&) () from /usr/lib64/libamd_comgr.so
#3  0x00007ffff728c9d2 in COMGR::InProcessDriver::execute(llvm::ArrayRef<char const*>) () from /usr/lib64/libamd_comgr.so
#4  0x00007ffff728ff8a in COMGR::AMDGPUCompiler::linkToExecutable() () from /usr/lib64/libamd_comgr.so
#5  0x00007ffff72ca2b0 in dispatchCompilerAction(amd_comgr_action_kind_s, COMGR::DataAction*, COMGR::DataSet*, COMGR::DataSet*, llvm::raw_ostream&) () from /usr/lib64/libamd_comgr.so
#6  0x00007ffff72d1508 in amd_comgr_do_action () from /usr/lib64/libamd_comgr.so
#7  0x00007ffff7c7d059 in device::Program::compileAndLinkExecutable(amd_comgr_data_set_s, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, amd::option::Options*, char**, unsigned long*) ()
   from /usr/lib64/libamdocl64.so
#8  0x00007ffff7c7e44d in device::Program::linkImplLC(amd::option::Options*) () from /usr/lib64/libamdocl64.so
#9  0x00007ffff7c84f4a in device::Program::build(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, char const*, amd::option::Options*) () from /usr/lib64/libamdocl64.so
#10 0x00007ffff7c92e47 in amd::Program::build(std::vector<amd::Device*, std::allocator<amd::Device*> > const&, char const*, void (*)(_cl_program*, void*), void*, bool) () from /usr/lib64/libamdocl64.so
#11 0x00007ffff7c6acac in amd::Device::BlitProgram::create(amd::Device*, char const*, char const*) () from /usr/lib64/libamdocl64.so
#12 0x00007ffff7cb456f in roc::Device::create(bool) () from /usr/lib64/libamdocl64.so
#13 0x00007ffff7cb5bc6 in roc::Device::init() () from /usr/lib64/libamdocl64.so
#14 0x00007ffff7c6878f in amd::Device::init() () from /usr/lib64/libamdocl64.so
#15 0x00007ffff7c8b79e in amd::Runtime::init() () from /usr/lib64/libamdocl64.so
#16 0x00007ffff7ce8a65 in std::call_once<clIcdGetPlatformIDsKHR::{lambda()#1}>(std::once_flag&, clIcdGetPlatformIDsKHR::{lambda()#1}&&)::{lambda()#2}::_FUN() () from /usr/lib64/libamdocl64.so
#17 0x00007ffff7d54207 in __pthread_once_slow () from /lib64/libpthread.so.0
#18 0x00007ffff7ce8b79 in clIcdGetPlatformIDsKHR () from /usr/lib64/libamdocl64.so
#19 0x00007ffff7f6bae9 in ?? () from /usr/lib64/OpenCL/vendors/ocl-icd/libOpenCL.so.1
#20 0x00007ffff7d54207 in __pthread_once_slow () from /lib64/libpthread.so.0
#21 0x00007ffff7f6d597 in clGetPlatformIDs () from /usr/lib64/OpenCL/vendors/ocl-icd/libOpenCL.so.1
#22 0x000055555555a0f1 in ?? ()
#23 0x00007ffff7d89f1b in __libc_start_main () from /lib64/libc.so.6
#24 0x000055555555c7ba in ?? ()
(gdb) Quit
(gdb) quit
A debugging session is active.
```

This is the output of rocminfo:

```
fireburn@axion ~ $ rocminfo
ROCk module is NOT loaded, possibly no GPU devices
fireburn is member of video group
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
  Name:                    Intel(R) Core(TM) i7-6820HK CPU @ 2.70GHz
  Marketing Name:          Intel(R) Core(TM) i7-6820HK CPU @ 2.70GHz
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
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3600                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32744480(0x1f3a420) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32744480(0x1f3a420) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx802                             
  Marketing Name:          Amethyst XT [Radeon R9 M295X]      
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26913(0x6921)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   723                                
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    4194304(0x400000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx802          
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

lspci -nn:

```
fireburn@axion ~ $ lspci -nn
00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [8086:1910] (rev 07)
00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) [8086:1901] (rev 07)
00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 530 [8086:191b] (rev 06)
00:04.0 Signal processing controller [1180]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [8086:1903] (rev 07)
00:14.0 USB controller [0c03]: Intel Corporation 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller [8086:a12f] (rev 31)
00:14.2 Signal processing controller [1180]: Intel Corporation 100 Series/C230 Series Chipset Family Thermal Subsystem [8086:a131] (rev 31)
00:16.0 Communication controller [0780]: Intel Corporation 100 Series/C230 Series Chipset Family MEI Controller #1 [8086:a13a] (rev 31)
00:17.0 SATA controller [0106]: Intel Corporation HM170/QM170 Chipset SATA Controller [AHCI Mode] [8086:a103] (rev 31)
00:1c.0 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #1 [8086:a110] (rev f1)
00:1c.4 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #5 [8086:a114] (rev f1)
00:1c.5 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #6 [8086:a115] (rev f1)
00:1c.6 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #7 [8086:a116] (rev f1)
00:1d.0 PCI bridge [0604]: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #9 [8086:a118] (rev f1)
00:1f.0 ISA bridge [0601]: Intel Corporation HM170 Chipset LPC/eSPI Controller [8086:a14e] (rev 31)
00:1f.2 Memory controller [0580]: Intel Corporation 100 Series/C230 Series Chipset Family Power Management Controller [8086:a121] (rev 31)
00:1f.3 Audio device [0403]: Intel Corporation 100 Series/C230 Series Chipset Family HD Audio Controller [8086:a170] (rev 31)
00:1f.4 SMBus [0c05]: Intel Corporation 100 Series/C230 Series Chipset Family SMBus [8086:a123] (rev 31)
01:00.0 Display controller [0380]: Advanced Micro Devices, Inc. [AMD/ATI] Amethyst XT [Radeon R9 M295X] [1002:6921]
3b:00.0 Ethernet controller [0200]: Qualcomm Atheros Killer E2400 Gigabit Ethernet Controller [1969:e0a1] (rev 10)
3c:00.0 Network controller [0280]: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter [168c:003e] (rev 32)
3d:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader [10ec:5227] (rev 01)
3e:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM951/PM951 [144d:a802] (rev 01)
```

---

## 评论 (15 条)

### 评论 #1 — FireBurn (2019-08-29T00:20:58Z)

This is the output if I answer no to the gdb library breakpoint question:

```
fireburn@axion ~ $ gdb clinfo
GNU gdb (Gentoo 8.3 vanilla) 8.3
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://bugs.gentoo.org/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from clinfo...
(No debugging symbols found in clinfo)
(gdb) start
Function "main" not defined.
Make breakpoint pending on future shared library load? (y or [n]) n
Starting program: /usr/bin/clinfo 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
[New Thread 0x7fffefd22700 (LWP 12753)]
[New Thread 0x7fffef521700 (LWP 12754)]
[New Thread 0x7fffeed20700 (LWP 12755)]
[New Thread 0x7fffee51f700 (LWP 12756)]
[New Thread 0x7fffedd1e700 (LWP 12757)]
[New Thread 0x7fffed51d700 (LWP 12758)]
[New Thread 0x7fffecd1c700 (LWP 12759)]
[New Thread 0x7fffdffff700 (LWP 12760)]
[New Thread 0x7fffdf7fe700 (LWP 12761)]

Thread 1 "clinfo" received signal SIGSEGV, Segmentation fault.
0x00007ffff7cc49d0 in roc::VirtualGPU::enableSyncBlit() const () from /usr/lib64/libamdocl64.so
(gdb) bt
#0  0x00007ffff7cc49d0 in roc::VirtualGPU::enableSyncBlit() const () from /usr/lib64/libamdocl64.so
#1  0x00007ffff7cb2a8a in roc::Device::xferQueue() const () from /usr/lib64/libamdocl64.so
#2  0x00007ffff7cb468b in roc::Device::create(bool) () from /usr/lib64/libamdocl64.so
#3  0x00007ffff7cb5bc6 in roc::Device::init() () from /usr/lib64/libamdocl64.so
#4  0x00007ffff7c6878f in amd::Device::init() () from /usr/lib64/libamdocl64.so
#5  0x00007ffff7c8b79e in amd::Runtime::init() () from /usr/lib64/libamdocl64.so
#6  0x00007ffff7ce8a65 in std::call_once<clIcdGetPlatformIDsKHR::{lambda()#1}>(std::once_flag&, clIcdGetPlatformIDsKHR::{lambda()#1}&&)::{lambda()#2}::_FUN() () from /usr/lib64/libamdocl64.so
#7  0x00007ffff7d54207 in __pthread_once_slow () from /lib64/libpthread.so.0
#8  0x00007ffff7ce8b79 in clIcdGetPlatformIDsKHR () from /usr/lib64/libamdocl64.so
#9  0x00007ffff7f6bae9 in ?? () from /usr/lib64/OpenCL/vendors/ocl-icd/libOpenCL.so.1
#10 0x00007ffff7d54207 in __pthread_once_slow () from /lib64/libpthread.so.0
#11 0x00007ffff7f6d597 in clGetPlatformIDs () from /usr/lib64/OpenCL/vendors/ocl-icd/libOpenCL.so.1
#12 0x000055555555a0f1 in ?? ()
#13 0x00007ffff7d89f1b in __libc_start_main () from /lib64/libc.so.6
#14 0x000055555555c7ba in ?? ()
(gdb) 
```

---

### 评论 #2 — JMadgwick (2019-08-29T11:51:32Z)

>Name:                    gfx802                             
  Marketing Name:          Amethyst XT [Radeon R9 M295X]

Have you previously had any success with this device? It's a gfx802 based chip and [not listed as supported](https://github.com/RadeonOpenCompute/ROCm#supported-gpus). All of the supported GPUs are gfx80**3**. Tonga is another gfx802 based device, this is known not to be supported and is listed as such. Unfortunately rocminfo and some other utilities still run with unsupported GPUs, creating a false impression that there is another problem elsewhere.
Sadly the documentation is lacking when it comes to more unusual GPUs such as yours. [There was further discussion on this matter last year](https://github.com/RadeonOpenCompute/ROCm/issues/509#issuecomment-421614262), looking at that again it seems that there is indeed **no gfx802 support** in ROCm whatsoever.
Try and use the AMDGPU-Pro driver instead, I have a feeling that it does supports OpenCL on this GPU and it's just the ROCm runtime which does not.

---

### 评论 #3 — FireBurn (2019-08-29T12:12:41Z)

Apologies, I thought Tonga was fully supported (without actually checking)

Are there any plans to add support in future? I'm assuming the AMDGPU-Pro isn't open source, I've been testing out the new ebuilds in Gentoo and I'm not that keen on using blobs when I don't need to

---

### 评论 #4 — FireBurn (2019-08-29T12:14:05Z)

Would it be possible to have the driver spit out that there isn't a compatible device rather than segfaulting?

---

### 评论 #5 — JMadgwick (2019-08-29T12:49:02Z)

> Are there any plans to add support in future?

The issue I linked had some discussion, the conclusion was that the devs had planned to add it but it got set back and other events have presumably overtaken it. I highly doubt it's going to be added now. The support for gfx803 is apparently no longer being actively developed and has become maintenance only.
> Would it be possible to have the driver spit out that there isn't a compatible device rather than segfaulting?

I'm not an AMD developer but I would have thought so. From the looks of it the failure occurs when an attempt is made to compile the OpenCL kernel (which fails as the compiler has no support for the GPU arch). I don't know if anything could be actually be printed to stdout, it would depend on how the driver is implemented.
I think it would be better if during installation some kind of check was run (using info gleaned from lspci) to ensure that the system doesn't have unsupported GPUs. Users could then be warned that GPU 'X' is unsupported and will causes errors. Maybe there could be a link to the closed source driver if that offers support.
If you leave this open then maybe the devs will take a look at it, but they seen to be busy recently and not very active on here at all compared to in the past where almost every issue would get some kind of comment.

---

### 评论 #6 — FireBurn (2019-08-29T13:20:43Z)

And something similar with Raven :

```
fireburn@quark ~ $ gdb clinfo
GNU gdb (Gentoo 8.3 vanilla) 8.3
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://bugs.gentoo.org/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from clinfo...
(No debugging symbols found in clinfo)
(gdb) start
Function "main" not defined.
Make breakpoint pending on future shared library load? (y or [n])
Starting program: /usr/bin/clinfo
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
[New Thread 0x7fffef48e700 (LWP 2992802)]
[New Thread 0x7fffeec8d700 (LWP 2992803)]
[New Thread 0x7fffee48c700 (LWP 2992804)]
[New Thread 0x7fffedc8b700 (LWP 2992805)]
[New Thread 0x7fffed48a700 (LWP 2992806)]
[New Thread 0x7fffecc89700 (LWP 2992807)]
[New Thread 0x7ffedffff700 (LWP 2992808)]
[New Thread 0x7ffedf7fe700 (LWP 2992809)]
[New Thread 0x7ffedeffd700 (LWP 2992810)]

Thread 1 "clinfo" received signal SIGSEGV, Segmentation fault.
0x00007ffff7abda02 in amd::GpuAgent::QueueCreate(unsigned long, unsigned int, void (*)(hsa_status_t, hsa_queue_s*, void*), void*, unsigned int, unsigned int, core::Queue**) ()
   from /usr/lib64/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007ffff7abda02 in amd::GpuAgent::QueueCreate(unsigned long, unsigned int, void (*)(hsa_status_t, hsa_queue_s*, void*), void*, unsigned int, unsigned int, core::Queue**) ()
   from /usr/lib64/libhsa-runtime64.so.1
#1  0x00007ffff7abc1c1 in amd::GpuAgent::CreateInterceptibleQueue() () from /usr/lib64/libhsa-runtime64.so.1
#2  0x00007ffff7abc424 in amd::GpuAgent::InitDma()::{lambda()#1}::operator()() const () from /usr/lib64/libhsa-runtime64.so.1
#3  0x00007ffff7abf1e7 in std::_Function_handler<core::Queue* (), amd::GpuAgent::InitDma()::{lambda()#1}>::_M_invoke(std::_Any_data const&) () from /usr/lib64/libhsa-runtime64.so.1
#4  0x00007ffff7ac3a70 in std::function<core::Queue* ()>::operator()() const () from /usr/lib64/libhsa-runtime64.so.1
#5  0x00007ffff7ac3361 in lazy_ptr<core::Queue>::make_body(bool) const () from /usr/lib64/libhsa-runtime64.so.1
#6  0x00007ffff7ac1fb6 in lazy_ptr<core::Queue>::operator->() const () from /usr/lib64/libhsa-runtime64.so.1
#7  0x00007ffff7abe9b7 in amd::GpuAgent::InvalidateCodeCaches() () from /usr/lib64/libhsa-runtime64.so.1
#8  0x00007ffff7acb20f in amd::LoaderContext::SegmentAlloc(amdgpu_hsa_elf_segment_t, hsa_agent_s, unsigned long, unsigned long, bool) () from /usr/lib64/libhsa-runtime64.so.1
#9  0x00007ffff7b2c9f7 in amd::hsa::loader::ExecutableImpl::LoadSegmentsV2(hsa_agent_s, amd::hsa::code::AmdHsaCode const*) () from /usr/lib64/libhsa-runtime64.so.1
#10 0x00007ffff7b2c865 in amd::hsa::loader::ExecutableImpl::LoadSegments(hsa_agent_s, amd::hsa::code::AmdHsaCode const*, unsigned int) () from /usr/lib64/libhsa-runtime64.so.1
#11 0x00007ffff7b2c2f2 in amd::hsa::loader::ExecutableImpl::LoadCodeObject(hsa_agent_s, hsa_code_object_s, unsigned long, char const*, hsa_loaded_code_object_s*) ()
   from /usr/lib64/libhsa-runtime64.so.1
#12 0x00007ffff7b2b63d in amd::hsa::loader::ExecutableImpl::LoadCodeObject(hsa_agent_s, hsa_code_object_s, char const*, hsa_loaded_code_object_s*) () from /usr/lib64/libhsa-runtime64.so.1
#13 0x00007ffff7aeb896 in HSA::hsa_executable_load_agent_code_object(hsa_executable_s, hsa_agent_s, hsa_code_object_reader_s, char const*, hsa_loaded_code_object_s*) ()
   from /usr/lib64/libhsa-runtime64.so.1
#14 0x00007ffff7b26e26 in hsa_executable_load_agent_code_object () from /usr/lib64/libhsa-runtime64.so.1
#15 0x00007ffff7ca7e00 in roc::LightningProgram::setKernels(amd::option::Options*, void*, unsigned long) () from /usr/lib64/libamdocl64.so
#16 0x00007ffff7c7847e in device::Program::linkImplLC(amd::option::Options*) () from /usr/lib64/libamdocl64.so
#17 0x00007ffff7c7e732 in device::Program::build(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, char const*, amd::option::Options*) ()
   from /usr/lib64/libamdocl64.so
#18 0x00007ffff7c8caf7 in amd::Program::build(std::vector<amd::Device*, std::allocator<amd::Device*> > const&, char const*, void (*)(_cl_program*, void*), void*, bool) () from /usr/lib64/libamdocl64.so
#19 0x00007ffff7c64142 in amd::Device::BlitProgram::create(amd::Device*, char const*, char const*) () from /usr/lib64/libamdocl64.so
#20 0x00007ffff7caed03 in roc::Device::create(bool) () from /usr/lib64/libamdocl64.so
#21 0x00007ffff7cb037b in roc::Device::init() () from /usr/lib64/libamdocl64.so
#22 0x00007ffff7c61c01 in amd::Device::init() () from /usr/lib64/libamdocl64.so
#23 0x00007ffff7c8517e in amd::Runtime::init() () from /usr/lib64/libamdocl64.so
#24 0x00007ffff7ce3b95 in std::call_once<clIcdGetPlatformIDsKHR::{lambda()#1}>(std::once_flag&, clIcdGetPlatformIDsKHR::{lambda()#1}&&)::{lambda()#2}::_FUN() () from /usr/lib64/libamdocl64.so
#25 0x00007ffff7d4f4d7 in __pthread_once_slow () from /lib64/libpthread.so.0
#26 0x00007ffff7ce3cac in clIcdGetPlatformIDsKHR () from /usr/lib64/libamdocl64.so
#27 0x00007ffff7f75293 in _find_and_check_platforms.lto_priv.0 () from /usr/lib64/OpenCL/vendors/ocl-icd/libOpenCL.so.1
#28 0x00007ffff7f7468f in __initClIcd () from /usr/lib64/OpenCL/vendors/ocl-icd/libOpenCL.so.1
#29 0x00007ffff7d4f4d7 in __pthread_once_slow () from /lib64/libpthread.so.0
#30 0x00007ffff7f7352c in clGetPlatformIDs () from /usr/lib64/OpenCL/vendors/ocl-icd/libOpenCL.so.1
#31 0x000055555555a06e in ?? ()
#32 0x00007ffff7d84f1b in __libc_start_main () from /lib64/libc.so.6
#33 0x000055555555c6da in ?? ()
(gdb) client_loop: send disconnect: Connection reset by peer
```

Reading the doc you linked to, this should probably work but isn't officially supported, again I don't think clinfo should segfault

---

### 评论 #7 — FireBurn (2019-08-29T13:23:16Z)

And the rocminfo for that machine:

```
fireburn@quark ~ $ rocminfo
ROCk module is NOT loaded, possibly no GPU devices
fireburn is member of video group
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
  Name:                    AMD Ryzen 5 2400G with Radeon Vega Graphics
  Marketing Name:          AMD Ryzen 5 2400G with Radeon Vega Graphics
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
    L1:                      32(0x20) KB
  Chip ID:                 5597(0x15dd)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3600
  BDFID:                   2048
  Internal Node ID:        0
  Compute Unit:            8
  SIMDs per CU:            4
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    33554048(0x1fffe80) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx902
  Marketing Name:          AMD Ryzen 5 2400G with Radeon Vega Graphics
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 5597(0x15dd)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1250
  BDFID:                   2048
  Internal Node ID:        0
  Compute Unit:            11
  SIMDs per CU:            4
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        160(0xa0)
  Max Work-item Per CU:    10240(0x2800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack
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

---

### 评论 #8 — FireBurn (2019-08-29T13:24:37Z)

This is in the dmesg

```
[565677.950900] clinfo[2992776]: segfault at 0 ip 00007ff21a730a02 sp 00007ffd1de637e0 error 6 in libhsa-runtime64.so.1.1.9[7ff21a6fe000+147000]
[565677.950907] Code: ff ff ff 48 8b 85 58 ff ff ff 48 8b 80 18 04 00 00 48 8b 95 78 ff ff ff 48 c1 e2 03 48 01 c2 48 8b 85 68 ff ff ff 48 8b 40 18 <48> 89 02 c6 45 b0 01 90 bb 00 00 00 00 0f b6 45 b0 83 f0 01 84 c0
[565681.798718] Evicting PASID 32770 queues
```

The queue bit didn't happen on Tonga

---

### 评论 #9 — JMadgwick (2019-08-29T13:33:17Z)

> this should probably work but isn't officially supported, again I don't think clinfo should segfault

It seems that it depends on the motherboard configuration. [The detailed (but now outdated) hardware compatibility page ](https://rocm.github.io/hardware.html)states this regarding APUs:
APUs may may not work due to OEM and ODM choices when it comes to key configurations parameters such as inclusion of the required CRAT tables and IOMMU configuration parameters in the system BIOS. As such, APU-based laptops, all-in-one systems, and desktop motherboards may not be properly detected by the ROCm drivers. You should check with your system vendor to see if these options are available before attempting to use an APU-based system with ROCm.

You could try tweaking the settings or having a look in the manual for your motherboard.

> I don't think clinfo should segfault

Ideally not, but it seems that there is no infrastructure in place to catch these problems, I'm doubtful that AMD will do anything about this.
For comparison trying to run clinfo on a gfx700 GPU causes a kernel oops (due to broken kernel module) plus the process hangs and cannot be killed. By comparison a segfault is not a big deal.


---

### 评论 #10 — drwetter (2019-08-31T16:23:10Z)

Seems related to https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/68 ?

---

### 评论 #11 — tasso (2023-12-12T22:55:41Z)

Is this still an issue?  If not, can we please close it?  Thanks!

---

### 评论 #12 — tasso (2023-12-18T22:25:49Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---

### 评论 #13 — FireBurn (2023-12-18T22:48:43Z)

I think I still saw this issue the last time I tested, I'll check

---

### 评论 #14 — FireBurn (2023-12-18T22:53:30Z)

No sorry that was a different issue, clinfo is working fine

---

### 评论 #15 — tasso (2023-12-19T00:32:26Z)

Great!  Thanks for checking.

---
