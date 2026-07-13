# Strix Halo gfx1151: 93 ML experiments, 5 critical bf16 bugs, AOTriton 19x speedup undocumented

- **Issue #:** 6034
- **State:** open
- **Created:** 2026-03-13T00:44:00Z
- **Updated:** 2026-05-17T00:55:02Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6034

## Summary

We ran 93+ autonomous ML training experiments on a Strix Halo system (Radeon 8060S, gfx1151) using TheROCk nightly PyTorch and discovered 5 critical bf16 bugs, an undocumented 19x attention speedup, and several ecosystem gaps that prevent consumer AMD GPUs from being viable ML research platforms.

**Full repo with all data, reproduction scripts, and cross-hardware comparison:** https://github.com/bkpaine1/amdsense

## Hardware
- **APU**: AMD Ryzen AI MAX+ 395
- **GPU**: Radeon 8060S (gfx1151) — integrated
- **Memory**: 128 GB unified
- **PyTorch**: 2.11.0a0+rocm7.11.0a20260106 (TheROCk nightly)
- **Workload**: [Karpathy autoresearch](https://github.com/karpathy/autoresearch) — 5-minute pretraining loop, val_bpb metric

## Results

Starting from a baseline val_bpb of 1.819, we achieved **1.227** — a 32.5% improvement through autonomous hyperparameter optimization. For comparison, the same recipe on an RTX 4090 (CUDA 12.4, PyTorch 2.4.1 stable) achieves 1.844.

The AMD system achieves 25% MFU vs the 4090's 7.7%, suggesting unified memory architecture has real advantages for memory-bound ML workloads.

## Critical Bugs (Reproduction Steps Included)

### 1. bf16 accumulation crash at small batch sizes
- **Repro**: Set `TOTAL_BATCH_SIZE = 2**13` in train.py
- **Result**: NaN within 15 steps, every time
- **Expected**: Training should complete without NaN
- **Notes**: `TOTAL_BATCH_SIZE = 2**14` with `DEVICE_BATCH_SIZE = 16` also NaN/crashes. Works fine at `2**15`.

### 2. bf16 crash at small head dimensions
- **Repro**: Set `HEAD_DIM = 32` in train.py
- **Result**: NaN crash
- **Expected**: Training should complete
- **Notes**: `HEAD_DIM = 64` works (and is CRITICAL for best results — +1.11% regression when reverted to 128)

### 3. Deep network instability
- **Repro**: Set `DEPTH = 12` or higher in train.py
- **Result**: Timeout/crash. `DEPTH = 16` NaN at step 23.
- **Expected**: Deeper networks should train stably
- **Notes**: `DEPTH = 10` succeeded once, crashed on second attempt. Non-deterministic.

### 4. Wide aspect ratio crash
- **Repro**: Set `ASPECT_RATIO = 128` in train.py
- **Result**: Timeout/crash
- **Expected**: Training should complete
- **Notes**: `ASPECT_RATIO = 64` and `32` work fine. 32 actually produces best results (val_bpb 1.227).

### 5. Sharp matrix LR cliff
- **Repro**: Set `MATRIX_LR = 0.20` in train.py
- **Result**: NaN/crash
- **Expected**: Graceful degradation
- **Notes**: `MATRIX_LR = 0.15` works fine. The cliff between 0.15 and 0.20 is unusually sharp, suggesting a precision boundary.

## Ecosystem Issues

### AOTriton experimental flag gives 19x speedup but is undocumented
```bash
export TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1
```
SDPA goes from 44ms to 2.3ms per call. This is the difference between "AMD is unusable for ML" and "AMD is competitive." **This should be the default, not hidden behind an undocumented env var.**

### TheROCk nightlies required for gfx1151
Stable ROCm does not ship gfx1151 kernels. Consumer Strix Halo users must use:
```
pip install torch --index-url https://rocm.nightlies.amd.com/v2/gfx1151/
```
There should be stable wheels for consumer GPUs.

### Default shell config crashes PyTorch
`PYTORCH_HIP_ALLOC_CONF=backend:malloc` is set in some ROCm shell profiles and crashes PyTorch. Users must `unset PYTORCH_HIP_ALLOC_CONF`. A framework default that crashes the framework is a bug.

### No HSA_OVERRIDE needed (good news)
TheROCk nightlies ship native gfx1151 kernels. `HSA_OVERRIDE_GFX_VERSION` is no longer needed. This should be documented prominently for consumer GPU users who are still using the override hack from older guides.

## Environment
```
PyTorch: 2.11.0a0+rocm7.11.0a20260106
HIP: 7.2.53150
ROCm Driver: 6.18.1-061801-generic
TheROCk Index: https://rocm.nightlies.amd.com/v2/gfx1151/
OS: Linux 6.18.1
```

## Full Data
- Repo: https://github.com/bkpaine1/amdsense
- Round 3 report (33 experiments, ablation, failure boundaries): [round3_report.md](https://github.com/bkpaine1/amdsense/blob/master/round3_report.md)
- AMD profiling report: [profile_report.md](https://github.com/bkpaine1/amdsense/blob/master/profile_report.md)
- NVIDIA comparison: [nvidia_4090_comparison.md](https://github.com/bkpaine1/amdsense/blob/master/nvidia_4090_comparison.md)
- Autonomous agent script: [autoresearch_agent3.py](https://github.com/bkpaine1/amdsense/blob/master/autoresearch_agent3.py)
- RunPod benchmark script: [runpod_benchmark.sh](https://github.com/bkpaine1/amdsense/blob/master/runpod_benchmark.sh)