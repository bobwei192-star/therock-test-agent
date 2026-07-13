# Compute Device result rate decreases ~51% when a second Compute Device is running

- **Issue #:** 242
- **State:** closed
- **Created:** 2017-11-03T01:37:01Z
- **Updated:** 2018-02-18T03:55:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/242

My issue is that my performance (result rate) decreases once I run OpenCL code on a second GPU.
I start the program and ask it to run on Device 0. I start the program a second time and ask it to run on Device 1. **Device 1 starts and stays at half performance compared to it's performance when ran alone. Device 0's performance decreases ~105%.**

(I setup the program to use 2 CPU threads for each Compute Device, in case that makes any difference for you.)

My two compute devices each have their own x8 PCIe 3.0 directly to the processor. 
Compute Devices: RX580 4GB (Qty 2)

./rocm_agent_enumerator -t gpu
```
gfx000
gfx803

```
Headless Ubuntu 17.10, AMD Ryzen 5 1600X, 32GiB system ram
uname -r   `4.11.0-kfd-compute-rocm-rel-1.6-180`

lspci -v -d1002
```

24:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev e7) (prog-if 00 [VGA controller])
	Subsystem: XFX Pine Group Inc. Ellesmere [Radeon RX 470/480/570/580]
	Flags: bus master, fast devsel, latency 0, IRQ 323
	Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Memory at f0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at e000 [size=256]
	Memory at fe900000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

24:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
	Subsystem: XFX Pine Group Inc. Device aaf0
	Flags: bus master, fast devsel, latency 0, IRQ 335
	Memory at fe960000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

25:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev e7) (prog-if 00 [VGA controller])
	Subsystem: XFX Pine Group Inc. Ellesmere [Radeon RX 470/480/570/580]
	Flags: bus master, fast devsel, latency 0, IRQ 330
	Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Memory at d0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at d000 [size=256]
	Memory at fe800000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at fe840000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

25:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
	Subsystem: XFX Pine Group Inc. Device aaf0
	Flags: bus master, fast devsel, latency 0, IRQ 337
	Memory at fe860000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel
```

dmesg | grep -i IOMMU
```
[    1.059385] AMD-Vi: IOMMU performance counters supported
[    1.059588] iommu: Adding device 0000:00:01.0 to group 0
[    1.059651] iommu: Adding device 0000:00:01.3 to group 1
[    1.059714] iommu: Adding device 0000:00:02.0 to group 2
[    1.059782] iommu: Adding device 0000:00:03.0 to group 3
[    1.059846] iommu: Adding device 0000:00:03.1 to group 4
[    1.059911] iommu: Adding device 0000:00:03.2 to group 5
[    1.059973] iommu: Adding device 0000:00:04.0 to group 6
[    1.060038] iommu: Adding device 0000:00:07.0 to group 7
[    1.060053] iommu: Adding device 0000:00:07.1 to group 7
[    1.060116] iommu: Adding device 0000:00:08.0 to group 8
[    1.060130] iommu: Adding device 0000:00:08.1 to group 8
[    1.060192] iommu: Adding device 0000:00:14.0 to group 9
[    1.060206] iommu: Adding device 0000:00:14.3 to group 9
[    1.060284] iommu: Adding device 0000:00:18.0 to group 10
[    1.060298] iommu: Adding device 0000:00:18.1 to group 10
[    1.060311] iommu: Adding device 0000:00:18.2 to group 10
[    1.060325] iommu: Adding device 0000:00:18.3 to group 10
[    1.060337] iommu: Adding device 0000:00:18.4 to group 10
[    1.060350] iommu: Adding device 0000:00:18.5 to group 10
[    1.060362] iommu: Adding device 0000:00:18.6 to group 10
[    1.060374] iommu: Adding device 0000:00:18.7 to group 10
[    1.060447] iommu: Adding device 0000:03:00.0 to group 11
[    1.060467] iommu: Adding device 0000:03:00.1 to group 11
[    1.060487] iommu: Adding device 0000:03:00.2 to group 11
[    1.060499] iommu: Adding device 0000:04:00.0 to group 11
[    1.060510] iommu: Adding device 0000:04:01.0 to group 11
[    1.060522] iommu: Adding device 0000:04:02.0 to group 11
[    1.060534] iommu: Adding device 0000:04:03.0 to group 11
[    1.060545] iommu: Adding device 0000:04:04.0 to group 11
[    1.060557] iommu: Adding device 0000:04:08.0 to group 11
[    1.060575] iommu: Adding device 0000:1e:00.0 to group 11
[    1.060590] iommu: Adding device 0000:23:00.0 to group 11
[    1.060674] iommu: Adding device 0000:24:00.0 to group 12
[    1.060699] iommu: Using direct mapping for device 0000:24:00.0
[    1.060725] iommu: Adding device 0000:24:00.1 to group 12
[    1.060796] iommu: Adding device 0000:25:00.0 to group 13
[    1.060821] iommu: Using direct mapping for device 0000:25:00.0
[    1.060851] iommu: Adding device 0000:25:00.1 to group 13
[    1.060862] iommu: Adding device 0000:26:00.0 to group 7
[    1.060872] iommu: Adding device 0000:26:00.2 to group 7
[    1.060882] iommu: Adding device 0000:26:00.3 to group 7
[    1.060891] iommu: Adding device 0000:27:00.0 to group 8
[    1.060901] iommu: Adding device 0000:27:00.2 to group 8
[    1.060910] iommu: Adding device 0000:27:00.3 to group 8
[    1.061089] AMD-Vi: Found IOMMU at 0000:00:00.2 cap 0x40
[    1.062314] perf: amd_iommu: Detected. (0 banks, 0 counters/bank)
[    1.383424] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
```


