# [Issue]: amd-smi fails to set memory partition to NPS4 (ROCM6.3.2)

- **Issue #:** 4439
- **State:** closed
- **Created:** 2025-03-03T19:36:35Z
- **Updated:** 2025-03-11T19:24:38Z
- **Labels:** Under Investigation, AMD Instinct MI300X, ROCm 6.3.2
- **URL:** https://github.com/ROCm/ROCm/issues/4439

### Problem Description

sudo amd-smi set --memory-partition NPS4

          ****** WARNING ******

          Setting Dynamic Memory (NPS) partition modes require users to quit all GPU workloads.
          AMD SMI will then attempt to change memory (NPS) partition mode.
          Upon a successful set, AMD SMI will then initiate an action to restart AMD GPU driver.
          This action will change all GPU's in the hive to the requested memory (NPS) partition mode.

          Please use this utility with caution.

Do you accept these terms? [Y/N] Y

GPU: 0 again - Updating memory partition for gpu 0: [█████...................................] 20/140 secs remain
    MEMORY_PARTITION: [AMDSMI_STATUS_AMDGPU_RESTART_ERR] Could not successfully restart
        driver after applying NPS4 on GPU ID: 0 BDF:0000:05:00.0

GPU: 1
    MEMORY_PARTITION: [AMDSMI_STATUS_NOT_SUPPORTED] Device does not support setting
        memory partition to NPS4 on GPU ID: 1 BDF:0000:05:00.1

### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 9554 64-Core Processor

### GPU

MI300X

### ROCm Version

ROCM6.3.2

### ROCm Component

_No response_

### Steps to Reproduce

1) Set compute partition to CPX by running:
amd-smi     set --compute-partition CPX
(Notice that now we have 64 GPU using ROCM-SMI)

2) Run 
amd-smi     set --memorypartition CPX

Now we see the issue

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_