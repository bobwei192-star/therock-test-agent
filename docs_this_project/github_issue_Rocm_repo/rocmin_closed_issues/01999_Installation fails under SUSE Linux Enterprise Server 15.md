#  Installation fails under SUSE Linux Enterprise Server 15

- **Issue #:** 1999
- **State:** closed
- **Created:** 2023-03-29T12:13:56Z
- **Updated:** 2024-03-09T01:49:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/1999

On a fresh install of SUSE Linux Enterprise Server 15 SP4, I get the following error after registering the appropriate repos and trying to install:
```
mate@MATTY-GA402RK:~> sudo zypper install amdgpu-dkms rocm-hip-libraries
Loading repository data...
Reading installed packages...
Resolving package dependencies...
2 Problems:
Problem: nothing provides 'gcc' needed by the to be installed amdgpu-dkms-1:5.18.13.50400-1510348.noarch
Problem: nothing provides 'libLLVM7 >= 7.0.1' needed by the to be installed rocblas-2.46.0.50400-sles153.72.x86_64

Problem: nothing provides 'gcc' needed by the to be installed amdgpu-dkms-1:5.18.13.50400-1510348.noarch
 Solution 1: do not install amdgpu-dkms-1:5.18.13.50400-1510348.noarch
 Solution 2: break amdgpu-dkms-1:5.18.13.50400-1510348.noarch by ignoring some of its dependencies
```