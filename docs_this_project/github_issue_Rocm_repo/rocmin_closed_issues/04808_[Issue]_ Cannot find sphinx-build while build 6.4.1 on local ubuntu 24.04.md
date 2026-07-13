# [Issue]: Cannot find sphinx-build while build 6.4.1 on local ubuntu 24.04

- **Issue #:** 4808
- **State:** closed
- **Created:** 2025-05-27T08:08:31Z
- **Updated:** 2025-05-27T08:49:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/4808

### Problem Description

Seems the install-prerequisites.sh didn't install the dependency python module sphinx.
Installing 'python3-sphinx' works for me.

### Operating System

ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

Intel(R) Core(TM) i9-9900K CPU @ 3.60GHz

### GPU

2x RX9070xt

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

Sync the latest ROCm release.
Run the install-prerequisites.sh on host local.
Build all components.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_