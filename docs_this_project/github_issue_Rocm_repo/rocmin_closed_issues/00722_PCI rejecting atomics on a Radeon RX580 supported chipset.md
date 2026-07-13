# PCI rejecting atomics on a Radeon RX580 supported chipset

- **Issue #:** 722
- **State:** closed
- **Created:** 2019-02-28T22:31:56Z
- **Updated:** 2024-10-02T11:15:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/722

I am attempting to use ROCm on a large 50+ GPU RX580 cluster and the README lists the RX580's as a supported chipset:
> ROCm officially supports AMD GPUs that use following chips:
> GFX8 GPUs
> "Fiji" chips, such as on the AMD Radeon R9 Fury X and Radeon Instinct MI8
> "Polaris 10" chips, such as on the AMD **Radeon RX 580** and Radeon Instinct MI6
> "Polaris 11" chips, such as on the AMD Radeon RX 570 and Radeon Pro WX 4100
> "Polaris 12" chips, such as on the AMD Radeon RX 550 and Radeon RX 540

I first noticed the problem when got this error code:
`hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104`

I'm on Ubuntu Server 18.04.1 using the 4.15.0-45-generic kernel:
`Linux host 4.15.0-45-generic #48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux`

After installing ROCm without any issues _dmesg | grep kfd_ returns the following:
```
[    5.737933] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[output omitted]
```
Output of _lspci -nn_ to show that my chipset is in fact an RX580:
```
01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X] [1002:67df] (rev e7)
01:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580] [1002:aaf0]
[output omitted]
```
What am I missing? Are there steps that I can take to remedy this? Thanks in advance!