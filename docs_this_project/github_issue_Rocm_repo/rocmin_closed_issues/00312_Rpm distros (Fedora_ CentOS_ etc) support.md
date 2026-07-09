# Rpm distros (Fedora, CentOS, etc) support

- **Issue #:** 312
- **State:** closed
- **Created:** 2018-01-25T04:32:50Z
- **Updated:** 2018-03-04T16:16:33Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/312

Dear AMD devs!

PLEASE, please restore the `rpm` repository support for your `ROCm` project, as it were in release 1.6. A vast majority of Linux distros are left behind now.

I'm running Fedora 27 and can't manage the whole `ROCm` thing to work. My RX 480 and RX 580 GPUs are working just fine with 'legacy' OpenCL driver from AMDGPU-PRO 17.50. But `ROCm` doesn't 'see' nor my Vega, nor Polaris-based cards at all.

If I plug in my Vega 64, Linux kernel 4.11 provided by you in 1.6 release hangs on very early boot stage. I installed pre-release kernel v. 4.15 and dkms-patched (by AMDGPU-PRO 17.50) kernel v. 4.11.11 (from official Fedora 26 repo) and both of them are booting fine with Vega and 3D acceleration works. But ROCm driver bundled with AMDGPU-PRO 17.50 fails (to discover GPUs? or what?) in all cases.

That's why I'm asking kindly to build rpm packages for ROCm v. 1.7. Or should I just give up and install Ubuntu?

BTW, please clarify one question. My system is driven by AMD FX 8120 CPU. **Is it suitable for ROCm when I only want GPU (not CPU) OpenCL computing?**