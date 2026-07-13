# [Issue]: AMDGPU RPM DKMS hard version dependency causes issue in HPC-environments

- **Issue #:** 5650
- **State:** closed
- **Created:** 2025-11-11T10:44:54Z
- **Updated:** 2026-01-21T20:58:41Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5650

### Problem Description

We are running a HPC-cluster (on Alma 8) with mixed AMD and Nvidia systems. We typically build compute node images on our headnode which are then deployed to our compute nodes.

The AMDGPU requires dkms = 3.1.1 whereas Nvidia nowadays installs dkms-3.2.2.

Can we lose the dependency on a specific DKMS version? 

### Operating System

Alma Linux 8

### CPU

AMD EPYC 9554 64-Core Processor

### GPU

AMD MI300A (target system)

### ROCm Version

7.1

### ROCm Component

_No response_

### Steps to Reproduce

Have dkms 3.2.2 installed and then try to 'dnf install amdgpu-dkms'.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_