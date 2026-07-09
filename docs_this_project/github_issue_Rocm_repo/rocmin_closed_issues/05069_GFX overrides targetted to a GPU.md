# GFX overrides targetted to a GPU

- **Issue #:** 5069
- **State:** closed
- **Created:** 2025-07-19T14:47:53Z
- **Updated:** 2025-07-22T06:28:55Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5069

### Suggestion Description

So I have a 9060XT 16GB and a RX 6600 8GB, I am using `rocm6.4`. Since the 9060XT is `gfx1200` it is working well but since the 6600 is `gfx1032`, I have to override it to `gfx1030`. 

Both individually are working, but I cannot get them to work simultaneously. When I use `os.environ['HSA_OVERRIDE_GFX_VERSION'] = '10.3.0'` all the GPU gfx versions change to gfx1030, so the 9060XT becomes unusable. 

Is there any way to assign GFX overrides to a specific GPU, or can the 6600 be permanently overridden to gfx1030, or will there ever be any official support for `gfx1032`?

### Operating System

Ubuntu 24.04

### GPU

9060XT 16GB and RX6600 8GB

### ROCm Component

_No response_