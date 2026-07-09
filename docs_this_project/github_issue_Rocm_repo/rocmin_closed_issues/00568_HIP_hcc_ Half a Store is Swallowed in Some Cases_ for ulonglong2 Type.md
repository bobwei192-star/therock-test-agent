# HIP/hcc: Half a Store is Swallowed in Some Cases, for ulonglong2 Type

- **Issue #:** 568
- **State:** closed
- **Created:** 2018-10-03T16:17:34Z
- **Updated:** 2018-12-04T09:06:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/568

Ubuntu 16.04, kernel 4.13, ROCm 1.9, gfx900 (gfx803 has same problem I think)

Consider this line I had to comment out:
https://github.com/949f45ac/xmr-stak-hip/blob/d0cd20c597dd9cfbe3c67e3bcb99a9bbf31a895c/hip_code/cuda_core.cu#L309
When I try using it instead of the line below (that actually works, by issuing the correct instruction via `asm`) then I can see in the generated ISA that only one `global_store_dwordx2` instruction is generated, instead of a `global_store_dwordx4` or at least 2 `store_dwordx2` instructions.
You can easily validate whether the whole thing works correctly by running `xmr-stak-test` after building. (Build instructions are in the repo’s README.)

Further below in the same function there is another such storage operation with the same data types and all, and that one actually works, so I think in the case where it doesn't work the compiler is confused by other circumstances – maybe he wants to actually split up the load into 2 (because the first half is already computed comparatively early) but forgets about one part somehow.

Cheers!