# Installing rock-dkms breaks HDMI / DisplayPort audio

- **Issue #:** 881
- **State:** closed
- **Created:** 2019-09-01T20:54:45Z
- **Updated:** 2019-09-30T19:51:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/881

I have encountered really strange behavior with HDMI audio:

* Restart computer
* HDMI audio works normally
* Turn off monitor and turn it back on again
* Screen turns on, but HDMI audio output is gone (PulseAudio no longer shows an available sink)

After many attempts I found that when ROCm is uninstalled, this doesn't happen. Installing `rock-dkms` and rebooting triggers this issue.

GPU: Radeon RX 570 4GB
OS: Ubuntu 18.04.3 (Kernel 5.0.0-25)
ROCm version: 2.7.1

Update 1: Just tested this with Kernel 4.15 (`sudo apt install linux-generic`) and the issue persists.
Update 2: Could not reproduce this on a different computer with RX 580 8GB. Same OS, same Kernel, same ROCm version.
Update 3: I could reproduce this issue by swapping RX 580 8GB with RX 570 4GB. 580 works fine, 570 doesn't.