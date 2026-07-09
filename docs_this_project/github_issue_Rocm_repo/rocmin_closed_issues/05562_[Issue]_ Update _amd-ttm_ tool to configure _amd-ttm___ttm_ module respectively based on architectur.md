# [Issue]: Update `amd-ttm` tool to configure `amd-ttm`/`ttm` module respectively based on architecture

- **Issue #:** 5562
- **State:** closed
- **Created:** 2025-10-22T19:45:41Z
- **Updated:** 2026-03-31T16:10:11Z
- **Labels:** Feature Request, status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5562

### Problem Description

**Issue:** On Strix Halo, passing the usual amdttm.page_pool_size value no longer provided the requested amount of unified memory (125 GiB in our case, and shown below).   This problem was consistent with Debian 13 / Kernel 6.12 / amdgpu 6.14.14 and Ubuntu 25.10 / Kernel 6.17 / amdgpu 6.17.0 both with ROCm 7.0.2/noble apt repositories configured.   

With the recent ROCm 7.0.2 release, we rolled forwards our Debian from Bookworm (12) to Trixie (13), now that it is officially supported and GTT allocations for unified memory no longer worked as they previously did. 

The testing was performed on a Strix Halo, but likely extends to all ROCm platforms.   Users that are using the deprecated amdgpu.gttsize parameter will land on a working configuration, and may not notice both the deprecation and conficting value warnings in their dmesg.  Who knows how long that will work, and to avoid a bunch of uncessary issues down the road, documentation updates should be made as this change suggests full deprecation is likely to happen in the next version. 

