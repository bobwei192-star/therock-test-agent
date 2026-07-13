# [Issue]: R9700 (gfx1201) — vLLM decode throughput is bimodal (~33 vs ~26 tok/s), fixed at process spawn and not recoverable without restart

- **Issue #:** 6347
- **State:** open
- **Created:** 2026-06-11T15:00:55Z
- **Updated:** 2026-06-15T09:05:36Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6347

### Summary

On a single **Radeon AI PRO R9700 (gfx1201)** running vLLM for LLM inference, decode throughput for the *same* model and *same* launch command lands on one of two stable values — roughly **33 tok/s ("fast")** or **26 tok/s ("slow")** — and which one you get is **random per process start**. There is nothing in between.

A process that starts fast can also **degrade to slow permanently** at some random later time; once slow, only restarting the process (HIP/CUDA context) recovers it — and that recovery is again a coin flip.

Over ~3 days we ran controlled experiments to find what triggers this. **Conclusion: the state appears to be fixed when the HIP process initializes, and we could not find any workload, clock setting, or keep-alive pattern that changes it afterward** (heavy inference, pure idle, and periodic keep-alive all degrade at similar rates). This is related to #6289 (RX 9070 XT, GFXCLK appearing stuck) but is reproducible here without any `HSA_OVERRIDE_GFX_VERSION` and with full diagnostics. Filed as a separate issue at the request of @darren-amd in https://github.com/ROCm/ROCm/issues/6289#issuecomment-4681353915.

---

### Background (what we observe and why it matters)

We run a small LLM inference server (vLLM, single GPU) serving Qwen3-14B-FP8. The model output is **always correct** in both states — only the **decode speed** differs (~33 vs ~26 tok/s, about a 21% drop). That drop is user-visible without measuring: at ~33 tok/s text renders faster than a person reads, at ~26 it renders slower, so a user notices it immediately. That is in fact how we first noticed it (a user reported the second long answer in a chat session "typing out" slower than the first).

Across both states we observed **no abnormal temperature** (junction ~82 °C under load), **no abnormal `gpu_busy_percent`** (100% under load), no GPU resets, no ring timeouts, no ECC events, and no dmesg errors. The behavior is therefore consistent with a GPU power/clock-management or queue-initialization issue rather than thermal throttling, utilization, or an application-level bug — though we cannot inspect SMU/MES firmware internals, so we are not in a position to rule out a lower-level cause.

---

### Symptom 1 — spawn lottery (fast vs slow is random per process start)

Restarting the container with the **identical** config is a dice roll. Each line below is the average of several single-stream decode measurements taken ~1 minute after a fresh spawn:

```
series A:  #1 25.93   #2 26.15   #3 26.05   #4 25.97   #5 33.15  <- fast
series B:  #1 25.66   #2 26.06   #3 25.85   #4 25.83   #5 33.19  <- fast
(other times the 1st spawn is already 33.x)
```

In a separate session, catching a fast process for the experiments below took anywhere from 1 to 10 restarts (observed: 1, 1, 1, 2, 2, 3, 7, 10 restarts to first reach 33.x). The split is:

- Strictly bimodal: every run is either ~26.x or ~33.x, never in between.
- Within a state, variance is tiny (±0.1–0.2 over 10 runs).
- Nothing in the application differs between spawns (same image, same flags, same env — verified via the launch cmdline and `/proc/<pid>/environ`).
- In the fast state, SCLK boosts to ~3.4 GHz under load. In the slow state, decode is ~26 even though SCLK telemetry under load often still *reads* ~3.4 GHz (see "clock telemetry" note below).

### Symptom 2 — a fast process degrades to slow, permanently, at a random time

A process that spawned fast stays fast while it gets traffic, then at some point drops into the slow band and never recovers on its own. We measured this two ways.

**(a) Idle-duration sweep.** Catch a fast process, then idle for growing gaps (1 min, 2 min, 3 min, …), measuring after each gap, until it degrades:

