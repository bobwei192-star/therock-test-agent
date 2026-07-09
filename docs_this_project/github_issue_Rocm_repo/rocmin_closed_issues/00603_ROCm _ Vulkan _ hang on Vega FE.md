# ROCm + Vulkan = hang on Vega FE

- **Issue #:** 603
- **State:** closed
- **Created:** 2018-11-06T03:52:19Z
- **Updated:** 2023-12-12T21:51:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/603

It doesn't matter if AMDVLK or RADV is used with Vega FE, anything touching ROCm will cause sooner or later cause an unrecoverable hang if Vulkan is used at the same time.

This isn't observed with OpenGL or other facilities, only Vulkan that I can tell.

It doesn't occur if only ROCm or only Vulkan is used, but occurs frequently when the two are combined. Most reliably seen with Overwatch, but happens on anything that uses Vulkan, including native Linux games.