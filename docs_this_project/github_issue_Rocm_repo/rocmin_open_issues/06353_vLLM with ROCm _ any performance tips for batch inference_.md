# vLLM with ROCm — any performance tips for batch inference?

- **Issue #:** 6353
- **State:** open
- **Created:** 2026-06-11T18:10:43Z
- **Updated:** 2026-06-25T13:19:49Z
- **Labels:** AMD Instinct MI210, status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6353

Running vLLM on MI210 for LLM batch inference. Getting ~400 tok/s with Llama 3 8B which seems low compared to A100 benchmarks (1200 tok/s).

Am I missing some ROCm-specific configuration? Or is this the expected performance gap?

```bash
vllm serve meta-llama/Meta-Llama-3-8B --dtype float16 --gpu-memory-utilization 0.9
```

Any tips for squeezing more performance out of MI210 for inference workloads?

Setup: MI210 (32GB), ROCm 6.0, vLLM 0.4.1