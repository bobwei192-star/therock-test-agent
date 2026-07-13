# [Feature]: Rocm GPU subset allocation should work on Podman rootless

- **Issue #:** 2860
- **State:** open
- **Created:** 2024-02-01T16:47:18Z
- **Updated:** 2024-12-19T20:00:07Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/2860

### Suggestion Description

Rocm is not able to isolate subset of GPUs on podman rootless

```
$ podman run --rm --device=/dev/kfd --device=/dev/dri/renderD128 docker.io/rocm/dev-ubuntu-22.04:5.7.1 rocm-smi

========================= ROCm System Management Interface =========================
=================================== Concise Info ===================================
GPU  Temp (DieEdge)  AvgPwr  SCLK    MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
0    47.0c           38.0W   800Mhz  1600Mhz  0%   auto  300.0W    0%   0%    
1    44.0c           39.0W   800Mhz  1600Mhz  0%   auto  300.0W    0%   0%    
2    40.0c           43.0W   800Mhz  1600Mhz  0%   auto  300.0W    0%   0%    
3    34.0c           42.0W   800Mhz  1600Mhz  0%   auto  300.0W    0%   0%    
====================================================================================
=============================== End of ROCm SMI Log ================================
```

Since ROCM container device access rely on device cgroups implementation in the kernel, but Podman rootless does not allow to mount device cgroups on the container. 

I have created also a couple of tickets about it in Podman [AMD GPU subset selection does not work](https://github.com/containers/podman/issues/21454) and [in]([Support partial AMD GPU selection on SLURM](https://github.com/containers/podman/issues/21468)), but both seems to be rejected. 

They answer is the following:

`Device cgroups in the container is not possible because the kernel doesn't allow it. On cgroup v2, the devices cgroup requires eBPF and it is not usable from a user namespace. On cgroup v1, similar problem since delegation is not safe and we do not use cgroups at all with unprivileged users`


This could affect the **performance** on SLURM workloads using podman. Since two workloads running in the same node will see their performance influenced by the other.   

Is there a different way to  support of subset of GPUs in podman rootless?




### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_