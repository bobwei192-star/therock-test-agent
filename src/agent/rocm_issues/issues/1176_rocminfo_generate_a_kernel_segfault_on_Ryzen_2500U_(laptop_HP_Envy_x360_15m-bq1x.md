# rocminfo generate a kernel segfault on Ryzen 2500U (laptop HP Envy x360 15m-bq1xx)

> **Issue #1176**
> **状态**: closed
> **创建时间**: 2020-07-10T01:48:40Z
> **更新时间**: 2020-12-17T03:30:36Z
> **关闭时间**: 2020-12-17T03:30:36Z
> **作者**: padonion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1176

## 描述

Hello everybody,
it's been a little while since last time I tried to play with my laptop and OpenCL.

I recently updated my OS to Ubuntu 20.04 and wanted to give a new try to ROCm (last try was not really successful but maturity takes time).
I added the repos for Ubuntu as mentioned on the ROCm documentation and installed only `rocm-dev`.

My user belongs to `render` group and the same for `/dev/kfd`:
```
[ padonion: ~ ]$ groups
padonion adm cdrom sudo dip video plugdev render lpadmin lxd sambashare
[ padonion: ~ ]$ ll /dev/kfd
crw-rw---- 1 root render 237, 0 Jul  9 18:16 /dev/kfd
```

If I try `clinfo`, I get no device:
```
 padonion: ~ ]$ /opt/rocm/opencl/bin/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3137.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```

If I try `rocminfo`, I create a segfault in the kernel:
```
[ padonion: ~ ]$ /opt/rocm/bin/rocminfo --help
ROCk module is loaded
Unable to open /dev/kfd read-write: Operation not permitted
padonion is member of render group
```

Same with `gdb`:
```
[ padonion: ~ ]$ gdb /opt/rocm/bin/rocminfo 
GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /opt/rocm/bin/rocminfo...
(No debugging symbols found in /opt/rocm/bin/rocminfo)
(gdb) run
Starting program: /opt/rocm-3.5.0/bin/rocminfo 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[Detaching after vfork from child process 4796]
ROCk module is loaded
Unable to open /dev/kfd read-write: Operation not permitted
padonion is member of render group
[New Thread 0x7ffff74a3700 (LWP 4799)]
[Thread 0x7ffff74f2780 (LWP 4792) exited]
```

And the trace in the kernel:
```
[...]
[  583.250290] BUG: unable to handle page fault for address: 0000000000001000
[  583.250294] #PF: supervisor write access in kernel mode
[  583.250295] #PF: error_code(0x0002) - not-present page
[  583.250296] PGD 31727a067 P4D 31727a067 PUD 3b7810067 PMD 0 
[  583.250299] Oops: 0002 [#1] SMP NOPTI
[  583.250301] CPU: 3 PID: 4792 Comm: rocminfo Not tainted 5.4.0-40-generic #44-Ubuntu
[  583.250302] Hardware name: HP HP ENVY x360 Convertible 15m-bq1xx/83C6, BIOS F.21 04/29/2019
[  583.250365] RIP: 0010:set_trap_handler+0x1d/0x50 [amdgpu]
[  583.250367] Code: 89 ef e8 56 ee cd c2 e9 06 ff ff ff 90 0f 1f 44 00 00 55 48 8b 87 20 01 00 00 80 b8 f8 01 00 00 00 48 89 e5 74 16 48 8b 46 78 <48> 89 90 00 10 00 00 48 89 88 08 10 00 00 31 c0 5d c3 31 c0 48 89
[  583.250368] RSP: 0018:ffffb75b42e1fd48 EFLAGS: 00010202
[  583.250370] RAX: 0000000000000000 RBX: ffffb75b42e1fda8 RCX: 00007ffff7cf9000
[  583.250371] RDX: 00007ffff7cf8000 RSI: ffff92e4b9ec6820 RDI: ffff92e4f985a800
[  583.250372] RBP: ffffb75b42e1fd48 R08: ffffb75b42e1fd88 R09: ffff92e50b170400
[  583.250372] R10: ffff92e5040e44c0 R11: 0000000000000000 R12: ffff92e4fc528000
[  583.250373] R13: ffff92e50b170400 R14: ffff92e50b170440 R15: 0000000040184b13
[  583.250375] FS:  00007ffff74f2780(0000) GS:ffff92e50f0c0000(0000) knlGS:0000000000000000
[  583.250376] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  583.250377] CR2: 0000000000001000 CR3: 000000038e618000 CR4: 00000000003406e0
[  583.250378] Call Trace:
[  583.250433]  kfd_ioctl_set_trap_handler+0x61/0xa0 [amdgpu]
[  583.250485]  kfd_ioctl+0x10e/0x410 [amdgpu]
[  583.250537]  ? kfd_ioctl_import_dmabuf+0x120/0x120 [amdgpu]
[  583.250541]  do_vfs_ioctl+0x407/0x670
[  583.250545]  ? do_user_addr_fault+0x216/0x450
[  583.250546]  ksys_ioctl+0x67/0x90
[  583.250548]  __x64_sys_ioctl+0x1a/0x20
[  583.250550]  do_syscall_64+0x57/0x190
[  583.250554]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[  583.250555] RIP: 0033:0x7ffff79fb37b
[  583.250557] Code: 0f 1e fa 48 8b 05 15 3b 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d e5 3a 0d 00 f7 d8 64 89 01 48
[  583.250558] RSP: 002b:00007fffffffdba8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[  583.250559] RAX: ffffffffffffffda RBX: 00007ffff7cf8000 RCX: 00007ffff79fb37b
[  583.250560] RDX: 00007fffffffdc00 RSI: 0000000040184b13 RDI: 0000000000000004
[  583.250561] RBP: 00007fffffffdc00 R08: 0000000000002000 R09: 0000000000000000
[  583.250562] R10: 00007ffff7fef1e0 R11: 0000000000000246 R12: 0000000040184b13
[  583.250563] R13: 0000000000000004 R14: 0000000000000000 R15: 0000000000000000
[  583.250564] Modules linked in: ccm rfcomm cmac algif_hash algif_skcipher af_alg bnep nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg edac_mce_amd snd_hda_codec snd_hda_core snd_hwdep snd_pcm ccp kvm snd_seq_midi snd_seq_midi_event rtwpci snd_rawmidi btusb hp_wmi uvcvideo hid_sensor_gyro_3d rtw88 hid_sensor_accel_3d hid_sensor_incl_3d btrtl hid_sensor_rotation hid_sensor_magn_3d btbcm videobuf2_vmalloc btintel videobuf2_memops hid_sensor_trigger joydev videobuf2_v4l2 industrialio_triggered_buffer input_leds kfifo_buf serio_raw sparse_keymap wmi_bmof hid_multitouch snd_seq videobuf2_common k10temp mac80211 hid_sensor_iio_common bluetooth industrialio videodev snd_seq_device snd_timer ecdh_generic ecc mc snd soundcore cfg80211 rtsx_pci_ms libarc4 memstick hp_accel lis3lv02d hp_wireless input_polldev mac_hid nf_log_ipv6 ip6t_REJECT nf_reject_ipv6 xt_hl ip6t_rt nf_log_ipv4 nf_log_common ipt_REJECT nf_reject_ipv4 xt_LOG
[  583.250595]  xt_limit xt_addrtype xt_tcpudp xt_conntrack nf_conntrack nf_defrag_ipv6 sch_fq_codel nf_defrag_ipv4 libcrc32c parport_pc ip6table_filter ip6_tables ppdev iptable_filter bpfilter lp parport ip_tables x_tables autofs4 dm_crypt hid_sensor_custom hid_logitech_hidpp hid_sensor_hub hid_logitech_dj usbhid amdgpu crct10dif_pclmul crc32_pclmul ghash_clmulni_intel rtsx_pci_sdmmc hid_generic amd_iommu_v2 aesni_intel gpu_sched i2c_algo_bit ttm crypto_simd cryptd drm_kms_helper glue_helper syscopyarea sysfillrect psmouse sysimgblt ahci nvme fb_sys_fops libahci i2c_piix4 rtsx_pci drm nvme_core wmi i2c_hid video i2c_scmi hid
[  583.250619] CR2: 0000000000001000
[  583.250620] ---[ end trace deda9912ff428391 ]---
[  583.250674] RIP: 0010:set_trap_handler+0x1d/0x50 [amdgpu]
[  583.250676] Code: 89 ef e8 56 ee cd c2 e9 06 ff ff ff 90 0f 1f 44 00 00 55 48 8b 87 20 01 00 00 80 b8 f8 01 00 00 00 48 89 e5 74 16 48 8b 46 78 <48> 89 90 00 10 00 00 48 89 88 08 10 00 00 31 c0 5d c3 31 c0 48 89
[  583.250677] RSP: 0018:ffffb75b42e1fd48 EFLAGS: 00010202
[  583.250678] RAX: 0000000000000000 RBX: ffffb75b42e1fda8 RCX: 00007ffff7cf9000
[  583.250679] RDX: 00007ffff7cf8000 RSI: ffff92e4b9ec6820 RDI: ffff92e4f985a800
[  583.250679] RBP: ffffb75b42e1fd48 R08: ffffb75b42e1fd88 R09: ffff92e50b170400
[  583.250680] R10: ffff92e5040e44c0 R11: 0000000000000000 R12: ffff92e4fc528000
[  583.250681] R13: ffff92e50b170400 R14: ffff92e50b170440 R15: 0000000040184b13
[  583.250682] FS:  00007ffff74f2780(0000) GS:ffff92e50f0c0000(0000) knlGS:0000000000000000
[  583.250683] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  583.250684] CR2: 0000000000001000 CR3: 000000038e618000 CR4: 00000000003406e0
[...]
```

Does somebody experienced something similar?
How can I help to have this platform supported?

Thank you all for this tremendous work on ROCm!
Christophe Kumsta.


---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2020-12-16T11:53:35Z)

