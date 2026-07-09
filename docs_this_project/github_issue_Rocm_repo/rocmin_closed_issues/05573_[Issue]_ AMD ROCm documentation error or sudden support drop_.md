# [Issue]: AMD ROCm documentation error or sudden support drop?

- **Issue #:** 5573
- **State:** closed
- **Created:** 2025-10-25T22:20:34Z
- **Updated:** 2025-10-30T20:16:10Z
- **Labels:** Documentation, status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5573

### Problem Description

Hey, today I read the ROCm documentation again and I was shocked, my 6950xt is not listed in the Linux installation guide anymore. It was always listed with AMD Radeon RX 6950 XT	RDNA2	gfx1030 and working runtime + HIP SDK.

Earlier this year I heard that you guys worked on WSL2 support and even created a ROCm wishlist for WSL. I was so, so happy to read this, sadly RDNA2 is still not supported, but whatever, I'm glad that it works on Linux. But I'm afraid now, because my GPU isn't even listed for the Linux installation guide anymore... is this because of ROCm 7?

I'm running Fedora 42 now and ROCm is packaged in the official repo, it's ROCm 6.3.x, it works! Even with a 6.16 or 6.17 kernel.

Dear AMD ROCm team, I can live without WSL support, but will you at least support us RDNA2 users on Linux? I have not tried ROCm 7 on Linux yet and I'm afraid to, please don't drop the support, when it worked on previous versions.

### Operating System

Linux & Windows

### CPU

5800x3d

### GPU

RDNA2 6950xt

### ROCm Version

6.3.x & 7.x?

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_