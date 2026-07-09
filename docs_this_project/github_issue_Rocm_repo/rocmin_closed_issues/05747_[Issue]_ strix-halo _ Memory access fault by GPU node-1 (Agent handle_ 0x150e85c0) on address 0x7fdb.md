# [Issue]: strix-halo : Memory access fault by GPU node-1 (Agent handle: 0x150e85c0) on address 0x7fdb980a6000. Reason: Page not present or supervisor privilege. Aborted (core dumped)

- **Issue #:** 5747
- **State:** closed
- **Created:** 2025-12-08T14:47:23Z
- **Updated:** 2026-01-08T10:34:34Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5747

### Problem Description

Was working with:
     - kernel.x86_64 6.17.7-300.fc43, 
     - kernel.x86_64 6.17.8-300.fc43
 but not with:
     - kernel.x86_64 6.17.9-300.fc43

It is possible that would be linked to a firmware regression.


### Operating System

LSB Version:    n/a Distributor ID: Fedora Description:    Fedora Linux 43 (KDE Plasma Desktop Edition) Release:        43 Codename:       n/a

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

Strix Halo [Radeon Graphics / Radeon 8050S Graphics / Radeon 8060S Graphics]

### ROCm Version

VBIOS version: 113-STRXLGEN-001

### ROCm Component

_No response_

### Steps to Reproduce

Was working with:
     - kernel.x86_64 6.17.7-300.fc43, 
     - kernel.x86_64 6.17.8-300.fc43
 but not with:
     - kernel.x86_64 6.17.9-300.fc43

It is possible that would be linked to a firmware regression.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_