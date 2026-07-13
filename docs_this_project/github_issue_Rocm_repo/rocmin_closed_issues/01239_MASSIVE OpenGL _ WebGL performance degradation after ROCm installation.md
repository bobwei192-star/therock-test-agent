# MASSIVE OpenGL / WebGL performance degradation after ROCm installation

- **Issue #:** 1239
- **State:** closed
- **Created:** 2020-09-23T17:58:16Z
- **Updated:** 2024-01-14T03:58:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/1239

Today I've run into a weird issue:

I'm working on an Electron application that uses three.js / WebGL.
Without ROCm installed everything's fine: The all-open amdgpu drivers provide smooth 60fps.

After installation of ROCm, however, I'm barely getting 4 (four) FPS!


Ubuntu 20.04 @ 5.4.0-48-generic
Radeon VII

Only difference I notice is that pre-ROCm, glxinfo reports `Device: AMD Radeon VII (VEGA20, DRM 3.35.0, 5.4.0-48-generic, LLVM 10.0.0) (0x66af)`, with ROCm it's `Device: AMD Radeon VII (VEGA20, DRM 3.40.0, 5.4.0-48-generic, LLVM 10.0.0) (0x66af)`

Any ideas?

NOTE: Even after installation of ROCm, Unigine Superposition runs at well over 100FPS, i.e. performance compared with pre-ROCm is the change.