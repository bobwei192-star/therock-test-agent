# Non-deterministic NaN corruption during CPU→GPU tensor transfer on gfx1030 (RX 6900 XT)

- **Issue #:** 6123
- **State:** open
- **Created:** 2026-04-07T00:11:16Z
- **Updated:** 2026-05-04T09:45:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/6123

**System Information**
GPU: AMD Radeon RX 6900 XT (gfx1030)
ROCm: 6.4.2
PyTorch: 2.9.1+rocm6.4
OS: Linux Mint 21.2 (Ubuntu 22.04 Jammy)
Kernel: Linux 5.15.0-153-generic
Driver: amdgpu

**Problem Description**
Non-deterministic NaN corruption occurs when transferring tensors from CPU to GPU using .to("cuda"). The corruption is not caused by the tensor values themselves.

**Minimal Reproducer**
```
import torch

# Create tensor once on CPU - data is constant, not recreated
w = torch.randn(13000, 384)

# Repeat only the transfer
for run in range(10):
    w_gpu = w.to("cuda")
    print(f"Run {run}: NaN={torch.isnan(w_gpu).any()}")

# Expected: all False
# Actual: NaN appears non-deterministically, more frequently after the first transfer
```

**Observations**
Bug affects tensors of all sizes
The first or second transfer of a new tensor succeeds more often than subsequent transfers
Repeated transfers of the same tensor fail more frequently
The bug is non-deterministic but highly reproducible over multiple runs
Random data and real model weights are both affected

**Real-world Impact**
This bug breaks PyTorch model inference. For example, OpenAI Whisper's token_embedding.weight matrix (51865 × 384, float32) is silently corrupted when loaded onto the GPU, producing NaN logits and crashing inference. The model loads without error but produces invalid results.

**Workaround**
Retry the transfer until no NaN values are detected:
pythonfor attempt in range(10):
    w_gpu = w_cpu.to("cuda")
    if not torch.isnan(w_gpu).any():
        break  # Transfer successful
This typically succeeds within 1–2 attempts.

**Additional Notes**
- torch.cuda.is_available() returns True and the GPU is correctly detected
- rocminfo correctly identifies the GPU as gfx1030
- No error or warning is raised during the corrupted transfer – the corruption is silent