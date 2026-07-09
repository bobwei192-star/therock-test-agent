# HD8790 unrecognized?

- **Issue #:** 1804
- **State:** closed
- **Created:** 2022-09-06T20:16:58Z
- **Updated:** 2023-12-22T19:36:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1804

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



