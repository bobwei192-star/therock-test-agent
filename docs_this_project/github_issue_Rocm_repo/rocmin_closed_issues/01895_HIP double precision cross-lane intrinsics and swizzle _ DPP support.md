# HIP double precision cross-lane intrinsics and swizzle / DPP support

- **Issue #:** 1895
- **State:** closed
- **Created:** 2023-01-21T09:09:28Z
- **Updated:** 2024-05-12T22:00:24Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/1895

Hello,
Using HIP, I currently perform cross-lane reductions with `__shfl_xor()` instructions.
These seem to be a perfect match for the  ds_swizzle_b32 instruction [1], but when looking at the assembly generated, it seems only ds_(b)permute_b32 instructions are generated.
The performance is impacted: many instructions are used to generate the addressing of lanes, while ds_swizzle_b32 require none if I understand correctly.
Furthermore, ref [1] also says that cross-lane data exchange can be performed at full throughput using DPP modifiers.
Things like
      `x += __shfl_down(y, 1, 16);`
could be translated into a single instruction add with DPP modifier if I understand correctly.

But anyway, maybe the compiler can't do it due to some limitations. Could we then have intrinsics that do the job, including for double-precision values ? The intrinsics I've seen are limited to 32-bit words...
Has someone advice as to how to get decent performance for such cross-lane operations in HIP targeted at AMD CDNA ?
If possible, I would like to avoid inline asm, as it is said it disables many compiler optimizations.

Thanks a lot!

[1] https://gpuopen.com/learn/amd-gcn-assembly-cross-lane-operations/