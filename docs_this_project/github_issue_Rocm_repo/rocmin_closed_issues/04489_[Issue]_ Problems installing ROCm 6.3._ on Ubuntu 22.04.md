# [Issue]: Problems installing ROCm 6.3.* on Ubuntu 22.04

- **Issue #:** 4489
- **State:** closed
- **Created:** 2025-03-12T23:47:41Z
- **Updated:** 2025-05-07T19:49:23Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4489

### Problem Description

I am working with the following system:

NAME="Ubuntu"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
CPU:
model name      : Intel(R) Xeon(R) Platinum 8480C
GPU:
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942
  Marketing Name:          AMD Instinct MI300X VF
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-

The specific kernel version that is running is 5.15.0-1081-azure (when I successfully install 6.2.4).  

When I update the kernel version to 6.8.0-1021-azure I am unable to install either 6.2.4 or 6.3.* (which requires the newer kernel based on [these docs](https://rocm.docs.amd.com/en/docs-6.3.1/compatibility/compatibility-matrix.html#compatibility-matrix)).

After updating the kernel and running `sudo modprobe amdgpu` I get the attached logs from dmesg (no errors from modprobe but it takes quite a while to return).

[modprobe_log.txt](https://github.com/user-attachments/files/19219195/modprobe_log.txt)


### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

AMD Instinct MI300X VF

### ROCm Version

ROCm 6.3.*

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_