# Update to Rocm 2.1 broke Opencl

- **Issue #:** 702
- **State:** closed
- **Created:** 2019-02-08T23:24:14Z
- **Updated:** 2021-01-07T05:26:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/702

Upon updating to ROCm 2.1 my system on reboot I received the error "UVD not responding trying to reset the VCPU". I restarted and booted from a lower kernel version and was able to boot, however, I am having issues starting OpenCL where whatever application I launch using OpenCL hangs. Using blender switching to Cycles, or going to preferences clicking the system tab hangs blender. Going to the konsole and doing CLinfo also hangs. I uninstalled and reinstalled and am continuing to have the same issue. 

Also does ROCm support kernel 4.20? 

Kernel version: 4.18.20
OS: Kubuntu 18.10
GPU1: AMD Fury X
GPU2: AMD Firepro w8100  