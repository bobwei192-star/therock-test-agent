# OpenCL on Linux: state of AMD drivers is now worse than it was back in the days of fglrx [SOLUTIONS]

- **Issue #:** 1660
- **State:** closed
- **Created:** 2022-01-25T18:42:45Z
- **Updated:** 2022-02-07T11:22:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1660

OpenCL on Linux : state of AMD drivers is now worse than it was back in the days of fglrx

* The last version of AMD OpenCL PAL for GCN5 generation and later dates back from Septembre 29 of 2020. The recent versions of the proprietary AMGPU-PRO driver do not support OpenCL for GCN5 hardware.
* The last version of AMD OpenCL Orca (“legacy”) for GCN1, 2, and 3 dates back from June 21 of 2021. The last verions of the proprietary AMDGPU-PRO driver do not support OpenCL for those cards. I don't know if it's a mistake, because this driver is still provided bu does not support GCN1, 2 and 3 (and I don't have GCN4 to do tests).
* ROCm/ROCr isn't for usual users, it seems developped for specific industrial usages, it [does not support graphical applications](https://github.com/RadeonOpenCompute/ROCm/issues/1397) (AMD said it's temporary but that can last for a long time) and only supports a very small amount of hardware : a tiny selection of PCIe graphics cards and no one integrated graphics solution from AMD APUs. Currently [only three chips](https://github.com/RadeonOpenCompute/ROCm/blob/c3f91afb2688deb638c360497e35b249f8026667/README.md#hardware-and-software-support) are said to be supported by ROCm.

I tell more about the situation here:

https://rebuild.sh/post/2022-01-25-OpenCL_on_Linux_state_of_AMD_drivers_is_now_worse_than_it_was_back_in_the_days_of_fglrx/

Here I maintain a script for Ubuntu to install last working Orca, last working PAL, ROCm (if you're feeling lucky), last working Clover (if you don't need image support), and also old AMD OpenCL APP for CPU:

> https://gitlab.com/illwieckz/i-love-compute#scripts