dmseg | grep kfd
Here are some boot messages:
```
[    1.229795] usb usb6: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-180 xhci-hcd
[    1.425181] kfd kfd: Initialized module
[    2.265702] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[    2.265929] kfd kfd: Reserved 2 pages for cwsr.
[    2.265973] kfd kfd: added device 1002:67df
[    3.462612] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[    3.465282] kfd kfd: Reserved 2 pages for cwsr.
[    3.465786] kfd kfd: added device 1002:67df
```
and these messages appear when starting even a single Compute Device: 
```
[   84.025373] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025402] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025422] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025442] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025462] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025482] kfd2kgd: Failed to create BO on domain VRAM. ret -12
```

I continuously get additional messages when running both Compute Devices:
```
[48405.710824] Started evicting process of pasid 2
[48405.711497] Finished evicting process of pasid 2
[48405.712811] Finished restoring process of pasid 1
[48406.126508] Started restoring process of pasid 2
[48406.126862] Started evicting process of pasid 1
[48406.127546] Finished evicting process of pasid 1
[48406.128858] Finished restoring process of pasid 2
[51389.814655] Started evicting process of pasid 2
[51389.814657] process_evict_queues: 14 callbacks suppressed
[51389.814658] Evicting PASID 2 queues
[51389.814696] Evicting PASID 2 queues
[51389.814840] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.814918] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.814984] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815049] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815115] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815180] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815246] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815311] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815377] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815392] Finished evicting process of pasid 2
[51389.815443] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815509] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815574] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815640] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815705] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815771] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815837] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815902] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815968] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816034] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816099] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816164] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816230] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816295] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816362] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816427] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816493] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816567] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816634] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816700] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51390.244946] Started restoring process of pasid 2
[51390.245612] Started evicting process of pasid 1
[51390.245612] Evicting PASID 1 queues
[51390.246302] Evicting PASID 1 queues
[51390.246320] Finished evicting process of pasid 1
[51390.247619] process_restore_queues: 12 callbacks suppressed
[51390.247619] Restoring PASID 2 queues
[51390.247623] Restoring PASID 2 queues
[51390.247626] Finished restoring process of pasid 2
[51390.660963] Started restoring process of pasid 1
[51390.661311] Started evicting process of pasid 2
[51390.661312] Evicting PASID 2 queues
[51390.661331] Evicting PASID 2 queues
[51390.661993] Finished evicting process of pasid 2
[51390.663301] Restoring PASID 1 queues
[51390.663305] Restoring PASID 1 queues
[51390.663307] Finished restoring process of pasid 1
```
