# Should rocminfo and rocm_agent_enumerator show R9 390 as gfx702?

- **Issue #:** 891
- **State:** closed
- **Created:** 2019-09-25T08:38:42Z
- **Updated:** 2023-12-19T15:06:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/891

I'm asking because according to [LLVM docs](https://llvm.org/docs/AMDGPUUsage.html#processors) my card shows as gfx702. I know HCC is deprecated, but I'm helping with Gentoo ROCm and I have implemented the patches for gfx700, gfx701, gfx702 from https://github.com/RadeonOpenCompute/hcc-clang-upgrade/pull/149 and I now have a compiler using the correct bitcodes.

So, really shouldn't these tools return gfx702 in my case? If so, I can send a patch in.