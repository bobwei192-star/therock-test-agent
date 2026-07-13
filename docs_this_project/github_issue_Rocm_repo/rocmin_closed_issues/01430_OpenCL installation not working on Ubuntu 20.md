# OpenCL installation not working on Ubuntu 20

- **Issue #:** 1430
- **State:** closed
- **Created:** 2021-03-26T21:32:02Z
- **Updated:** 2021-04-01T05:07:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/1430

Coming over from https://github.com/RadeonOpenCompute/ROCm/issues/1411 but I am opening a new ticket because that issue is trying to use an unsupported card. Long story short, the OpenCL installation on Ubuntu 20 does not appear to be working correctly. I am running a Vega Frontier Edition Air, so my card is supported. I uninstalled everything before starting the ROCm installation and it all went smoothly. The problem arises when I try to run the two installation confirmation checks:
```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```
Neither succeeds unless I run them as root with `sudo`. The first simply produces
```
ROCk module is loaded
Unable to open /dev/kfd read-write: Permission denied
aaron is member of render group
```
The second produces:
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3241.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```
If I prepend `sudo` to the commands, they produce the expected output.

This is more than simply the confirmation. When I try to run Luxmark or Blender, neither finds the graphics card as a valid OpenCL device. I tried running those applications as root in the hope that they would find the cards, but alas, no.

----

Editing to specify that I am using Ubuntu 20.04.2 LTS.