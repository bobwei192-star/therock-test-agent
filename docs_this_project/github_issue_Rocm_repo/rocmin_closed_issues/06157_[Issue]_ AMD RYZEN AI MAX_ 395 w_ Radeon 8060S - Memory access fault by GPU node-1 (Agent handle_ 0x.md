# [Issue]: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S - Memory access fault by GPU node-1 (Agent handle: 0x58935a90) on address 0x7fbe6a804000. Reason: Page not present or supervisor privilege.

- **Issue #:** 6157
- **State:** closed
- **Created:** 2026-04-17T11:58:18Z
- **Updated:** 2026-06-09T17:18:41Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6157

### Problem Description

Installed vllm 0.19.0+rocm721, installed all the dependencies one by one. When running vllm serve, it crashes after loading the model.

vllm serve amd/gpt-oss-120b-w-mxfp4-a-fp8 --max-model-len 65332 --gpu-memory-utilization 0.8
...
(EngineCore pid=5379) [QUARK-INFO]: C++ kernel build directory: /home/ross/.cache/torch_extensions/py312_cpu/kernel_ext. First-time compilation may take a few minutes... Building for architectures PYTORCH_ROCM_ARCH='gfx1151'.
(EngineCore pid=5379) Successfully preprocessed all matching files.
(EngineCore pid=5379)
(EngineCore pid=5379) [QUARK-INFO]: C++ kernel compilation is already complete. Ending the C++ kernel compilation check. Total time: 0.8475 seconds
Memory access fault by GPU node-1 (Agent handle: 0x58935a90) on address 0x7fbe6a804000. Reason: Page not present or supervisor privilege.
HW Exception by GPU node-1 (Agent handle: 0x5b522e50) reason :GPU Hang
./start.sh: line 22:  5255 Aborted                    (core dumped) vllm serve amd/gpt-oss-120b-w-mxfp4-a-fp8 --max-model-len 65332 --gpu-memory-utilization 0.8
(vllm) [ross@cachyos vllm]$ /home/ross/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

Tried downgrading the linux-firmware-amdgpu to 20251111, added amdgpu.cwsr_enable=0 to kernel params, all not working.

The firmware details,
sudo cat /sys/kernel/debug/dri/1/amdgpu_firmware_info
`VCE feature version: 0, firmware version: 0x00000000
UVD feature version: 0, firmware version: 0x00000000
MC feature version: 0, firmware version: 0x00000000
ME feature version: 35, firmware version: 0x00000020
PFP feature version: 35, firmware version: 0x00000031
CE feature version: 0, firmware version: 0x00000000
RLC feature version: 1, firmware version: 0x11530506
RLC SRLC feature version: 0, firmware version: 0x00000000
RLC SRLG feature version: 0, firmware version: 0x00000000
RLC SRLS feature version: 0, firmware version: 0x00000000
RLCP feature version: 1, firmware version: 0x11530506
RLCV feature version: 0, firmware version: 0x00000000
MEC feature version: 35, firmware version: 0x00000022
IMU feature version: 0, firmware version: 0x0b352300
SOS feature version: 0, firmware version: 0x00000000
ASD feature version: 553648393, firmware version: 0x21000109
TA XGMI feature version: 0x00000000, firmware version: 0x00000000
TA RAS feature version: 0x00000000, firmware version: 0x00000000
TA HDCP feature version: 0x00000000, firmware version: 0x1700004d
TA DTM feature version: 0x00000000, firmware version: 0x1200001d
TA RAP feature version: 0x00000000, firmware version: 0x00000000
TA SECUREDISPLAY feature version: 0x00000000, firmware version: 0x00000000
SMC feature version: 0, program: 10, firmware version: 0x0a640600 (100.6.0)
SDMA0 feature version: 60, firmware version: 0x00000012
VCN feature version: 0, firmware version: 0x09118010
DMCU feature version: 0, firmware version: 0x00000000
DMCUB feature version: 0, firmware version: 0x09003e00
TOC feature version: 0, firmware version: 0x0000000b
MES_KIQ feature version: 6, firmware version: 0x0000006f
MES feature version: 1, firmware version: 0x00000086
VPE feature version: 60, firmware version: 0x00000017
VBIOS version: 113-STRXLGEN-001`

output of uname -a,
uname -a
Linux cachyos 6.19.11-1-cachyos-deckify #1 SMP PREEMPT_DYNAMIC Wed, 08 Apr 2026 14:51:52 +0000 x86_64 GNU/Linux

All firmwares,
pacman -Q | grep linux-firmware
linux-firmware 1:20260309-1
linux-firmware-amdgpu 1:20260309-1
linux-firmware-atheros 1:20260309-1
linux-firmware-broadcom 1:20260309-1
linux-firmware-cirrus 1:20260309-1
linux-firmware-intel 1:20260309-1
linux-firmware-mediatek 1:20260309-1
linux-firmware-nvidia 1:20260309-1
linux-firmware-other 1:20260309-1
linux-firmware-radeon 1:20260309-1
linux-firmware-realtek 1:20260309-1
linux-firmware-whence 1:20260309-1




### Operating System

CachyOS Linux

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

Radeon 8060S

### ROCm Version

7.2.1-2.1

### ROCm Component

_No response_

### Steps to Reproduce

Installed vllm 0.19.0+rocm721, installed all the dependencies one by one. 

Then run,

vllm serve amd/gpt-oss-120b-w-mxfp4-a-fp8 --max-model-len 65332 --gpu-memory-utilization 0.8


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.18
Runtime Ext Version:     1.15
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Uuid:                    CPU-XX
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
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
    L1:                      49152(0xc000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   5187
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            32
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    97971060(0x5d6eb74) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    97971060(0x5d6eb74) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    97971060(0x5d6eb74) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    97971060(0x5d6eb74) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1151
  Uuid:                    GPU-XX
  Marketing Name:          Radeon 8060S Graphics
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
    L1:                      32(0x20) KB
    L2:                      2048(0x800) KB
    L3:                      32768(0x8000) KB
  Chip ID:                 5510(0x1586)
  ASIC Revision:           0(0x0)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   2900
  BDFID:                   25856
  Internal Node ID:        1
  Compute Unit:            40
  SIMDs per CU:            2
  Shader Engines:          2
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:       APU
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
    x                        2147483647(0x7fffffff)
    y                        65535(0xffff)
    z                        65535(0xffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 34
  SDMA engine uCode::      18
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    92274688(0x5800000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    92274688(0x5800000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1151
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
        x                        2147483647(0x7fffffff)
        y                        65535(0xffff)
        z                        65535(0xffff)
      FBarrier Max Size:       32
    ISA 2
      Name:                    amdgcn-amd-amdhsa--gfx11-generic
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
        x                        2147483647(0x7fffffff)
        y                        65535(0xffff)
        z                        65535(0xffff)
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    aie2p
  Uuid:                    AIE-XX
  Marketing Name:          RyzenAI-npu5
  Vendor Name:             AMD
  Feature:                 AGENT_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        1(0x1)
  Queue Min Size:          64(0x40)
  Queue Max Size:          64(0x40)
  Queue Type:              SINGLE
  Node:                    0
  Device Type:             DSP
  Cache Info:
    L2:                      2048(0x800) KB
    L3:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          0(0x0)
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            0
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:0
  Memory Properties:
  Features:                AGENT_DISPATCH
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, COARSE GRAINED
      Size:                    97971060(0x5d6eb74) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65536(0x10000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    97971060(0x5d6eb74) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*** Done ***

### Additional Information

dmesg -T,
[Fri Apr 17 19:55:54 2026] chrome: page allocation failure: order:0, mode:0xc0d60(GFP_NOFS|__GFP_HIGH|__GFP_ZERO|__GFP_COMP|__GFP_NOMEMALLOC), nodemask=(null),cpuset=user@1000.service,mems_allowed=0
[Fri Apr 17 19:55:54 2026] CPU: 9 UID: 1000 PID: 4194 Comm: chrome Tainted: G        W           6.19.11-1-cachyos-deckify #1 PREEMPT(full)  9fff08c9212a99aea2ebbcfea09c365efa718419
[Fri Apr 17 19:55:54 2026] Tainted: [W]=WARN
[Fri Apr 17 19:55:54 2026] Hardware name: ONE-NETBOOK ONEXPLAYER APEX/ONEXPLAYER APEX, BIOS 0.14 01/29/2026
[Fri Apr 17 19:55:54 2026] Sched_ext: lavd_1.1.0_gc505008f_x86_64_unknown_linux_gnu (enabled+all), task: runnable_at=-3ms
[Fri Apr 17 19:55:54 2026] Call Trace:
[Fri Apr 17 19:55:54 2026]  <TASK>
[Fri Apr 17 19:55:54 2026]  dump_stack_lvl+0x5d/0x80
[Fri Apr 17 19:55:54 2026]  warn_alloc+0x163/0x190
[Fri Apr 17 19:55:54 2026]  __alloc_pages_slowpath.constprop.1+0x910/0xdb0
[Fri Apr 17 19:55:54 2026]  __alloc_frozen_pages_noprof+0x33b/0x350
[Fri Apr 17 19:55:54 2026]  folio_alloc_noprof+0xb9/0x330
[Fri Apr 17 19:55:54 2026]  ? rmap_walk_anon+0xd8/0x1f0
[Fri Apr 17 19:55:54 2026]  isolate_lock_cluster+0x11d/0x240
[Fri Apr 17 19:55:54 2026]  folio_alloc_swap+0x571/0x940
[Fri Apr 17 19:55:54 2026]  shrink_folio_list+0x52f/0x1330
[Fri Apr 17 19:55:54 2026]  evict_folios+0x44d/0xb40
[Fri Apr 17 19:55:54 2026]  try_to_shrink_lruvec+0x1be/0x2a0
[Fri Apr 17 19:55:54 2026]  shrink_one+0xc2/0x230
[Fri Apr 17 19:55:54 2026]  shrink_node+0xc0b/0xe40
[Fri Apr 17 19:55:54 2026]  do_try_to_free_pages+0xb3/0x550
[Fri Apr 17 19:55:54 2026]  try_to_free_pages+0xe1/0x210
[Fri Apr 17 19:55:54 2026]  __alloc_pages_slowpath.constprop.1+0x366/0xdb0
[Fri Apr 17 19:55:54 2026]  ? blk_mq_flush_plug_list+0x1b3/0x760
[Fri Apr 17 19:55:54 2026]  __alloc_frozen_pages_noprof+0x33b/0x350
[Fri Apr 17 19:55:54 2026]  folio_alloc_noprof+0xb9/0x330
[Fri Apr 17 19:55:54 2026]  page_cache_ra_unbounded+0x125/0x270
[Fri Apr 17 19:55:54 2026]  filemap_fault+0x631/0x1ba0
[Fri Apr 17 19:55:54 2026]  ? swap_entries_put_cache+0xf2/0x100
[Fri Apr 17 19:55:54 2026]  ? do_swap_page+0x1b0/0x19e0
[Fri Apr 17 19:55:54 2026]  __do_fault+0x34/0x1d0
[Fri Apr 17 19:55:54 2026]  do_read_fault+0x42/0x220
[Fri Apr 17 19:55:54 2026]  ? pte_offset_map_rw_nolock+0x1f/0x90
[Fri Apr 17 19:55:54 2026]  __handle_mm_fault+0xc8d/0x10c0
[Fri Apr 17 19:55:54 2026]  handle_mm_fault+0xe4/0x2e0
[Fri Apr 17 19:55:54 2026]  do_user_addr_fault+0x21c/0x900
[Fri Apr 17 19:55:54 2026]  exc_page_fault+0x7e/0x180
[Fri Apr 17 19:55:54 2026]  asm_exc_page_fault+0x26/0x30
[Fri Apr 17 19:55:54 2026] RIP: 0033:0x56026e5ded7c
[Fri Apr 17 19:55:54 2026] Code: 5d c3 48 8b b8 08 03 00 00 48 8b 07 48 8d 0d 63 a9 71 0a 48 29 c1 48 c1 c9 03 48 81 f9 78 ed 07 00 77 14 48 8d 15 bd cc 90 fc <f6> 04 11 08 74 07 5d ff a0 88 00 00 00 67 0f b9 40 02 cc cc 55 48
[Fri Apr 17 19:55:54 2026] RSP: 002b:00007fffdbd653c0 EFLAGS: 00010287
[Fri Apr 17 19:55:54 2026] RAX: 0000560278a4a2d8 RBX: 0000029000000449 RCX: 0000000000055e7e
[Fri Apr 17 19:55:54 2026] RDX: 000056026aeeba39 RSI: 00007fffdbd65420 RDI: 0000303c03748800
[Fri Apr 17 19:55:54 2026] RBP: 00007fffdbd653c0 R08: 0000000000000290 R09: 0000000080000000
[Fri Apr 17 19:55:54 2026] R10: 0000000000000000 R11: 0000560270056b50 R12: 0000000000000000
[Fri Apr 17 19:55:54 2026] R13: 0000560278a949c8 R14: 0000000000000000 R15: 0000303c0071a780
[Fri Apr 17 19:55:54 2026]  </TASK>
[Fri Apr 17 19:55:54 2026] Mem-Info:
[Fri Apr 17 19:55:54 2026] active_anon:1554076 inactive_anon:107331 isolated_anon:0
                            active_file:323925 inactive_file:3342128 isolated_file:0
                            unevictable:32797 dirty:66 writeback:56
                            slab_reclaimable:66982 slab_unreclaimable:112013
                            mapped:323529 shmem:37141 pagetables:19095
                            sec_pagetables:1261 bounce:0
                            kernel_misc_reclaimable:0
                            free:101755 free_pcp:2760 free_cma:0
[Fri Apr 17 19:55:54 2026] Node 0 active_anon:6216304kB inactive_anon:429324kB active_file:1295700kB inactive_file:13368512kB unevictable:131188kB isolated(anon):0kB isolated(file):0kB mapped:1294116kB dirty:264kB writeback:224kB shmem:148564kB shmem_thp:0kB shmem_pmdmapped:0kB anon_thp:75776kB kernel_stack:30352kB pagetables:76380kB sec_pagetables:5044kB all_unreclaimable? no Balloon:0kB
[Fri Apr 17 19:55:54 2026] Node 0 DMA free:11264kB boost:0kB min:8kB low:20kB high:32kB reserved_highatomic:0KB free_highatomic:0KB active_anon:0kB inactive_anon:0kB active_file:0kB inactive_file:0kB unevictable:0kB writepending:0kB zspages:0kB present:15996kB managed:15360kB mlocked:0kB bounce:0kB free_pcp:0kB local_pcp:0kB free_cma:0kB
[Fri Apr 17 19:55:54 2026] lowmem_reserve[]: 0 1631 95659 95659 95659
[Fri Apr 17 19:55:54 2026] Node 0 DMA32 free:377040kB boost:0kB min:1116kB low:2736kB high:4356kB reserved_highatomic:0KB free_highatomic:0KB active_anon:140460kB inactive_anon:323992kB active_file:61208kB inactive_file:721068kB unevictable:0kB writepending:296kB zspages:24356kB present:1743304kB managed:1671004kB mlocked:0kB bounce:0kB free_pcp:1384kB local_pcp:0kB free_cma:0kB
[Fri Apr 17 19:55:54 2026] lowmem_reserve[]: 0 0 94028 94028 94028
[Fri Apr 17 19:55:54 2026] Node 0 Normal free:14684kB boost:0kB min:66452kB low:162724kB high:258996kB reserved_highatomic:2048KB free_highatomic:2044KB active_anon:6078316kB inactive_anon:103832kB active_file:1234700kB inactive_file:12647080kB unevictable:131188kB writepending:244kB zspages:1110604kB present:98009856kB managed:96284696kB mlocked:116kB bounce:0kB free_pcp:9668kB local_pcp:0kB free_cma:0kB
[Fri Apr 17 19:55:54 2026] lowmem_reserve[]: 0 0 0 0 0
[Fri Apr 17 19:55:54 2026] Node 0 DMA: 0*4kB 0*8kB 0*16kB 0*32kB 0*64kB 0*128kB 0*256kB 0*512kB 1*1024kB (U) 1*2048kB (M) 2*4096kB (M) = 11264kB
[Fri Apr 17 19:55:54 2026] Node 0 DMA32: 1*4kB (U) 2*8kB (UM) 7*16kB (UE) 88*32kB (UME) 127*64kB (UME) 102*128kB (UME) 65*256kB (UM) 56*512kB (UME) 48*1024kB (UME) 90*2048kB (UM) 18*4096kB (UM) = 376644kB
[Fri Apr 17 19:55:54 2026] Node 0 Normal: 2*4kB (UH) 5*8kB (UH) 69*16kB (UEH) 38*32kB (UEH) 21*64kB (UEH) 16*128kB (UH) 17*256kB (UEH) 5*512kB (UH) 1*1024kB (H) 0*2048kB 0*4096kB = 13696kB
[Fri Apr 17 19:55:54 2026] Node 0 hugepages_total=0 hugepages_free=0 hugepages_surp=0 hugepages_size=1048576kB
[Fri Apr 17 19:55:54 2026] Node 0 hugepages_total=0 hugepages_free=0 hugepages_surp=0 hugepages_size=2048kB
[Fri Apr 17 19:55:54 2026] 3706536 total pagecache pages
[Fri Apr 17 19:55:54 2026] 2971 pages in swap cache
[Fri Apr 17 19:55:54 2026] Free swap  = 127224588kB
[Fri Apr 17 19:55:54 2026] Total swap = 131524600kB
[Fri Apr 17 19:55:54 2026] 24942289 pages RAM
[Fri Apr 17 19:55:54 2026] 0 pages HighMem/MovableOnly
[Fri Apr 17 19:55:54 2026] 449524 pages reserved
[Fri Apr 17 19:55:54 2026] 0 pages cma reserved
[Fri Apr 17 19:55:54 2026] 0 pages hwpoisoned
[Fri Apr 17 19:55:54 2026] Memory cgroup min protection 0kB -- low protection 0kB
[Fri Apr 17 19:56:16 2026] warn_alloc: 47 callbacks suppressed
[Fri Apr 17 19:56:16 2026] kswapd0: page allocation failure: order:0, mode:0xc0de0(GFP_KERNEL|__GFP_HIGH|__GFP_ZERO|__GFP_COMP|__GFP_NOMEMALLOC), nodemask=(null),cpuset=/,mems_allowed=0
[Fri Apr 17 19:56:16 2026] CPU: 3 UID: 0 PID: 244 Comm: kswapd0 Tainted: G        W           6.19.11-1-cachyos-deckify #1 PREEMPT(full)  9fff08c9212a99aea2ebbcfea09c365efa718419
[Fri Apr 17 19:56:16 2026] Tainted: [W]=WARN
[Fri Apr 17 19:56:16 2026] Hardware name: ONE-NETBOOK ONEXPLAYER APEX/ONEXPLAYER APEX, BIOS 0.14 01/29/2026
[Fri Apr 17 19:56:16 2026] Sched_ext: lavd_1.1.0_gc505008f_x86_64_unknown_linux_gnu (enabled+all), task: runnable_at=-70ms
[Fri Apr 17 19:56:16 2026] Call Trace:
[Fri Apr 17 19:56:16 2026]  <TASK>
[Fri Apr 17 19:56:16 2026]  dump_stack_lvl+0x5d/0x80
[Fri Apr 17 19:56:16 2026]  warn_alloc+0x163/0x190
[Fri Apr 17 19:56:16 2026]  __alloc_pages_slowpath.constprop.1+0x910/0xdb0
[Fri Apr 17 19:56:16 2026]  __alloc_frozen_pages_noprof+0x33b/0x350
[Fri Apr 17 19:56:16 2026]  folio_alloc_noprof+0xb9/0x330
[Fri Apr 17 19:56:16 2026]  ? rmap_walk_anon+0xd8/0x1f0
[Fri Apr 17 19:56:16 2026]  isolate_lock_cluster+0x11d/0x240
[Fri Apr 17 19:56:16 2026]  folio_alloc_swap+0x571/0x940
[Fri Apr 17 19:56:16 2026]  shrink_folio_list+0x52f/0x1330
[Fri Apr 17 19:56:16 2026]  evict_folios+0x44d/0xb40
[Fri Apr 17 19:56:16 2026]  try_to_shrink_lruvec+0x1be/0x2a0
[Fri Apr 17 19:56:16 2026]  shrink_one+0xc2/0x230
[Fri Apr 17 19:56:16 2026]  shrink_node+0xc0b/0xe40
[Fri Apr 17 19:56:16 2026]  ? asm_sysvec_apic_timer_interrupt+0x1a/0x20
[Fri Apr 17 19:56:16 2026]  ? mem_cgroup_iter+0x1c3/0x220
[Fri Apr 17 19:56:16 2026]  balance_pgdat+0x6e5/0xcf0
[Fri Apr 17 19:56:16 2026]  ? __scx_update_idle+0x18d/0x270
[Fri Apr 17 19:56:16 2026]  ? psi_group_change+0x176/0x330
[Fri Apr 17 19:56:16 2026]  ? timer_delete_sync+0xaf/0xc0
[Fri Apr 17 19:56:16 2026]  ? schedule_timeout+0x8b/0x100
[Fri Apr 17 19:56:16 2026]  kswapd+0x1f5/0x470
[Fri Apr 17 19:56:16 2026]  ? __pfx_autoremove_wake_function+0x10/0x10
[Fri Apr 17 19:56:16 2026]  ? __pfx_kswapd+0x10/0x10
[Fri Apr 17 19:56:16 2026]  kthread+0xfc/0x240
[Fri Apr 17 19:56:16 2026]  ? __pfx_kthread+0x10/0x10
[Fri Apr 17 19:56:16 2026]  ret_from_fork+0x222/0x270
[Fri Apr 17 19:56:16 2026]  ? __pfx_kthread+0x10/0x10
[Fri Apr 17 19:56:16 2026]  ret_from_fork_asm+0x1a/0x30
[Fri Apr 17 19:56:16 2026]  </TASK>
[Fri Apr 17 19:56:16 2026] Mem-Info:
[Fri Apr 17 19:56:16 2026] active_anon:1615846 inactive_anon:95488 isolated_anon:0
                            active_file:314063 inactive_file:3343096 isolated_file:0
                            unevictable:32797 dirty:136 writeback:1
                            slab_reclaimable:66810 slab_unreclaimable:111834
                            mapped:213728 shmem:36891 pagetables:19097
                            sec_pagetables:1271 bounce:0
                            kernel_misc_reclaimable:0
                            free:101982 free_pcp:4751 free_cma:0
[Fri Apr 17 19:56:16 2026] Node 0 active_anon:6463384kB inactive_anon:381952kB active_file:1256252kB inactive_file:13372384kB unevictable:131188kB isolated(anon):0kB isolated(file):0kB mapped:854912kB dirty:544kB writeback:4kB shmem:147564kB shmem_thp:0kB shmem_pmdmapped:0kB anon_thp:73728kB kernel_stack:30384kB pagetables:76388kB sec_pagetables:5084kB all_unreclaimable? no Balloon:0kB
[Fri Apr 17 19:56:16 2026] Node 0 DMA free:11264kB boost:0kB min:8kB low:20kB high:32kB reserved_highatomic:0KB free_highatomic:0KB active_anon:0kB inactive_anon:0kB active_file:0kB inactive_file:0kB unevictable:0kB writepending:0kB zspages:0kB present:15996kB managed:15360kB mlocked:0kB bounce:0kB free_pcp:0kB local_pcp:0kB free_cma:0kB
[Fri Apr 17 19:56:16 2026] lowmem_reserve[]: 0 1631 95659 95659 95659
[Fri Apr 17 19:56:16 2026] Node 0 DMA32 free:376580kB boost:0kB min:1116kB low:2736kB high:4356kB reserved_highatomic:0KB free_highatomic:0KB active_anon:210368kB inactive_anon:260644kB active_file:138932kB inactive_file:653604kB unevictable:0kB writepending:156kB zspages:9196kB present:1743304kB managed:1671004kB mlocked:0kB bounce:0kB free_pcp:3276kB local_pcp:456kB free_cma:0kB
[Fri Apr 17 19:56:16 2026] lowmem_reserve[]: 0 0 94028 94028 94028
[Fri Apr 17 19:56:16 2026] Node 0 Normal free:20084kB boost:0kB min:66452kB low:162724kB high:258996kB reserved_highatomic:2048KB free_highatomic:2048KB active_anon:6252948kB inactive_anon:120512kB active_file:1117768kB inactive_file:12718780kB unevictable:131188kB writepending:392kB zspages:946664kB present:98009856kB managed:96284696kB mlocked:116kB bounce:0kB free_pcp:15716kB local_pcp:4612kB free_cma:0kB
[Fri Apr 17 19:56:16 2026] lowmem_reserve[]: 0 0 0 0 0
[Fri Apr 17 19:56:16 2026] Node 0 DMA: 0*4kB 0*8kB 0*16kB 0*32kB 0*64kB 0*128kB 0*256kB 0*512kB 1*1024kB (U) 1*2048kB (M) 2*4096kB (M) = 11264kB
[Fri Apr 17 19:56:16 2026] Node 0 DMA32: 124*4kB (U) 150*8kB (U) 105*16kB (UME) 71*32kB (UE) 101*64kB (UME) 90*128kB (UME) 64*256kB (UM) 57*512kB (UME) 48*1024kB (UME) 90*2048kB (UM) 18*4096kB (UM) = 376400kB
[Fri Apr 17 19:56:16 2026] Node 0 Normal: 1*4kB (U) 1*8kB (U) 1*16kB (U) 151*32kB (U) 135*64kB (UE) 12*128kB (UE) 5*256kB (UE) 0*512kB 0*1024kB 1*2048kB (H) 0*4096kB = 18364kB
[Fri Apr 17 19:56:16 2026] Node 0 hugepages_total=0 hugepages_free=0 hugepages_surp=0 hugepages_size=1048576kB
[Fri Apr 17 19:56:16 2026] Node 0 hugepages_total=0 hugepages_free=0 hugepages_surp=0 hugepages_size=2048kB
[Fri Apr 17 19:56:16 2026] 3698248 total pagecache pages
[Fri Apr 17 19:56:16 2026] 4321 pages in swap cache
[Fri Apr 17 19:56:16 2026] Free swap  = 127422364kB
[Fri Apr 17 19:56:16 2026] Total swap = 131524600kB
[Fri Apr 17 19:56:16 2026] 24942289 pages RAM
[Fri Apr 17 19:56:16 2026] 0 pages HighMem/MovableOnly
[Fri Apr 17 19:56:16 2026] 449524 pages reserved
[Fri Apr 17 19:56:16 2026] 0 pages cma reserved
[Fri Apr 17 19:56:16 2026] 0 pages hwpoisoned
[Fri Apr 17 19:56:16 2026] Memory cgroup min protection 0kB -- low protection 0kB
[Fri Apr 17 19:56:43 2026] gmc_v11_0_process_interrupt: 85 callbacks suppressed
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a05000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 Faulty UTCL2 client ID: TCP (0x8)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 RW: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a00000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 Faulty UTCL2 client ID: TCP (0x8)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 RW: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a00000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 Faulty UTCL2 client ID: TCP (0x8)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: 	 RW: 0x0
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a01000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a01000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a02000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a02000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a03000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a03000 from client 10
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:200)
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:  Process VLLM::EngineCor pid 7304 thread VLLM::EngineCor pid 7304
[Fri Apr 17 19:56:43 2026] amdgpu 0000:65:00.0: amdgpu:   in page starting at address 0x00007ff512a04000 from client 10
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: Failed to evict queue 1
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: GPU reset begin!. Source:  3
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: remove_all_kfd_queues_mes: Failed to remove queue 0 for dev 60565
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: Dumping IP State
[Fri Apr 17 19:56:45 2026] amdgpu 0000:65:00.0: amdgpu: Dumping IP State Completed
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: MODE2 reset
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: GPU reset succeeded, trying to resume
[Fri Apr 17 19:56:46 2026] [drm] PCIE GART of 512M enabled (table at 0x0000008000900000).
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: VRAM is lost due to GPU reset!
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: SMU is resuming...
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: SMU is resumed successfully!
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x09003E00
[Fri Apr 17 19:56:46 2026] workqueue: Failed to create a worker thread: -ENOMEM
[Fri Apr 17 19:56:46 2026] sched_ext: BPF scheduler "lavd_1.1.0_gc505008f_x86_64_unknown_linux_gnu" disabled (scx_bpf_error)
[Fri Apr 17 19:56:46 2026] sched_ext: lavd_1.1.0_gc505008f_x86_64_unknown_linux_gnu: src/bpf/main.bpf.c:1727: task_ctx_stor first lookup failed
[Fri Apr 17 19:56:46 2026]    scx_bpf_error_bstr+0x117/0x1d0
[Fri Apr 17 19:56:46 2026]    bpf_prog_84f7d094df6d952b_lavd_init_task+0x77/0x2b2
[Fri Apr 17 19:56:46 2026]    bpf__sched_ext_ops_init_task+0x4b/0xb0
[Fri Apr 17 19:56:46 2026]    scx_fork+0xaf/0x1c0
[Fri Apr 17 19:56:46 2026]    copy_process+0xdc1/0x1d60
[Fri Apr 17 19:56:46 2026]    kernel_clone+0xbc/0x4a0
[Fri Apr 17 19:56:46 2026]    kernel_thread+0x71/0xa0
[Fri Apr 17 19:56:46 2026]    kthreadd+0x298/0x310
[Fri Apr 17 19:56:46 2026]    ret_from_fork+0x222/0x270
[Fri Apr 17 19:56:46 2026]    ret_from_fork_asm+0x1a/0x30
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring jpeg_dec_0 uses VM inv eng 4 on hub 8
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring jpeg_dec_1 uses VM inv eng 6 on hub 8
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: ring vpe uses VM inv eng 7 on hub 8
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: amdgpu: GPU reset(3) succeeded!
[Fri Apr 17 19:56:46 2026] amdgpu 0000:65:00.0: [drm] device wedged, but recovered through reset
[Fri Apr 17 19:56:46 2026] warn_alloc: 47 callbacks suppressed
[Fri Apr 17 19:56:46 2026] kwin_wayland: page allocation failure: order:0, mode:0xc0d60(GFP_NOFS|__GFP_HIGH|__GFP_ZERO|__GFP_COMP|__GFP_NOMEMALLOC), nodemask=(null),cpuset=user@1000.service,mems_allowed=0
[Fri Apr 17 19:56:46 2026] CPU: 24 UID: 1000 PID: 2802 Comm: kwin_wayland Tainted: G        W           6.19.11-1-cachyos-deckify #1 PREEMPT(full)  9fff08c9212a99aea2ebbcfea09c365efa718419
[Fri Apr 17 19:56:46 2026] Tainted: [W]=WARN
[Fri Apr 17 19:56:46 2026] Hardware name: ONE-NETBOOK ONEXPLAYER APEX/ONEXPLAYER APEX, BIOS 0.14 01/29/2026
[Fri Apr 17 19:56:46 2026] Call Trace:
[Fri Apr 17 19:56:46 2026]  <TASK>
[Fri Apr 17 19:56:46 2026]  dump_stack_lvl+0x5d/0x80
[Fri Apr 17 19:56:46 2026]  warn_alloc+0x163/0x190
[Fri Apr 17 19:56:46 2026]  __alloc_pages_slowpath.constprop.1+0x910/0xdb0
[Fri Apr 17 19:56:46 2026]  __alloc_frozen_pages_noprof+0x33b/0x350
[Fri Apr 17 19:56:46 2026]  folio_alloc_noprof+0xb9/0x330
[Fri Apr 17 19:56:46 2026]  ? rmap_walk_anon+0xd8/0x1f0
[Fri Apr 17 19:56:46 2026]  isolate_lock_cluster+0x11d/0x240
[Fri Apr 17 19:56:46 2026]  folio_alloc_swap+0x4aa/0x940
[Fri Apr 17 19:56:46 2026]  shrink_folio_list+0x52f/0x1330
[Fri Apr 17 19:56:46 2026]  evict_folios+0x44d/0xb40
[Fri Apr 17 19:56:46 2026]  try_to_shrink_lruvec+0x1be/0x2a0
[Fri Apr 17 19:56:46 2026]  shrink_one+0xc2/0x230
[Fri Apr 17 19:56:46 2026]  shrink_node+0xc0b/0xe40
[Fri Apr 17 19:56:46 2026]  do_try_to_free_pages+0xb3/0x550
[Fri Apr 17 19:56:46 2026]  try_to_free_pages+0xe1/0x210
[Fri Apr 17 19:56:46 2026]  __alloc_pages_slowpath.constprop.1+0x366/0xdb0
[Fri Apr 17 19:56:46 2026]  __alloc_frozen_pages_noprof+0x33b/0x350
[Fri Apr 17 19:56:46 2026]  folio_alloc_noprof+0xb9/0x330
[Fri Apr 17 19:56:46 2026]  btrfs_alloc_folio_array+0x57/0xe0
[Fri Apr 17 19:56:46 2026]  btrfs_submit_compressed_read+0x199/0x2c0
[Fri Apr 17 19:56:46 2026]  submit_one_bio+0xb2/0xc0
[Fri Apr 17 19:56:46 2026]  btrfs_do_readpage+0x4ab/0x8e0
[Fri Apr 17 19:56:46 2026]  btrfs_readahead+0xe6/0x190
[Fri Apr 17 19:56:46 2026]  ? __pfx_end_bbio_data_read+0x10/0x10
[Fri Apr 17 19:56:46 2026]  read_pages+0x75/0x220
[Fri Apr 17 19:56:46 2026]  page_cache_ra_unbounded+0x1d5/0x270
[Fri Apr 17 19:56:46 2026]  filemap_fault+0x631/0x1ba0
[Fri Apr 17 19:56:46 2026]  ? __memcg_kmem_charge_page+0xa4/0xf0
[Fri Apr 17 19:56:46 2026]  ? __alloc_frozen_pages_noprof+0x1c2/0x350
[Fri Apr 17 19:56:46 2026]  __do_fault+0x34/0x1d0
[Fri Apr 17 19:56:46 2026]  do_read_fault+0x42/0x220
[Fri Apr 17 19:56:46 2026]  __handle_mm_fault+0xc8d/0x10c0
[Fri Apr 17 19:56:46 2026]  handle_mm_fault+0xe4/0x2e0
[Fri Apr 17 19:56:46 2026]  do_user_addr_fault+0x21c/0x900
[Fri Apr 17 19:56:46 2026]  exc_page_fault+0x7e/0x180
[Fri Apr 17 19:56:46 2026]  asm_exc_page_fault+0x26/0x30
[Fri Apr 17 19:56:46 2026] RIP: 0033:0x7f03e28e7090
[Fri Apr 17 19:56:46 2026] Code: Unable to access opcode bytes at 0x7f03e28e7066.
[Fri Apr 17 19:56:46 2026] RSP: 002b:00007ffd064fb678 EFLAGS: 00010202
[Fri Apr 17 19:56:46 2026] RAX: 00007f03e893ced0 RBX: 0000558d8b46beb0 RCX: 0000000000000000
[Fri Apr 17 19:56:46 2026] RDX: 00007f03fb803b58 RSI: 0000000000000040 RDI: 0000558d8b77b910
[Fri Apr 17 19:56:46 2026] RBP: 00007ffd064fb6a0 R08: 0000000000000001 R09: 0000000000000030
[Fri Apr 17 19:56:46 2026] R10: 0000000000000000 R11: 00007f03f45b0c80 R12: 0000558d8b745e80
[Fri Apr 17 19:56:46 2026] R13: 0000558d8b46bf38 R14: 0000558d8b51ed20 R15: 0000558d8b51b120
[Fri Apr 17 19:56:46 2026]  </TASK>
[Fri Apr 17 19:56:46 2026] Mem-Info:
[Fri Apr 17 19:56:46 2026] active_anon:223756 inactive_anon:27069 isolated_anon:0
                            active_file:71289 inactive_file:3030326 isolated_file:0
                            unevictable:32797 dirty:12717 writeback:2559
                            slab_reclaimable:66622 slab_unreclaimable:113046
                            mapped:129246 shmem:41635 pagetables:15987
                            sec_pagetables:1279 bounce:0
                            kernel_misc_reclaimable:0
                            free:105059 free_pcp:2977 free_cma:0
[Fri Apr 17 19:56:46 2026] Node 0 active_anon:895024kB inactive_anon:108276kB active_file:285156kB inactive_file:12121304kB unevictable:131188kB isolated(anon):0kB isolated(file):0kB mapped:516984kB dirty:50868kB writeback:10236kB shmem:166540kB shmem_thp:0kB shmem_pmdmapped:0kB anon_thp:102400kB kernel_stack:31664kB pagetables:63948kB sec_pagetables:5116kB all_unreclaimable? no Balloon:0kB
[Fri Apr 17 19:56:46 2026] Node 0 DMA free:11264kB boost:0kB min:8kB low:20kB high:32kB reserved_highatomic:0KB free_highatomic:0KB active_anon:0kB inactive_anon:0kB active_file:0kB inactive_file:0kB unevictable:0kB writepending:0kB zspages:0kB present:15996kB managed:15360kB mlocked:0kB bounce:0kB free_pcp:0kB local_pcp:0kB free_cma:0kB
[Fri Apr 17 19:56:46 2026] lowmem_reserve[]: 0 1631 95659 95659 95659
[Fri Apr 17 19:56:46 2026] Node 0 DMA32 free:376380kB boost:0kB min:1116kB low:2736kB high:4356kB reserved_highatomic:0KB free_highatomic:0KB active_anon:8380kB inactive_anon:29476kB active_file:6684kB inactive_file:445408kB unevictable:0kB writepending:13016kB zspages:5532kB present:1743304kB managed:1671004kB mlocked:0kB bounce:0kB free_pcp:1840kB local_pcp:796kB free_cma:0kB
[Fri Apr 17 19:56:46 2026] lowmem_reserve[]: 0 0 94028 94028 94028
[Fri Apr 17 19:56:46 2026] Node 0 Normal free:32592kB boost:0kB min:66452kB low:162724kB high:258996kB reserved_highatomic:2048KB free_highatomic:2048KB active_anon:885964kB inactive_anon:79552kB active_file:278524kB inactive_file:11675168kB unevictable:131188kB writepending:48196kB zspages:853096kB present:98009856kB managed:96284696kB mlocked:116kB bounce:0kB free_pcp:10068kB local_pcp:2256kB free_cma:0kB
[Fri Apr 17 19:56:46 2026] lowmem_reserve[]: 0 0 0 0 0
[Fri Apr 17 19:56:46 2026] Node 0 DMA: 0*4kB 0*8kB 0*16kB 0*32kB 0*64kB 0*128kB 0*256kB 0*512kB 1*1024kB (U) 1*2048kB (M) 2*4096kB (M) = 11264kB
[Fri Apr 17 19:56:46 2026] Node 0 DMA32: 2124*4kB (UM) 5116*8kB (UM) 5848*16kB (UME) 1137*32kB (UME) 1306*64kB (UME) 469*128kB (UME) 148*256kB (UM) 30*512kB (UM) 0*1024kB 0*2048kB 0*4096kB = 376240kB
[Fri Apr 17 19:56:46 2026] Node 0 Normal: 0*4kB 727*8kB (U) 431*16kB (U) 240*32kB (U) 59*64kB (U) 18*128kB (U) 3*256kB (U) 2*512kB (U) 0*1024kB 1*2048kB (H) 0*4096kB = 30312kB
[Fri Apr 17 19:56:46 2026] Node 0 hugepages_total=0 hugepages_free=0 hugepages_surp=0 hugepages_size=1048576kB
[Fri Apr 17 19:56:46 2026] Node 0 hugepages_total=0 hugepages_free=0 hugepages_surp=0 hugepages_size=2048kB
[Fri Apr 17 19:56:46 2026] 3146215 total pagecache pages
[Fri Apr 17 19:56:46 2026] 3178 pages in swap cache
[Fri Apr 17 19:56:46 2026] Free swap  = 127791504kB
[Fri Apr 17 19:56:46 2026] Total swap = 131524600kB
[Fri Apr 17 19:56:46 2026] 24942289 pages RAM
[Fri Apr 17 19:56:46 2026] 0 pages HighMem/MovableOnly
[Fri Apr 17 19:56:46 2026] 449524 pages reserved
[Fri Apr 17 19:56:46 2026] 0 pages cma reserved
[Fri Apr 17 19:56:46 2026] 0 pages hwpoisoned
[Fri Apr 17 19:56:46 2026] Memory cgroup min protection 0kB -- low protection 0kB
[Fri Apr 17 19:56:51 2026] ops->cpu_acquire/release() are deprecated, use sched_switch TP instead
[Fri Apr 17 19:56:51 2026] sched_ext: BPF scheduler "lavd_1.1.0_gc505008f_x86_64_unknown_linux_gnu" enabled
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1000
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: Failed to remove queue 0
[Fri Apr 17 19:56:55 2026] amdgpu: Resetting wave fronts (cpsch) on dev 000000005a97b4d9
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: no vmid pasid mapping supported
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: GPU reset begin!. Source:  3
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: Dumping IP State
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: Dumping IP State Completed
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: MODE2 reset
[Fri Apr 17 19:56:55 2026] amdgpu 0000:65:00.0: amdgpu: GPU reset succeeded, trying to resume