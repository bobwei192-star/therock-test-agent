# clinfo segfaults with rocm-2.7

- **Issue #:** 880
- **State:** closed
- **Created:** 2019-08-29T00:18:55Z
- **Updated:** 2023-12-19T00:32:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/880

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