Thanks @padonion for reaching out.
Recommend to try with the latest ROCm 3.10 and update me asap.
Thank you.

---

### 评论 #2 — padonion (2020-12-17T02:22:33Z)

Hello,
rocm has been de-installed / installed from scratch (3.10 requires it)
and OpenCL is working on Ryzen 2500U!
To mention, I got rid of unsupported kernel (unofficial ppa with recent kernels) as it breaks the compilation of rocm dkm.

Thanks very much to all team!
I will play around now.

This issue can be closed.

```
ROCk module is loaded
Able to open /dev/kfd read-write
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
  Name:                    AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
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
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16092468(0xf58d34) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16092468(0xf58d34) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series]
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
  Chip ID:                 5597(0x15dd)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1100                               
  BDFID:                   1024                               
  Internal Node ID:        1                                  
  Compute Unit:            8                                  
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
      Size:                    262144(0x40000) KB                 
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
      Name:                    amdgcn-amd-amdhsa--gfx902          
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
And opencl:
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3212.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series]
  Device Topology:				 PCI[ B#4, D#0, F#0 ]
  Max compute units:				 8
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
  Max clock frequency:				 1100Mhz
  Address bits:					 64
  Max memory allocation:			 228170136
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 8192
  Max samplers within kernel:			 5597
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 268435456
  Constant buffer size:				 228170136
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 228170136
  Max global variable size:			 228170136
  Max global variable preferred total size:	 268435456
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
  Platform ID:					 0x7f6437f81cf0
  Name:						 gfx902
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3212.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```


