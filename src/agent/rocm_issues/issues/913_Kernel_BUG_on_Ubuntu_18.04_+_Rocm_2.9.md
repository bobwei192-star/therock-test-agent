# Kernel BUG on Ubuntu 18.04 + Rocm 2.9

> **Issue #913**
> **状态**: closed
> **创建时间**: 2019-10-18T21:23:58Z
> **更新时间**: 2021-01-07T05:27:03Z
> **关闭时间**: 2021-01-07T05:27:02Z
> **作者**: evilbulgarian
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/913

## 描述

etherminer works fine up until exit. same with /opt/rocm/opencl/bin/x86_64/clinfo which at the end of its run also locks up and reboot is required.

```script
/opt/rocm/bin/rocminfo:

ROCk module is loaded
vladi is member of video group
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
  Name:                    Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
  Marketing Name:          Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
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
  Max Clock Freq. (MHz):   2900                               
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
      Size:                    8096436(0x7b8ab4) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8096436(0x7b8ab4) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
  Marketing Name:          Hawaii PRO [Radeon R9 290/390]     
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
  Chip ID:                 26545(0x67b1)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1000                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            40                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
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

/opt/rocm/opencl/bin/x86_64/clinfo:
Number of platforms:                             2                   
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 1.2 CUDA 10.2.120
  Platform Name:                                 NVIDIA CUDA
  Platform Vendor:                               NVIDIA Corporation
  Platform Extensions:                           cl_khr_global_int32_base_atomics cl_kh
r_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_exte
nded_atomics cl_khr_fp64 cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_
nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts cl
_nv_create_buffer                                                                      
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:                                 AMD Accelerated Parallel Processing     Platform Vendor:                               Advanced Micro Devices, Inc.            Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices
  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Hawaii PRO [Radeon R9 290/390]
  Device Topology:                               PCI[ B#1, D#0, F#0 ]
  Max compute units:                             40
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
  Max clock frequency:                           1000Mhz
  Address bits:                                  64
  Max memory allocation:                         3650722201
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26545
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128                           [25/257]
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            4294967296
  Constant buffer size:                          3650722201
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          3650722201
  Max global variable size:                      3650722201
  Max global variable preferred total size:      4294967296
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
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7f874d346d30
  Name:                                          gfx701
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0 
  Driver version:                                2982.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2 
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_a
tomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_loca
l_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr
_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_dev
ice_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_kh
r_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

BUG:

[ 2395.761094] BUG: unable to handle kernel NULL pointer dereference at 0000000000000038
[ 2395.761207] IP: amdgpu_ib_schedule+0x54/0x5b0 [amdgpu]
[ 2395.761212] PGD 0 P4D 0 
[ 2395.761219] Oops: 0000 [#1] SMP PTI
[ 2395.761223] Modules linked in: binfmt_misc ccm nls_iso8859_1 nvidia_uvm(OE) intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm_intel kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc nvidia_drm(POE) nvidia_modeset(POE) arc4 aesni_intel aes_x86_64 crypto_simd glue_helper cryptd intel_cstate nvidia(POE) intel_rapl_perf snd_seq_midi snd_seq_midi_event amdgpu(OE) snd_rawmidi serio_raw snd_hda_codec_hdmi snd_hda_intel rt2800usb rt2x00usb rt2800lib snd_hda_codec snd_hda_core snd_hwdep rt2x00lib snd_seq mac80211 snd_pcm amdttm(OE) ipmi_devintf snd_seq_device ipmi_msghandler snd_timer cfg80211 input_leds amdkcl(OE) i915 amd_sched(OE) mei_me amd_iommu_v2 snd drm_kms_helper mei drm soundcore i2c_algo_bit fb_sys_fops syscopyarea sysfillrect sysimgblt shpchp video acpi_pad mac_hid
[ 2395.761300]  sch_fq_codel parport_pc ppdev lp parport ip_tables x_tables autofs4 hid_generic usbhid hid psmouse r8169 mii ahci libahci
[ 2395.761322] CPU: 1 PID: 1573 Comm: ethminer Tainted: P           OE    4.15.0-65-generic #74-Ubuntu
[ 2395.761324] Hardware name: BIOSTAR Group TB250-BTC/TB250-BTC, BIOS 5.12 04/13/2018
[ 2395.761419] RIP: 0010:amdgpu_ib_schedule+0x54/0x5b0 [amdgpu]
[ 2395.761422] RSP: 0018:ffffbc2304e4ba20 EFLAGS: 00010202
[ 2395.761427] RAX: 0000000000000001 RBX: ffff9f7bf91a1800 RCX: 0000000000000000
[ 2395.761430] RDX: 0000000000000000 RSI: 0000000000000001 RDI: ffff9f7c4dec8028
[ 2395.761433] RBP: ffffbc2304e4ba88 R08: ffffbc2304e4baa8 R09: ffff9f7c56002f00
[ 2395.761436] R10: ffffbc2304e4bad0 R11: 0000000000002000 R12: 0000000000000001
[ 2395.761438] R13: 0000000000000008 R14: ffff9f7c4dec8028 R15: 0000000000ffd000
[ 2395.761442] FS:  00007f544366b700(0000) GS:ffff9f7c5ed00000(0000) knlGS:0000000000000000
[ 2395.761445] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 2395.761448] CR2: 0000000000000038 CR3: 00000001dbe0a005 CR4: 00000000003606e0
[ 2395.761451] Call Trace:
[ 2395.761461]  ? __kmalloc+0x1e7/0x220
[ 2395.761591]  amdgpu_amdkfd_submit_ib+0xd9/0x170 [amdgpu]
[ 2395.761720]  deallocate_vmid.isra.16+0xff/0x110 [amdgpu]
[ 2395.761848]  destroy_queue_nocpsch_locked+0x17b/0x220 [amdgpu]
[ 2395.761971]  process_termination_nocpsch+0x6c/0x140 [amdgpu]
[ 2395.762092]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
[ 2395.762214]  kfd_process_notifier_release+0x18c/0x220 [amdgpu]
[ 2395.762220]  __mmu_notifier_release+0x47/0xd0
[ 2395.762225]  exit_mmap+0x161/0x1c0
[ 2395.762230]  ? kmem_cache_free+0x1b3/0x1e0
[ 2395.762235]  ? kmem_cache_free+0x1b3/0x1e0
[ 2395.762240]  ? exit_robust_list+0x5c/0x130
[ 2395.762247]  mmput+0x57/0x140
[ 2395.762252]  do_exit+0x2a0/0xbc0
[ 2395.762259]  ? __fput+0x193/0x220
[ 2395.762264]  do_group_exit+0x43/0xb0
[ 2395.762270]  get_signal+0x142/0x7a0
[ 2395.762278]  do_signal+0x37/0x720
[ 2395.762282]  ? put_unused_fd+0x31/0x80
[ 2395.762288]  ? SYSC_accept4+0x195/0x210
[ 2395.762293]  ? handle_mm_fault+0xb1/0x210
[ 2395.762300]  ? __do_page_fault+0x2a1/0x4b0
[ 2395.762307]  exit_to_usermode_loop+0x73/0xd0
[ 2395.762312]  do_syscall_64+0x121/0x130
[ 2395.762318]  entry_SYSCALL_64_after_hwframe+0x3d/0xa2
[ 2395.762322] RIP: 0033:0x7f54509dd237
[ 2395.762325] RSP: 002b:00007f544366ad30 EFLAGS: 00000293 ORIG_RAX: 0000000000000120
[ 2395.762330] RAX: fffffffffffffe00 RBX: 0000000000000019 RCX: 00007f54509dd237
[ 2395.762333] RDX: 00007f544366ad78 RSI: 00007f544366ad80 RDI: 0000000000000019
[ 2395.762336] RBP: 00007f544366ad80 R08: 0000000000000000 R09: 00007f544366ae10
[ 2395.762339] R10: 0000000000080000 R11: 0000000000000293 R12: 00007f544366ad78
[ 2395.762341] R13: 0000000000080000 R14: 0000000001cd06f0 R15: 00007ffed6f28480
[ 2395.762345] Code: 89 45 a0 48 89 cb 48 89 55 b0 41 89 f4 49 89 fe 0f b6 87 1c 02 00 00 0f 84 5a 03 00 00 48 8b 49 70 48 8b 53 10 84 c0 48 89 4d a8 <48> 8b 4a 38 48 89 4d c0 0f 84 ff 04 00 00 48 83 7d a8 00 74 0e 
[ 2395.762505] RIP: amdgpu_ib_schedule+0x54/0x5b0 [amdgpu] RSP: ffffbc2304e4ba20
[ 2395.762508] CR2: 0000000000000038
[ 2395.762512] ---[ end trace b0b557149eafae35 ]---
[ 2395.762515] Fixing recursive fault but reboot is needed!
```

---

## 评论 (2 条)

### 评论 #1 — JMadgwick (2019-10-19T19:29:46Z)

This bug is probably one of the known Hawaii bugs. Despite being listed on the Readme as supported Hawaii has not been working since 1.9.
As you want to use OpenCL, install [AMDGPU-PRO](https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux) instead. [AMDGPU-PRO](https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux) works correctly for OpenCL, I tested it myself recently. Make sure you fully uninstall ROCm first then install [AMDGPU-PRO](https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux).

---

### 评论 #2 — ROCmSupport (2021-01-07T05:27:02Z)

Hi All,
Hawaii is no more officially ROCm supported device. Please check for more details:
[https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Thank you.

---
