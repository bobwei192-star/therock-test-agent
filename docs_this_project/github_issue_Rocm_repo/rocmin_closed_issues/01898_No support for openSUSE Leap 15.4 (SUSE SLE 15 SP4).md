# No support for openSUSE Leap 15.4 (SUSE SLE 15 SP4)

- **Issue #:** 1898
- **State:** closed
- **Created:** 2023-01-25T16:02:39Z
- **Updated:** 2023-11-10T16:41:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/1898

ROCm folders for SLE 15 SP4 & Leap 15.4 are deleted today (20230125) at https://repo.radeon.com/rocm/zyp/ . Now only 15.3 packages are available. But support for openSUSE 15.3 is ended in December 2022.
Moreover, ROCm 5.4.1 didn't work with Leap 15.4 when it was available - clinfo reported "Number of devices = 0".

After installing ROCm 5.3.3 (rocm-opencl-runtime) for Leap 15.3 clinfo reports availability for devices, but OpenCL applications don't work due to incompatibility.

OpenCL PAL drivers from 20.40 still work OK.

I cannot report bug to AMD Community - https://community.amd.com/t5/discussions/bd-p/amd-rocm-discussions has too strict requirements for posting.

```
:~> clinfo
Number of platforms 1
Platform Name AMD Accelerated Parallel Processing
Platform Vendor Advanced Micro Devices, Inc.
Platform Version OpenCL 2.1 AMD-APP (3486.0)
Platform Profile FULL_PROFILE
Platform Extensions cl_khr_icd cl_amd_event_callback
Platform Extensions function suffix AMD
Platform Host timer resolution 1ns

Platform Name AMD Accelerated Parallel Processing
Number of devices 1
Device Name gfx902:xnack+
Device Vendor Advanced Micro Devices, Inc.
Device Vendor ID 0x1002
Device Version OpenCL 2.0
Driver Version 3486.0 (HSA1.1,LC)
Device OpenCL C Version OpenCL C 2.0
Device Type GPU​
...
```
