# Support using the Visual Studio generators when CMake HIP language is enabled

- **Issue #:** 2359
- **State:** open
- **Created:** 2023-07-31T11:27:28Z
- **Updated:** 2025-05-28T19:50:06Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/2359

Currently, trying to use the Visual Studio generators with CMake when the HIP language is enables results in a hardcoded error. This workflow should be enabled either via the VS extensions or some other method.

[Relevant Kitware ticket.](https://gitlab.kitware.com/cmake/cmake/-/issues/24245)