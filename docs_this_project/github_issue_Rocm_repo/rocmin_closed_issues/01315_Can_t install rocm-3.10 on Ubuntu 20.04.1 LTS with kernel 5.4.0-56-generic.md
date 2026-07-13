# Can't install rocm-3.10 on Ubuntu 20.04.1 LTS with kernel 5.4.0-56-generic

- **Issue #:** 1315
- **State:** closed
- **Created:** 2020-12-02T04:17:26Z
- **Updated:** 2020-12-14T06:10:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1315

First off, I don't know if this is the appropriate place for this but I first ran into this error when trying to install rocm-3.10. I'm getting a similar error to that [listed here](https://community.amd.com/t5/drivers-software/can-t-install-amdgpu-drivers-on-ubuntu-20-04-1-5-4-0-56-generic/m-p/426676).

I can't install rock-dkms, rocm-dkms, or rocm-dev via apt. Similarly when trying to install the Radeon Software for Linux 20.20 Release using the amdgpu-install script, which tries to install amdgpu-dkms. I run into the same issue of this snippet:

```
...
Setting up amdgpu-dkms (1:5.6.0.15-1098277) ...
Loading new amdgpu-5.6.0.15-1098277 DKMS files...
Building for 5.4.0-56-generic
Building for architecture x86_64
Building initial module for 5.4.0-56-generic
Error! Bad return status for module build on kernel: 5.4.0-56-generic (x86_64)
Consult /var/lib/dkms/amdgpu/5.6.0.15-1098277/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
dpkg: dependency problems prevent configuration of amdgpu:
 amdgpu depends on amdgpu-dkms (= 1:5.6.0.15-1098277); however:
  Package amdgpu-dkms is not configured yet.

dpkg: error processing package amdgpu (--configure):
 dependency problems - leaving unconfigured
...
```

I've attached the make log here: [make.log](https://github.com/RadeonOpenCompute/ROCm/files/5626862/make.log)

It looks like it's complaining about some ‘pci_platform_rom’ function not being defined. I wasn't able to find that function anywhere in the included source files under /var/lib/dkms/amdgpu/source, but I was able to find it under the [ROCK-Kernel repo](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/36767d92bdfecb49f2c5f112285b483549420267/drivers/pci/rom.c).

If anyone can help me figure out what's wrong here or what I can do to fix it, I would greatly appreciate it.