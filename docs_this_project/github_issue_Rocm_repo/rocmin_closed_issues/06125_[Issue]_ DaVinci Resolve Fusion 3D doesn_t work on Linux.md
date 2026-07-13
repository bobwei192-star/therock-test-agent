# [Issue]: DaVinci Resolve Fusion 3D doesn't work on Linux

- **Issue #:** 6125
- **State:** closed
- **Created:** 2026-04-07T19:43:08Z
- **Updated:** 2026-05-28T16:00:22Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6125

### Problem Description

As I said on https://github.com/ROCm/ROCm/issues/5982#issuecomment-4199305082

The Fusion tab of DaVinci Resolve is not working for a long time now, this is probably something that Blackmagic needs to fix by itself so I don't know if this is exactly related to ROCm, but it would be appreciated some attention. The track for this on [Blackmagic Forum](https://forum.blackmagicdesign.com/viewtopic.php?f=22&t=222293).

The entire 3D workflow doesn't work, Hardware Render doesn't work, the 3D Viewer doesn't work, the prints below show the Fusion console, the 3D Viewer space and a simple node tree for demonstration, anything on the Renderer3D being hardware accelerated doesn't appear, and the 3D viewer is always rendered by the GPU it seems, so it doesn't show anything.

<img width="564" height="354" alt="Image" src="https://github.com/user-attachments/assets/9f7ca933-75a0-49e7-be1b-4b5ad1d2ada5" />
<img width="704" height="406" alt="Image" src="https://github.com/user-attachments/assets/43bb13d1-ca15-4a44-b5b4-57f0635fab7f" />
<img width="692" height="239" alt="Image" src="https://github.com/user-attachments/assets/27e1e002-ecfb-4a21-a0c2-e5fd69deef99" />

I'm using the latest version of DaVinci Resolve (20.3.2 at the moment), some users on the Blackmagic Forum says that on older versions of DaVinci Resolve worked just fine, I didn't tested it so I can't speak for them, some NVIDIA users says that Blackmagic solved the issue, some AMD users says that works with distrobox and others says that it doesn't, I'm not following up that thread anymore so thats all I know, I didn't tested distrobox either.

### Operating System

Arch Linux

### CPU

AMD Ryzen 5 5600

### GPU

AMD Radeon RX 7600

### ROCm Version

7.2.1

### ROCm Component

_No response_

### Steps to Reproduce

Use the Fusion tab of DaVinci Resolve, add some nodes to make a simple 3D scene, like adding a text to the renderer3d like i've shown on the image

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

My environment variables are

```
GTK_CSD=0
GTK_USE_PORTAL=1
XMODIFIERS=@im=fcitx
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
QT_IM_MODULES="wayland;fcitx"
SDL_IM_MODULE=wayland
MANGOHUD=1
KWIN_WAYLAND_SUPPORT_XX_PIP_V1=1
ENABLE_LAYER_MESA_ANTI_LAG=1
```