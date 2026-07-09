# WMMA operations produce wrong results on RDNA3 with ROCm 5.7

- **Issue #:** 6349
- **State:** open
- **Created:** 2026-06-11T18:10:36Z
- **Updated:** 2026-06-11T18:46:05Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6349

Running matrix multiply-accumulate using `wmma::mma_sync` on RX 7800 XT gives incorrect output for non-square matrices (e.g., 16x32 @ 32x16). Works fine for 16x16 @ 16x16.

Reproduced with ROCm 5.7.1 on Ubuntu 22.04. Same kernel works correctly on CUDA (RTX 3060).

Is this a known limitation or am I missing something in the launch config?

```cpp
wmma::fragment<wmma::matrix_a, 16, 16, 16, half, wmma::row_major> a_frag;
wmma::fragment<wmma::matrix_b, 16, 16, 16, half, wmma::col_major> b_frag;
wmma::fragment<wmma::accumulator, 16, 16, 16, float> c_frag;
wmma::fill_fragment(c_frag, 0.0f);
wmma::mma_sync(c_frag, a_frag, b_frag, c_frag);
```

GPU: AMD Radeon RX 7800 XT (gfx1101)
ROCm: 5.7.1
Driver: 6.7.0