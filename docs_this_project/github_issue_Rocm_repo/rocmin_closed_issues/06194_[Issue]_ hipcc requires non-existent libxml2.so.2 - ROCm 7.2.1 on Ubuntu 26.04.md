# [Issue]: hipcc requires non-existent libxml2.so.2 - ROCm 7.2.1 on Ubuntu 26.04

- **Issue #:** 6194
- **State:** closed
- **Created:** 2026-04-29T22:06:12Z
- **Updated:** 2026-06-09T17:27:35Z
- **Labels:** status: triage
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6194

### Problem Description

After installing ROCm 7.2.1 on Ubuntu 26.04 successfully (without dkms - see Issue #6193)  hipcc was not functioning because /opt/rocm-7.2.1/lib/llvm/bin/ld.lld is hard-coded to require libxml2.so.2.  Ubuntu 26.04 only has libxml2.so.16 so building anything with hipcc failed because it could not find a compatible shared library for libxml2

The fix I implemented was to download a version of libxml2.so.2 and install it into /lib/x86_64-linux-gnu

wget https://launchpad.net/ubuntu/+archive/primary/+files/libxml2_2.12.7+dfsg+really2.9.14-0.4ubuntu0.4_amd64.deb
sudo dpkg --fsys-tarfile libxml2_2.12.7+dfsg+really2.9.14-0.4ubuntu0.4_amd64.deb | tar -xO ./usr/lib/x86_64-linux-gnu/libxml2.so.2.9.14 > /lib/x86_64-linux-gnu/libxml2.so.2.9.14
sudo ln -s /lib/x86_64-linux-gnu/libxml2.so.2.9.14 /lib/x86_64-linux-gnu/libxml2.so.2




### Operating System

Ubuntu 26.04 (Resolute Raccoon)

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### ROCm Version

ROCm 7.2.1

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_