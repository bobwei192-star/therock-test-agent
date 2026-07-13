# [Feature]: RX 9060 XT support on Windows.

- **Issue #:** 5010
- **State:** closed
- **Created:** 2025-07-08T19:33:43Z
- **Updated:** 2025-07-22T21:11:51Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5010

### Suggestion Description

I installed ComfyUI using ZLUDA. ComfyUI runs and launches properly. However, when I try to generate a 3D model using Hunyuan 3D, I get an error:
rocBLAS error: Cannot read C:\Program Files\AMD\ROCm\6.2\bin/rocblas/library/TensileLibrary.dat: No such file or directory for GPU arch: gfx1200
As far as I understand—please correct me if I’m wrong—AMD ROCm on Windows 11 still doesn't support the RX 9000 series. In the documentation, RDNA 4.0 cards haven't yet been added to the Windows support list.
When will RX 9000 series support be added for Windows 11?

### Operating System

Windows 11

### GPU

Rx 9060xt

### ROCm Component

ROCm 6.2 with zluda