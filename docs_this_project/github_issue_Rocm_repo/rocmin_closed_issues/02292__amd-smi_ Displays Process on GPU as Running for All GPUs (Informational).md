# ‘amd-smi’ Displays Process on GPU as Running for All GPUs (Informational)

- **Issue #:** 2292
- **State:** closed
- **Created:** 2023-06-28T22:06:31Z
- **Updated:** 2024-03-24T04:43:52Z
- **Labels:** 5.6.0, Informational
- **URL:** https://github.com/ROCm/ROCm/issues/2292

```amd-smi``` displays processes as running for all GPUs when it may be running only on one GPU. 

```amd-smi``` currently uses the Linux kernel's definition of running processes. Future implementations may use the Kernel Fusion Driver's (KFD) definition of running processes. 

For more detailed information, refer to the memory usage for each GPU.