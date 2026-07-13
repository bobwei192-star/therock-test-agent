# [Issue]: Regression to issue in #4204

- **Issue #:** 5091
- **State:** closed
- **Created:** 2025-07-23T03:01:57Z
- **Updated:** 2025-09-16T17:51:27Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5091

### Problem Description

cc: @ppanchad-amd,  @lucbruni-amd

Hi guys,
So it seems the issue I identified in https://github.com/ROCm/ROCm/issues/4204 has resurfaced. 

Unfortunately I can't immediately point to where/when the regression occurred, as last time the issue was ["fixed internally"](https://github.com/ROCm/ROCm/issues/4204#issuecomment-2701294095) and I admittedly haven't been keeping an eye on my amdgpu kernel module updates to be able to pinpoint which public commit (if any) the regression might be visible in.

What I can say is `apt dist-upgrade` has been failing for me for maybe a month now due to errors compiling the `amdgpu` DKMS module. I finally took 5 minutes to look at why it wasn't compiling tonight and the first thing I did -- hoping whatever the issue was had been fixed -- was to bump the apt repo I was using from https://repo.radeon.com/amdgpu/5.4.1/ to https://repo.radeon.com/amdgpu/6.4.2/. This didn't fix the problem. Next I googled the compile error and wound back at https://github.com/ROCm/ROCm/issues/4204 😄 .

Anyway, adding `unset TMPDIR` to the top of the pre-build script immediately fixed the problem. I'm happy to help troubleshoot if needed (and assuming the issue is even located in a public repo), but I'm hoping it'll be trivial on your end to see where the issue was re-introduced internally.

Please let me know if you need anything from me.

### Operating System

Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

AMD Ryzen Threadripper 2950X 16-Core Processor

### GPU

AMD Radeon RX 6600

### ROCm Version

AMD GPU DKMS Kernel Module from https://repo.radeon.com/amdgpu/ version 5.4.1 and 6.4.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_