Anyone using this properly today, also may not search sysfs looking for the new parameters when it stops working, so it would probably be a good idea to drop in the release notes (https://rocm.docs.amd.com/en/latest/about/release-notes.html and https://github.com/ROCm/ROCm/releases/tag/rocm-7.0.2) 

It would be good on these RTD pages too:
https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300a.html (needs update)
https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installryz/native_linux/install-ryzen.html (missing completely)


**Addition Observations:** Both partitions were upgraded from working Debian 12 / ROCm 7.0.1 and Ubuntu 25.04 / ROCm 7.0.1 respectively, from working configurations with no changes to kernel parameters, further suggesting the issue originates from the ROCm 7.0.1 to 7.0.2 upgrade. 

**Workaround:** Adding the deprecated amdgpu.gttsize value delivered the requested configuration, along with deprecation warnings, and warnings about conflicting values between parameters in the newer upstream version (amdgpu 6.17.0-5)

**Fix:** Migrate `amdttm.page_pool_size` to `ttm.page_pool_size` and `amdttm.pages_limit` to `ttm.pages_limit` and remove deprecated `amdgpu.gttsize` to clear noise during enumeration.

Additional outputs from amd-smi, dmesg follow the requested system information pattern below.



```
#   echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
GPU:
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Name:                    gfx1151                            
  Marketing Name:          AMD Radeon Graphics                
      Name:                    amdgcn-amd-amdhsa--gfx1151         
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   

#   echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
OS:
NAME="Debian GNU/Linux"
VERSION="13 (trixie)"
ai2:~#   echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
CPU: 
model name	: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

#   echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
GPU:
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Name:                    gfx1151                            
  Marketing Name:          AMD Radeon Graphics                
      Name:                    amdgcn-amd-amdhsa--gfx1151         
      Name:                    amdgcn-amd-amdhsa--gfx11-generic 
```





Below are the results from Debian 13 (Officially supported with ROCm 7.0.2) and Ubuntu 25.10 (Using upstream amdgpu with ROCm 7.0.2).   

```
# amd-smi 
+------------------------------------------------------------------------------+
| AMD-SMI 26.0.2+39589fda      amdgpu version: Linuxver ROCm version: 7.0.2    |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:c5:00.0    AMD Radeon Graphics | N/A        N/A   0             N/A/0 W |
|   0       0     N/A             N/A | N/A        N/A              161/512 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+
```

Debian 13 - amdgpu.gttsize=amdttm.page_pool_size (125GiB) , no deprecation warning present, and GTT set correctly to 125GiB, and no warning of conflicting values.

```
[    0.000000] Linux version 6.12.48+deb13-amd64 (debian-kernel@lists.debian.org) (x86_64-linux-gnu-gcc-14 (Debian 14.2.0-19) 14.2.0, GNU ld (GNU Binutils for Debian) 2.44) #1 SMP PREE
MPT_DYNAMIC Debian 6.12.48-1 (2025-09-20)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.12.48+deb13-amd64 root=UUID=1a6903bb-2dec-435d-845d-4f6e21505860 ro transparent_hugepage=always numa_balancing=disable amdgpu.gt
tsize=128000 amdttm.pages_limit=32768000 amdttm.page_pool_size=32768000
...
[    3.635701] amdgpu 0000:c5:00.0: amdgpu: VRAM: 512M 0x0000008000000000 - 0x000000801FFFFFFF (512M used)
[    3.635703] amdgpu 0000:c5:00.0: amdgpu: GART: 512M 0x00007FFF00000000 - 0x00007FFF1FFFFFFF
[    3.636121] [drm] amdgpu: 512M of VRAM memory ready
[    3.636122] [drm] amdgpu: 128000M of GTT memory ready.
```

Debian 13 - amdttm.page_pool_size (125GiB), no deprecation warning, GTT not set correctly (63973MiB)

```
[    0.000000] Linux version 6.12.48+deb13-amd64 (debian-kernel@lists.debian.org) (x86_64-linux-gnu-gcc-14 (Debian 14.2.0-19) 14.2.0, GNU ld (GNU Binutils for Debian) 2.44) #1 SMP PREE
MPT_DYNAMIC Debian 6.12.48-1 (2025-09-20)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.12.48+deb13-amd64 root=UUID=1a6903bb-2dec-435d-845d-4f6e21505860 ro transparent_hugepage=always numa_balancing=disable amdttm.pa
ges_limit=32768000 amdttm.page_pool_size=32768000
...
[    3.657645] amdgpu 0000:c5:00.0: amdgpu: VRAM: 512M 0x0000008000000000 - 0x000000801FFFFFFF (512M used)
[    3.657647] amdgpu 0000:c5:00.0: amdgpu: GART: 512M 0x00007FFF00000000 - 0x00007FFF1FFFFFFF
[    3.657841] [drm] amdgpu: 512M of VRAM memory ready
[    3.657851] [drm] amdgpu: 63973M of GTT memory ready.
```

```
+------------------------------------------------------------------------------+
| AMD-SMI 26.0.2+39589fda      amdgpu version: 6.17.0-5 ROCm version: 7.0.2    |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:c5:00.0  Radeon 8060S Graphics | N/A        N/A   0             N/A/0 W |
|   0       0     N/A             N/A | N/A        N/A              161/512 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+
```

Ubuntu 25.10 - amdgpu.gttsize=amdttm.page_pool_size (125GiB) , deprecation warning present, and GTT set correctly to 125GiB, and also a warning about conflicting values.
```
[    0.000000] Linux version 6.17.0-5-generic (buildd@lcy02-amd64-035) (x86_64-linux-gnu-gcc (Ubuntu 15.2.0-4ubuntu2) 15.2.0, GNU ld (GNU Binutils for Ubuntu) 2.45) #5-Ubuntu SMP PREEM
PT_DYNAMIC Mon Sep 22 10:00:33 UTC 2025 (Ubuntu 6.17.0-5.5-generic 6.17.0-rc7)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.17.0-5-generic root=UUID=cea76f55-f802-4ef3-a1cd-ebda84150293 ro transparent_hugepage=always amdgpu.gttsize=128000 amdttm.pages_
limit=32768000 amdttm.page_pool_size=32768000 numa_balancing=disable quiet splash crashkernel=2G-4G:320M,4G-32G:512M,32G-64G:1024M,64G-128G:2048M,128G-:4096M vt.handoff=7
...
[    3.368748] amdgpu 0000:c5:00.0: amdgpu: amdgpu: 512M of VRAM memory ready
[    3.368749] amdgpu 0000:c5:00.0: amdgpu: [drm] Configuring gttsize via module parameter is deprecated, please use ttm.pages_limit
[    3.368750] amdgpu 0000:c5:00.0: amdgpu: [drm] GTT size has been set as 134217728000 but TTM size has been set as 65867993088, this is unusual
[    3.368751] amdgpu 0000:c5:00.0: amdgpu: amdgpu: 128000M of GTT memory ready.
```
Ubuntu 25.10 - amdttm.page_pool_size (125GiB), no deprecation warning, GTT not set correctly (62816MiB)
```
[    0.000000] Linux version 6.17.0-5-generic (buildd@lcy02-amd64-035) (x86_64-linux-gnu-gcc (Ubuntu 15.2.0-4ubuntu2) 15.2.0, GNU ld (GNU Binutils for Ubuntu) 2.45) #5-Ubuntu SMP PREEM
PT_DYNAMIC Mon Sep 22 10:00:33 UTC 2025 (Ubuntu 6.17.0-5.5-generic 6.17.0-rc7)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-6.17.0-5-generic root=UUID=cea76f55-f802-4ef3-a1cd-ebda84150293 ro transparent_hugepage=always amdttm.pages_limit=32768000 amdttm.
page_pool_size=32768000 numa_balancing=disable quiet splash crashkernel=2G-4G:320M,4G-32G:512M,32G-64G:1024M,64G-128G:2048M,128G-:4096M vt.handoff=7
...
[    3.309617] amdgpu 0000:c5:00.0: amdgpu: VRAM: 512M 0x0000008000000000 - 0x000000801FFFFFFF (512M used)
[    3.309619] amdgpu 0000:c5:00.0: amdgpu: GART: 512M 0x00007FFF00000000 - 0x00007FFF1FFFFFFF
[    3.310034] amdgpu 0000:c5:00.0: amdgpu: amdgpu: 512M of VRAM memory ready
[    3.310035] amdgpu 0000:c5:00.0: amdgpu: amdgpu: 62816M of GTT memory ready.
```

### Operating System

Debian,  Ubuntu

### CPU

Strix Halo

### GPU

gfx1151

### ROCm Version

7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_