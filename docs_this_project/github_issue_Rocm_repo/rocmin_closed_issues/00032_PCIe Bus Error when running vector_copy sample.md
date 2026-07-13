# PCIe Bus Error when running vector_copy sample

- **Issue #:** 32
- **State:** closed
- **Created:** 2016-09-25T17:19:40Z
- **Updated:** 2016-09-29T11:45:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/32

I followed the README to install ROCm driver. However, when I try to run `vector_copy` sample, the program hangs, and I see report about a PCIe error on `dmesg`.

Configuration:
- Intel Core i7 6700K on GIGABYTE GA-Z170-HD3 (rev. 1.0) motherboard with Intel Z170 chipset.
- AMD Radeon Fury Nano GPU in the PCIe x16 slot
- Ubuntu 16.04 on AMD64 architecture
- `uname -r`: `4.4.0-kfd-compute-rocm-rel-1.2-31`

Kernel log (`dmesg`) messages after running the `vector_copy` sample:

```
[  942.180230] pcieport 0000:00:1c.4: AER: Uncorrected (Fatal) error received: id=00e4
[  942.180239] pcieport 0000:00:1c.4: PCIe Bus Error: severity=Uncorrected (Fatal), type=Transaction Layer, id=00e4(Receiver ID)
[  942.180327] pcieport 0000:00:1c.4:   device [8086:a114] error status/mask=00040000/00000000
[  942.180392] pcieport 0000:00:1c.4:    [18] Malformed TLP          (First)
[  942.180444] pcieport 0000:00:1c.4:   TLP Header: 6c000002 06000000 0000000f b76e6008
[  942.180511] pcieport 0000:00:1c.4: broadcast error_detected message
[  942.180513] amdgpu 0000:06:00.0: device has no AER-aware driver
[  942.180514] snd_hda_intel 0000:06:00.1: device has no AER-aware driver
[  943.188998] pcieport 0000:00:1c.4: Root Port link has been reset
[  943.189001] pcieport 0000:00:1c.4: AER: Device recovery failed
```

`/opt/rocm/rocm-smi -a` output:

```
===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]      : GPU ID: 0x7300
============================================================================
============================================================================
GPU[0]      : Temperature: 511.0c
============================================================================
============================================================================
GPU[0]      : Unable to determine current clocks. Check dmesg or GPU temperature
============================================================================
GPU[0]      : Fan Level: 255 (100.0)%
============================================================================
============================================================================
GPU[0]      : Current PowerPlay Level: auto
============================================================================
============================================================================
GPU[0]      : Current OverDrive value: 0%
============================================================================
============================================================================
GPU[0]      : Supported GPU clock frequencies on GPU0
GPU[0]      : 0: 300Mhz
GPU[0]      : 1: 508Mhz
GPU[0]      : 2: 717Mhz
GPU[0]      : 3: 874Mhz
GPU[0]      : 4: 911Mhz
GPU[0]      : 5: 944Mhz
GPU[0]      : 6: 974Mhz
GPU[0]      : 7: 1000Mhz
GPU[0]      :
GPU[0]      : Supported GPU Memory clock frequencies on GPU0
GPU[0]      : 0: 500Mhz
GPU[0]      :
============================================================================
===================          End of ROCm SMI Log         ===================
```
