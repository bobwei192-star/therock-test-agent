# ROCk module is NOT loaded, possibly no GPU devices on Radeon RX 6700S

- **Issue #:** 1794
- **State:** closed
- **Created:** 2022-08-21T08:51:26Z
- **Updated:** 2024-02-16T16:38:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/1794

Hi all,

I have followed the steps on this page to install ROCm v5.2.3 using the installer:
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.2.3/page/How_to_Install_ROCm.html

Running` /opt/rocm-5.2.3/bin/rocminfo` I get:

`ROCk module is NOT loaded, possibly no GPU devices`

Noting I am using Ubuntu 20.4 on WSL2. 

As far as I am concerned, ROCm should support RDNA GPUs like the RX 6700s series, is that correct?

What do you think went wrong?