```
run 1:  survived 1, 2, 3 min gaps  ->  degraded at the 4-minute gap (total ~10 min)
run 2:  survived 1, 2, 3, ... 46 min gaps (identical config)
        ->  degraded at the 47-minute gap (total ~18.9 hours, 47 probe cycles)
```

Same config, same machine: one died after a single 4-minute idle gap, the other survived 46 progressively longer gaps over almost 19 hours. **There is no fixed idle timer.** The "lifetime" of a fast process looks random and appears set at spawn. (Note: the degrade-cycle measurement itself can read a bit below the steady slow value — e.g. run 2's degrade sample was 23.5 tok/s with SCLK transiently at 3.36 GHz — before settling into the ~26 band.)

**(b) Clock telemetry is misleading.** In both sweep runs, every probe found the GPU at SCLK **41 MHz** (it drops there within ~1 minute of idle, even with `power_dpm_force_performance_level=high`). Run 2 was probed from a 41 MHz idle state 47 times and stayed fast 46 of them — so **sitting at 41 MHz is not the trigger**. And in the *slow* state, SCLK under load still samples ~3.4 GHz while decode is ~26. So the reported SCLK does not predict or explain the slow/fast state.

---

### Controlled experiment — is the degradation triggered by the workload? (Answer: no)

We suspected heavy inference might be the trigger. We tested it directly: catch a fast process, apply one of three treatments, then measure. 3 rounds each (9 total).

```
HEAVY      (2x 2048-token reasoning generations immediately, then measure):
           33 / 26 / 33   -> 1 of 3 degraded
PURE_IDLE  (10 min idle, zero activity, then measure):
           26 / 33 / 33   -> 1 of 3 degraded
KEEPALIVE  (one tiny request every 90 s for 10 min, then measure):
           26 / 26 / 26   -> 3 of 3 degraded
```

- **HEAVY and PURE_IDLE degrade at the same rate (1/3).** Doing heavy work or doing absolutely nothing makes no difference, so the "heavy load triggers it" hypothesis is not supported. (Our earlier "heavy load killed it" observation was a coincidence: that process simply reached the end of its random fast-state lifetime around when the user happened to be active.)
- **Clock state at measurement is irrelevant**: HEAVY was measured with SCLK still ~2300–2500 MHz (just finished generating), PURE_IDLE from a 74 MHz deep-idle floor — same degradation rate despite a ~30x difference.
- **Frequent keep-alive did not help, and the 3/3 result may even suggest it hurts.** This matches a separate earlier negative result where a 90 s / 1-token keep-alive daemon failed to prevent degradation over 4 hours. The 19-hour survivor above was only probed at growing 1–47 min intervals. We cannot conclude from n=3 whether frequent wake/sleep transitions actively raise the failure rate, but they clearly do not prevent it.

---

### What we tried and ruled out (none keep a fast process fast)

| Attempt | Result |
|---|---|
| `power_dpm_force_performance_level=high` | idle SCLK still drops to 41 MHz; does not prevent degradation |
| `manual` + force highest DPM level (2350 MHz table peak) | pins ~2300 MHz, **kills boost** → 26.6 tok/s (same as slow state) |
| `power_dpm_force_performance_level=auto` | **fast state never even appears** — 0/8 spawns reached 33 |
| keep-alive, light (1 token / 90 s) | no effect over 4 h |
| keep-alive, frequent (in the 9-run test) | no effect, 3/3 degraded |
| profile_peak | not useful on this card — it pins the 2350 MHz table peak, i.e. the slow number, since our fast state boosts *above* the table peak |

The only thing that works is **restarting the process until it lands in the fast state.**

---

### Interpretation

The fast/slow outcome — and the fragility/lifetime of a fast process — appears to be **decided when the HIP process / its hardware queues are initialized**, independent of any subsequent workload, clock setting, or keep-alive we tested. This is consistent with a **race at process/queue initialization** rather than a workload- or time-triggered transition, and it would explain why this is hard to reproduce on demand: a lucky spawn looks healthy for hours no matter what you do to it, so a single manual test usually lands on the lucky case. Running many spawns (as we did) surfaces the bimodal split clearly.

---

### Environment (full, for reproduction)

**Hardware / OS**
- GPU: single AMD Radeon AI PRO R9700 (gfx1201, 32 GB), device `0x7551`
- CPU: Intel Core i7-8700K
- OS: Ubuntu 24.04, kernel `6.17.0-23-generic`, in-tree amdgpu
- vbios `113-APM107573-101`, SMC FW `0x00684a00` (104.74.0)
- dmesg: `smu driver if version = 0x2e (46), smu fw if version = 0x32 (50) — SMU driver if version not matched`
- Host ROCm 7.2.3 (kernel driver only); inference runs in a container
- `power/runtime_status`: `active`
- **No `HSA_OVERRIDE_GFX_VERSION` set anywhere** — card detected natively as gfx1201, kfd `gfx_target_version 120001`

**Container (where inference runs)**
- Base image: `vllm/vllm-openai-rocm:v0.22.1` (official ROCm vLLM image)
- vLLM 0.22.1, torch 2.10.0+rocm7.2 (`torch.version.hip = 7.2.53211`), transformers 5.10.2
- Since gfx1201 is not officially enabled in this image, we apply a small build-time patch to make it run on gfx1201: (a) wrap the `amdsmi` import that otherwise hard-fails, and (b) add gfx1201 to the AITER "is supported" gate so the AITER Triton path is selectable. This is essentially what vLLM PR #43615 ("[ROCm] Enable AITER and FP8 inference on GFX120x") upstreams; our manual setup matches its defaults. Patch diff available on request.

**Launch command**
```
vllm serve /models/qwen3-14b-fp8/ \
  --dtype bfloat16 \
  --gpu-memory-utilization 0.90 \
  --max-model-len 16384 \
  --max-num-seqs 9 \
  --enable-prefix-caching \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser hermes \
  --served-model-name qwen3-14b-fp8 \
  --attention-backend ROCM_AITER_UNIFIED_ATTN \
  --kv-cache-dtype fp8 \
  --compilation-config '{"cudagraph_mode":"PIECEWISE"}'
```

**Key environment variables**
```
VLLM_ROCM_USE_AITER=1
VLLM_ROCM_USE_AITER_RMSNORM=0      # AITER RMSNorm crashes on gfx12; native RMSNorm works
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE
ROCBLAS_USE_HIPBLASLT=1
TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1
PYTORCH_ROCM_ARCH=gfx1201
```

**Model**
- `Qwen/Qwen3-14B-FP8` (the official Qwen FP8 build of Qwen3-14B; `Qwen3ForCausalLM`, FP8 e4m3, dynamic per-tensor activation — `quant_method: fp8`, `activation_scheme: dynamic`). License Apache-2.0.

**How we measure**
- Single-stream decode: a fixed prompt, `max_tokens=100`, `temperature=0.7`, measure `completion_tokens / wall_time`, averaged over several runs. The fast/slow split is unmistakable (33.x vs 26.x with ±0.1 variance), so no special tooling is needed. (A degrade sample taken at the exact moment of transition can read a bit lower before settling.)

---

### Diagnostics we can provide

This is a dedicated test box and the bimodal behavior reproduces reliably across spawns. On request we can provide: per-cycle logs of both sweep runs, a 10-second SCLK time series of fast vs slow states, full `collect_env` / `rocminfo --support`, the gfx1201 enabling patch diff, or run any targeted diagnostic (e.g. `freq1_input` / `gpu_busy_percent` / `mem_busy_percent` time series, `runtime_status`, `umr` dumps) during a known-fast or known-slow window.

### Related
- #6289 — RX 9070 XT, GFXCLK appears stuck at 41 MHz during ROCm inference (same GPU family). Note our data argues the 41 MHz idle floor is *not* itself the cause here (a fast process survived 46 probes from 41 MHz), so this may be the same underlying behavior seen from a different angle.
