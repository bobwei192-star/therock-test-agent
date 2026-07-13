# ROCk module is NOT loaded, possibly no GPU devices in ubuntu18.04 LTS

- **Issue #:** 1656
- **State:** closed
- **Created:** 2022-01-12T08:31:45Z
- **Updated:** 2022-02-02T07:10:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/1656

I am currently trying to install rocm on the aws g4ad (Radeon Pro V520) instance, but the following error occurs.

1. info1
> ubuntu@ip-172-31-46-201:~$ uname -m && cat /etc/*release

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

2. info2
> ubuntu@ip-172-31-46-201:~$ uname -a

Linux ip-172-31-46-201 5.4.0-1061-aws #64~18.04.1-Ubuntu SMP Fri Dec 3 17:59:13 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux


3. info3
> dmesg | grep kfd

nothing 

> dmesg | grep amd

[    0.000000] Linux version 5.4.0-1061-aws (buildd@lcy01-amd64-018) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #64~18.04.1-Ubuntu SMP Fri Dec 3 17:59:13 UTC 2021 (Ubuntu 5.4.0-1061.64~18.04.1-aws 5.4.157)
[    3.257253] amdkcl: loading out-of-tree module taints kernel.
[    3.263107] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    3.367302] amdgpu: Unknown symbol amd_iommu_bind_pasid (err -2)
[    3.372601] amdgpu: Unknown symbol amd_iommu_set_invalidate_ctx_cb (err -2)
[    3.377680] amdgpu: Unknown symbol amd_iommu_free_device (err -2)
[    3.383345] amdgpu: Unknown symbol amd_iommu_unbind_pasid (err -2)
[    3.395251] amdgpu: Unknown symbol amd_iommu_init_device (err -2)
[    3.400283] amdgpu: Unknown symbol amd_iommu_set_invalid_ppr_cb (err -2)
[    8.302375] amdgpu: Unknown symbol amd_iommu_bind_pasid (err -2)
[    8.303030] amdgpu: Unknown symbol amd_iommu_set_invalidate_ctx_cb (err -2)
[    8.303949] amdgpu: Unknown symbol amd_iommu_free_device (err -2)
[    8.305159] amdgpu: Unknown symbol amd_iommu_unbind_pasid (err -2)
[    8.305214] amdgpu: Unknown symbol amd_iommu_init_device (err -2)
[    8.306291] amdgpu: Unknown symbol amd_iommu_set_invalid_ppr_cb (err -2)








## - I followed this tutorial though and got the following issue.
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#installing-a-rocm-package-from-a-debian-repository
> /opt/rocm/bin/rocminfo

ROCk module is NOT loaded, possibly no GPU devices



 > /opt/rocm/opencl/bin/clinfo

Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3305.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0





Is there any way to solve this problem? please. thank you
