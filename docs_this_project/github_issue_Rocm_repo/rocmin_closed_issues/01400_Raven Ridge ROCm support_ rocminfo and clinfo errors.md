# Raven Ridge ROCm support: rocminfo and clinfo errors

- **Issue #:** 1400
- **State:** closed
- **Created:** 2021-03-05T10:40:09Z
- **Updated:** 2021-03-08T05:43:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/1400

Hi,

## Error description

I have the following errors after installing ROCm in Ubuntu 20.04.1, kernel 5.4.0-66 in a Raven Ridge platform:

*  `rocminfo`:

```
/opt/rocm/bin/rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Bad address
qtec is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

With `strace`:

```
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 EFAULT (Bad address)
```

Context:

```
...
recvfrom(5, "{\"error\":\"io.systemd.UserDatabas"..., 131080, MSG_DONTWAIT, NULL, NULL) = 66
epoll_ctl(6, EPOLL_CTL_MOD, 5, {0, {u32=1307226368, u64=94181350093056}}) = 0
epoll_wait(6, [], 4, 0)                 = 0
epoll_wait(6, [], 4, 0)                 = 0
epoll_ctl(6, EPOLL_CTL_DEL, 5, NULL)    = 0
close(5)                                = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
close(6)                                = 0
close(7)                                = 0
write(1, "\33[37mqtec is member of render gr"..., 40qtec is member of render group
) = 40
getpid()                                = 3103
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 EFAULT (Bad address)
write(1, "\33[31mhsa api call failure at: /s"..., 61hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
) = 61
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -335, SEEK_CUR)                = -1 ESPIPE (Illegal seek)
exit_group(4104)                        = ?
+++ exited with 8 +++
```


*  `clinfo`: Doesn't work either:

```
qtec@qtec-QT5222:~$ clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3212.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```

Is it Raven Ridge really supported? ROCm documentation describes this platform as 'Limited support'. What does it mean?

According to the ROCm documentation:

> The integrated GPUs in AMD APUs are not officially supported targets for ROCm. As described below, "Carrizo", "Bristol Ridge", and "Raven Ridge" APUs are enabled in our upstream drivers and the ROCm OpenCL runtime. However, they are not enabled in the HIP runtime, and may not work due to motherboard or OEM hardware limitations. As such, they are not yet officially supported targets for ROCm.
> ...
> 
> Not supported or limited support under ROCm
> 
> Limited support
> 
> AMD "Raven Ridge" APUs are enabled to run OpenCL, but do not yet support HIP or our libraries built on top of these compilers and runtimes.
> 
>     As of ROCm 2.1, "Raven Ridge" requires the use of upstream kernel drivers.
>     In addition, various "Raven Ridge" platforms may not work due to OEM and ODM choices when it comes to key configurations parameters such as inclusion of the required CRAT tables and IOMMU configuration parameters in the system BIOS.
>     Before purchasing such a system for ROCm, please verify that the BIOS provides an option for enabling IOMMUv2 and that the system BIOS properly exposes the correct CRAT table. Inquire with your vendor about the latter.


I can see the iommu is enabled in the BIOS and then check the following:

*  IOMMUv2:

```
sudo lsmod | grep iommu
amd_iommu_v2           20480  1 amdgpu
```

```
qtec@qtec-QT5222:~/acpitables$ sudo dmesg | grep -i iommu
[    0.566029] iommu: Default domain type: Translated 
[    0.736370] pci 0000:00:00.2: AMD-Vi: Unable to read/write to IOMMU perf counter.
[    0.736754] pci 0000:00:01.0: Adding to iommu group 0
[    0.736862] pci 0000:00:01.1: Adding to iommu group 1
[    0.736973] pci 0000:00:01.2: Adding to iommu group 2
[    0.737084] pci 0000:00:08.0: Adding to iommu group 3
[    0.737182] pci 0000:00:08.1: Adding to iommu group 4
[    0.737286] pci 0000:00:08.2: Adding to iommu group 5
[    0.737376] pci 0000:00:14.0: Adding to iommu group 6
[    0.737400] pci 0000:00:14.3: Adding to iommu group 6
[    0.737518] pci 0000:00:18.0: Adding to iommu group 7
[    0.737542] pci 0000:00:18.1: Adding to iommu group 7
[    0.737565] pci 0000:00:18.2: Adding to iommu group 7
[    0.737589] pci 0000:00:18.3: Adding to iommu group 7
[    0.737612] pci 0000:00:18.4: Adding to iommu group 7
[    0.737635] pci 0000:00:18.5: Adding to iommu group 7
[    0.737657] pci 0000:00:18.6: Adding to iommu group 7
[    0.737680] pci 0000:00:18.7: Adding to iommu group 7
[    0.737842] pci 0000:03:00.0: Adding to iommu group 8
[    0.737932] pci 0000:03:00.0: Using iommu direct mapping
[    0.737991] pci 0000:03:00.1: Adding to iommu group 9
[    0.738089] pci 0000:03:00.2: Adding to iommu group 10
[    0.738185] pci 0000:03:00.3: Adding to iommu group 11
[    0.738287] pci 0000:03:00.4: Adding to iommu group 12
[    0.738369] pci 0000:03:00.5: Adding to iommu group 13
[    0.738491] pci 0000:03:00.7: Adding to iommu group 14
[    0.738579] pci 0000:04:00.0: Adding to iommu group 15
[    0.738696] pci 0000:04:00.1: Adding to iommu group 16
[    0.738783] pci 0000:04:00.2: Adding to iommu group 17
[    0.739100] pci 0000:00:00.2: AMD-Vi: Found IOMMU cap 0x40
[    3.193014] AMD-Vi: AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
```

* CRAT table:

```
sudo acpidump -b
```

[crat.dat](https://drive.google.com/file/d/1ccTOyF8Ms0N_DCc_NPLyU_nY6o36xWnR/view?usp=sharing)

> BIOS properly exposes the correct CRAT table.

How do I know if it is the correct CRAT table? could the issue be related with a wrong table?

## System/hardware information

```
03:00.0 "VGA compatible controller" "Advanced Micro Devices, Inc. [AMD/ATI]" "Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series]" -r83 "Advanced Micro Devices, Inc. [AMD/ATI]" "Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series]"
```

*  `CPU: AMD Ryzen Embedded V1605B with Radeon Vega Gfx (8) @ 2.000GHz`
*  `GPU: AMD ATI Radeon Vega Series / Radeon Vega Mobile Series`

```
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
```

```
Linux qtec-QT5222 5.4.0-66-generic #74-Ubuntu SMP Wed Jan 27 22:54:38 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

```
edac_mce_amd           32768  0
amdgpu               5824512  4
amd_iommu_v2           20480  1 amdgpu
amd_sched              32768  1 amdgpu
amdttm                102400  1 amdgpu
amdkcl                 24576  2 amdttm,amdgpu
drm_kms_helper        184320  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
drm                   491520  8 drm_kms_helper,amd_sched,amdttm,amdgpu,amdkcl
amd_xgbe              184320  0
i2c_amd_mp2_pci        20480  0
```

```
[    3.774178] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    3.775259] kfd kfd: amdgpu: added device 1002:15dd
```





