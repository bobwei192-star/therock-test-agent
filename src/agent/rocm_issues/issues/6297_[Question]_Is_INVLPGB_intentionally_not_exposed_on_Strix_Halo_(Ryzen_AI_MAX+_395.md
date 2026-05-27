# [Question] Is INVLPGB intentionally not exposed on Strix Halo (Ryzen AI MAX+ 395)? Has measurable downstream cost in GPU training workloads.

> **Issue #6297**
> **状态**: open
> **创建时间**: 2026-05-24T14:26:38Z
> **更新时间**: 2026-05-26T15:42:19Z
> **作者**: h34v3nzc0dex
> **标签**: status: triage
> **URL**: https://github.com/ROCm/ROCm/issues/6297

## 标签

- **status: triage** (颜色: #585dd7)

## 负责人

- darren-amd

## 描述


## Summary

On Strix Halo (Ryzen AI MAX+ 395 / Zen 5 / gfx1151), `/proc/cpuinfo` does **not** list the `invlpgb` flag despite Zen 5 architecturally supporting it. This appears to be the root cause of a reproducible CPU-saturation storm during HuggingFace Trainer evaluation in GPU LoRA training workloads — every per-checkpoint eval pegs all 32 cores at 100% for 5–10 minutes via TLB-shootdown IPIs.

Filing this as a question (not a bug report) because we genuinely don't know whether this is:
1. **Intentional silicon-side non-implementation** on Zen 5 mobile parts, in which case downstream workarounds are the only path; or
2. **A kernel/microcode detection gap** in `arch/x86/kernel/cpu/amd.c`, in which case there's an upstream fix that would eliminate the storm class entirely.

If the AMD kernel team can confirm which it is, that closes the question for the broader Strix Halo / Ryzen AI MAX community and tells us whether to keep pursuing workarounds or wait for a fix.

## Environment

- AMD Ryzen AI MAX+ 395 (Zen 5)
- AMD Radeon 8060S iGPU (gfx1151, RDNA 3.5)
- Ubuntu 24.04 LTS, kernel 6.19.14 mainline
- ROCm 7.13 nightly (training venv) + ROCm 7.1.0 stable (system)
- 128 GB unified memory

`/proc/cpuinfo` (relevant excerpt):
```
$ grep -c invlpgb /proc/cpuinfo
0
```

## Observed symptom

In a Qwen3.5-27B bf16 LoRA fine-tune workload (single-GPU, Strix Halo), every HuggingFace Trainer evaluation step (`Trainer.evaluate()`) triggers:

- All 32 logical cores pegged at 100% sustained
- Duration: 5–10 minutes per eval, dominating wall-clock time
- GPU stays at ~30–40% utilization throughout (i.e., the eval is CPU-bound, not GPU-bound)
- `perf top` (when we briefly profiled it) showed `flush_tlb_func` + `call_function_single_interrupt` dominating

The workload is GPU-resident (model + attention all on gfx1151), so the IPI storm is *not* from data movement. It's from page churn during eval-mode forward passes, hitting the kernel `mm/vmscan.c` reclaim path which batches dirty folios into pagevecs of size `PAGEVEC_SIZE = 31` and fires `try_to_unmap_flush_dirty` every batch. Without `INVLPGB`, each shootdown is a per-CPU IPI — at the rate the eval generates them, the whole system grinds.

## Why this matters in practice

- For users running GPU LoRA fine-tuning on Strix Halo, eval frequency has to be drastically reduced or moved entirely out-of-process to avoid 5–10 min stalls per checkpoint
- The workaround we've documented in our community guide is to use `llama-perplexity` for eval against a merged-GGUF checkpoint (storm-free path), but it requires GGUF conversion per checkpoint and isn't a drop-in fix
- Other Strix Halo users running long-context inference workloads (large prefill batches, RAG, multi-turn agentic loops) likely hit attenuated versions of the same storm even without HF Trainer in the picture, given the same TLB-shootdown pattern

## Workaround for affected users (interim)

Until the INVLPGB question is settled, the practical workaround we've found is to run eval out-of-process via `llama-perplexity` after each checkpoint save. Documented with reproducer here: https://github.com/h34v3nzc0dex/strix-halo-llm-finetune-guide#step-7--the-eval-problem

## Question for AMD

1. Is `INVLPGB` intentionally not exposed on Strix Halo / Ryzen AI MAX mobile parts? (i.e., a silicon/firmware decision)
2. If not — is there a known kernel detection gap, and is a fix in flight?
3. If `INVLPGB` is genuinely unavailable on this silicon, are there other Zen 5 fast-shootdown paths (e.g., adjacent extensions) that the kernel could be leveraging on Strix Halo but currently isn't?

Happy to provide additional `perf` / `ftrace` data, run an instrumented kernel, or test patches if useful. Test bench is available and reproducer is deterministic.

