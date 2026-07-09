# [Issue]: Krackan Point GPU hang (gfx1152) Ryzen AI 350 (MES:0x82)

- **Issue #:** 5844
- **State:** closed
- **Created:** 2026-01-08T16:16:51Z
- **Updated:** 2026-06-23T10:59:32Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5844

### Problem Description

#### OS
**NAME** CachyOS Linux

#### CPU
**model name** AMD Ryzen AI 7 350 w/ Radeon 860M

#### GPU
```
  Name:                    AMD Ryzen AI 7 350 w/ Radeon 860M
  Marketing Name:          AMD Ryzen AI 7 350 w/ Radeon 860M
  Name:                    gfx1152
  Marketing Name:          AMD Radeon 860M Graphics
      Name:                    amdgcn-amd-amdhsa--gfx1152
      Name:                    amdgcn-amd-amdhsa--gfx11-generic
  Name:                    aie2
  Marketing Name:          AIE-ML
```

#### KERNEL
Linux host 6.18.3-2-cachyos #1 SMP PREEMPT_DYNAMIC Sat, 03 Jan 2026 20:06:51 +0000 x86_64 GNU/Linux
Command line: `quiet zswap.enabled=0 nowatchdog splash rw root=UUID=redacted amdgpu.cwsr_enable=0 initrd=\initramfs-linux-cachyos.img`

#### FIRMWARE-INFO:
```
MES_KIQ feature version: 6, firmware version: 0x00000079
MES feature version: 1, firmware version: 0x00000082
```

### Operating System

CachyOS (arch based)

### CPU

AMD Ryzen AI 7 350

### GPU

Radeon 860M

### ROCm Version

7.1.1

### ROCm Component

_No response_

### Steps to Reproduce

Just using the desktop (no AI workload, plain dumb desktop usage) is enough

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

