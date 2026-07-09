# [gfx1151] Silent hard hang under sustained vLLM inference with MES 0x86 — amdgpu hangcheck never fires

- **Issue #:** 6165
- **State:** closed
- **Created:** 2026-04-20T16:23:58Z
- **Updated:** 2026-06-12T12:27:48Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6165

Follow-up to [ROCm/ROCm#5724](https://github.com/ROCm/ROCm/issues/5724) and [ROCm/ROCm#5991](https://github.com/ROCm/ROCm/issues/5991). The MES 0x83 page-fault class was resolved for us by upgrading to MES 0x86 (upstream `linux-firmware` tag `20260410`). A **distinct, silent hang** remains on the same node under sustained compute — no page fault, no GPU reset, no MCE, no kernel log. Filing because the fence-ring evidence below narrows it beyond what dmesg shows and may be useful for triage.

## System

| | |
|---|---|
| Machine | Framework Desktop (2025) |
| SoC | AMD Ryzen AI MAX+ 395 (Strix Halo) |
| GPU | Radeon 8060S, gfx1151, PCI `0000:c1:00.0` `[1002:1586]` |
| BIOS | 03.04 (2025-11-19), LVFS latest |
| Distro | Ubuntu Questing (25.10 / 26.04-preLTS) |
| Kernel | `7.0.0-070000-generic` (mainline, `#202604122140 SMP PREEMPT_DYNAMIC Sun Apr 12 22:05:40 UTC 2026`) |
| Kernel cmdline (relevant) | `iommu=pt amdgpu.gttsize=126976 ttm.pages_limit=32505856 amd_iommu=on amdgpu.cwsr_enable=0` |
| `linux-firmware` in use | Ubuntu `20250901` + upstream `20260410` override at `/lib/firmware/updates/amdgpu/` |
| **MES firmware** | `MES feature version: 1, firmware version: 0x00000086` |

### Container / runtime

- Image: `docker.io/kyuz0/vllm-therock-gfx1151:latest` (built 2026-04-19 21:31 UTC)
- vLLM: `0.19.2rc1.dev14+gf150107ef.d20260419`
- PyTorch: `2.13.0a0+rocm7.13.0a20260419`
- HIP: `7.13.26154`

## Symptom

Running vLLM with `cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit` (MoE 35B/3B active, AWQ-4bit, ~20 GiB weights), `--enforce-eager`, `--max-num-seqs 1`, `--max-model-len 262144`, `--gpu-memory-utilization 0.75`, vision encoder disabled.

Under sustained prefill load (agentic client sending back-to-back long-context requests), the engine wedges after **20–90 seconds**:

```
Engine 000: Avg prompt throughput: 0.0 tokens/s,
            Avg generation throughput: 0.0 tokens/s,
            Running: 1 reqs, Waiting: 1 reqs,
            GPU KV cache usage: 0.9%
```

From that point:

1. CPU-only services (systemd-cron, sysstat, tailscaled, journald) keep heartbeating for **2–4 minutes**.
2. The whole box then fully freezes. Only a hard reboot recovers it.
3. After reboot: `EXT4-fs (dm-0): orphan cleanup on readonly fs` + `system.journal … corrupted or uncleanly shut down` (hard-hang confirmation).

### What is NOT present in dmesg

- No `amdgpu … page fault`, no `GCVM_L2_PROTECTION_FAULT_STATUS`.
- No `GPU reset` / `device wedged`.
- No MCE / `hardware error` / `machine check`.
- No OOM / `Killed process`.
- No thermal / throttling / `under-voltage` / `brown-out`.
- No panic / Oops / Call Trace.

The **only** kernel tell on the crashing boot is `pcieport 0000:00:08.1: PME: Spurious native interrupt!`, typically 30–60 s after the engine wedges, consistently present across every reproduction on this node.

## Reproduction

1. Kernel ≥ 6.18-rc6 (or mainline as above), `amdgpu.cwsr_enable=0`.
2. Upstream `linux-firmware 20260410` installed to `/lib/firmware/updates/amdgpu/`, MES reports `0x86`.
3. vLLM via `docker.io/kyuz0/vllm-therock-gfx1151:latest`, settings above.
4. Drive concurrent long-context prefill load (~20 k-token prompts, back-to-back).
5. Hang within 20–90 s.

Short conversational requests do **not** trigger it. A ≥10 k-token prefill burst or sustained decode does.

## Fence-ring evidence (new this round)

### How it was collected

A 2-second-cadence sampler of `/sys/kernel/debug/dri/0000:c1:00.0/amdgpu_fence_info` running as a systemd service on the host, log rotated on each service start so the file active at the moment the box freezes survives the reboot.

Sampler (`/usr/local/bin/gpu-fence-sampler.sh`):

```bash
#!/bin/bash
# Fence-info sampler: 2s cadence, timestamped.
# Rotates on service start so prior-boot data is preserved across crash+reboot.
set -u
LOG=/var/log/gpu-fences.log
if [ -s "$LOG" ]; then
  for i in 4 3 2 1; do
    [ -f "$LOG.$i" ] && mv "$LOG.$i" "$LOG.$((i+1))"
  done
  mv "$LOG" "$LOG.1"
fi
: > "$LOG"
printf '=== boot $(uname -r) start %s ===\n' "$(date -u +%F\ %T)" >> "$LOG"
while true; do
  ts=$(date -u +%H:%M:%S.%3N)
  {
    printf '=== %s ===\n' "$ts"
    cat /sys/kernel/debug/dri/0000:c1:00.0/amdgpu_fence_info
  } >> "$LOG"
  sleep 2
done
```

systemd unit (`/etc/systemd/system/gpu-fence-sampler.service`):

```
[Unit]
Description=amdgpu fence sampler (2s) for hang investigation
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/local/bin/gpu-fence-sampler.sh
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### MES scheduler ring (`mes_3.0.0`) across the wedge

Projected from one representative crash boot (full log attached below as `gpu-fences.log.2`). Each row is a 2 s sample; columns are `Last signaled fence` / `Last emitted`.

| UTC | mes_3.0.0 sig / em | interpretation |
|---|---|---|
| 15:36:00.409 | `0x3ef` / `0x3ef` | normal advance |
| 15:36:46.633 | `0x559` / `0x559` | first request just submitted |
| 15:36:48.641 | `0x561` / `0x561` | advance |
| 15:36:50.648 | `0x561` / `0x561` | advance |
| **15:36:52.666** | **`0x570`** / **`0x570`** | **last observed advance** |
| 15:36:54.675 | `0x570` / `0x570` | frozen |
| 15:37:08.731 | `0x570` / `0x570` | **vLLM reports first `0.0 tok/s`** (≈16 s after MES last advanced) |
| 15:37:46.907 | `0x570` / `0x570` | first `pcieport … PME: Spurious native interrupt!` fires |
| 15:39:39.403 | `0x570` / `0x570` | CPU-only services still heartbeating |
| 15:41:07.794 | `0x570` / `0x570` | **last sampler read before full box freeze** (4 min 14 s of MES freeze captured) |

Across every post-freeze snapshot:

- `Last signaled fence == Last emitted` — host and device agree the ring is idle; host is *not* queuing new MES work.
- `Last reset = 0x00000000` — amdgpu's GPU reset path is **never** invoked.
- `Last preempted = 0x00000000` — no preemption attempts.

### What this rules in / out

- **Rules in:** amdgpu hangcheck/watchdog never fires for this failure mode — that's the reason the crash is silent in dmesg.
- **Rules in:** MES firmware is not fully dead on the bus — the debugfs node is still readable throughout the 2.5–4 min window, i.e. PCIe config space is alive. But the MES ring is not being driven.
- **Does not resolve:** whether the root cause is in MES firmware itself (wedged on chip) or in the amdgpu MES command path (deadlocked on host). `amdgpu_fence_info` is blind to KFD user-mode compute queues (doorbell-driven), which is where vLLM's actual compute submissions live.
- **Does not resolve:** whether a compute shader is still running on the CUs, or the CUs are idle.

## Ruled out (single-variable probes, all exonerated on this node)

| Probe | Result |
|---|---|
| `TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1` dropped | still crashed |
| `amdgpu.noretry=1` | still crashed |
| `ATTENTION_BACKEND=ROCM_ATTN` (vs default `TRITON_ATTN`) | still crashed — note `chunked_prefill_paged_decode.py:398 Cannot use ROCm custom paged attention kernel, falling back to Triton implementation`, so this override is a no-op for the AWQ decode path |
| `VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1` | crashed ~40 s |
| `VLLM_USE_TRITON_FLASH_ATTN=0` | crashed ~23 s |
| `VLLM_ROCM_USE_MMAP_FOR_TRITON=0` | crashed (~60 s) |
| BIOS upgrade | already on latest (03.04, 2025-11-19) |
| Thermal / RAM / GTT pressure | all flat at values well below any threshold during the whole repro window |
| PSU sag | inconsistent with symptom — CPU + NVMe + net keep running 2–4 min after GPU wedge; no under-voltage/MCE/throttle events |

## Known workaround (not a fix)

`VLLM_LOGGING_LEVEL=DEBUG` prevents the hang. The mechanism appears to be that per-step stderr writes throttle the Python submission loop enough that GPU utilisation drops from ~100% to ~70%, which dodges the timing window that triggers the hang. This is consistent with the `pcieport 0000:00:08.1: PME: Spurious native interrupt!` precursor pointing at root-complex bursty-submission stress.

## Questions for AMD

1. Is there a recommended debugfs / sysfs observable for **KFD user-mode compute queue** state that would let us see whether a shader is wedged vs the doorbell path itself? `amdgpu_fence_info` is blind to the actual vLLM compute work.
2. Why does the MES ring freeze while the amdgpu hangcheck never fires? Is the watchdog not armed for MES-ring idleness, or is it armed but the recovery path itself deadlocks before logging?
3. Is the `pcieport 0000:00:08.1: PME: Spurious native interrupt!` signal on Strix Halo (GPU root-complex, `00:08.0`) a known accompanying symptom, and does it point to a specific layer (SMU, PCIe AER, MES)?

---

## Attachments

### `amdgpu_firmware_info` (full)

```
VCE feature version: 0, firmware version: 0x00000000
UVD feature version: 0, firmware version: 0x00000000
MC feature version: 0, firmware version: 0x00000000
ME feature version: 35, firmware version: 0x00000020
PFP feature version: 35, firmware version: 0x00000031
CE feature version: 0, firmware version: 0x00000000
RLC feature version: 1, firmware version: 0x11530506
RLC SRLC feature version: 0, firmware version: 0x00000000
RLC SRLG feature version: 0, firmware version: 0x00000000
RLC SRLS feature version: 0, firmware version: 0x00000000
RLCP feature version: 1, firmware version: 0x11530506
RLCV feature version: 0, firmware version: 0x00000000
MEC feature version: 35, firmware version: 0x00000022
IMU feature version: 0, firmware version: 0x0b352300
SOS feature version: 0, firmware version: 0x00000000
ASD feature version: 553648393, firmware version: 0x21000109
TA XGMI feature version: 0x00000000, firmware version: 0x00000000
TA RAS feature version: 0x00000000, firmware version: 0x00000000
TA HDCP feature version: 0x00000000, firmware version: 0x1700004d
TA DTM feature version: 0x00000000, firmware version: 0x1200001d
TA RAP feature version: 0x00000000, firmware version: 0x00000000
TA SECUREDISPLAY feature version: 0x00000000, firmware version: 0x00000000
SMC feature version: 0, program: 10, firmware version: 0x0a640600 (100.6.0)
SDMA0 feature version: 60, firmware version: 0x00000012
VCN feature version: 0, firmware version: 0x09118010
DMCU feature version: 0, firmware version: 0x00000000
DMCUB feature version: 0, firmware version: 0x09004100
TOC feature version: 0, firmware version: 0x0000000b
MES_KIQ feature version: 6, firmware version: 0x0000006f
MES feature version: 1, firmware version: 0x00000086
VPE feature version: 60, firmware version: 0x00000017
VBIOS version: 113-STRXLGEN-001
```

### GPU `lspci -vvv` (relevant sections)

```
c1:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Strix Halo
        [Radeon Graphics / Radeon 8050S Graphics / Radeon 8060S Graphics] (rev c1)
    Subsystem: Framework Computer Inc. Device 000a
    IOMMU group: 17
    Region 0: Memory at 6800000000 (64-bit, prefetchable) [size=512M]
    Region 2: Memory at b0000000  (64-bit, prefetchable) [size=2M]
    Region 5: Memory at b0400000  (32-bit, non-prefetchable) [size=1M]
    Capabilities: [50] Power Management version 3
        Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA
               PME(D0-,D1+,D2+,D3hot+,D3cold+)
    Capabilities: [64] Express (v2) Legacy Endpoint
        LnkCap: Port #0, Speed 16GT/s, Width x16
        LnkSta: Speed 16GT/s, Width x16
                TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
    Capabilities: [2a0 v1] Access Control Services
    Capabilities: [2b0 v1] Address Translation Service (ATS)   Enable+
    Capabilities: [2c0 v1] Page Request Interface (PRI)
```

(Link is at its target 16 GT/s × 16 with no training errors, ATS enabled, PRI capability present. No AER errors.)

### vLLM log — transition into wedge

Selected lines from the vLLM server stdout for the probe-2 crash (`VLLM_USE_TRITON_FLASH_ATTN=0`). Client IPs redacted.

```
15:36:28  INFO: Application startup complete.
15:36:45  WARNING chunked_prefill_paged_decode.py:398
          Cannot use ROCm custom paged attention kernel,
          falling back to Triton implementation.
15:36:46  INFO: 127.0.0.1:45814 - "POST /v1/chat/completions HTTP/1.1" 200 OK
15:36:47  INFO: 127.0.0.1:45814 - "POST /v1/chat/completions HTTP/1.1" 200 OK
15:36:48  Engine 000: Avg prompt throughput: 6.9 tokens/s,
                     Avg generation throughput: 0.2 tokens/s,
                     Running: 0 reqs, Waiting: 0 reqs
15:36:48..:51   several 200 OK responses, both localhost and remote client
15:36:58  Engine 000: Avg prompt throughput: 207.4 tokens/s,
                     Avg generation throughput: 3.4 tokens/s,
                     Running: 1 reqs, Waiting: 1 reqs,
                     GPU KV cache usage: 0.6%
15:37:08  Engine 000: Avg prompt throughput: 0.0 tokens/s,    ← wedge
                     Avg generation throughput: 0.0 tokens/s,
                     Running: 1 reqs, Waiting: 1 reqs,
                     GPU KV cache usage: 0.9%
(from this point no further engine log lines are emitted)
15:37:46  kernel: pcieport 0000:00:08.1: PME: Spurious native interrupt!
(cron/sysstat keep running until ~15:40:29, then full box freeze)
```

### Full fence-info sampler log (crash boot)

> Attached as `gpu-fences.log.2` (≈ 820 KB, gzipped). Contents are 2 s-cadence snapshots of `/sys/kernel/debug/dri/0000:c1:00.0/amdgpu_fence_info` covering 9 min 8 s spanning pre-wedge, wedge, and sampler death at full box freeze. No sensitive data.
[gpu-fences.log.2.gz](https://github.com/user-attachments/files/26903760/gpu-fences.log.2.gz)

[amdgpu_firmware_info.txt](https://github.com/user-attachments/files/26903759/amdgpu_firmware_info.txt)

### Also available on request

- `journalctl -b -1` for each of 4 crashing boots on 2026-04-20 (will redact hostnames/IPs before sharing if preferred).
- vLLM full stdout/stderr for each reproduction.
- `gpu-fences.log.1`, `.log.3` — fence-info sampler logs for the other crashing boots on 2026-04-20 (similar signature, same 0x570-class freeze on a different last-fence value each run).