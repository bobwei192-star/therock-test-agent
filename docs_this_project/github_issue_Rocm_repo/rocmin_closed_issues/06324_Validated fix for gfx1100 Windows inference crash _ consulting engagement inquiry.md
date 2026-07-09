# Validated fix for gfx1100 Windows inference crash — consulting engagement inquiry

- **Issue #:** 6324
- **State:** closed
- **Created:** 2026-06-02T15:34:19Z
- **Updated:** 2026-06-04T19:41:38Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6324

I've diagnosed and validated a fix for the deterministic exit code 2 crash affecting every gfx1100 user running ROCm inference on Windows (Ollama, llama.cpp).

Root causes found (two independent issues):

KV cache stream affinity — Windows ROCm enforces stream affinity on device allocations; ggml-hip accesses KV cache buffer on a non-default compute stream without a sync barrier
Flash Attention memory layout — gfx1100 Windows-specific fault on split K/V view tensors
Validated on RX 7900 GRE · gfx1100 · Windows 11 · ROCm 7.1:

110.17 tokens/s (llama-server direct)
108.75 tokens/s (Ollama end-to-end)
1.34s total inference time
All HIP stream sync tests passing
Also documented: ROCm 7.1 + VS 2026 clang header conflicts in clang/21/include/ that block any Windows ROCm build against current MSVC STL — not documented anywhere publicly.

Full write-up, patch, and test suite at: https://github.com/Beat-k/BEATEK_ROCm

I'd like to discuss a consulting engagement to integrate this properly into the ROCm Windows stack. Is there a business development or partner engineering contact I can reach directly?

— Jeremy F. Jackson · BEATEK Holdings, LLC · [jeremy.jackson0@beatek.io](mailto:jeremy.jackson0@beatek.io)

[BEATEK_ROCm_Capability_Brief.pdf](https://github.com/user-attachments/files/28516694/BEATEK_ROCm_Capability_Brief.pdf)