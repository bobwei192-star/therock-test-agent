# [Issue]: ROCm 6.4.1 support for Fedora 42 (dnf/yum) — repo availability?

- **Issue #:** 4899
- **State:** closed
- **Created:** 2025-06-08T15:57:58Z
- **Updated:** 2025-08-08T03:20:26Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/4899

### Problem Description

Hey ROCm team,

I’m running Fedora 42 with an AMD Radeon RX 7900 XTX, and I’ve noticed that ROCm 6.4.1 isn’t yet available via the usual YUM-compatible repos. So far, I’ve only been able to install 6.3.1 using:

sudo dnf install rocm-dev rocm-utils rocminfo rocm-smi 
It looks like RHEL 9.6 already has access to ROCm 6.4.1 via a separate .rpm and repo (amdgpu-install-6.4.60401-1.el9.noarch.rpm), but that’s not working out-of-the-box for Fedora users. I checked https://repo.radeon.com/rocm/yum and it still stops at 6.3.

A bit of context:

I’m part of a growing group of Fedora users (we’ve got a Discord server too) who are interested in ROCm. Some of us are using ROCm for development or GPU workloads, and we’re just hoping for a bit more clarity on Fedora support going forward.

Is there a plan to publish 6.4.1+ to it soon?

Really appreciate the work you all are doing on ROCm — just wanted to bring this up in case it slipped under the radar.

Thanks!
Daniel

### Operating System

Fedora 42

### CPU

Ryzen 9 5950x

### GPU

RX 7900 XTX

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

Check available ROCm versions in DNF

sudo dnf info rocm-dev
❌ ROCm 6.4.1 not found
✅ Only 6.3.1 is available

Try to explicitly install 6.4.1

sudo dnf install rocm-dev-6.4.1
❌ Output: No match for argument

Check the YUM repo directly
Visit: https://repo.radeon.com/rocm/yum/
❌ No 6.4.1/ directory listed — only 6.3/ exists

Compare to RHEL 9.6
ROCm 6.4.1 is available via:

sudo dnf install https://repo.radeon.com/amdgpu-install/6.4.1/rhel/9.6/amdgpu-install-6.4.60401-1.el9.noarch.rpm
sudo dnf install rocm
✅ Successfully installs 6.4.1 on RHEL 9.6

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_