# clinfo  gives terminate called after throwing an instance of 'cl::Error'

- **Issue #:** 511
- **State:** closed
- **Created:** 2018-08-23T22:31:05Z
- **Updated:** 2018-08-25T06:33:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/511

Hi All, 
im having some issues getting Vega 56/64 GPUs to show up in platforms

Ubuntu 16.04 with kerenl 4.13
mainboard/ CPU are all PCIE 3.0 compatible.


**i can sun "/opt/rocm/bin/rocminfo " successfully and lists all the GPUs. however when running "/opt/rocm/opencl/bin/x86_64/clinfo" i get:**

:~$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)


**running "/opt/rocm/bin/rocm-smi -hw" gives:**

 GPU  DID    ECC        VBIOS
  5   687f   N/A   113-D0500100-103
  3   687f   N/A   113-D0500300-102
  1   687f   N/A   113-D0500100-104
  6   687f   N/A   113-D0500100-102
  4   687f   N/A   113-D0500350-102
  2   687f   N/A   113-D0500100-104
  0   1902   N/A   None





**i can verify the installation of ROCm:**

:~$ apt show rocm-libs -a
Package: rocm-libs
Version: 1.8.192
Priority: optional
Section: devel
Maintainer: Advanced Micro Devices Inc.
Installed-Size: 13.3 kB
Depends: rocfft, rocrand, hipblas, rocblas
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 772 B
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack



:~$ dmesg | grep kfd
[    1.618386] kfd kfd: Initialized module
[    3.753602] kfd kfd: Allocated 3969056 bytes on gart
[    3.753739] kfd kfd: added device 1002:687f
[    5.742944] kfd kfd: Allocated 3969056 bytes on gart
[    5.743203] kfd kfd: added device 1002:687f
[    7.775265] kfd kfd: Allocated 3969056 bytes on gart
[    7.775648] kfd kfd: added device 1002:687f
[    9.754696] kfd kfd: Allocated 3969056 bytes on gart
[    9.755192] kfd kfd: added device 1002:687f
[   11.800216] kfd kfd: Allocated 3969056 bytes on gart
[   11.800847] kfd kfd: added device 1002:687f
[   13.807090] kfd kfd: Allocated 3969056 bytes on gart
[   13.807851] kfd kfd: added device 1002:687f


any help would be much appreciated