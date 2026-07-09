# GUI Apps - Blender, Darktable, Gimp, DaVinci Resolve, Natron, etc.

- **Issue #:** 1397
- **State:** closed
- **Created:** 2021-03-01T17:03:56Z
- **Updated:** 2024-08-15T14:19:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/1397

Earlier, several issues that have been open and worked on for some time were closed by @ROCmSupport.  The justification for closing the tickets was that **ROCm is now not supporting any GUI applications**, and will now only support headless applications.  For example, see this post:
- https://github.com/RadeonOpenCompute/ROCm/issues/1345#issuecomment-787750471

The purpose of creating this thread is to:

1. Ensure users & prospective buyers to be aware that **AMD ROCm is not suitable for any GUI applications**, such as Blender, Darktable, Gimp, DaVinci Resolve, Natron, etc.

2. Mark that the fact AMD ROCm does not support any GUI applications as being an issue for ML.  For example, some machine learning cases require some form of GUI, including machine vision (eg. facial or object recognition); or interactive cases (eg. geospatial: 5G tower placement for optimizing signal strength)

3.  Request that AMD ROCm consider supporting these types of graphical OpenCL applications with their graphics cards.  There is no word yet from AMD on whether or not ROCm will be supported in headless mode for these applications (example: parallel-GPU-compute render farm for blender).

For these cases specifically, it seems that nvidia CUDA (https://developer.nvidia.com/cuda-zone) is a better system, and AMD ROCm cannot be considered to be in parity or a potential point for transition.