# apt repo: rocm-dkms contains outdated firmware

- **Issue #:** 527
- **State:** closed
- **Created:** 2018-09-14T07:26:11Z
- **Updated:** 2018-12-24T22:48:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/527

The rocm-dkms package (currently ver 1.8.199) in the apt repo contains really old firmware, e.g., VCN version 1.24 for raven ridge (linux-firmware.git is at 1.73). From linux kernel 4.19 onwards, raven ridge fails to boot linux with the old firmware (see https://bugs.freedesktop.org/show_bug.cgi?id=107880).

Best regards
Marvin