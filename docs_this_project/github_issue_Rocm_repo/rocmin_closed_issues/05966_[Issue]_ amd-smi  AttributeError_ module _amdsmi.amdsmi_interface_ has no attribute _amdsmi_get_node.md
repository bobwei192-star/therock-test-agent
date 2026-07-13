# [Issue]: amd-smi  AttributeError: module 'amdsmi.amdsmi_interface' has no attribute 'amdsmi_get_node_handle' in multi rocm installation

- **Issue #:** 5966
- **State:** closed
- **Created:** 2026-02-13T13:47:43Z
- **Updated:** 2026-03-04T15:36:57Z
- **Labels:** status: assessed
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5966

### Problem Description

In multi ROCm installation with 7.2.0 and 6.2.4 amd-smi produces the following error

```
AttributeError: module 'amdsmi.amdsmi_interface' has no attribute 'amdsmi_get_node_handle'
```

Most likely related to https://github.com/ROCm/ROCm/issues/5875

### Operating System

Alma 9.7

### CPU

Irrelevant

### GPU

Irrelevant

### ROCm Version

6.2.4 + 7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

Installed amdgpu-dkms from 30.10.3 and ROCm 6.2.4 and 7.2.0 from the repo and run amd-smi when 7.2.0 module is loaded get the error. When 6.2.4 is loaded output is correct.