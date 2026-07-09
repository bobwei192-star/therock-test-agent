# [BUG] 99% GPU (ROCm) idle usage when both LLM and Embedding models are loaded simultaneously

- **Issue #:** 6390
- **State:** open
- **Created:** 2026-06-30T17:48:57Z
- **Updated:** 2026-06-30T17:58:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/6390

### Platform

Linux/CachyOS with newest kernel 7.1

### Backend - Lemonade

10.8.1

### GPU / APU Model

PC with RX6600 8 gb and laptop with Ryzen 7 AI 350 (860M)

### Component

llama.cpp ROCm 7.13


### Bug Description

When running a single model (either an LLM or an Embedding model), the GPU (via ROCm) idle usage is normal (around 0%). However, as soon as both an LLM model and an Embedding model are loaded simultaneously into VRAM, the GPU usage immediately spikes to 99%-100% and stays there permanently, even when the server is completely idle and no requests are being processed.

This behavior does not seem to be a VRAM capacity issue (OOM / swapping), as it happens even with very lightweight models where the total VRAM allocation is only around 4.5 GB out of 8 GB available.

Note that this issue does not occur when using the Vulkan backend; both models sit at 0% idle GPU usage as expected, which indicates the problem is specific to the ROCm multi-process resource handling

### Steps to Reproduce

Models tested (all combinations exhibit the same behavior):

LLM Models: 
* gemma-4-12B-it-qat-GGUF-UD-Q4_K_XL

* gemma-4-E4B-it-qat-GGUF-UD-Q4_K_XL

Embedding Models:

* embeddinggemma-300m-GGUF-Q8_0

* qwen3-0.6b-embedding

### Expected vs Actual Behavior

Under the hood, Lemonade spawns two separate instances of llama-server. When both are bound to the ROCm backend simultaneously, it appears that a busy-waiting loop or thread conflict occurs between the two instances (possibly related to the BackendWatchdog, --metrics polling, or the --warmup phase).

Moving the embedding model to the CPU completely mitigates the issue, confirming that the bug is tightly coupled with multi-process ROCm resource handling inside llama-server / Lemonade.



### Log Output

[Llama rx6600 Gemmae4b.txt](https://github.com/user-attachments/files/29517522/Llama.rx6600.Gemmae4b.txt)

[Llama rx6600 Gemma12b.txt](https://github.com/user-attachments/files/29517533/Llama.rx6600.Gemma12b.txt)