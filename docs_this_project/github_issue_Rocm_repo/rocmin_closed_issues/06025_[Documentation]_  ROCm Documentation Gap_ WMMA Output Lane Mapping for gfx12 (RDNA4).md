# [Documentation]:  ROCm Documentation Gap: WMMA Output Lane Mapping for gfx12 (RDNA4)

- **Issue #:** 6025
- **State:** closed
- **Created:** 2026-03-08T15:15:36Z
- **Updated:** 2026-03-30T09:00:51Z
- **Labels:** Documentation, status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6025

### Description of errors

# ROCm Documentation Gap: WMMA Output Lane Mapping for gfx12 (RDNA4)

## Summary

The RDNA4 ISA reference and GPUOpen guides document the `v_wmma_f32_16x16x16_f16` instruction encoding and HIP intrinsic signatures, but do not specify the **output lane-to-element mapping** — i.e., which matrix element each lane's accumulator register corresponds to.

This is critical information for anyone writing HIP WMMA kernels directly (outside of rocBLAS/CK). Without it, developers have to reverse-engineer the mapping empirically or dig through CK source code.

## The Missing Information

On gfx12 (Wave32), `v_wmma_f32_16x16x16_f16` uses a **column-distributed fragment layout**:

```
Lane i (0..31) holds:
  Column:  i % 16
  Rows:    (i / 16) * 8  ..  (i / 16) * 8 + 7
  acc[j] = element at row (i/16)*8 + j, column i%16
```

Or as a formula:

```
VGPR[lane][j] = matrix[(lane / 16) * 8 + j][lane % 16]
```

The fast-varying dimension across lanes is the **column index** (N), not the row index (M). This means `lane % 16` selects the column, not the row.

## Why This Matters

The natural assumption for many developers is `lane % 16 = row`, which produces **silently transposed** 16x16 output tiles. The kernel compiles and runs without errors — the output is just wrong in a way that's difficult to diagnose without knowing the correct mapping.

We hit this exact issue building a fused MXFP4 WMMA GEMM kernel on Radeon AI PRO R9700 (gfx1201). It took systematic debugging (identity matrix tests, single-tile isolation, lane-by-lane inspection) to identify the root cause.

## Where This Should Be Documented

The mapping is already present in CK source code (`wmma_gemm.hpp`, lines 31-80) as an ASCII diagram, but:

1. **RDNA4 ISA Reference** — documents instruction encoding but not output lane mapping
2. **GPUOpen "Using Matrix Cores on RDNA4" guide** — shows intrinsic signatures and fragment descriptions, but does not specify which dimension lanes index
3. **No standalone reference** exists that says "for FP16 WMMA on gfx12, lanes index columns"

Adding a lane mapping table or diagram to the GPUOpen guide (similar to what CK has internally) would prevent this issue for every future WMMA kernel developer on RDNA4.

## Additional Observations

The same column-distributed layout appears to apply to all WMMA data types on gfx12 (verified for FP16 and INT4), which is consistent with MFMA on CDNA where `lane % 16` also selects the column. This is a shared architectural convention that would be worth documenting explicitly.

## Verification

We verified the mapping on:
- **Hardware**: AMD Radeon AI PRO R9700 (gfx1201, RDNA4, 32GB)
- **ROCm**: 7.1.0
- **Compiler**: hipcc (clang-19)
- **Tests**: identity matrices, small known matrices, asymmetric matrices (for INT4), and large matrices up to 17408x5120

Full writeup with derivation, correct store patterns, and verification methodology: (https://github.com/JohnTDI-cpu/rdna4-wmma-guide)

## Environment

- ROCm version: 7.1.0
- GPU: gfx1201 (Radeon AI PRO R9700)
- OS: Ubuntu (ROCm default)
- Component: Documentation (ISA Reference / GPUOpen)

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_