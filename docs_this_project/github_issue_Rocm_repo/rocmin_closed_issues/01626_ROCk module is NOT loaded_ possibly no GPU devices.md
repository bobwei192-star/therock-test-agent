# ROCk module is NOT loaded, possibly no GPU devices

- **Issue #:** 1626
- **State:** closed
- **Created:** 2021-11-24T02:22:13Z
- **Updated:** 2024-01-20T02:47:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1626

Hi, I am appreciate to use this excellent products.I tried to install rocm packages in my machine,but I met a proplem.
There is my configuration:

1. Linux Distribution Information

> uname -m && cat /etc/*release

x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.6 LTS"
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic

2. Kernel Information

> uname -srmv

Linux 5.4.0-90-generic #101~18.04.1-Ubuntu SMP Fri Oct 22 09:25:04 UTC 2021 x86_64

3. My GPU
AMD Radeon(TM) Vage 10 Graphics with PCI\VEN_1002&DEV_15DD&SUBSYS_83DA103C&REV_D0

> sudo lshw -class display

*-display                 
       description: VGA compatible controller
       product: SVGA II Adapter
       vendor: VMware
       physical id: f
       bus info: pci@0000:00:0f.0
       version: 00
       width: 32 bits
       clock: 33MHz
       capabilities: vga_controller bus_master cap_list rom
       configuration: driver=vmwgfx latency=64
       resources: irq:16 ioport:1070(size=16) memory:e8000000-efffffff memory:fe000000-fe7fffff memory:c0000-dffff

I followed the steps of the installation guide and didn't have any problems until`/opt/rocm-4.5.0/bin/rocminfo`:
> /opt/rocm-4.5.0/bin/rocminfo

ROCk module is NOT loaded, possibly no GPU devices

> /opt/rocm-4.5.0/opencl/bin/clinfo

Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.2 AMD-APP (3361.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0

I looked [issue#1404](https://github.com/RadeonOpenCompute/ROCm/issues/1404), I tried to run:
> dmesg | grep kfd

I got nothing.

> dmesg | grep amd

[    0.000000] Linux version 5.4.0-90-generic (buildd@lcy01-amd64-026) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #101~18.04.1-Ubuntu SMP Fri Oct 22 09:25:04 UTC 2021 (Ubuntu 5.4.0-90.101~18.04.1-generic 5.4.148)

I tried re-install again, but I met the same wrong.Can you help me? Thank you.