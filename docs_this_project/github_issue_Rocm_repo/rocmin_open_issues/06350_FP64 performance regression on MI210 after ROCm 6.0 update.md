# FP64 performance regression on MI210 after ROCm 6.0 update

- **Issue #:** 6350
- **State:** open
- **Created:** 2026-06-11T18:10:38Z
- **Updated:** 2026-06-11T18:43:32Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6350

After upgrading from ROCm 5.7 to 6.0, FP64 throughput on MI210 dropped by ~15%. Measured with:

```python
import torch
x = torch.randn(4096, 4096, dtype=torch.float64, device='cuda')
# Benchmark: 1000 matmul iterations
```

ROCm 5.7: 11.2 TFLOPS (FP64)
ROCm 6.0: 9.5 TFLOPS (FP64)

FP32 performance is unchanged. This affects molecular dynamics simulations significantly since we rely on FP64 for energy conservation.

Is this expected behavior? Any workarounds?

Setup: MI210, Ubuntu 22.04, ROCm 6.0.2