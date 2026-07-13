# [Issue]: VM crashes with error: kvm run failed Bad address from ProxmoxVE 8.2.4

- **Issue #:** 3414
- **State:** closed
- **Created:** 2024-07-12T11:57:24Z
- **Updated:** 2024-12-12T11:26:19Z
- **Labels:** AMD Radeon RX 7900 XTX, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3414

### Problem Description

System crashes when trying to use `rocminfo` with `amdgpu-dkms` installed.

When not installing/uninstalling them, then the command works fine.

<details><summary>Crash details</summary>
<p>
Jul 12 14:02:46 cookie3-pm QEMU[2515]: error: kvm run failed Bad address
Jul 12 14:02:46 cookie3-pm QEMU[2515]: RAX=00000000000033a0 RBX=0000000000000675 RCX=0003000125380073 RDX=0000000000000674
Jul 12 14:02:46 cookie3-pm QEMU[2515]: RSI=ffffb0073eb033a0 RDI=ffff985422480000 RBP=ffffb0010174b938 RSP=ffffb0010174b938
Jul 12 14:02:46 cookie3-pm QEMU[2515]: R8 =0003000000000073 R9 =ffffb0073eb00000 R10=0000000000000000 R11=0000000000000000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: R12=0000000000000675 R13=ffff985422480000 R14=ffff985413740be0 R15=ffffb0073eb00000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: RIP=ffffffffc06c66b3 RFL=00000286 [--S--P-] CPL=0 II=0 A20=1 SMM=0 HLT=0
Jul 12 14:02:46 cookie3-pm QEMU[2515]: ES =0000 0000000000000000 00000000 00000000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: CS =0010 0000000000000000 ffffffff 00a09b00 DPL=0 CS64 [-RA]
Jul 12 14:02:46 cookie3-pm QEMU[2515]: SS =0018 0000000000000000 ffffffff 00c09300 DPL=0 DS   [-WA]
Jul 12 14:02:46 cookie3-pm QEMU[2515]: DS =0000 0000000000000000 00000000 00000000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: FS =0000 00007ccc84951e80 00000000 00000000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: GS =0000 ffff986b1fc80000 00000000 00000000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: LDT=0000 fffffe6100000000 00000000 00000000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: TR =0040 fffffe61f662c000 00004087 00008b00 DPL=0 TSS64-busy
Jul 12 14:02:46 cookie3-pm QEMU[2515]: GDT=     fffffe61f662a000 0000007f
Jul 12 14:02:46 cookie3-pm QEMU[2515]: IDT=     fffffe0000000000 00000fff
Jul 12 14:02:46 cookie3-pm QEMU[2515]: CR0=80050033 CR2=00007ccc83e606f0 CR3=0000000100fa0000 CR4=00350ee0
Jul 12 14:02:46 cookie3-pm QEMU[2515]: DR0=0000000000000000 DR1=0000000000000000 DR2=0000000000000000 DR3=0000000000000000
Jul 12 14:02:46 cookie3-pm QEMU[2515]: DR6=00000000ffff0ff0 DR7=0000000000000400
Jul 12 14:02:46 cookie3-pm QEMU[2515]: EFER=0000000000000d01
Jul 12 14:02:46 cookie3-pm QEMU[2515]: Code=55 48 21 c1 8d 04 d5 00 00 00 00 4c 09 c1 48 01 c6 48 89 e5 <48> 89 0e 31 c0 5d 31 d2 31 c9 31 f6 45 31 c0 e9 19 c7 87 fa 66 0f 1f 84 00 00 00 00 00 90
</p>
</details> 

<details><summary>Host System Configuration</summary>
<p>

ASRockRack ROMED8-2T
AMD EPYC 7252 8-Core Processor , 3200 Mhz, 8 Core(s), 16 Logical Processor(s)
8x Samsung 32GB M393A4K40EB3-CWE 3200MHz DDR4
PowerColor Hellhound RX7900XTX 24G-L/OC


# Firmware Information

BMC Firmware Version	2.02.00
BIOS Firmware Version	P3.80
PSP Firmware Version	0.C.0.88
Microcode Version		08301072


$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 12 (bookworm)
Release:        12
Codename:       bookworm

$ uname -a
Linux cookie3-pm 6.8.8-2-pve #1 SMP PREEMPT_DYNAMIC PMX 6.8.8-2 (2024-06-24T09:00Z) x86_64 GNU/Linux

$ mokutil --sb-state
SecureBoot disabled
Platform is in Setup Mode

</p>
</details> 


<details><summary>Guest OS Configuration</summary>
<p>

$ lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy

$ uname -a
Linux services 6.5.0-41-generic #41~22.04.2-Ubuntu SMP PREEMPT_DYNAMIC Mon Jun  3 11:32:55 UTC 2 x86_64 x86_64 x86_64 GNU/Linux

$ sudo mokutil --sb-state
SecureBoot disabled

</p>
</details> 

### Operating System

ProxmoxVE 8.2.4 - Debian GNU/Linux 12 (bookworm)

### CPU

AMD EPYC 7252 8-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.0

### ROCm Component

ROCK-Kernel-Driver

### Steps to Reproduce

- Install ProxmoxVE 8.2.4
- Configure VFIO and reboot
- Create Ubuntu 22.04.4 VM
- Follow the installation instructions here: https://rocm.docs.amd.com/projects/radeon/en/docs-6.1.3/docs/install/native_linux/install-radeon.html
- Reboot and test the installation

When using the default `amdgpu-install -y --usecase=graphics,rocm` this results in a crash of the VM.
When using `amdgpu-install -y --usecase=rocm,opencl,hip --no-dkms` or uninstalling the following packages `amdgpu-dkms-firmware dctrl-tools (2.24-3build2) dkms amdgpu-dkms`, `rocminfo` works as expected.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details><summary>Details</summary>
<p>

ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.13
Runtime Ext Version:     1.4
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD EPYC 7252 8-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD EPYC 7252 8-Core Processor
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
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   0
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    98830380(0x5e4082c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    98830380(0x5e4082c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    98830380(0x5e4082c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1100
  Uuid:                    GPU-72709ac3cd9084fa
  Marketing Name:          Radeon RX 7900 XTX
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
    L2:                      6144(0x1800) KB
    L3:                      98304(0x18000) KB
  Chip ID:                 29772(0x744c)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2371
  BDFID:                   256
  Internal Node ID:        1
  Compute Unit:            96
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
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
  Packet Processor uCode:: 202
  SDMA engine uCode::      20
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx1100
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

</p>
</details> 

### Additional Information

I've attached some logs from both the host and the VM running this:

- [from host.txt](https://github.com/user-attachments/files/16193404/from.host.txt)
- [from vm.txt](https://github.com/user-attachments/files/16193407/from.vm.txt)
