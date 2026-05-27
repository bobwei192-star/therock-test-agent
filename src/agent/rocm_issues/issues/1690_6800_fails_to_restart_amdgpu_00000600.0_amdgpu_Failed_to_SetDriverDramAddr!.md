# 6800 fails to restart: amdgpu 0000:06:00.0: amdgpu: Failed to SetDriverDramAddr!

> **Issue #1690**
> **状态**: closed
> **创建时间**: 2022-02-23T14:12:06Z
> **更新时间**: 2022-02-24T21:35:52Z
> **关闭时间**: 2022-02-24T14:02:55Z
> **作者**: andreevmipt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1690

## 描述

After upgrading to kernel linux-5.14.7-gentoo and later versions the following error occurs, after resetting ethminer:
With linux-5.13.5-gentoo no problems observed
dev-libs/rocm-opencl-runtime - 4.3.0
Card model:           XFX Speedster MERC 319 AMD Radeon RX 6800 XT Black

Kernel log:
Feb 22 21:41:04 gentoo64 kernel: [drm] PCIE GART of 512M enabled (table at 0x0000008000000000).
Feb 22 21:41:04 gentoo64 kernel: [drm] PSP is resuming...
Feb 22 21:41:04 gentoo64 kernel: [drm] reserve 0xa00000 from 0x800f400000 for PSP TMR
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command SETUP_TMR(0x5) failed and response status is (0x80000306)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode SDMA0(0x0) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode CP_CE(0x8) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode CP_PFP(0x9) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode CP_ME(0xA) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode CP_MEC1(0xB) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode CP_MEC2(0xD) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode RLC_RESTORE_LIST_GPM_MEM(0x12) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode RLC_RESTORE_LIST_SRM_MEM(0x13) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode RLC_IRAM(0x14) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode RLC_DRAM(0x15) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode RLC_G(0x16) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command AUTOLOAD_RLC(0x21) failed and response status is (0xFFFF000D)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode VCN(0x1C) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode VCN1(0x1D) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: [drm] failed to load ucode DMCUB(0x22) 
Feb 22 21:41:05 gentoo64 kernel: [drm] psp gfx command LOAD_IP_FW(0x6) failed and response status is (0x80000203)
Feb 22 21:41:05 gentoo64 kernel: amdgpu 0000:06:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
Feb 22 21:41:05 gentoo64 kernel: amdgpu 0000:06:00.0: amdgpu: SMU is resuming...
Feb 22 21:41:08 gentoo64 kernel: amdgpu 0000:06:00.0: amdgpu: Failed to SetDriverDramAddr!
Feb 22 21:41:08 gentoo64 kernel: amdgpu 0000:06:00.0: amdgpu: Failed to setup smc hw!
Feb 22 21:41:08 gentoo64 kernel: [drm:amdgpu_file_to_fpriv [amdgpu]] *ERROR* resume of IP block <smu> failed -62
Feb 22 21:41:08 gentoo64 kernel: amdgpu 0000:06:00.0: amdgpu: amdgpu_device_ip_resume failed (-62).

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2022-02-24T14:02:55Z)

Hi @andreevmipt 
Thanks for reaching out.
ROCm 5.0 does not support 5.14 kernel and so things will break.
ROCm 5.0 supports the latest linux 5.13/5.11 kernels, so recommend to try the same.
Thank you.

---

### 评论 #2 — andreevmipt (2022-02-24T21:35:51Z)

Thank you, got it

---
