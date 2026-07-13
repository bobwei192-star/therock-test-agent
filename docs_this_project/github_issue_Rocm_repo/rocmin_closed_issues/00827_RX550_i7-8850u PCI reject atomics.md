# RX550/i7-8850u PCI reject atomics

- **Issue #:** 827
- **State:** closed
- **Created:** 2019-06-24T01:36:48Z
- **Updated:** 2023-04-14T17:29:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/827

I have checked the ROCm supported hardware before purchasing the Samsung notebook NP940X5N. But still rocm driver is not working after apt-get install the rocm binary. Detailed info below. Can anyone guide what to debug next?

OS: Ubuntu 19.04

Intel® Core™ i7-8550U CPU @ 1.80GHz × 8 

lspci | grep Display
01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X] (rev c3)

dmesg | grep kfd
[    4.324747] kfd kfd: skipped device 1002:699f, PCI rejects atomics

dkms status
amdgpu, 2.5-27, 5.0.0-17-generic, x86_64: installed
