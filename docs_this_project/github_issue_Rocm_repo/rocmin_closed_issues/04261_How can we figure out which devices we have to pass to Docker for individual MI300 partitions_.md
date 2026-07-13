# How can we figure out which devices we have to pass to Docker for individual MI300 partitions?

- **Issue #:** 4261
- **State:** closed
- **Created:** 2025-01-15T07:13:49Z
- **Updated:** 2025-01-24T05:55:00Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4261

Individual GPUs can be mounted in Docker containers with the --device switch (as described here: https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/docker.html#docker-restrict-gpus).
To figure out which device path belongs to which GPU, we get the BDF id of each GPU via ROCm and then compare it with the files in /dev/dri/by-path.

Unfortunately, ROCm and AMD-SMI report the same BDF id for all partitions of a MI300 (which makes sense, because there are no individual PCI devices for the partitions).

How can we figure out which device/path we have to use to mount individual partitions in Docker? Is there another API function that we can use?

This is from our host with one MI300 (in TPX mode):
```
============================ ROCm System Management Interface ============================
======================================= PCI Bus ID =======================================
GPU[0]		: PCI Bus: 0000:01:00.0
GPU[1]		: PCI Bus: 0000:01:00.1
GPU[2]		: PCI Bus: 0000:01:00.2
==========================================================================================
================================== End of ROCm SMI Log ===================================

$ ls -l /dev/dri/by-path/
total 0
lrwxrwxrwx 1 root root  8 Dec 11 01:56 pci-0000:01:00.0-card -> ../card1
lrwxrwxrwx 1 root root 13 Dec 11 01:56 pci-0000:01:00.0-render -> ../renderD128
lrwxrwxrwx 1 root root  8 Dec 10 14:39 pci-0000:c2:00.0-card -> ../card0
lrwxrwxrwx 1 root root  8 Dec 11 01:56 platform-amdgpu_xcp_0-card -> ../card2
lrwxrwxrwx 1 root root 13 Dec 11 01:56 platform-amdgpu_xcp_0-render -> ../renderD129
lrwxrwxrwx 1 root root  8 Dec 11 01:56 platform-amdgpu_xcp_1-card -> ../card3
lrwxrwxrwx 1 root root 13 Dec 11 01:56 platform-amdgpu_xcp_1-render -> ../renderD130
lrwxrwxrwx 1 root root  8 Dec 11 01:56 platform-amdgpu_xcp_2-card -> ../card4
lrwxrwxrwx 1 root root 13 Dec 11 01:56 platform-amdgpu_xcp_2-render -> ../renderD131
lrwxrwxrwx 1 root root  8 Dec 11 01:56 platform-amdgpu_xcp_3-card -> ../card5
lrwxrwxrwx 1 root root 13 Dec 11 01:56 platform-amdgpu_xcp_3-render -> ../renderD132
lrwxrwxrwx 1 root root  8 Dec 11 01:56 platform-amdgpu_xcp_4-card -> ../card6
lrwxrwxrwx 1 root root 13 Dec 11 01:56 platform-amdgpu_xcp_4-render -> ../renderD133
lrwxrwxrwx 1 root root  8 Dec 11 01:56 platform-amdgpu_xcp_5-card -> ../card7
lrwxrwxrwx 1 root root 13 Dec 11 01:56 platform-amdgpu_xcp_5-render -> ../renderD134
lrwxrwxrwx 1 root root  8 Dec 11 01:56 platform-amdgpu_xcp_6-card -> ../card8
lrwxrwxrwx 1 root root 13 Dec 11 01:56 platform-amdgpu_xcp_6-render -> ../renderD135
```
It looks like if

/dev/dri/renderD128 is partition 0
/dev/dri/renderD129 is partition 1
/dev/dri/renderD130 is partition 2
/dev/dri/renderD131 etc. are just "blanks"

Can we just assume that if partition 0 is /dev/dri/renderD128, then partition 1 must be /dev/dri/renderD129 etc.?

Thank you!