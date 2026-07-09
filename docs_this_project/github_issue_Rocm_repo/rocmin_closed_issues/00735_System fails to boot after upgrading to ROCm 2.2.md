# System fails to boot after upgrading to ROCm 2.2

- **Issue #:** 735
- **State:** closed
- **Created:** 2019-03-14T04:29:36Z
- **Updated:** 2019-03-14T23:48:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/735

Hi,

First of all, my system is:
-AMD Threadripper 1950X
-Vega FE*2 + Radeon VII
-ubuntu 18.04, kernel 4.18.0-16-generic

I just upgraded to ROCm 2.2, unfortunately that was done with apt upgrade so there are other items, thus I don't mean to be conclusive.

After the upgrade, I found the system failed to boot. I entered grub and tried to remove quiet splash to see through the log, unfortunately it froze at different point everytime, will all lines being shown saying "OK" in green.
Then, I followed some online guides to add "nomodeset" to grub, with that the systems boots normally. However, it doesn't load the GPUs in the kernel and I can't see them in clinfo anymore nor using them.

The new kernel 4.18.0-16 was installed on 03-07 and a reboot was done on 03-11 without any issues, so I assumed that wasn't the cause.
I tried to use autoremove to remove rocm, but the problem persists (after removal, still only nomodeset allows the system to boot). Could that be still related to ROCm? It would be great if you can confirm if the removal should have got rid of the cause, I shall forward this issue elsewhere.

The below is a list of upgrades installed on 2019-03-13, in case anything looked fishy, unfortunately it's quite long.

```
Start-Date: 2019-03-13  22:28:08
Commandline: apt upgrade
Requested-By: sandbo (1000)
Upgrade: hsa-rocr-dev:amd64 (1.1.9-49-g39f1af5, 1.1.9-55-gbac2a9b), 
libxcb-present-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
hsakmt-roct-dev:amd64 (1.0.9-111-gc65f2de, 1.0.9-121-g876627e), 
libseccomp2:amd64 (2.3.1-2.1ubuntu4, 2.3.1-2.1ubuntu4.1), 
hsakmt-roct:amd64 (1.0.9-111-gc65f2de, 1.0.9-121-g876627e), 
virtinst:amd64 (1:1.5.1-0ubuntu1.1, 1:1.5.1-0ubuntu1.2), 
libxcb-xfixes0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rock-dkms:amd64 (2.1-96, 2.2-31), 
rocm-opencl:amd64 (1.2.0-2019020110, 1.2.0-2019030702), 
libsystemd0:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libsystemd0:i386 (237-3ubuntu10.13, 237-3ubuntu10.15), 
hip_base:amd64 (1.5.19025, 1.5.19055), 
libxcb-present0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-present0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
hsa-ext-rocr-dev:amd64 (1.1.9-49-g39f1af5, 1.1.9-55-gbac2a9b), 
libxcb-xfixes0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocrand:amd64 (1.8.2, 1.8.2), rocfft:amd64 (0.8.9.0, 0.9.0.0), 
google-chrome-stable:amd64 (72.0.3626.121-1, 73.0.3683.75-1), 
hcc:amd64 (1.3.19045, 1.3.19092), 
udev:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libxcb-shm0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-shm0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-randr0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-render0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-render0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb1-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libudev1:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libudev1:i386 (237-3ubuntu10.13, 237-3ubuntu10.15), 
comgr:amd64 (1.1.0, 1.1.0), 
libtiff5:amd64 (4.0.9-5ubuntu0.1, 4.0.9-5ubuntu0.2), 
libtiff5:i386 (4.0.9-5ubuntu0.1, 4.0.9-5ubuntu0.2), 
libxcb-randr0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-dri3-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb1:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb1:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-shape0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libnss-myhostname:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libxcb-res0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-libs:amd64 (2.1.96, 2.2.31), 
systemd-sysv:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
rocm-dev:amd64 (2.1.96, 2.2.31), 
libxcb-xv0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-utils:amd64 (2.1.96, 2.2.31), 
libpam-systemd:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libxcb-render0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-shape0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
virt-manager:amd64 (1:1.5.1-0ubuntu1.1, 1:1.5.1-0ubuntu1.2), 
systemd:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
hip_doc:amd64 (1.5.19025, 1.5.19055), 
libnss-systemd:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
miopen-hip:amd64 (1.7.1, 1.7.1), 
rocm-device-libs:amd64 (0.0.1, 0.0.1), 
hip_hcc:amd64 (1.5.19025, 1.5.19055), 
rocm-opencl-dev:amd64 (1.2.0-2019020110, 1.2.0-2019030702), 
hip_samples:amd64 (1.5.19025, 1.5.19055), 
libxcb-sync-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
cxlactivitylogger:amd64 (5.6.7254, 5.6.7259), 
libxcb-dri2-0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-glx0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-glx0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-glx0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocprofiler-dev:amd64 (1.0.0, 1.0.0), 
libxcb-dri2-0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-dri2-0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-smi:amd64 (1.0.0-100-g3cacdb9, 1.0.0-102-gdb444a9), 
libxcb-dri3-0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-dri3-0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-dkms:amd64 (2.1.96, 2.2.31), 
libxcb-xkb1:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-sync1:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-sync1:i386 (1.13-1, 1.13-2~ubuntu18.04)
End-Date: 2019-03-13  22:29:28

```