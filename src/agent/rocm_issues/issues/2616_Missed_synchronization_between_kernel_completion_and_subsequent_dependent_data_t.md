# Missed synchronization between kernel completion and subsequent dependent data transfer results in an error 

> **Issue #2616**
> **状态**: closed
> **创建时间**: 2023-10-31T15:14:10Z
> **更新时间**: 2025-05-29T16:03:45Z
> **关闭时间**: 2025-05-29T15:31:40Z
> **作者**: Rmalavally
> **标签**: Under Investigation, 5.7.0, 5.7.1, OpenMP (ROCm)
> **URL**: https://github.com/ROCm/ROCm/issues/2616

## 标签

- **Under Investigation** (颜色: #0052cc)
- **5.7.0** (颜色: #fef2c0)
- **5.7.1** (颜色: #b60205)
- **OpenMP (ROCm)** (颜色: #f9d0c4)

## 描述

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
