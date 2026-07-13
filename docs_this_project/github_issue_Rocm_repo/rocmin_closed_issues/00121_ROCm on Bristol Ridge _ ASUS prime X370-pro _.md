# ROCm on Bristol Ridge + ASUS prime X370-pro ?

- **Issue #:** 121
- **State:** closed
- **Created:** 2017-05-15T12:44:03Z
- **Updated:** 2017-08-30T22:35:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/121

Is there any experience with runing ROCm-1.5.x on Bristol Ridge (A12-9800) + ASUS Prime X370-Pro? I use Fedora 25. The ROCK 4.9.0 kernel seems to have a problem with this hardware setup: Lightdm login manager or X launched from text console via startx hangs the machine after one or two seconds.
The ROCR example/test program crashes with
```
./vector_copy 
Profiling of privileged counters is not available
Profiling is not available
CPU Node [1] has no GPU connected
vector_copy: /home/heid/sonst/ROCR-Runtime/src/core/runtime/amd_topology.cpp:178: void amd::BuildTopology(): Assertion `!(cpu == NULL && gpu == NULL)' failed.
```
Is there any way to fix that?
I use kernel parameters "amd_iommu=on iommu=pt" - is this advisable?

The relevant kernel modules seem to be there
```
lsmod | grep amd -i
amdkfd                219075  1
amd_iommu_v2            8347  1 amdkfd
amdgpu               1441978  1
edac_mce_amd           19427  0
ttm                    87495  1 amdgpu
drm_kms_helper        139401  1 amdgpu
drm                   327504  4 amdgpu,ttm,drm_kms_helper
i2c_algo_bit            6079  2 igb,amdgpu
```
and IOMMUv2 is present:
```Hi,
dmesg | grep iommu -i
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.9.0 root=UUID=401c6f91-f069-42b4-856e-1f24b13edda3 ro amd_iommu=on iommu=pt
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.9.0 root=UUID=401c6f91-f069-42b4-856e-1f24b13edda3 ro amd_iommu=on iommu=pt
[    0.964991] AMD-Vi: IOMMU performance counters supported
[    0.965918] iommu: Adding device 0000:00:01.0 to group 0
[    0.966108] iommu: Using direct mapping for device 0000:00:01.0
[    0.966244] iommu: Adding device 0000:00:01.1 to group 0
[    0.966420] iommu: Adding device 0000:00:02.0 to group 1
[    0.966555] iommu: Using direct mapping for device 0000:00:02.0
[    0.966676] iommu: Adding device 0000:00:02.4 to group 1
[    0.966800] iommu: Adding device 0000:00:02.5 to group 1
[    0.966964] iommu: Adding device 0000:00:03.0 to group 2
[    0.967082] iommu: Using direct mapping for device 0000:00:03.0
[    0.967220] iommu: Adding device 0000:00:08.0 to group 3
[    0.967337] iommu: Using direct mapping for device 0000:00:08.0
[    0.967481] iommu: Adding device 0000:00:09.0 to group 4
[    0.967597] iommu: Using direct mapping for device 0000:00:09.0
[    0.967699] iommu: Adding device 0000:00:09.2 to group 4
[    0.967844] iommu: Adding device 0000:00:10.0 to group 5
[    0.967960] iommu: Using direct mapping for device 0000:00:10.0
[    0.968113] iommu: Adding device 0000:00:11.0 to group 6
[    0.968247] iommu: Using direct mapping for device 0000:00:11.0
[    0.968408] iommu: Adding device 0000:00:14.0 to group 7
[    0.968540] iommu: Using direct mapping for device 0000:00:14.0
[    0.968658] iommu: Adding device 0000:00:14.3 to group 7
[    0.968856] iommu: Adding device 0000:00:18.0 to group 8
[    0.968997] iommu: Using direct mapping for device 0000:00:18.0
[    0.969110] iommu: Adding device 0000:00:18.1 to group 8
[    0.969211] iommu: Adding device 0000:00:18.2 to group 8
[    0.969313] iommu: Adding device 0000:00:18.3 to group 8
[    0.969413] iommu: Adding device 0000:00:18.4 to group 8
[    0.969512] iommu: Adding device 0000:00:18.5 to group 8
[    0.969610] iommu: Adding device 0000:05:00.0 to group 1
[    0.969705] iommu: Adding device 0000:05:00.1 to group 1
[    0.969807] iommu: Adding device 0000:05:00.2 to group 1
[    0.969905] iommu: Adding device 0000:1d:00.0 to group 1
[    0.970014] iommu: Adding device 0000:1d:02.0 to group 1
[    0.970128] iommu: Adding device 0000:1d:03.0 to group 1
[    0.970244] iommu: Adding device 0000:1d:04.0 to group 1
[    0.970358] iommu: Adding device 0000:1d:06.0 to group 1
[    0.970472] iommu: Adding device 0000:1d:07.0 to group 1
[    0.970592] iommu: Adding device 0000:25:00.0 to group 1
[    0.970713] iommu: Adding device 0000:26:00.0 to group 1
[    0.970834] iommu: Adding device 0000:28:00.0 to group 1
[    0.971461] AMD-Vi: Found IOMMU at 0000:00:00.2 cap 0x40
[    0.974898] perf: amd_iommu: Detected. (0 banks, 0 counters/bank)
[    6.102064] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
```
