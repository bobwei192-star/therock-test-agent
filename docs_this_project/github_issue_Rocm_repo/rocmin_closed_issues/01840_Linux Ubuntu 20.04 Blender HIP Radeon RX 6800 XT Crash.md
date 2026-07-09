# Linux Ubuntu 20.04 Blender HIP Radeon RX 6800 XT Crash

- **Issue #:** 1840
- **State:** closed
- **Created:** 2022-10-17T15:23:34Z
- **Updated:** 2024-04-21T13:19:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/1840

Blender Version
3.3+

When using HIP Gpu render in view port after few seconds all freeze and getting this error.
drm.amdgpu_cs_ioctl [amdgpu] *ERROR* failed to initialize parser - 125!
Only reboot or restart X may bring control

What is interesting i can render with HIP gpu without any problems, only using view port rendering (when using HIP) getting this error. Only cpu render works fine

I know about some kernel problems making this kind of crash but in my case the only program making this is Blender.That;s why i reporting this bug here. All Games, programs working stable without this error.

Radeon Pro renderer works fine also . The only problem is GPU render in view port with cycles.

similar problem described here:
https://developer.blender.org/T100353
