# Compiling using HIP Ray Tracing(RT) requires manually set environment variables

- **Issue #:** 2337
- **State:** open
- **Created:** 2023-07-27T15:26:43Z
- **Updated:** 2024-12-17T16:12:32Z
- **Labels:** Verified Issue, Windows, 5.5.1
- **URL:** https://github.com/ROCm/ROCm/issues/2337

A beta version of HIP RT is available with the AMD HIP SDK for Windows. To enable HIP RT compilation from command line, add following environment variables in addition to the steps described in #2336
- HIP_ROOT_DIR = C:\Program Files\AMD\ROCm\5.5\ (Compile the blender with HIPRT)
- HIPRT_ROOT_DIR = folder structure should be folder name../dist/bin/release (Point HIPRT bitcode file (.bc from HIP SDK /bin directory) files.
