# RocM and Azure

> **Issue #1141**
> **状态**: closed
> **创建时间**: 2020-06-07T11:44:53Z
> **更新时间**: 2021-02-15T06:34:08Z
> **关闭时间**: 2021-02-15T06:16:27Z
> **作者**: incardon
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1141

## 描述

Did someone has experience on installing RocM on Azure ? Because starting from few days I am not able to make RocM working anymore. As soon as I install rocm-dkms package the amdgpu driver crash on start. 

[ 11.589569] amdgpu c7e9:00:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:217 vmid:0 pasid:0, for process pid 0 thread pid 0) 
[ 11.591955] amdgpu c7e9:00:00.0: amdgpu: in page starting at address 0x000000f400100000 from client 27 [ 11.659995] amdgpu c7e9:00:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:217 vmid:0 pasid:0, for process pid 0 thread pid 0) 
[ 11.659995] amdgpu c7e9:00:00.0: amdgpu: in page starting at address 0x000000f400101000 from client 27 
[ 12.004451] amdgpu c7e9:00:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] ERROR ring kiq_2.1.0 test failed (-110) 
[ 12.049879] [drm:amdgpu_gfx_enable_kcq [amdgpu]] ERROR KCQ enable failed 
[ 12.092608] [drm:amdgpu_device_init [amdgpu]] ERROR hw_init of IP block <gfx_v9_0> failed -110 [ 12.141149] amdgpu c7e9:00:00.0: amdgpu: amdgpu_device_ip_init failed 
[ 12.193592] amdgpu c7e9:00:00.0: amdgpu: Fatal error during GPU init

I tried SLES15 Ubuntu 18.04 and CentOS 8.1 following the instruction here:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

Partition used
Standard NV4as_v4 (4 vcpus, 14 GiB memory)

AMD Gpu is a Radeon Instinct MI25 partitioned

---

## 评论 (2 条)

### 评论 #1 — rur0 (2020-12-02T07:13:34Z)

I am also experiencing issues with azure and rocm
I got rocm installed on 5.4.0-54-generic, however running lspci gives
```bash
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (AGP disabled) (rev 03)
00:07.0 ISA bridge: Intel Corporation 82371AB/EB/MB PIIX4 ISA (rev 01)
00:07.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)
00:07.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 02)
00:08.0 VGA compatible controller: Microsoft Corporation Hyper-V virtual VGA
```
*note the missing MI25 GPU !

---

### 评论 #2 — ROCmSupport (2021-02-15T06:16:27Z)

Thanks @for reaching us.
We are not supporting ROCm on Azure. We have plans to support in future on a specific hardware and can be shared via our documentation.
Request you to stay tuned for the updates.
Thank you.

---
