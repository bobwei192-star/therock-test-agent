# Missed synchronization between kernel completion and subsequent dependent data transfer results in an error 

- **Issue #:** 2616
- **State:** closed
- **Created:** 2023-10-31T15:14:10Z
- **Updated:** 2025-05-29T16:03:45Z
- **Labels:** Under Investigation, 5.7.0, 5.7.1, OpenMP (ROCm)
- **URL:** https://github.com/ROCm/ROCm/issues/2616

### Missed synchronization between kernel completion and subsequent dependent data transfer results in an error

ROCm OpenMP 5.7.1 and earlier may result in a randomly appearing defect that is observable as target regions computing wrong answer/results. This is due to a missed synchronization between kernel completion and subsequent dependent data transfer.
 
If this behavior is observed, run the application with the following environment variable set:

HSA_ENABLE_SDMA=0

**Note:** Performance impact may be observed when the above environment variable is used.

### Operating System

Ubuntu 22.04 with AMDGPU 6.2.4 driver

### CPU

AMD EPYC 7A53 64-Core Processor, AMD EPYC 7313 16-Core Processor, and others

### GPU

MI200, MI100, Radeon Pro W6800

### ROCm Version

ROCm 5.7.0, 5.7.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### Output of /opt/rocm/bin/rocminfo --support

NA