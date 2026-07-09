# [Issue]: __AMDGCN_WAVEFRONT_SIZE undefined for gfx1201 — breaks amd_warp_functions.h

- **Issue #:** 6111
- **State:** closed
- **Created:** 2026-04-02T18:04:46Z
- **Updated:** 2026-04-13T21:13:53Z
- **Labels:** status: assessed
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6111

### Problem

Compiling any HIP program for `gfx1201` (RDNA4) fails because `amd_warp_functions.h:86` uses `__AMDGCN_WAVEFRONT_SIZE` which the compiler does not define for wave-variable RDNA4 architectures.

### Reproduction

```bash
hipcc test.hip -o test --offload-arch=gfx1201
```

Error:
```
/usr/include/hip/amd_detail/amd_warp_functions.h:86:33: error:
  use of undeclared identifier '__AMDGCN_WAVEFRONT_SIZE'
   86 | static constexpr int warpSize = __AMDGCN_WAVEFRONT_SIZE;
```

### Root Cause

The HIP 7.0 changelog documents that `warpSize` is "no longer a `constexpr`." However, `amd_warp_functions.h:86` still uses:

```cpp
static constexpr int warpSize = __AMDGCN_WAVEFRONT_SIZE;
```

The compiler defines neither `__AMDGCN_WAVEFRONT_SIZE` nor `__AMDGCN_WAVEFRONT_SIZE__` for gfx1201 because RDNA4 supports both wave32 and wave64 (wave-variable), so no compile-time constant exists.

Verified:
```bash
/opt/rocm/lib/llvm/bin/clang++ -x hip --cuda-device-only \
  --offload-arch=gfx1201 -dM -E - < /dev/null | grep WAVEFRONT
# returns nothing
```

### Workaround

Patch the header:

```diff
-static constexpr int warpSize = __AMDGCN_WAVEFRONT_SIZE;
+#ifdef __AMDGCN_WAVEFRONT_SIZE
+static constexpr int warpSize = __AMDGCN_WAVEFRONT_SIZE;
+#else
+static constexpr int warpSize = 32;
+#endif
```

Or pass `-D__AMDGCN_WAVEFRONT_SIZE=32` to hipcc.

### Expected Fix

The header should handle the case where `__AMDGCN_WAVEFRONT_SIZE` is not defined — either via `#ifdef` guard or by using a runtime query (as the HIP 7.0 changelog implies).

### Environment

- **GPU:** AMD Radeon AI PRO R9700 (gfx1201, RDNA4)
- **ROCm:** 7.2.0 and 7.2.1
- **OS:** Ubuntu 24.04, kernel 6.17.0
- **Impact:** Blocks compilation of all HIP programs targeting gfx1201

### Related

- #6110 (gfx1201 "2 ISAs" device rejection)