# Recommended TFLOPs benchmark script

- **Issue #:** 5923
- **State:** closed
- **Created:** 2026-02-02T17:58:36Z
- **Updated:** 2026-05-12T17:40:49Z
- **Labels:** status: triage
- **Assignees:** benrichard-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5923

Hey,

 please, how can I verify TFLOPs values shown here <https://www.amd.com/en/products/accelerators/instinct/mi300/mi325x.html#tabs-27754605c8-item-1cfc3fe320-tab>?

I am trying to verify that using my pytorch script:

~~~python
import torch
import time

# Make sure you're on ROCm
assert torch.version.hip is not None

device = "cuda"

M = N = K = 2**14

# dtype = torch.float32 # FP32 (Vector)
dtype = torch.float64 # FP64 (Vector)

A = torch.randn((M, K), device=device, dtype=dtype)
B = torch.randn((K, N), device=device, dtype=dtype)

# Warmup
for _ in range(10):
    C = torch.matmul(A, B)

torch.cuda.synchronize()

# Timed runs
iters = 20
start = time.time()
for _ in range(iters):
    C = torch.matmul(A, B)

torch.cuda.synchronize()
elapsed = time.time() - start

# FLOPs calculation
flops = 2 * M * N * K * iters
tflops = flops / elapsed / 1e12

print(f"Elapsed time: {elapsed:.3f} s")
print(f"GEMM Throughput: {tflops:.1f} TFLOPs")
~~~

I am getting 82.4 TFLOPs for float64 and 130.6 float32. I actually expected something like 164 TFLOPs for float64 as the script makes matrix multiplication.
 
Please provide some script (preferably bash, python - pytorch, etc.) I can use in my stack:
- Ubuntu 22.04
- CPU: AMD EPYC 9965
- GPU: AMD MI325x

Thanks in advance