---

### 评论 #3 — padonion (2020-12-17T02:25:14Z)

Even HIP is working (that's new !)

```
➜ /opt/rocm/bin/hipconfig --full                                                              (base) 
HIP version  : 3.10.20465-f9876b8d

== hipconfig
HIP_PATH     : /opt/rocm-3.10.0/hip
ROCM_PATH    : /opt/rocm-3.10.0
HIP_COMPILER : clang
HIP_PLATFORM : hcc
HIP_RUNTIME  : ROCclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm-3.10.0/hip/include -I/opt/rocm-3.10.0/llvm/bin/../lib/clang/12.0.0 -I/opt/rocm-3.10.0/hsa/include -D__HIP_ROCclr__

== hip-clang
HSA_PATH         : /opt/rocm-3.10.0/hsa
HIP_CLANG_PATH   : /opt/rocm-3.10.0/llvm/bin
clang version 12.0.0 (/src/external/llvm-project/clang 60f39e2924d51c1e8606f2135f95e9047fb1da5d)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-3.10.0/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 12.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver1

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
-D__HIP_ROCclr__ -std=c++11 -isystem /opt/rocm-3.10.0/llvm/lib/clang/12.0.0/include/.. -isystem /opt/rocm-3.10.0/hsa/include -D__HIP_ROCclr__ -isystem /opt/rocm-3.10.0/hip/include -O3
hip-clang-ldflags  : Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
 -L/opt/rocm-3.10.0/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm

=== Environment Variables
PATH=/home/padonion/miniconda3/bin:/home/padonion/miniconda3/condabin:/home/padonion/.cargo/bin:/home/padonion/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

== Linux Kernel
Hostname     : padonion-hp
Linux padonion-hp 5.4.0-58-generic #64-Ubuntu SMP Wed Dec 9 08:16:25 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
```

---

### 评论 #4 — ROCmSupport (2020-12-17T03:30:36Z)

Thanks @padonion for the update.
Am closing this.

---
