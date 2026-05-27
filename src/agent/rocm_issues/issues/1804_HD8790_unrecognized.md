# HD8790 unrecognized?

> **Issue #1804**
> **状态**: closed
> **创建时间**: 2022-09-06T20:16:58Z
> **更新时间**: 2023-12-22T19:36:39Z
> **关闭时间**: 2023-12-20T02:01:22Z
> **作者**: raspico
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1804

## 描述

I have a laptop with Intel i7-4810 CPU (with integrated graphics) and  Mars XTX [Radeon HD 8790M]
It loads and initializes amdgpu driver;  `lshw -c video` shows
```
*-display                 
       description: VGA compatible controller
       product: Mars XTX [Radeon HD 8790M]
       ...
       configuration: driver=amdgpu latency=0
       resources: irq:38 memory:e0000000-efffffff memory:f7c00000-f7c3ffff ioport:e000(size=256) memory:f7c40000-f7c5ffff
  *-display
       description: VGA compatible controller
       product: 4th Gen Core Processor Integrated Graphics Controller
```
but rocminfo does not see it and clnfo shows number of devices=0 for platform:  AMD Accelerated Parallel Processing

I see that `journalctl -b` has this line
```
kernel: kfd kfd: amdgpu: OLAND  not supported in kfd
```
Using Fedora 36  kernel 5.19.6-200 and rocm-opencl-5.2.3-1.fc36.x86_64

The out-of-the-box config for this system had radeon.modeset=0 but amdgpu complained about radeon driver running SI so I added
 `radeon.si_support=0 amdgpu.si_support=1 `
to the kernel command line, which seemed to help activating the amdgpu driver, with those kernel messages:
```
Sep 06 14:59:32 localhost.localdomain kernel: [drm] amdgpu kernel modesetting enabled.
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu: vga_switcheroo: detected switching method \_SB_.PCI0.GFX0.ATPX handle
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu: CRAT table not found
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu: Virtual CRAT table created for CPU
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu: Topology: Add CPU node
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu 0000:01:00.0: enabling device (0000 -> 0003)
Sep 06 14:59:32 localhost.localdomain kernel: kfd kfd: amdgpu: OLAND  not supported in kfd
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: Fetched VBIOS from ATRM
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu: ATOM BIOS: BR46109.001
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: VRAM: 2048M 0x000000F400000000 - 0x000000F47FFFFFFF (2048M used)
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: GART: 1024M 0x000000FF00000000 - 0x000000FF3FFFFFFF
Sep 06 14:59:32 localhost.localdomain kernel: [drm] amdgpu: 2048M of VRAM memory ready
Sep 06 14:59:32 localhost.localdomain kernel: [drm] amdgpu: 7950M of GTT memory ready.
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: PCIE GART of 1024M enabled (table at 0x000000F400000000).
Sep 06 14:59:32 localhost.localdomain kernel: [drm] amdgpu: dpm initialized
Sep 06 14:59:32 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: SE 1, SH per SE 1, CU per SH 6, active_cu_number 6
Sep 06 14:59:33 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: Using ATPX for runtime pm
Sep 06 14:59:33 localhost.localdomain kernel: [drm] Initialized amdgpu 3.47.0 20150101 for 0000:01:00.0 on minor 0
Sep 06 14:59:33 localhost.localdomain kernel: amdgpu 0000:01:00.0: [drm] Cannot find any crtc or sizes
Sep 06 14:59:42 localhost.localdomain kernel: amdgpu 0000:01:00.0: [drm] Cannot find any crtc or sizes
Sep 06 14:59:42 localhost.localdomain kernel: amdgpu 0000:01:00.0: [drm] Cannot find any crtc or sizes
Sep 06 14:59:55 localhost.localdomain gnome-shell[2064]: Added device '/dev/dri/card0' (amdgpu) using non-atomic mode setting.
Sep 06 15:00:03 localhost.localdomain gnome-shell[2783]: Added device '/dev/dri/card0' (amdgpu) using non-atomic mode setting.
Sep 06 15:01:38 localhost.localdomain kernel: amdgpu 0000:01:00.0: amdgpu: Disabling VM faults because of PRT request!





---

## 评论 (6 条)

### 评论 #1 — illwieckz (2022-10-08T05:46:43Z)

GCN1 and GCN2 cards aren't supported by ROCm. Oland is a GCN1 card so your card isn't supported.

You'll need an old Orca driver, the one from amdgpu-pro `21.20-1271047`. Some more recent versions of amdgpu-pro distributed newer Orca driver but without old GCN support. This one both lists OpenCL GCN1 and GCN2 devices on Ubuntu 22.04 (support for some cards is buggy anyway).

The package is usually named `opencl-orca-amdgpu-pro-icd`.

You can find it for Red Hat 8.4 there: https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-20

Try the `opencl-orca-amdgpu-pro-icd-21.20-1271047.el8.x86_64.rpm` package, with some luck it may work on recent Fedora, and with some luck support for your device will not be buggy.

Edit: see details on https://gitlab.com/illwieckz/i-love-compute

---

### 评论 #2 — nartmada (2023-12-18T19:30:13Z)

Hi @raspico, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.


---

### 评论 #3 — illwieckz (2023-12-18T20:47:41Z)

@nartmada @raspico The Radeon HD 8790M is a GCN1 card from 2013, it has never been supported by ROCm. Not only this card had never been supported, but the complete family this card belongs to had never been supported. This issue can be closed.

---

### 评论 #4 — raspico (2023-12-20T02:01:49Z)

Thanks for clarifying this.

---

### 评论 #5 — illwieckz (2023-12-22T00:27:52Z)

@raspico you may find there a tutorial I wrote for installing the Latest Mesa rusticl OpenCL driver that is known to work with your card, here:

- https://github.com/ROCm/ROCm/issues/2743#issuecomment-1867079776

This tutorial is for Ubuntu but maybe you will be able to adapt it for Fedora. They key thing is the installation of a recent Mesa OpenCL driver and the trick about the `RUSTICL_ENABLE='radeonsi'` environment variable. I'm not from AMD by the way, I just happen to have good knowledge of what works and what doesn't with AMD 😃️.

---

### 评论 #6 — nartmada (2023-12-22T19:36:38Z)

Thanks @illwieckz for sharing your tutorial :)

---
