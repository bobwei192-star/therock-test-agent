# ASUS A88XM-A (BIOS: 3001) + A10-7850K Xorg screen corruption/hang with Ubuntu 16.04 + ROCm 1.4

- **Issue #:** 66
- **State:** closed
- **Created:** 2017-01-01T15:14:26Z
- **Updated:** 2017-01-04T03:19:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/66

Hi,

Recently I tried to upgrade my system (HW: ASUS A88XM-A BIOS: 3001, IOMMUv2 enabled + A10-7850K, the DVI display is used with a ATEN Advance Tech Inc. CS-64U KVM) to Ubuntu 16.04 from Ubuntu 14.04, however I ran into some issue. The system right now works perfectly (Xorg + HSA) with an earlier ROCm version.

```
ii  linux-headers-4.4.0-kfd-compute-rocm-rel-1.1.1-10                4.4.0-kfd-compute-rocm-rel-1.1.1-10-1                  amd64        Linux kernel headers for 4.4.0-kfd-compute-rocm-rel-1.1.1-10 on amd64
ii  linux-image-4.4.0-kfd-compute-rocm-rel-1.1.1-10                  4.4.0-kfd-compute-rocm-rel-1.1.1-10-1                  amd64        Linux kernel, version 4.4.0-kfd-compute-rocm-rel-1.1.1-10
ii  rocm                                                             1.1.2                                                  amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-dev                                                         1.1.2                                                  amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-kernel                                                      1.1.1                                                  amd64        Radeon Open Compute (ROCm) drivers
ii  rocm-smi                                                         1.0.0                                                  amd64        System Management Interface for ROCm
```

However the same system with a new Ubuntu 16.04 + ROCm 1.4 installation is not working correctly. The HSA example (vectory_copy) seems to works correctly without errors, but the screen show some kind of corrupted image (please see the attachment). The strace showed that the Xorg process is waiting on select syscall. The system will hang on the "service lightdm restart" command. I have attached both the dmesg both the Xorg log and a screenshot about the screen corruption/hang.

![2017101154457](https://cloud.githubusercontent.com/assets/8523206/21581667/d6595c48-d03b-11e6-96c8-2ebe29953cbb.png)
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/680041/dmesg.txt)

[Xorg.0.log.txt](https://github.com/RadeonOpenCompute/ROCm/files/680044/Xorg.0.log.txt)

Any idea how to fix the screen corruption/hang?

Thanks for your help,
Best Regards,
Zoltan
