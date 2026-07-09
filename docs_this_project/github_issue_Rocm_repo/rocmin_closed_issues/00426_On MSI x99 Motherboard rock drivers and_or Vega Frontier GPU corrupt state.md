# On MSI x99 Motherboard rock drivers and/or Vega Frontier GPU corrupt state

- **Issue #:** 426
- **State:** closed
- **Created:** 2018-05-28T14:25:32Z
- **Updated:** 2021-01-05T11:00:46Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/426

`clinfo` hangs, `rocm-smi` seems to report nonsense:
```
$ /opt/rocm/bin/rocm-smi -d 1 -a 


====================    ROCm System Management Interface    ====================
================================================================================
GPU[1]          : GPU ID: 0x6863
================================================================================
================================================================================
GPU[1]          : Temperature: 511.0c
================================================================================
================================================================================
GPU[1]          : Unable to determine current clocks. Check dmesg or GPU temperature
================================================================================
GPU[1]          : Fan Level: 255 (100.0)%
================================================================================
================================================================================
GPU[1]          : Current PowerPlay Level: manual
================================================================================
================================================================================
GPU[1]          : Current OverDrive value: 0%
================================================================================
================================================================================
GPU[1]          : Minimum SCLK: 1528MHz
GPU[1]          : Minimum MCLK: 0MHz
GPU[1]          : Activity threshold: 0%
GPU[1]          : Hysteresis Up: 0ms
GPU[1]          : Hysteresis Down: 0ms
================================================================================
================================================================================
GPU[1]          : Average GPU Power: 16777215.0 W
================================================================================
================================================================================
GPU[1]          : Supported GPU clock frequencies on GPU1
GPU[1]          : 0: 852Mhz 
GPU[1]          : 1: 991Mhz 
GPU[1]          : 2: 1138Mhz 
GPU[1]          : 3: 1269Mhz 
GPU[1]          : 4: 1348Mhz 
GPU[1]          : 5: 1440Mhz 
GPU[1]          : 6: 1528Mhz 
GPU[1]          : 7: 1600Mhz 
GPU[1]          : 
GPU[1]          : Supported GPU Memory clock frequencies on GPU1
GPU[1]          : 0: 167Mhz 
GPU[1]          : 1: 500Mhz 
GPU[1]          : 2: 800Mhz 
GPU[1]          : 3: 945Mhz 
GPU[1]          : 
================================================================================
WARNING: One or more commands failed
====================           End of ROCm SMI Log          ====================
```

I also have a few tens of thousands of lines of this in my kernel log:
```
 kernel: [905094.420501] amdgpu: [powerplay] Failed to send message: 0x23, ret value: 0xffffffff
 kernel: [905094.420631] amdgpu: [powerplay] Failed to send message: 0x26, ret value: 0xffffffff
 kernel: [905094.421095] amdgpu: [powerplay] Failed to send message: 0x46, ret value: 0xffffffff
 kernel: [905094.421532] amdgpu: [powerplay] Failed to send message: 0x46, ret value: 0xffffffff
 kernel: [905094.425385] amdgpu: [powerplay] Failed to send message: 0x26, ret value: 0xffffffff
 kernel: [905094.425489] amdgpu: [powerplay] Failed to send message: 0x23, ret value: 0xffffffff
 kernel: [905094.425590] amdgpu: [powerplay] Failed to send message: 0x61, ret value: 0xffffffff
 kernel: [905094.425690] amdgpu: [powerplay] Failed to send message: 0x37, ret value: 0xffffffff
 kernel: [905094.425880] amdgpu: [powerplay] Failed to send message: 0x23, ret value: 0xffffffff
 kernel: [905094.426008] amdgpu: [powerplay] Failed to send message: 0x26, ret value: 0xffffffff
 kernel: [905096.503380] amdgpu: [powerplay] Failed to send message: 0x23, ret value: 0xffffffff
```