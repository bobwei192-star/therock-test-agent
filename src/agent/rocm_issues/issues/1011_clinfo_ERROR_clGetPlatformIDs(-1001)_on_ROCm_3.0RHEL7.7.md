# clinfo ERROR: clGetPlatformIDs(-1001) on ROCm 3.0/RHEL7.7

> **Issue #1011**
> **状态**: closed
> **创建时间**: 2020-02-06T22:13:59Z
> **更新时间**: 2020-04-07T14:32:22Z
> **关闭时间**: 2020-03-23T21:19:56Z
> **作者**: akostadinov
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1011

## 描述

Hello, tried to isntall ROCm 3.0 on RHEL 7.7. First removed old install and followed [guide](https://rocm-documentation.readthedocs.io/en/latest/Installation_Guide/Installation-Guide.html#preparing-rhel-v7-7-7-for-installation).

<details>
 <summary>rocminfo is fine (click to expand)</summary>

```
$ rocminfo 
ROCk module is loaded
avalon is member of video group
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
  Name:                    Intel(R) Core(TM)2 CPU          4400  @ 2.00GHz
  Marketing Name:          Intel(R) Core(TM)2 CPU          4400  @ 2.00GHz
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
  Max Clock Freq. (MHz):   2000                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            2                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    5943620(0x5ab144) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    5943620(0x5ab144) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
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
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
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
      Size:                    16760832(0xffc000) KB              
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
      Name:                    amdgcn-amd-amdhsa--gfx900          
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
</details>

clinfo not:
```
$ /opt/rocm/opencl/bin/x86_64/clinfo 
ERROR: clGetPlatformIDs(-1001)
$ /usr/bin/clinfo 
Number of platforms                               0
```
I have read #682 but not the same 
```
$ cat /etc/OpenCL/vendors/amdocl64.icd 
libamdocl64.so
```

I read [hipinfo debugging advise](https://github.com/RadeonOpenCompute/ROCm/issues/511#issuecomment-415597320):
```
$ make hipInfo
/opt/rocm/hip/bin/hipcc hipInfo.cpp -o hipInfo
/opt/rocm/hcc/bin/../lib/libhc_am.so: undefined reference to `hsa_amd_memory_lock_to_pool@ROCR_1'
clang-10: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [hipInfo] Error 1
```

<details>
 <summary>I have edited Makefile to add `-v` (click to expand)</summary>

```
$ make hipInfo
/opt/rocm/hip/bin/hipcc hipInfo.cpp -o hipInfo
/opt/rocm/hcc/bin/../lib/libhc_am.so: undefined reference to `hsa_amd_memory_lock_to_pool@ROCR_1'
clang-10: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [hipInfo] Error 1
[avalon@koTaH hipInfo]$ man Makefile 
No manual entry for Makefile
[avalon@koTaH hipInfo]$ vi Makefile 
[avalon@koTaH hipInfo]$ make hipInfo
/opt/rocm/hip/bin/hipcc hipInfo.cpp -v -o hipInfo
HCC clang version 10.0.0 (/data/jenkins-workspace/centos_pipeline_job_3.0/rocm-rel-3.0/rocm-3.0-6-20191216/centos/external/hcc-tot/llvm-project/clang 40756364719e83a2ddd5abe0affe700723cdd852) (based on HCC 3.0.19493-75ea952e-40756364719e )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/hcc/bin
Found candidate GCC installation: /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7
Found candidate GCC installation: /usr/lib/gcc/x86_64-redhat-linux/4.8.2
Found candidate GCC installation: /usr/lib/gcc/x86_64-redhat-linux/4.8.5
Selected GCC installation: /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7
Candidate multilib: .;@m64
Candidate multilib: 32;@m32
Selected multilib: .;@m64
Found HCC installation: /opt/rocm/hcc/bin/..
 "/opt/rocm/hcc/bin/clang-10" -cc1 -D__KALMAR_HC__=1 -D__HCC_HC__=1 -triple x86_64-unknown-linux-gnu -emit-obj -mrelax-all -disable-free -disable-llvm-verifier -main-file-name hipInfo.cpp -mrelocation-model static -mthread-model posix -mframe-pointer=all -fmath-errno -masm-verbose -mconstructor-aliases -munwind-tables -fuse-init-array -target-cpu x86-64 -dwarf-column-info -debugger-tuning=gdb -v -resource-dir /opt/rocm/hcc/lib/clang/10.0.0 -I/opt/rocm/hcc/bin/../include -I/opt/rocm/hcc/bin/../hcc/include -isystem /opt/rocm/hcc/include -isystem /opt/rocm/hip/include/hip/hcc_detail/cuda -isystem /opt/rocm/hsa/include -isystem /opt/rocm/hip/include -D __HIPCC__ -D HIP_VERSION_MAJOR=3 -D HIP_VERSION_MINOR=0 -D HIP_VERSION_PATCH=19493 -D __HIP_ARCH_GFX900__=1 -internal-isystem /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7 -internal-isystem /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/x86_64-redhat-linux -internal-isystem /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/backward -internal-isystem /usr/local/include -internal-isystem /opt/rocm/hcc/lib/clang/10.0.0/include -internal-externc-isystem /include -internal-externc-isystem /usr/include -Wno-deprecated-register -std=c++amp -fdeprecated-macro -fdebug-compilation-dir /home/avalon/hipInfo -ferror-limit 19 -fmessage-length 0 -fgnuc-version=4.2.1 -fobjc-runtime=gcc -fcxx-exceptions -fexceptions -fdiagnostics-show-option -fcolor-diagnostics -famp -fhsa-ext -fgpu-rdc -faddrsig -o /tmp/hipInfo-f1864a.o -x hc-host hipInfo.cpp
clang -cc1 version 10.0.0 based upon HCC 3.0.19493-75ea952e-40756364719e  default target x86_64-unknown-linux-gnu
ignoring nonexistent directory "/opt/rocm/hcc/bin/../hcc/include"
ignoring nonexistent directory "/include"
ignoring duplicate directory "/opt/rocm/hcc/bin/../include"
  as it is a non-system directory that duplicates a system directory
#include "..." search starts here:
#include <...> search starts here:
 /opt/rocm/hcc/bin/../include
 /opt/rocm/hip/include/hip/hcc_detail/cuda
 /opt/rocm/hsa/include
 /opt/rocm/hip/include
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/x86_64-redhat-linux
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/backward
 /usr/local/include
 /opt/rocm/hcc/lib/clang/10.0.0/include
 /usr/include
End of search list.
 "/opt/rocm/hcc/bin/clang-10" -cc1 -D__KALMAR_HC__=1 -D__HCC_HC__=1 -famp-is-device -fno-builtin -fno-common -O2 -triple amdgcn--amdhsa-hcc -aux-triple x86_64-unknown-linux-gnu -S -disable-free -disable-llvm-verifier -main-file-name hipInfo.cpp -mrelocation-model pic -pic-level 1 -mthread-model posix -mframe-pointer=all -fmath-errno -no-integrated-as -mconstructor-aliases -fuse-init-array -dwarf-column-info -debugger-tuning=gdb -v -resource-dir /opt/rocm/hcc/lib/clang/10.0.0 -I/opt/rocm/hcc/bin/../include -I/opt/rocm/hcc/bin/../hcc/include -isystem /opt/rocm/hcc/include -isystem /opt/rocm/hip/include/hip/hcc_detail/cuda -isystem /opt/rocm/hsa/include -isystem /opt/rocm/hip/include -D __HIPCC__ -D HIP_VERSION_MAJOR=3 -D HIP_VERSION_MINOR=0 -D HIP_VERSION_PATCH=19493 -D __HIP_ARCH_GFX900__=1 -internal-isystem /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7 -internal-isystem /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/x86_64-redhat-linux -internal-isystem /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/backward -internal-isystem /usr/local/include -internal-isystem /opt/rocm/hcc/lib/clang/10.0.0/include -internal-externc-isystem /include -internal-externc-isystem /usr/include -Wno-deprecated-register -std=c++amp -fdeprecated-macro -fno-dwarf-directory-asm -fdebug-compilation-dir /home/avalon/hipInfo -ferror-limit 19 -fmessage-length 0 -fgnuc-version=4.2.1 -fobjc-runtime=gcc -fcxx-exceptions -fexceptions -fdiagnostics-show-option -fcolor-diagnostics -famp -fhsa-ext -fgpu-rdc -emit-llvm-bc -o /tmp/hipInfo-56ebbf.s -x hc-kernel hipInfo.cpp
clang -cc1 version 10.0.0 based upon HCC 3.0.19493-75ea952e-40756364719e  default target x86_64-unknown-linux-gnu
ignoring nonexistent directory "/opt/rocm/hcc/bin/../hcc/include"
ignoring nonexistent directory "/include"
ignoring duplicate directory "/opt/rocm/hcc/bin/../include"
  as it is a non-system directory that duplicates a system directory
ignoring duplicate directory "/usr/local/include"
ignoring duplicate directory "/opt/rocm/hcc/lib/clang/10.0.0/include"
ignoring duplicate directory "/usr/include"
#include "..." search starts here:
#include <...> search starts here:
 /opt/rocm/hcc/bin/../include
 /opt/rocm/hip/include/hip/hcc_detail/cuda
 /opt/rocm/hsa/include
 /opt/rocm/hip/include
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/x86_64-redhat-linux
 /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../include/c++/7/backward
 /usr/local/include
 /opt/rocm/hcc/lib/clang/10.0.0/include
 /usr/include
End of search list.
 "/opt/rocm/hcc/bin/hc-kernel-assemble" /tmp/hipInfo-56ebbf.s /tmp/hipInfo-5cc65b.o
 "/opt/rocm/hcc/bin/clamp-link" --verbose -lstdc++ -L/opt/rocm/hcc/bin/../lib --rpath=/opt/rocm/hcc/bin/../lib -ldl -lm -lpthread -lhc_am -lmcwamp --amdgpu-target=gfx900 --hash-style=gnu --eh-frame-hdr -m elf_x86_64 -dynamic-linker /lib64/ld-linux-x86-64.so.2 -o hipInfo /lib/../lib64/crt1.o /lib/../lib64/crti.o /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbegin.o -L/opt/rocm/hcc/lib -L/opt/rocm/hsa/lib -L/opt/rocm/lib -L/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7 -L/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64 -L/lib/../lib64 -L/usr/lib/../lib64 -L/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../.. -L/opt/rocm/hcc/bin/../lib -L/lib -L/usr/lib --rpath=/opt/rocm/hip/lib /opt/rocm/hip/lib/libhip_hcc.so --rpath=/opt/rocm/hcc/lib -ldl -lm -lpthread -lhc_am --whole-archive -lmcwamp --no-whole-archive -lhsa-runtime64 -lhc_am -lm /tmp/hipInfo-f1864a.o /tmp/hipInfo-5cc65b.o -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtend.o /lib/../lib64/crtn.o -lclang_rt.builtins-x86_64
AMDGPU target array: gfx900

new kernel args: /tmp/tmp.khe38Jk3I6/hipInfo-5cc65b.be48095a4e07283adfc00018ae0bea59.kernel.bc

new host args: /tmp/tmp.khe38Jk3I6/hipInfo-5cc65b.be48095a4e07283adfc00018ae0bea59.host.o

new other args: --verbose -lstdc++ -L/opt/rocm/hcc/bin/../lib --rpath=/opt/rocm/hcc/bin/../lib -ldl -lm -lpthread -lhc_am -lmcwamp --hash-style=gnu --eh-frame-hdr -m elf_x86_64 -dynamic-linker /lib64/ld-linux-x86-64.so.2 -o hipInfo /lib/../lib64/crt1.o /lib/../lib64/crti.o /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbegin.o -L/opt/rocm/hcc/lib -L/opt/rocm/hsa/lib -L/opt/rocm/lib -L/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7 -L/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64 -L/lib/../lib64 -L/usr/lib/../lib64 -L/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../.. -L/opt/rocm/hcc/bin/../lib -L/lib -L/usr/lib --rpath=/opt/rocm/hip/lib /opt/rocm/hip/lib/libhip_hcc.so --rpath=/opt/rocm/hcc/lib -ldl -lm -lpthread -lhc_am --whole-archive -lmcwamp --no-whole-archive -lhsa-runtime64 -lhc_am -lm /tmp/hipInfo-f1864a.o -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtend.o /lib/../lib64/crtn.o -lclang_rt.builtins-x86_64

Generating AMD GCN kernel
Finished generation of AMD GCN kernels
GNU ld version 2.27-41.base.el7_7.2
  Supported emulations:
   elf_x86_64
   elf32_x86_64
   elf_i386
   elf_iamcu
   i386linux
   elf_l1om
   elf_k1om
using internal linker script:
==================================================
/* Script for -z combreloc: combine and sort reloc sections */
/* Copyright (C) 2014-2016 Free Software Foundation, Inc.
   Copying and distribution of this script, with or without modification,
   are permitted in any medium without royalty provided the copyright
   notice and this notice are preserved.  */
OUTPUT_FORMAT("elf64-x86-64", "elf64-x86-64",
	      "elf64-x86-64")
OUTPUT_ARCH(i386:x86-64)
ENTRY(_start)
SEARCH_DIR("=/usr/x86_64-redhat-linux/lib64"); SEARCH_DIR("=/usr/lib64"); SEARCH_DIR("=/usr/local/lib64"); SEARCH_DIR("=/lib64"); SEARCH_DIR("=/usr/x86_64-redhat-linux/lib"); SEARCH_DIR("=/usr/local/lib"); SEARCH_DIR("=/lib"); SEARCH_DIR("=/usr/lib");
SECTIONS
{
  /* Read-only sections, merged into text segment: */
  PROVIDE (__executable_start = SEGMENT_START("text-segment", 0x400000)); . = SEGMENT_START("text-segment", 0x400000) + SIZEOF_HEADERS;
  .interp         : { *(.interp) }
  .note.gnu.build-id : { *(.note.gnu.build-id) }
  .hash           : { *(.hash) }
  .gnu.hash       : { *(.gnu.hash) }
  .dynsym         : { *(.dynsym) }
  .dynstr         : { *(.dynstr) }
  .gnu.version    : { *(.gnu.version) }
  .gnu.version_d  : { *(.gnu.version_d) }
  .gnu.version_r  : { *(.gnu.version_r) }
  .rela.dyn       :
    {
      *(.rela.init)
      *(.rela.text .rela.text.* .rela.gnu.linkonce.t.*)
      *(.rela.fini)
      *(.rela.rodata .rela.rodata.* .rela.gnu.linkonce.r.*)
      *(.rela.data .rela.data.* .rela.gnu.linkonce.d.*)
      *(.rela.tdata .rela.tdata.* .rela.gnu.linkonce.td.*)
      *(.rela.tbss .rela.tbss.* .rela.gnu.linkonce.tb.*)
      *(.rela.ctors)
      *(.rela.dtors)
      *(.rela.got)
      *(.rela.bss .rela.bss.* .rela.gnu.linkonce.b.*)
      *(.rela.ldata .rela.ldata.* .rela.gnu.linkonce.l.*)
      *(.rela.lbss .rela.lbss.* .rela.gnu.linkonce.lb.*)
      *(.rela.lrodata .rela.lrodata.* .rela.gnu.linkonce.lr.*)
      *(.rela.ifunc)
    }
  .rela.plt       :
    {
      *(.rela.plt)
      PROVIDE_HIDDEN (__rela_iplt_start = .);
      *(.rela.iplt)
      PROVIDE_HIDDEN (__rela_iplt_end = .);
    }
  .init           :
  {
    KEEP (*(SORT_NONE(.init)))
  }
  .plt            : { *(.plt) *(.iplt) }
.plt.got        : { *(.plt.got) }
.plt.bnd        : { *(.plt.bnd) }
  .text           :
  {
    *(.text.unlikely .text.*_unlikely .text.unlikely.*)
    *(.text.exit .text.exit.*)
    *(.text.startup .text.startup.*)
    *(.text.hot .text.hot.*)
    *(.text .stub .text.* .gnu.linkonce.t.*)
    /* .gnu.warning sections are handled specially by elf32.em.  */
    *(.gnu.warning)
  }
  .fini           :
  {
    KEEP (*(SORT_NONE(.fini)))
  }
  PROVIDE (__etext = .);
  PROVIDE (_etext = .);
  PROVIDE (etext = .);
  .rodata         : { *(.rodata .rodata.* .gnu.linkonce.r.*) }
  .rodata1        : { *(.rodata1) }
  .eh_frame_hdr : { *(.eh_frame_hdr) *(.eh_frame_entry .eh_frame_entry.*) }
  .eh_frame       : ONLY_IF_RO { KEEP (*(.eh_frame)) *(.eh_frame.*) }
  .gcc_except_table   : ONLY_IF_RO { *(.gcc_except_table
  .gcc_except_table.*) }
  .gnu_extab   : ONLY_IF_RO { *(.gnu_extab*) }
  /* These sections are generated by the Sun/Oracle C++ compiler.  */
  .exception_ranges   : ONLY_IF_RO { *(.exception_ranges
  .exception_ranges*) }
  /* Adjust the address for the data segment.  We want to adjust up to
     the same address within the page on the next page up.  */
  . = DATA_SEGMENT_ALIGN (CONSTANT (MAXPAGESIZE), CONSTANT (COMMONPAGESIZE));
  /* Exception handling  */
  .eh_frame       : ONLY_IF_RW { KEEP (*(.eh_frame)) *(.eh_frame.*) }
  .gnu_extab      : ONLY_IF_RW { *(.gnu_extab) }
  .gcc_except_table   : ONLY_IF_RW { *(.gcc_except_table .gcc_except_table.*) }
  .exception_ranges   : ONLY_IF_RW { *(.exception_ranges .exception_ranges*) }
  /* Thread Local Storage sections  */
  .tdata	  : { *(.tdata .tdata.* .gnu.linkonce.td.*) }
  .tbss		  : { *(.tbss .tbss.* .gnu.linkonce.tb.*) *(.tcommon) }
  .preinit_array     :
  {
    PROVIDE_HIDDEN (__preinit_array_start = .);
    KEEP (*(.preinit_array))
    PROVIDE_HIDDEN (__preinit_array_end = .);
  }
  .init_array     :
  {
    PROVIDE_HIDDEN (__init_array_start = .);
    KEEP (*(SORT_BY_INIT_PRIORITY(.init_array.*) SORT_BY_INIT_PRIORITY(.ctors.*)))
    KEEP (*(.init_array EXCLUDE_FILE (*crtbegin.o *crtbegin?.o *crtend.o *crtend?.o ) .ctors))
    PROVIDE_HIDDEN (__init_array_end = .);
  }
  .fini_array     :
  {
    PROVIDE_HIDDEN (__fini_array_start = .);
    KEEP (*(SORT_BY_INIT_PRIORITY(.fini_array.*) SORT_BY_INIT_PRIORITY(.dtors.*)))
    KEEP (*(.fini_array EXCLUDE_FILE (*crtbegin.o *crtbegin?.o *crtend.o *crtend?.o ) .dtors))
    PROVIDE_HIDDEN (__fini_array_end = .);
  }
  .ctors          :
  {
    /* gcc uses crtbegin.o to find the start of
       the constructors, so we make sure it is
       first.  Because this is a wildcard, it
       doesn't matter if the user does not
       actually link against crtbegin.o; the
       linker won't look for a file to match a
       wildcard.  The wildcard also means that it
       doesn't matter which directory crtbegin.o
       is in.  */
    KEEP (*crtbegin.o(.ctors))
    KEEP (*crtbegin?.o(.ctors))
    /* We don't want to include the .ctor section from
       the crtend.o file until after the sorted ctors.
       The .ctor section from the crtend file contains the
       end of ctors marker and it must be last */
    KEEP (*(EXCLUDE_FILE (*crtend.o *crtend?.o ) .ctors))
    KEEP (*(SORT(.ctors.*)))
    KEEP (*(.ctors))
  }
  .dtors          :
  {
    KEEP (*crtbegin.o(.dtors))
    KEEP (*crtbegin?.o(.dtors))
    KEEP (*(EXCLUDE_FILE (*crtend.o *crtend?.o ) .dtors))
    KEEP (*(SORT(.dtors.*)))
    KEEP (*(.dtors))
  }
  .jcr            : { KEEP (*(.jcr)) }
  .data.rel.ro : { *(.data.rel.ro.local* .gnu.linkonce.d.rel.ro.local.*) *(.data.rel.ro .data.rel.ro.* .gnu.linkonce.d.rel.ro.*) }
  .dynamic        : { *(.dynamic) }
  .got            : { *(.got) *(.igot) }
  . = DATA_SEGMENT_RELRO_END (SIZEOF (.got.plt) >= 24 ? 24 : 0, .);
  .got.plt        : { *(.got.plt)  *(.igot.plt) }
  .data           :
  {
    *(.data .data.* .gnu.linkonce.d.*)
    SORT(CONSTRUCTORS)
  }
  .data1          : { *(.data1) }
  _edata = .; PROVIDE (edata = .);
  . = .;
  __bss_start = .;
  .bss            :
  {
   *(.dynbss)
   *(.bss .bss.* .gnu.linkonce.b.*)
   *(COMMON)
   /* Align here to ensure that the .bss section occupies space up to
      _end.  Align after .bss to ensure correct alignment even if the
      .bss section disappears because there are no input sections.
      FIXME: Why do we need it? When there is no .bss section, we don't
      pad the .data section.  */
   . = ALIGN(. != 0 ? 64 / 8 : 1);
  }
  .lbss   :
  {
    *(.dynlbss)
    *(.lbss .lbss.* .gnu.linkonce.lb.*)
    *(LARGE_COMMON)
  }
  . = ALIGN(64 / 8);
  . = SEGMENT_START("ldata-segment", .);
  .lrodata   ALIGN(CONSTANT (MAXPAGESIZE)) + (. & (CONSTANT (MAXPAGESIZE) - 1)) :
  {
    *(.lrodata .lrodata.* .gnu.linkonce.lr.*)
  }
  .ldata   ALIGN(CONSTANT (MAXPAGESIZE)) + (. & (CONSTANT (MAXPAGESIZE) - 1)) :
  {
    *(.ldata .ldata.* .gnu.linkonce.l.*)
    . = ALIGN(. != 0 ? 64 / 8 : 1);
  }
  . = ALIGN(64 / 8);
  _end = .; PROVIDE (end = .);
  . = DATA_SEGMENT_END (.);
  /* Stabs debugging sections.  */
  .stab          0 : { *(.stab) }
  .stabstr       0 : { *(.stabstr) }
  .stab.excl     0 : { *(.stab.excl) }
  .stab.exclstr  0 : { *(.stab.exclstr) }
  .stab.index    0 : { *(.stab.index) }
  .stab.indexstr 0 : { *(.stab.indexstr) }
  .comment       0 : { *(.comment) }
  /* DWARF debug sections.
     Symbols in the DWARF debugging sections are relative to the beginning
     of the section so we begin them at 0.  */
  /* DWARF 1 */
  .debug          0 : { *(.debug) }
  .line           0 : { *(.line) }
  /* GNU DWARF 1 extensions */
  .debug_srcinfo  0 : { *(.debug_srcinfo) }
  .debug_sfnames  0 : { *(.debug_sfnames) }
  /* DWARF 1.1 and DWARF 2 */
  .debug_aranges  0 : { *(.debug_aranges) }
  .debug_pubnames 0 : { *(.debug_pubnames) }
  /* DWARF 2 */
  .debug_info     0 : { *(.debug_info .gnu.linkonce.wi.*) }
  .debug_abbrev   0 : { *(.debug_abbrev) }
  .debug_line     0 : { *(.debug_line .debug_line.* .debug_line_end ) }
  .debug_frame    0 : { *(.debug_frame) }
  .debug_str      0 : { *(.debug_str) }
  .debug_loc      0 : { *(.debug_loc) }
  .debug_macinfo  0 : { *(.debug_macinfo) }
  /* SGI/MIPS DWARF 2 extensions */
  .debug_weaknames 0 : { *(.debug_weaknames) }
  .debug_funcnames 0 : { *(.debug_funcnames) }
  .debug_typenames 0 : { *(.debug_typenames) }
  .debug_varnames  0 : { *(.debug_varnames) }
  /* DWARF 3 */
  .debug_pubtypes 0 : { *(.debug_pubtypes) }
  .debug_ranges   0 : { *(.debug_ranges) }
  /* DWARF Extension.  */
  .debug_macro    0 : { *(.debug_macro) }
  .gnu.attributes 0 : { KEEP (*(.gnu.attributes)) }
  /DISCARD/ : { *(.note.GNU-stack) *(.gnu_debuglink) *(.gnu.lto_*) }
}


==================================================
attempt to open /tmp/tmp.khe38Jk3I6/kernel_hsa.o succeeded
/tmp/tmp.khe38Jk3I6/kernel_hsa.o
attempt to open /tmp/tmp.khe38Jk3I6/hipInfo-5cc65b.be48095a4e07283adfc00018ae0bea59.host.o succeeded
/tmp/tmp.khe38Jk3I6/hipInfo-5cc65b.be48095a4e07283adfc00018ae0bea59.host.o
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++.a failed
attempt to open /opt/rocm/hcc/lib/libstdc++.so failed
attempt to open /opt/rocm/hcc/lib/libstdc++.a failed
attempt to open /opt/rocm/hsa/lib/libstdc++.so failed
attempt to open /opt/rocm/hsa/lib/libstdc++.a failed
attempt to open /opt/rocm/lib/libstdc++.so failed
attempt to open /opt/rocm/lib/libstdc++.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++.so succeeded
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++.so
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++.so
attempt to open /usr/lib64/libstdc++.so.6 succeeded
/usr/lib64/libstdc++.so.6
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++_nonshared.a failed
attempt to open /opt/rocm/hcc/lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/hcc/lib/libstdc++_nonshared.a failed
attempt to open /opt/rocm/hsa/lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/hsa/lib/libstdc++_nonshared.a failed
attempt to open /opt/rocm/lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/lib/libstdc++_nonshared.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++_nonshared.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++_nonshared.a succeeded
attempt to open /opt/rocm/hcc/bin/../lib/libdl.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libdl.a failed
attempt to open /opt/rocm/hcc/lib/libdl.so failed
attempt to open /opt/rocm/hcc/lib/libdl.a failed
attempt to open /opt/rocm/hsa/lib/libdl.so failed
attempt to open /opt/rocm/hsa/lib/libdl.a failed
attempt to open /opt/rocm/lib/libdl.so failed
attempt to open /opt/rocm/lib/libdl.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libdl.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libdl.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libdl.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libdl.a failed
attempt to open /lib/../lib64/libdl.so succeeded
-ldl (/lib/../lib64/libdl.so)
attempt to open /opt/rocm/hcc/bin/../lib/libm.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libm.a failed
attempt to open /opt/rocm/hcc/lib/libm.so failed
attempt to open /opt/rocm/hcc/lib/libm.a failed
attempt to open /opt/rocm/hsa/lib/libm.so failed
attempt to open /opt/rocm/hsa/lib/libm.a failed
attempt to open /opt/rocm/lib/libm.so failed
attempt to open /opt/rocm/lib/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.a failed
attempt to open /lib/../lib64/libm.so succeeded
-lm (/lib/../lib64/libm.so)
attempt to open /opt/rocm/hcc/bin/../lib/libpthread.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libpthread.a failed
attempt to open /opt/rocm/hcc/lib/libpthread.so failed
attempt to open /opt/rocm/hcc/lib/libpthread.a failed
attempt to open /opt/rocm/hsa/lib/libpthread.so failed
attempt to open /opt/rocm/hsa/lib/libpthread.a failed
attempt to open /opt/rocm/lib/libpthread.so failed
attempt to open /opt/rocm/lib/libpthread.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libpthread.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libpthread.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libpthread.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libpthread.a failed
attempt to open /lib/../lib64/libpthread.so succeeded
opened script file /lib/../lib64/libpthread.so
opened script file /lib/../lib64/libpthread.so
attempt to open /lib64/libpthread.so.0 succeeded
/lib64/libpthread.so.0
attempt to open /usr/lib64/libpthread_nonshared.a succeeded
attempt to open /opt/rocm/hcc/bin/../lib/libhc_am.so succeeded
-lhc_am (/opt/rocm/hcc/bin/../lib/libhc_am.so)
attempt to open /opt/rocm/hcc/bin/../lib/libmcwamp.so succeeded
-lmcwamp (/opt/rocm/hcc/bin/../lib/libmcwamp.so)
attempt to open /lib/../lib64/crt1.o succeeded
/lib/../lib64/crt1.o
attempt to open /lib/../lib64/crti.o succeeded
/lib/../lib64/crti.o
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbegin.o succeeded
/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbegin.o
attempt to open /opt/rocm/hip/lib/libhip_hcc.so succeeded
/opt/rocm/hip/lib/libhip_hcc.so
attempt to open /opt/rocm/hcc/bin/../lib/libdl.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libdl.a failed
attempt to open /opt/rocm/hcc/lib/libdl.so failed
attempt to open /opt/rocm/hcc/lib/libdl.a failed
attempt to open /opt/rocm/hsa/lib/libdl.so failed
attempt to open /opt/rocm/hsa/lib/libdl.a failed
attempt to open /opt/rocm/lib/libdl.so failed
attempt to open /opt/rocm/lib/libdl.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libdl.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libdl.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libdl.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libdl.a failed
attempt to open /lib/../lib64/libdl.so succeeded
-ldl (/lib/../lib64/libdl.so)
attempt to open /opt/rocm/hcc/bin/../lib/libm.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libm.a failed
attempt to open /opt/rocm/hcc/lib/libm.so failed
attempt to open /opt/rocm/hcc/lib/libm.a failed
attempt to open /opt/rocm/hsa/lib/libm.so failed
attempt to open /opt/rocm/hsa/lib/libm.a failed
attempt to open /opt/rocm/lib/libm.so failed
attempt to open /opt/rocm/lib/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.a failed
attempt to open /lib/../lib64/libm.so succeeded
-lm (/lib/../lib64/libm.so)
attempt to open /opt/rocm/hcc/bin/../lib/libpthread.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libpthread.a failed
attempt to open /opt/rocm/hcc/lib/libpthread.so failed
attempt to open /opt/rocm/hcc/lib/libpthread.a failed
attempt to open /opt/rocm/hsa/lib/libpthread.so failed
attempt to open /opt/rocm/hsa/lib/libpthread.a failed
attempt to open /opt/rocm/lib/libpthread.so failed
attempt to open /opt/rocm/lib/libpthread.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libpthread.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libpthread.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libpthread.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libpthread.a failed
attempt to open /lib/../lib64/libpthread.so succeeded
opened script file /lib/../lib64/libpthread.so
opened script file /lib/../lib64/libpthread.so
attempt to open /lib64/libpthread.so.0 succeeded
/lib64/libpthread.so.0
attempt to open /usr/lib64/libpthread_nonshared.a succeeded
attempt to open /opt/rocm/hcc/bin/../lib/libhc_am.so succeeded
-lhc_am (/opt/rocm/hcc/bin/../lib/libhc_am.so)
attempt to open /opt/rocm/hcc/bin/../lib/libmcwamp.so succeeded
-lmcwamp (/opt/rocm/hcc/bin/../lib/libmcwamp.so)
attempt to open /opt/rocm/hcc/bin/../lib/libhsa-runtime64.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libhsa-runtime64.a failed
attempt to open /opt/rocm/hcc/lib/libhsa-runtime64.so failed
attempt to open /opt/rocm/hcc/lib/libhsa-runtime64.a failed
attempt to open /opt/rocm/hsa/lib/libhsa-runtime64.so failed
attempt to open /opt/rocm/hsa/lib/libhsa-runtime64.a failed
attempt to open /opt/rocm/lib/libhsa-runtime64.so succeeded
-lhsa-runtime64 (/opt/rocm/lib/libhsa-runtime64.so)
attempt to open /opt/rocm/hcc/bin/../lib/libhc_am.so succeeded
-lhc_am (/opt/rocm/hcc/bin/../lib/libhc_am.so)
attempt to open /opt/rocm/hcc/bin/../lib/libm.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libm.a failed
attempt to open /opt/rocm/hcc/lib/libm.so failed
attempt to open /opt/rocm/hcc/lib/libm.a failed
attempt to open /opt/rocm/hsa/lib/libm.so failed
attempt to open /opt/rocm/hsa/lib/libm.a failed
attempt to open /opt/rocm/lib/libm.so failed
attempt to open /opt/rocm/lib/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.a failed
attempt to open /lib/../lib64/libm.so succeeded
-lm (/lib/../lib64/libm.so)
attempt to open /tmp/hipInfo-f1864a.o succeeded
/tmp/hipInfo-f1864a.o
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++.a failed
attempt to open /opt/rocm/hcc/lib/libstdc++.so failed
attempt to open /opt/rocm/hcc/lib/libstdc++.a failed
attempt to open /opt/rocm/hsa/lib/libstdc++.so failed
attempt to open /opt/rocm/hsa/lib/libstdc++.a failed
attempt to open /opt/rocm/lib/libstdc++.so failed
attempt to open /opt/rocm/lib/libstdc++.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++.so succeeded
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++.so
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++.so
attempt to open /usr/lib64/libstdc++.so.6 succeeded
/usr/lib64/libstdc++.so.6
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libstdc++_nonshared.a failed
attempt to open /opt/rocm/hcc/lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/hcc/lib/libstdc++_nonshared.a failed
attempt to open /opt/rocm/hsa/lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/hsa/lib/libstdc++_nonshared.a failed
attempt to open /opt/rocm/lib/libstdc++_nonshared.so failed
attempt to open /opt/rocm/lib/libstdc++_nonshared.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++_nonshared.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libstdc++_nonshared.a succeeded
attempt to open /opt/rocm/hcc/bin/../lib/libm.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libm.a failed
attempt to open /opt/rocm/hcc/lib/libm.so failed
attempt to open /opt/rocm/hcc/lib/libm.a failed
attempt to open /opt/rocm/hsa/lib/libm.so failed
attempt to open /opt/rocm/hsa/lib/libm.a failed
attempt to open /opt/rocm/lib/libm.so failed
attempt to open /opt/rocm/lib/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libm.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libm.a failed
attempt to open /lib/../lib64/libm.so succeeded
-lm (/lib/../lib64/libm.so)
attempt to open /opt/rocm/hcc/bin/../lib/libgcc_s.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libgcc_s.a failed
attempt to open /opt/rocm/hcc/lib/libgcc_s.so failed
attempt to open /opt/rocm/hcc/lib/libgcc_s.a failed
attempt to open /opt/rocm/hsa/lib/libgcc_s.so failed
attempt to open /opt/rocm/hsa/lib/libgcc_s.a failed
attempt to open /opt/rocm/lib/libgcc_s.so failed
attempt to open /opt/rocm/lib/libgcc_s.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc_s.so succeeded
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc_s.so
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc_s.so
attempt to open /lib64/libgcc_s.so.1 succeeded
/lib64/libgcc_s.so.1
attempt to open libgcc.a failed
attempt to open /opt/rocm/hcc/bin/../lib/libgcc.a failed
attempt to open /opt/rocm/hcc/lib/libgcc.a failed
attempt to open /opt/rocm/hsa/lib/libgcc.a failed
attempt to open /opt/rocm/lib/libgcc.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc.a succeeded
attempt to open /opt/rocm/hcc/bin/../lib/libgcc.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libgcc.a failed
attempt to open /opt/rocm/hcc/lib/libgcc.so failed
attempt to open /opt/rocm/hcc/lib/libgcc.a failed
attempt to open /opt/rocm/hsa/lib/libgcc.so failed
attempt to open /opt/rocm/hsa/lib/libgcc.a failed
attempt to open /opt/rocm/lib/libgcc.so failed
attempt to open /opt/rocm/lib/libgcc.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc.a succeeded
attempt to open /opt/rocm/hcc/bin/../lib/libc.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libc.a failed
attempt to open /opt/rocm/hcc/lib/libc.so failed
attempt to open /opt/rocm/hcc/lib/libc.a failed
attempt to open /opt/rocm/hsa/lib/libc.so failed
attempt to open /opt/rocm/hsa/lib/libc.a failed
attempt to open /opt/rocm/lib/libc.so failed
attempt to open /opt/rocm/lib/libc.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libc.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libc.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libc.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/../../../../lib64/libc.a failed
attempt to open /lib/../lib64/libc.so succeeded
opened script file /lib/../lib64/libc.so
opened script file /lib/../lib64/libc.so
attempt to open /lib64/libc.so.6 succeeded
/lib64/libc.so.6
attempt to open /usr/lib64/libc_nonshared.a succeeded
(/usr/lib64/libc_nonshared.a)elf-init.oS
attempt to open /lib64/ld-linux-x86-64.so.2 succeeded
/lib64/ld-linux-x86-64.so.2
/lib64/ld-linux-x86-64.so.2
attempt to open /opt/rocm/hcc/bin/../lib/libgcc_s.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libgcc_s.a failed
attempt to open /opt/rocm/hcc/lib/libgcc_s.so failed
attempt to open /opt/rocm/hcc/lib/libgcc_s.a failed
attempt to open /opt/rocm/hsa/lib/libgcc_s.so failed
attempt to open /opt/rocm/hsa/lib/libgcc_s.a failed
attempt to open /opt/rocm/lib/libgcc_s.so failed
attempt to open /opt/rocm/lib/libgcc_s.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc_s.so succeeded
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc_s.so
opened script file /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc_s.so
attempt to open /lib64/libgcc_s.so.1 succeeded
/lib64/libgcc_s.so.1
attempt to open libgcc.a failed
attempt to open /opt/rocm/hcc/bin/../lib/libgcc.a failed
attempt to open /opt/rocm/hcc/lib/libgcc.a failed
attempt to open /opt/rocm/hsa/lib/libgcc.a failed
attempt to open /opt/rocm/lib/libgcc.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc.a succeeded
attempt to open /opt/rocm/hcc/bin/../lib/libgcc.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libgcc.a failed
attempt to open /opt/rocm/hcc/lib/libgcc.so failed
attempt to open /opt/rocm/hcc/lib/libgcc.a failed
attempt to open /opt/rocm/hsa/lib/libgcc.so failed
attempt to open /opt/rocm/hsa/lib/libgcc.a failed
attempt to open /opt/rocm/lib/libgcc.so failed
attempt to open /opt/rocm/lib/libgcc.a failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc.so failed
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/libgcc.a succeeded
attempt to open /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtend.o succeeded
/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtend.o
attempt to open /lib/../lib64/crtn.o succeeded
/lib/../lib64/crtn.o
attempt to open /opt/rocm/hcc/bin/../lib/libclang_rt.builtins-x86_64.so failed
attempt to open /opt/rocm/hcc/bin/../lib/libclang_rt.builtins-x86_64.a succeeded
ld-linux-x86-64.so.2 needed by /usr/lib64/libstdc++.so.6
found ld-linux-x86-64.so.2 at /lib64/ld-linux-x86-64.so.2
libamd_comgr.so.1 needed by /opt/rocm/hip/lib/libhip_hcc.so
found libamd_comgr.so.1 at //opt/rocm/lib/libamd_comgr.so.1
libhsakmt.so.1 needed by /opt/rocm/lib/libhsa-runtime64.so
found libhsakmt.so.1 at //opt/rocm/lib64/libhsakmt.so.1
libz.so.1 needed by /opt/rocm/lib/libhsa-runtime64.so
found libz.so.1 at //usr/lib64/libz.so.1
librt.so.1 needed by /opt/rocm/lib/libhsa-runtime64.so
found librt.so.1 at //usr/lib64/librt.so.1
libtinfo.so.5 needed by //opt/rocm/lib/libamd_comgr.so.1
found libtinfo.so.5 at //usr/lib64/libtinfo.so.5
libnuma.so.1 needed by //opt/rocm/lib64/libhsakmt.so.1
found libnuma.so.1 at //usr/lib64/libnuma.so.1
libpci.so.3 needed by //opt/rocm/lib64/libhsakmt.so.1
found libpci.so.3 at //usr/lib64/libpci.so.3
libresolv.so.2 needed by //usr/lib64/libpci.so.3
found libresolv.so.2 at //usr/lib64/libresolv.so.2
/opt/rocm/hcc/bin/../lib/libhc_am.so: undefined reference to `hsa_amd_memory_lock_to_pool@ROCR_1'
clang-10: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [hipInfo] Error 1
```
</details>

Any ideas what is wrong? @jlgreathouse ?

---

## 评论 (9 条)

### 评论 #1 — jcdutton (2020-02-14T18:40:44Z)

You need to install (the small binary blob bit of ROCM):
libhsa-runtime64.so



---

### 评论 #2 — akostadinov (2020-02-17T13:51:03Z)

@jcdutton , thanks a lot for the info! I'll try as soon as I get back home next week.

In the past that was not needed and I don't see this in the installation guide? Do you know how to do it? I'll check the RPM repo but asking in case it is somewhere else.

---

### 评论 #3 — akostadinov (2020-02-21T21:09:27Z)

@jcdutton , I see the following line in log above:
```
attempt to open /opt/rocm/lib/libhsa-runtime64.so succeeded
-lhsa-runtime64 (/opt/rocm/lib/libhsa-runtime64.so)
```
The file is there. Or is there another file to be installed? I can't see any other package providing a library with that name. Could you point me at proper package or download location?

Update: I have manually linked `/opt/rocm/hsa/lib/libhsa-runtime64.so` to `/opt/rocm/hsa/lib/libhsa-runtime64.so.1` but this doesn't seem to make any difference. The file was already there. So what am I missing?

---

### 评论 #4 — pramenku (2020-02-29T10:04:10Z)

> 
> 
> @jcdutton , I see the following line in log above:
> 
> ```
> attempt to open /opt/rocm/lib/libhsa-runtime64.so succeeded
> -lhsa-runtime64 (/opt/rocm/lib/libhsa-runtime64.so)
> ```
> 
> The file is there. Or is there another file to be installed? I can't see any other package providing a library with that name. Could you point me at proper package or download location?
> 
> Update: I have manually linked `/opt/rocm/hsa/lib/libhsa-runtime64.so` to `/opt/rocm/hsa/lib/libhsa-runtime64.so.1` but this doesn't seem to make any difference. The file was already there. So what am I missing?

Can you please give a try with ROCm3.1.  Issue should not be seen with 3.1.
Clean uninstall  older rocm driver and make sure all libs/headers are removed from /opt/rocm.
After that freshly install ROCm3.1


---

### 评论 #5 — akostadinov (2020-03-18T12:22:51Z)

@pramenku , huh busy days, I have installed 3.1. First I tried direct update and it all went into a mess. Then I removed all RPMs from repo, removed manually dkms modules, updated OS, rebooted and tried again.

Result was some errors even running `rocminfo`. But this time it was easy to track down to missing files. With `rpm -V` I figured out that perhaps half packages reported to be installed but none of their files actually existed. doing `yum reinstall` on all packages fixed the issue and now `rocm-smi`, `rocminfo` and `clinfo` all work.

One other detail is that `rocminfo` only works ar `root` now. There is no `render` user. My user already has group `video`. So I need to debug this.

Anyway, there seems to be a serious issue with the RPMs. I have never seen installing RPMs to result in missing files. My guess is that my previous problem was related to this but I could not identify the missing files then. And now this change to have `rocm-version` directory does not make any sense to me. Does AMD want to support multiple versions of the stack simultaneously on one machine?

I'm a little bit frustrated by lack of stability of drivers for so long. And so little software supported. Still software expects the proprietary drivers. I think AMD needs to become more committed to their OSS story and this will focus resources instead of spreading effort and providing this very disheartening user experience. But who am I to tell them. Maybe I need to donate the card to some gamer as it is a shame to waste this nice card :)

I guess I need to finish my rant and go check if I can get things I'm interested atm (folding@home for corona) running. 

---

### 评论 #6 — akostadinov (2020-03-18T12:30:15Z)

What I see as non-root is:
```
hsa api call failure at: /data/jenkins_workspace/centos_pipeline_job_3.1/rocm-rel-3.1/rocm-3.1-44-20200302/centos/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

I figured out rw access to `/dev/kfd` is needed. But it was owned by `root.root` and permissions `600`. I needed to make it `660` and be owned by group `video` to get `rocminfo` working.

My assumption is some configuration is missing to make the file with proper permissions.

Anybody knows what in the RPMs needs to be fixed?

---

### 评论 #7 — akostadinov (2020-03-18T13:09:14Z)

Needed to set `kfd` udev rules. I had this file from the past. Not sure if I created or was part of earlier ROCm versions. But it appeared to be slightly incorrect. Anyway, this fixed the issue with `kfd` file permissions. I don't know why RPMs do not set such rule by default.

```
$ sudo udevadm info -a /dev/kfd
$ cat /etc/udev/rules.d/kfd.rules 
KERNEL=="kfd", GROUP="video", MODE="0660"
$ sudo restorecon /etc/udev/rules.d/kfd.rules
```

---

### 评论 #8 — akostadinov (2020-03-23T21:19:56Z)

Ok, there is some issue with the RPMs installation. Also mode and ownership of `kfd` needs to be manually setup. But I'd rather close this issue and see how future versions will come. Hopefully RHEL8 will be supported soon.

---

### 评论 #9 — akostadinov (2020-04-07T14:32:21Z)

Just FYI no RPM issues I hit with 3.3. My custom `kfd.rules` has been removed though and default permissions for `/dev/kfd` are `666`. IMO they should be `660`. At least group is correct `video`.

---
