# Radeon VII not working with Raven Ridge APU

- **Issue #:** 740
- **State:** closed
- **Created:** 2019-03-15T19:56:39Z
- **Updated:** 2019-03-15T21:04:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/740

Hello,

I have been unable to find a Rocm/kernel version combination that will support my Radeon VII on a Raven Ridge system.

I have been able to use the integrated graphics in my Raven Ridge 2200G APU to run OpenCL code, using Rocm 2.1 and the 4.18 kernel. The system had no other GPU at the time. Everything seemed to work well.

Since then, I have installed a Radeon VII, and now neither device is usable in Rocm. Though in most cases Rocm installation appears to be successful, I have been unable to get any device to enumerate in /opt/rocm/opencl/bin/x86_64/clinfo.  I've tried kernels 4.15 and 4.18, and Rocm versions 2.0 through 2.2. Depending on the combination used, the errors include #1001 (Not found), or "Segmentation fault (core dumped)"

Has the Rocm team tested a Vega20 device on a Raven Ridge platform? If so, what Rocm and kernel versions are supposed to work together?

Although I had intended to use the Raven graphics to drive monitors and the VII to run compute kernels, I'd be happy if I could get the Radeon VII working on its own. Unfortunately, disabling the integrated graphics in BIOS doesn't seem to help.

Thanks!