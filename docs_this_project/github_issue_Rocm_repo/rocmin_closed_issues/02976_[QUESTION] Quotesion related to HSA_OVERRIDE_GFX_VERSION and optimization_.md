# [QUESTION] Quotesion related to HSA_OVERRIDE_GFX_VERSION and optimization? 

- **Issue #:** 2976
- **State:** closed
- **Created:** 2024-03-25T13:02:23Z
- **Updated:** 2024-07-17T14:16:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/2976

I not fully understand does this variable is solution or just trick/workaround. I mean if we can use gfx1100 code for gfx1103 or gfx1102 why just not link all this codes internally inside ROCM why it force users to use this variable? Does it produce some problem (like performance or etc) of using existing code but for another compatible GPU

Also I want to know what difference in case if I rebuild ROCM especially for gfx1102 or gfx1103, does it will produce exactly the same files like for gfx1100 but with another name or it will produce optimized code/files for specific architecture?

If it produce optimized code, what parts of already prebuilt ROCM need to rebuild - if I correctly understand it should be enough to rebuild only this packages: rocBLAS, rocFFT, rocSPARSE, MIOpen, rocRAND, rccl... is not it?