Output of dmesg when it happens:
```
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
[UFW BLOCK] IN=wlan0 OUT= MAC=01:00:5e:00:00:01:5c:cf:7f:0b:41:b5:08:00 SRC=192.168.0.106 DST=224.0.0.1 LEN=32 TOS=0x00 PREC=0x00 TTL=1 ID=2 PROTO=2
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
amdgpu 0000:04:00.0: amdgpu: MES failed to respond to msg=MISC (WAIT_REG_MEM)
amdgpu 0000:04:00.0: amdgpu: failed to reg_write_reg_wait
[...]
Plenty of:
amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
[...]
And some crashes too:
 task:kwin_wayland    state:D stack:0     pid:1159  tgid:1159  ppid:1153   task_flags:0x400100 flags:0x00080003
 Call Trace:
  <TASK>
  __schedule+0x5f3/0x1ea0
  ? drm_ioctl+0x2a6/0x510
  ? sysvec_apic_timer_interrupt+0xe/0x80
  ? asm_sysvec_apic_timer_interrupt+0x1a/0x20
  schedule+0x55/0x170
  schedule_preempt_disabled+0x15/0x30
  __ww_mutex_lock+0x823/0x1050
  modeset_lock.llvm.4911137008902742515.cold+0x38/0x63
  drm_modeset_lock_all_ctx+0x33/0x170
  drm_mode_obj_get_properties_ioctl+0xdb/0x220
  drm_ioctl+0x27b/0x510
  ? __pfx_drm_mode_obj_get_properties_ioctl+0x10/0x10
  amdgpu_drm_ioctl+0x42/0x90 [amdgpu 5b5cc9b41fade2a33a1b7e61a8bfdb18c33cf438]
  __x64_sys_ioctl+0x207/0x2c0
  do_syscall_64+0x89/0x1f0
  ? __se_sys_close.llvm.10203526816879280367+0x7a/0x90
  ? do_syscall_64+0xc9/0x1f0
  ? do_syscall_64+0xc9/0x1f0
  ? do_syscall_64+0xc9/0x1f0
  ? do_syscall_64+0xc9/0x1f0
  entry_SYSCALL_64_after_hwframe+0x76/0x7e
 RIP: 0033:0x7f4ba9f3c17f
 RSP: 002b:00007ffcdf48a1b0 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
 RAX: ffffffffffffffda RBX: 000055ffcde42110 RCX: 00007f4ba9f3c17f
 RDX: 00007ffcdf48a250 RSI: 00000000c02064b9 RDI: 0000000000000013
 RBP: 00007ffcdf48a250 R08: 4e332f279cbf46e3 R09: 0000000000000020
 R10: 0000000000000021 R11: 0000000000000246 R12: 00000000c02064b9
 R13: 0000000000000013 R14: 0000000000000013 R15: cccccccc00000056
  </TASK>
 task:eDP-1           state:D stack:0     pid:1196  tgid:1159  ppid:1153   task_flags:0x400040 flags:0x00080003
 Call Trace:
  <TASK>
  __schedule+0x5f3/0x1ea0
  ? add_hole+0x157/0x1a0
  ? common_interrupt+0x13/0xa0
  ? asm_common_interrupt+0x26/0x40
  schedule+0x55/0x170
  schedule_preempt_disabled+0x15/0x30
  __mutex_lock_slowpath+0x21a/0x440
  amdgpu_mes_reg_write_reg_wait+0x9a/0x150 [amdgpu 5b5cc9b41fade2a33a1b7e61a8bfdb18c33cf438]
  amdgpu_gmc_flush_gpu_tlb+0x19c/0x330 [amdgpu 5b5cc9b41fade2a33a1b7e61a8bfdb18c33cf438]
  amdgpu_gart_invalidate_tlb+0x8c/0xb0 [amdgpu 5b5cc9b41fade2a33a1b7e61a8bfdb18c33cf438]
  amdgpu_ttm_alloc_gart+0x1a8/0x200 [amdgpu 5b5cc9b41fade2a33a1b7e61a8bfdb18c33cf438]
  amdgpu_dm_plane_helper_prepare_fb+0xe5/0x300 [amdgpu 5b5cc9b41fade2a33a1b7e61a8bfdb18c33cf438]
  drm_atomic_helper_prepare_planes.cold+0x5a/0x66
  drm_atomic_helper_commit+0x61/0x2a0
  drm_mode_atomic_ioctl.cold+0x2d8/0x3fc
  drm_ioctl+0x27b/0x510
  ? __pfx_drm_mode_atomic_ioctl+0x10/0x10
  amdgpu_drm_ioctl+0x42/0x90 [amdgpu 5b5cc9b41fade2a33a1b7e61a8bfdb18c33cf438]
  __x64_sys_ioctl+0x207/0x2c0
  do_syscall_64+0x89/0x1f0
  ? do_syscall_64+0xc9/0x1f0
  ? __x64_sys_poll+0xb9/0x150
  ? do_syscall_64+0xc9/0x1f0
  ? __x64_sys_sendmsg+0xa0/0xe0
  ? do_syscall_64+0xc9/0x1f0
  entry_SYSCALL_64_after_hwframe+0x76/0x7e
 RIP: 0033:0x7f4ba9f3c17f
 RSP: 002b:00007f4b8ddf94f0 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
 RAX: ffffffffffffffda RBX: 00007f4b88035d00 RCX: 00007f4ba9f3c17f
 RDX: 00007f4b8ddf95e0 RSI: 00000000c03864bc RDI: 0000000000000013
 RBP: 00007f4b8ddf95e0 R08: 00007f4b8800273c R09: 00007f4b88037570
 R10: 00007f4b88002680 R11: 0000000000000246 R12: 00000000c03864bc
 R13: 0000000000000013 R14: 00007f4b88037700 R15: 0000000000000000
  </TASK>
 amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
 amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
 amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
 amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
 amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
 amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
 amdgpu 0000:04:00.0: amdgpu: MES ring buffer is full.
```

Output of rocminfo:
```
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.18
Runtime Ext Version:     1.14
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
  Name:                    AMD Ryzen AI 7 350 w/ Radeon 860M
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen AI 7 350 w/ Radeon 860M
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
  Max Clock Freq. (MHz):   5090
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    32121744(0x1ea2390) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32121744(0x1ea2390) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32121744(0x1ea2390) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32121744(0x1ea2390) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1152
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon 860M Graphics
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
    L2:                      1024(0x400) KB
  Chip ID:                 4372(0x1114)
  ASIC Revision:           0(0x0)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   3000
  BDFID:                   1024
  Internal Node ID:        1
  Compute Unit:            8
  SIMDs per CU:            2
  Shader Engines:          1
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
  Packet Processor uCode:: 16
  SDMA engine uCode::      15
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16060872(0xf511c8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16060872(0xf511c8) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx1152
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
  Name:                    aie2
  Uuid:                    AIE-XX
  Marketing Name:          AIE-ML
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
    L2:                      1024(0x400) KB
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
      Size:                    32121744(0x1ea2390) KB
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
      Size:                    32121744(0x1ea2390) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*** Done ***
```

### Additional Information

There's also issue #5724 but I don't think it's related, since I'm not using MES firmware 0x83 and not the same gfx architecture (mine is gfx1152, vs gfx1151 in the other issue)

Yet, I've tried the *solutions* in the other thread but it doesn't work.

I might have used AI workload in some boot, but the crash I'm reporting here is definitively without any AI workload when it happened. Video decoding was running through, if it could make sense.