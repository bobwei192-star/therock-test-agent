# Radeon RX 580 [drm:uvd_v6_0_ring_test_ring] *ERROR* amdgpu: ring 12 test failed (0xCAFEDEAD

> **Issue #263**
> **状态**: closed
> **创建时间**: 2017-11-25T15:47:05Z
> **更新时间**: 2018-06-03T15:09:29Z
> **关闭时间**: 2018-06-03T15:09:29Z
> **作者**: aep
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/263

## 描述

according to #188 the in-kernel amdgpu driver is supposed to be used instead of amdgpu-pro (which apparantly depends on an older kernel anyway).

so is the RX580 supported?

````
[aep@archlinux ROCK-Kernel-Driver]$ dmesg | grep amdgpu
[    1.330063] [drm] amdgpu kernel modesetting enabled.
[    1.332779] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.334035] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[    1.334310] amdgpu 0000:01:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    1.335806] [drm] amdgpu: 8192M of VRAM memory ready
[    1.335981] [drm] amdgpu: 8192M of GTT memory ready.
[    1.336811] amdgpu 0000:01:00.0: amdgpu: using MSI.
[    1.337335] [drm] amdgpu: irq initialized.
[    1.480684] amdgpu: [powerplay] amdgpu: powerplay sw initialized
[    1.486725] amdgpu 0000:01:00.0: fence driver on ring 0 use gpu addr 0x0000000000400008, cpu addr 0xffff8801388f2008
[    1.487287] amdgpu 0000:01:00.0: fence driver on ring 1 use gpu addr 0x0000000000400018, cpu addr 0xffff8801388f2018
[    1.487919] amdgpu 0000:01:00.0: fence driver on ring 2 use gpu addr 0x0000000000400028, cpu addr 0xffff8801388f2028
[    1.488534] amdgpu 0000:01:00.0: fence driver on ring 3 use gpu addr 0x0000000000400038, cpu addr 0xffff8801388f2038
[    1.489137] amdgpu 0000:01:00.0: fence driver on ring 4 use gpu addr 0x0000000000400048, cpu addr 0xffff8801388f2048
[    1.489797] amdgpu 0000:01:00.0: fence driver on ring 5 use gpu addr 0x0000000000400058, cpu addr 0xffff8801388f2058
[    1.490431] amdgpu 0000:01:00.0: fence driver on ring 6 use gpu addr 0x0000000000400068, cpu addr 0xffff8801388f2068
[    1.490944] amdgpu 0000:01:00.0: fence driver on ring 7 use gpu addr 0x0000000000400078, cpu addr 0xffff8801388f2078
[    1.491438] amdgpu 0000:01:00.0: fence driver on ring 8 use gpu addr 0x0000000000400088, cpu addr 0xffff8801388f2088
[    1.491806] amdgpu 0000:01:00.0: fence driver on ring 9 use gpu addr 0x000000000040009c, cpu addr 0xffff8801388f209c
[    1.492351] amdgpu 0000:01:00.0: fence driver on ring 10 use gpu addr 0x00000000004000ac, cpu addr 0xffff8801388f20ac
[    1.492993] amdgpu 0000:01:00.0: fence driver on ring 11 use gpu addr 0x00000000004000bc, cpu addr 0xffff8801388f20bc
[    1.494834] amdgpu 0000:01:00.0: fence driver on ring 12 use gpu addr 0x000000f4002ad420, cpu addr 0xffffc9000225a420
[    1.495829] amdgpu 0000:01:00.0: fence driver on ring 13 use gpu addr 0x00000000004000dc, cpu addr 0xffff8801388f20dc
[    1.496454] amdgpu 0000:01:00.0: fence driver on ring 14 use gpu addr 0x00000000004000ec, cpu addr 0xffff8801388f20ec
[    1.540852] amdgpu: [powerplay] Can't find requested voltage id in vdd_dep_on_sclk table!
[    1.542523] amdgpu: [powerplay] VDDCI is larger than max VDDCI in VDDCI Voltage Table!
[   12.033679] [drm:uvd_v6_0_ring_test_ring] *ERROR* amdgpu: ring 12 test failed (0xCAFEDEAD)
[   12.033941] [drm:amdgpu_device_init] *ERROR* hw_init of IP block <uvd_v6_0> failed -22
[   12.034196] amdgpu 0000:01:00.0: amdgpu_init failed
[   12.218057] [drm] amdgpu: ttm finalized
[   12.218240] amdgpu 0000:01:00.0: Fatal error during GPU init
[   12.218396] [drm] amdgpu: finishing device.
[   12.223160] amdgpu: probe of 0000:01:00.0 failed with error -22
````

---

## 评论 (2 条)

### 评论 #1 — pacxx (2017-11-26T12:26:04Z)

Currently not, however there is an open pull request that adds support for Polaris 12. You need to compile the kernel and the thunk with this patch. I managed to get rocm going on my rx550 however you don't get full support, i.e., OpenCL crashes in device localization.

---

### 评论 #2 — aep (2017-11-26T14:01:42Z)

FWIW: 1.6.x works for me and offers a significant performance increase over amdgpu for opencl

---
