# [Issue]: Unable to run Ray and VLLM on servers with Ubuntu 24.04.3 LTS and MI300x GPUs

- **Issue #:** 5780
- **State:** open
- **Created:** 2025-12-15T22:42:54Z
- **Updated:** 2026-02-26T15:02:53Z
- **Labels:** Feature Request, status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5780

### Problem Description

We have been given access to 4 servers each having 8 MI300x GPUs in them. But we have not been able to successfully run VLLM with Ray which prevent us from being able to run VLLM on more then one server.

The problem is that when we start VLLM on a Ray node we get the error torch.AcceleratorError: HIP error: invalid device ordinal

Note that if we start VLLM without Ray, it starts without problem. 

We are also able to start VLLM with Ray on the 4 servers when we use a docker image that has Ubuntu 22.04.5 LTS  with glibc 2.35   instead of Ubuntu 24.04.3 LTS with glibc 2.39.

To run tests and troubleshoot the issue we created docker images. One with the same Ubuntu version then the one on the host and one with an older version.

Component                | Host Venv                         | Docker Ubuntu 24.04       | Docker Ubuntu 22.04 (TCP)
-------------------- |--------------------------|--------------------------|---------------------------
OS                               | Ubuntu 24.04.3 LTS        | Ubuntu 24.04.3 LTS          | Ubuntu 22.04.5 LTS       
glibc                            | 2.39                                  | 2.39                                    | 2.35                     
Python                        | 3.12.3                                | 3.12.3                                 | 3.12.12                  
vLLM                          | 0.11.2                                 | 0.11.2                                  | 0.11.2                   
PyTorch                     | 2.9.0a0+git1c57644         | 2.9.0a0+git1c57644        | 2.9.0a0+git1c57644       
Ray                            | 2.52.1                                 | 2.52.1                                 | 2.52.1                   
ROCm                        | 7.1.1                                    | 7.1.0                                  | 7.1.0                    

=== BEHAVIOR SUMMARY ===

Host Venv (runing on the host itself)+ Ray :         ❌ HIP error: invalid device ordinal
Host Venv (runing on the host itself) Without Ray:      ✅ Works (not tested in this report)
Docker Ubuntu 24.04 + Ray: ❌ HIP error: invalid device ordinal
Docker Ubuntu 24.04 (no Ray): ✅ Works
Docker Ubuntu 22.04 + Ray: ✅ Works

If it may help, we also tried different environment variables setting but without success, We tried GPU_DEVICE_ORDINAL (any variation), HIP_VISIBLE_DEVICES,  ROCR_VISIBLE_DEVICES,  CUDA_VISIBLE_DEVICES,  ROCM_PATH, HIP_PATH, VLLM_USE_V1

So there seems to be a GPU numbering mismatch between Ray and HIP. 

Would you be able to help us figuring out where the problem is and how to fix it ^Maybe you have a modified code that works on tour side we can use ?

Thanks a lot for your help on this

### Operating System

OS: NAME="Ubuntu" VERSION="24.04.3 LTS (Noble Numbat)"

### CPU

CPU:  model name      : AMD EPYC 9534 64-Core Processor

### GPU

GPU:   Name:                    AMD EPYC 9534 64-Core Processor       Marketing Name:          AMD EPYC 9534 64-Core Processor       Name:                    AMD EPYC 9534 64-Core Processor       Marketing Name:          AMD EPYC 9534 64-Core Processor       Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-   Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-   Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-   Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-   Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-   Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-   Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-   Name:                    gfx942                                Marketing Name:          AMD Instinct MI300X                       Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-

### ROCm Version

7.1.1 (also tried 7.1.0)

### ROCm Component

_No response_

### Steps to Reproduce

Start a single Ray node on a single server and then launch VLLM. The error is seen as VLLM initialize

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_