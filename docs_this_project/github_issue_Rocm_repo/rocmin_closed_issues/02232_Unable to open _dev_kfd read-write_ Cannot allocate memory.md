# Unable to open /dev/kfd read-write: Cannot allocate memory

- **Issue #:** 2232
- **State:** closed
- **Created:** 2023-06-09T12:50:04Z
- **Updated:** 2023-11-10T16:24:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/2232

As I try: 

`rocminfo

ROCk module is loaded

Unable to open /dev/kfd read-write: Cannot allocate memory

igor is member of render group

hsa api call failure at: /src/rocminfo/rocminfo.cc:1142

Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
`

look into dmesg: 

`sudo dmesg | grep kfd

[    3.548555] kfd kfd: amdgpu: PITCAIRN  not supported in kfd
`
Info: 

`uname -r

5.4.0-54-generic
`
`lspci | grep VGA

01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
`

I've been using this guidance here: https://github.com/Grench6/RX580-rocM-tensorflow-ubuntu20.4-guide

Thanks in advance for help! 