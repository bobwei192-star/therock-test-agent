# Ryzen 4000 series APU support pt2

- **Issue #:** 1732
- **State:** closed
- **Created:** 2022-04-27T18:54:22Z
- **Updated:** 2024-10-09T14:51:35Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/1732

recently I noticed that opencl-amd (from the AUR) version 22.10 works remarkably well, but my vram is 
`  Global memory size                              536870912 (512MiB)`
I want more, 512 MB is not a lot, so I was wondering if rocm could support using the gtt memory space as "vram"