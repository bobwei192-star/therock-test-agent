# RHEL (AlmaLinux) 9.1 amdgpu disabled by "...invalid ip discovery binary signature from vram"

> **Issue #1896**
> **状态**: closed
> **创建时间**: 2023-01-22T16:18:16Z
> **更新时间**: 2024-03-31T14:05:01Z
> **关闭时间**: 2024-03-31T14:05:00Z
> **作者**: klausbu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1896

## 描述

I am using an MSI delta 15 notebook with a dedicated AMD GPU which is running Windows 10 and RHEL (AlmaLinux) 9.1 in a dual boot configuration on separate drives. I installed the ROCm software stack including rocm-amdgpu-dkms (5.4.0). The dedicated GPU is frecuently not initialized at boot time due to an "invalid ip discovery binary signature from vram"... see below.  I can temporarily fix the problem by reinstalling the Windows 10 Adrenaline software. During the process, the installer switches sometimes into a "repair" mode which apparently fixes the wrong settings at motherboard level and enables a successful Linux boot that initializes the GPU. 

**Is there a permanent solution for this amdgpu Linux problem?**

...
Jan 16 23:33:32 localhost kernel: amdgpu 0000:03:00.0: amdgpu: get invalid ip discovery binary signature from vram
Jan 16 23:33:32 localhost kernel: amdgpu 0000:03:00.0: amdgpu: amdgpu_discovery is not set properly
Jan 16 23:33:32 localhost kernel: amdgpu 0000:03:00.0: amdgpu: failed to read ip discovery binary from file
Jan 16 23:33:32 localhost kernel: [drm:amdgpu_discovery_set_ip_blocks [amdgpu]] *ERROR* amdgpu_discovery_init failed
Jan 16 23:33:32 localhost kernel: amdgpu 0000:03:00.0: amdgpu: Fatal error during GPU init
Jan 16 23:33:32 localhost kernel: amdgpu 0000:03:00.0: amdgpu: amdgpu: finishing device.
Jan 16 23:33:32 localhost kernel: amdgpu: probe of 0000:03:00.0 failed with error -22
Jan 16 23:33:32 localhost kernel: checking generic (fc20000000 300000) vs hw (fc20000000 10000000)
Jan 16 23:33:32 localhost kernel: checking generic (fc20000000 300000) vs hw (fc20000000 10000000)
Jan 16 23:33:32 localhost kernel: fb0: switching to amdgpu from EFI VGA
Jan 16 23:33:32 localhost kernel: Console: switching to colour dummy device 80x25
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: vgaarb: deactivate vga console
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: enabling device (0006 -> 0007)
Jan 16 23:33:32 localhost kernel: [drm] initializing kernel modesetting (RENOIR 0x1002:0x1638 0x1462:0x1316 0xC4).
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: Trusted Memory Zone (TMZ) feature enabled
Jan 16 23:33:32 localhost kernel: [drm] register mmio base: 0xFC900000
Jan 16 23:33:32 localhost kernel: [drm] register mmio size: 524288
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 0 <soc15_common>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 1 <gmc_v9_0>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 2 <vega10_ih>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 3 <psp>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 4 <smu>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 5 <dm>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 6 <gfx_v9_0>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 7 <sdma_v4_0>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 8 <vcn_v2_0>
Jan 16 23:33:32 localhost kernel: [drm] add ip block number 9 <jpeg_v2_0>
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: Fetched VBIOS from VFCT
Jan 16 23:33:32 localhost kernel: amdgpu: ATOM BIOS: 113-CEZANNE-018
Jan 16 23:33:32 localhost kernel: [drm] VCN decode is enabled in VM mode
Jan 16 23:33:32 localhost kernel: [drm] VCN encode is enabled in VM mode
Jan 16 23:33:32 localhost kernel: [drm] JPEG decode is enabled in VM mode
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: PCIE atomic ops is not supported
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: MODE2 reset
Jan 16 23:33:32 localhost kernel: [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: VRAM: 512M 0x000000F400000000 - 0x000000F41FFFFFFF (512M used)
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
Jan 16 23:33:32 localhost kernel: [drm] Detected VRAM RAM=512M, BAR=512M
Jan 16 23:33:32 localhost kernel: [drm] RAM width 128bits DDR4
Jan 16 23:33:32 localhost kernel: [drm] amdgpu: 512M of VRAM memory ready
Jan 16 23:33:32 localhost kernel: [drm] amdgpu: 3072M of GTT memory ready.
Jan 16 23:33:32 localhost kernel: [drm] GART: num cpu pages 262144, num gpu pages 262144
Jan 16 23:33:32 localhost kernel: [drm] PCIE GART of 1024M enabled.
Jan 16 23:33:32 localhost kernel: [drm] PTB located at 0x000000F400900000
Jan 16 23:33:32 localhost kernel: amdgpu 0000:07:00.0: amdgpu: PSP runtime database doesn't exist


---

## 评论 (2 条)

### 评论 #1 — nartmada (2024-03-23T04:05:49Z)

Hi @klausbu, apologies for the slow response.  It looks like you did not fill out the Issue Template when you are creating this ticket.  What is the dGPU on the laptop?  What are the repro steps?  Thanks.




---

### 评论 #2 — nartmada (2024-03-31T14:05:00Z)

Closing the ticket.  Please re-open with the Issue Template filled properly.  Thanks.

---
