# [Issue]: EL9 pakages for ROCm 7.1 are actually for EL8

- **Issue #:** 5617
- **State:** closed
- **Created:** 2025-11-02T20:40:46Z
- **Updated:** 2025-11-06T13:30:51Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5617

### Problem Description

The ROCm 7.1 packages for EL9 at https://repo.radeon.com/rocm/rhel9/7.1/main/ are actually for EL8 as the `.el8.` part of the name suggests:

<img width="652" height="232" alt="Image" src="https://github.com/user-attachments/assets/5c3ab7d2-6510-41d4-a445-b164f8eec916" />

Downloading and unpacking a couple of RPMs showed that indeed the contents of the EL8 and EL9 packages are identical. 

### Operating System

RedHat Enterprise Linux 9

### CPU

n/a

### GPU

n/a

### ROCm Version

ROCm 7.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_