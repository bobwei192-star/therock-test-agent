# [Feature]: Support Linux 6.17 in Ubuntu 25.10

- **Issue #:** 5553
- **State:** closed
- **Created:** 2025-10-21T18:09:43Z
- **Updated:** 2025-10-22T15:31:44Z
- **Labels:** Feature Request, status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5553

### Suggestion Description

Currently the ROCm 7.02 drivers are ABI compatible with Ubuntu 25.04, so desktop users will prefer the newer distribution for Radeon / Strix Halo to take advantage of newer software, kernels, performance, hardware support, etc. 

Moving from 25.04 is a common upgrade pattern, so supporting 25.10  for users on Strix Halo and discrete Radeon GPUs make sense. 

Note: Related upstream patches for MES for Strix Halo are merged in to 6.18rc2, as well as current -proposed on 6.14, so we expect them in 6.17 as well. 

https://github.com/torvalds/linux/commit/1fb710793ce2619223adffaf981b1ff13cd48f17

https://bugs.launchpad.net/ubuntu/+source/linux-oem-6.14/+bug/2125201
* [noble] Fix system hang observed with comfy-ui (LP: [#2125201](https://bugs.launchpad.net/bugs/2125201))
    - drm/amd/include : Update MES v12 API for fence update
    - SAUCE: drm/amdgpu: Enable MES lr_compute_wa by default

### Operating System

Ubuntu 25.10

### GPU

gfx1151, gfx1100

### ROCm Component

amdgpu 6.14.14