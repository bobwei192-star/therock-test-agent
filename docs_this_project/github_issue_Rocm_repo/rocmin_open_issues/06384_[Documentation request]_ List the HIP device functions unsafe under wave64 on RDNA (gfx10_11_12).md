# [Documentation request]: List the HIP device functions unsafe under wave64 on RDNA (gfx10/11/12)

- **Issue #:** 6384
- **State:** open
- **Created:** 2026-06-25T15:14:57Z
- **Updated:** 2026-06-26T19:25:41Z
- **Assignees:** mangupta, b-sumner, dennyiriawan, ssahasra, saadrahim
- **URL:** https://github.com/ROCm/ROCm/issues/6384

### Description of errors

### Context

Narrow follow up to #4121 (closed) and hipamd #59. Not asking to reverse the `__AMDGCN_WAVEFRONT_SIZE` deprecation, restore `constexpr warpSize`, or support -mwavefrontsize64 on RDNA - those are understood as final.

Since LLVM llvm-project PR #164217 (merged) removed the wavefront macros and LLVM llvm-project PR #140185 (open) offers `-Wno-unsupported-wave64` for users who proceed anyway, the remaining blocker for downstream libraries changed from seeing if "they can compile it" to "which HIP device primitives can be safely called"

### The ask

hipamd #59 states the root cause: *"In wave64 mode, some cross-lane instructions only support 32 lanes, which makes hardware support of some cross-lane HIP functions impossible."*

Please publish the **exact set of HIP device functions that are unsafe or partial (32 lane only) under wave64 on gfx10/11/12**. This lets third party libraries write wave64 kernels that avoid those primitives, or route only those to a wave32 fallback. It cannot be derived from the ISA docs the HIP-primitive → ISA-op mapping is not user visible.

### Why it's actionable

A reviewer on LLVM llvm-project PR #140185 noted that wave64 *codegen* works on RDNA and the problem is library level. If accurate, the unsupported boundary is a finite, nameable set of device functions, not wave64 as a whole. Naming it turns 'unsupported, don't' into a 'hazard map'.

### Use case

I contribute to llama.cpp with changes affecting RDNA3 (gfx1100). An opt-in wave64 build recovers a decode gap vs Vulkan (ggml-org/llama.cpp#20934): up to +16% tg128, +12% on MoE long context, 0/10 of the tested models regressed once FA-VEC stays wave32. `__shfl_xor(val, 32, 64)` is a silent no-op on gfx1100 wave64, so reductions must stay 32-wide, but I cannot enumerate the rest without AMD documenting it. The supported route is WMMA (landing upstream) and packed-FP32 dual issue in wave32; a hazard list would let me and other contributors either build a verifiably safe wave64 path or know exactly which primitives to route around in wave32.

### Suggested answer shape

| HIP device function | wave64 on RDNA |
| --- | --- |
| `__shfl` / `__shfl_sync` | ? |
| `__shfl_xor_sync` (offset ≥ 32) | silent no-op (gfx1100) |
| `__shfl_up`/`__shfl_down` (delta ≥ 32) | ? |
| `__ballot` / `__any_sync` / `__all_sync` | ? |
| `__reduce_*_sync` | ? |
| `__match_any_sync` | ? |

`safe` / `unsafe` / `partial: 32-lane-only above lane 32` would each resolve it.

### Not a duplicate of #6111

#6111 is a build breakage bug: `__AMDGCN_WAVEFRONT_SIZE` *undefined* for gfx1201 breaking `amd_warp_functions.h` (closed as a stale Ubuntu `libamdhip64-dev` 5.7.1 header-shadowing issue). This request is a *documentation* ask about which HIP device functions are unsafe under wave64 on RDNA, a different artifact, not resolved by #6111's fix.

### Not asking for

- Support for `-mwavefrontsize64` on RDNA
- Restoring `__AMDGCN_WAVEFRONT_SIZE` or `constexpr warpSize`
- Lifting the HIP wave64 restriction
- Only documenting its boundary at the device function level.


### Refs

- #4121 · #6111 · hipamd #59
- https://github.com/llvm/llvm-project/pull/140185
- https://github.com/llvm/llvm-project/pull/164217
- https://github.com/ggml-org/llama.cpp/issues/20934

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_