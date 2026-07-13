# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104

- **Issue #:** 624
- **State:** closed
- **Created:** 2018-11-26T10:40:28Z
- **Updated:** 2019-04-15T20:06:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/624

Hi, I am trying to install ROCm 1.9.2 on desktop with vega10
CPU AMD Ryzen 7 1700 Eight-Core Processor

> uname -a
Linux wukong 4.4.0-139-generic #165-Ubuntu SMP Wed Oct 24 10:58:50 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

> dmesg | grep amd
[    0.000000] Linux version 4.4.0-139-generic (buildd@lcy01-amd64-006) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10) ) #165-Ubuntu SMP Wed Oct 24 10:58:50 UTC 2018 (Ubuntu 4.4.0-139.165-generic 4.4.160)
[    0.566793] amd_nb: Cannot enumerate AMD northbridges
[    0.988289] perf: amd_iommu: Detected. (0 banks, 0 counters/bank)

> lspci | grep -i vga
0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)

> dkms status
amdgpu, 1.9-307: added

The rocminfo doesn't work, and looks the gpu driver is not installed correctly.
Do you have any suggestion on this issue? Thanks.