# [Issue]: bfloat16 functions emit duplicate host symbols in multi-TU HIP builds

- **Issue #:** 6112
- **State:** closed
- **Created:** 2026-04-02T18:05:10Z
- **Updated:** 2026-04-13T21:13:41Z
- **Labels:** status: triage
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6112

### Problem

When multiple `.cu` / `.hip` files include HIP headers and use bfloat16, the linker reports duplicate symbol errors for functions like `__float2bfloat16`, `__bfloat1622float2`, `__double2bfloat16`, etc. — despite these being declared `static inline` in the header.

### Reproduction

Any multi-TU HIP project that includes bfloat16 headers. Reproduced with llama.cpp (`cmake -DGGML_HIP=ON -DAMDGPU_TARGETS=gfx1201`):

```
ld.lld: error: duplicate symbol: __float2bfloat16(float)
>>> defined at acc.cu
>>> defined at arange.cu
ld.lld: error: duplicate symbol: __bfloat1622float2(__hip_bfloat162)
ld.lld: error: duplicate symbol: __double2bfloat16(double)
ld.lld: error: duplicate symbol: __float22bfloat162_rn(HIP_vector_type<float, 2u>)
ld.lld: error: duplicate symbol: __high2float(__hip_bfloat162)
ld.lld: error: duplicate symbol: __low2float(__hip_bfloat162)
```

### Root Cause

In `amd_hip_bf16.h:131`:

```cpp
#define __BF16_HOST_DEVICE_STATIC__ __BF16_HOST_DEVICE__ static inline
```

The functions are correctly declared `static inline`. However, when the HIP compiler processes `.cu` files for dual-target compilation (device + host), the `static inline` qualifier appears to be stripped or ignored during host-side emission, causing each translation unit to emit a non-static host symbol.

### What doesn't work

- `-Wl,--allow-multiple-definition` / `-Wl,-z,muldefs`: Links but causes **runtime segfaults** (wrong symbol resolved)
- `__attribute__((weak))`: Stripped by HIP compiler during dual-target compilation
- `-fvisibility=hidden`: No effect
- `-fgpu-rdc`: Needs HIP-specific linker flags that CMake doesn't route correctly

### Workaround

No clean workaround found. Possible approaches:
1. Concatenate all `.cu` files into a single translation unit
2. Build with `-fgpu-rdc` and `--hip-link` (requires HIP-aware linker invocation)
3. Build ROCm from source (confirmed working by tlee933/llama.cpp-rdna4-gfx1201)

### Expected Fix

The HIP compiler should properly honor `static inline` on host-side emission during dual-target compilation, or emit these as `weak` symbols.

### Environment

- **GPU:** AMD Radeon AI PRO R9700 (gfx1201, RDNA4)
- **ROCm:** 7.2.0 and 7.2.1
- **OS:** Ubuntu 24.04, kernel 6.17.0
- **Impact:** Blocks building any multi-file HIP project using bfloat16 (including llama.cpp with ~40 .cu files). Affects all GPU architectures, not just RDNA4.

### Related

- #6110 (gfx1201 "2 ISAs" device rejection)
- #6111 (gfx1201 `__AMDGCN_WAVEFRONT_SIZE` undefined)