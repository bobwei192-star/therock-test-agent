# gfx1151 (Strix Halo / Bosgame M5 / Sixunited AXB35-02) — HSA `Memory critical error by agent node-0 ... Reason: Memory in use` on first GGUF model upload, persists on kernel 7.0.1 (KFD ABI 1.22) across all software combinations

- **Issue #:** 6182
- **State:** open
- **Created:** 2026-04-25T04:56:42Z
- **Updated:** 2026-06-26T14:55:40Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6182


## TL;DR

On a Bosgame M5 (Sixunited AXB35-02 board, AMI BIOS 1.07 / 2025-09-12), every PyTorch/HIP workload that loads a sizeable model into `cuda:0` reproduces a non-recoverable HSA fault:

```
Memory critical error by agent node-0 (Agent handle: 0x...) on address 0x7f.... Reason: Memory in use.
```

The crash fires at `hsaKmtFreeMemory` of a 4 KB host-mapped page allocated on node 1 during HSA queue/scratch setup. **Software is fully exhausted**: 4 kernels (incl. mainline 7.0.1 with KFD ABI 1.22), 4 ROCm versions (incl. stable 7.2.2), 5 HSA env-var levers, 8 kernel cmdline variants, two firmware revisions, two BIOS UMA settings, two containers (incl. AMD official `rocm/pytorch:rocm7.2.2`). A simple `hipMalloc/hipMemset/hipDeviceSynchronize/hipFree` cycle works; only the model-load pattern fails. ~~llama.cpp + ROCm runs end-to-end on the same GPU with identical kernel/firmware.~~ *(Edit 2026-04-27: corrected — my llama.cpp here is Vulkan RADV, not ROCm; see What works section.)* Filing because the matrix is now tight enough to be diagnostic.

## Hardware

| | |
|---|---|
| Mini-PC | Bosgame M5 (BeyondMax Series) |
| Mainboard | Sixunited AXB35-02 |
| SoC | AMD Ryzen AI MAX+ 395 w/ Radeon 8060S (Strix Halo) |
| GPU target | `gfx1151`, 40 CUs, wavefront 32 |
| RAM | 128 GB unified |
| BIOS | AMI 1.07 / 2025-09-12 (Bosgame has shipped no updates since launch) |
| BIOS UMA "Dedicated Graphics Memory" | 0.5 GB (also tested 64 GB — same crash) |
| Secure Boot | disabled |

The same physical board (AXB35-02) is rebadged by GMKtec as the EVO-X2, which has BIOS v1.12 (2025-12-09) — community-confirmed safe for cross-flash on Bosgame M5 ([strixhalo.wiki AXB35 firmware page](https://strixhalo.wiki/Hardware/Boards/Sixunited_AXB35/Firmware)). I have not cross-flashed (yet); leaving that as a separate hardware-side variable.

## Software stack

| | |
|---|---|
| OS | Fedora 43 Workstation |
| Kernel | `7.0.1-262.vanilla.fc43.x86_64` (`@kernel-vanilla/stable` Copr) |
| KFD ABI | MAJOR=1, MINOR=22 (`/usr/src/kernels/.../include/uapi/linux/kfd_ioctl.h`) |
| Mainline kernel fixes confirmed in tree | b42f3bf9 VGPR save-restore, 71776e0965f9 CWSR export, 7a5fb05b ABI 1.20→1.22 |
| firmware | `linux-firmware-20260110-1.fc43` (also tested 20260309) |
| Kernel cmdline | `rhgb quiet iommu=pt ttm.pages_limit=32505856` (also tried with `amd_iommu=off`, `amdgpu.cwsr_enable=0`, `amdgpu.sched_policy=2`, `amdgpu.vm_fragment_size=9`, `amdgpu.gttsize=126976`, `amdttm.*`, `ttm.page_pool_size`) |

**ROCm userspace stacks tested (all crash identically):**
- AMD official `docker.io/rocm/pytorch:rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.10.0` (2026-04-15) — torch 2.10.0+rocm7.2.2.git40d237bf, hip 7.2.53211
- TheRock nightly `kyuz0/amd-strix-halo-comfyui:latest` — torch 2.11.0a0+rocm7.12.0a20260211, hip 7.3.53390
- TheRock pinned `7.11.0a20260106`
- Direct `repo.radeon.com` torch wheel `2.10.0+rocm7.2.0.lw.gitb6ee5fde`

## Symptom

```
:0:rocdevice.cpp:... Memory critical error by agent node-0 (Agent handle: 0x...) on address 0x7f.... Reason: Memory in use.
```

Reproduces in any process that loads a transformer-style text encoder or large UNet onto `cuda:0`. Consistent across:
- **WAN 2.2 ti2v 5B fp16 (Q5_K_M GGUF)** at 512×384×17 frames — fires at `Requested to load WanTEModel` (the umt5-xxl text encoder)
- WAN 2.2 i2v 14B fp8+fp16
- SeedVR2 video upscaler (any size)
- Flux 2 dev (fp8 mixed + bf16 Mistral)
- Plain `torch.zeros(N, dtype=torch.float32, device='cuda:0')` for any N **once the process has done some prior `cuda` work, in some cases** — but see "Negative" below

Non-recoverable: HSA runtime can't free more memory after, process effectively dead.

## What works

- **`hipMalloc(64 MB) + hipMemset + hipDeviceSynchronize + hipFree`** on kernel 7.0.1 (KFD ABI 1.22) — passes cleanly. Source:
  ```c
  #include <hip/hip_runtime.h>
  #include <cstdio>
  int main() {
    void *p; hipError_t e;
    e = hipMalloc(&p, 64*1024*1024); printf("hipMalloc: %s\n", hipGetErrorString(e));
    e = hipMemset(p, 0, 64*1024*1024); printf("hipMemset: %s\n", hipGetErrorString(e));
    e = hipDeviceSynchronize(); printf("sync: %s\n", hipGetErrorString(e));
    hipFree(p); printf("OK\n"); return 0;
  }
  // hipcc t.cpp -o t --offload-arch=gfx1151 && ./t  →  OK
  ```
  This same reproducer crashed identically on kernel 6.18.5 (KFD ABI 1.18). The kernel-side ABI bump fixed the simple allocator path.

- **Synthetic torch alloc loops** in a fresh process — pass:
  ```python
  for size in [64*1024*1024, 256*1024*1024, 1024*1024*1024, 5*1024*1024*1024]:
      t = torch.zeros(size//4, dtype=torch.float32, device="cuda:0")
      torch.cuda.synchronize()
      del t; torch.cuda.empty_cache()
  ```
  Also: 200 iterations of `4096×4096 fp16` matmul + free + empty_cache in 1.6s, no crash.

- **llama.cpp + Vulkan RADV** — runs Qwen3.6-35B-A3B-UD-Q4_K_XL end-to-end on this same GPU, no crashes. Vulkan path only, no HIP exercised. *(Edit 2026-04-27: original report incorrectly said "llama.cpp + ROCm" — build here is `GGML_HIP=OFF / GGML_VULKAN=ON`. I have not verified a HIP-built llama.cpp on this hardware. The implication "distinct HIP allocator path from torch's" therefore does not follow from this data point.)*

- **sd.cpp Vulkan** — runs Flux 2 / WAN 2.2 GGUF end-to-end. Confirms hardware + power + VRAM partitioning are healthy.

## Failing trace (`AMD_LOG_LEVEL=4 AMD_LOG_MASK=0x60000 HSAKMT_DEBUG_LEVEL=7`)

Full trace at `comfyui_extended_trace.log` (192 lines, kernel 7.0.1 + ROCm 7.12 nightly), attached. Failing sequence at `Requested to load WanTEModel`:

```
[hsaKmtAllocMemoryAlignCtx] node 1 address 0x7f0417800000 size 2101346304 from device
[hsaKmtMapMemoryToGPUNodesCtx] address 0x7f0417800000 number of nodes 1
[hsaKmtAllocMemoryAlignCtx] node 1 address 0x7f091de3f000 size 4096 from host    ← 4 KB scratch on node 1, host-mapped
[hsaKmtMapMemoryToGPUNodesCtx] address 0x7f091de3f000 number of nodes 1
[hsaKmtAllocMemoryAlignCtx] node 0 address 0x7f07ae407000 size 4096 from host
[hsaKmtMapMemoryToGPUNodesCtx] address 0x7f07ae407000
[hsaKmtMapMemoryToGPUNodesCtx] address 0x7f07adc0d000
"Allocating VRAM for EOP"
[hsaKmtMapMemoryToGPUNodesCtx] address 0x7f073b23d000
"Allocating GTT for CWSR"
hsaKmtSVMSetAttrCtx: address 0x7f0678600000 size 0x1256000
[hsaKmtUnmapMemoryToGPUCtx] address 0x7f091de3f000   ← ioctl returns success
[hsaKmtFreeMemoryCtx] address 0x7f091de3f000          ← ioctl returns success
Memory critical error by agent node-0 (Agent handle: 0x560304d08f00) on address 0x7f091de3f000. Reason: Memory in use.
```

**Object identity**: the failing 4 KB page on node 1 is allocated `from host` early in HSA queue setup. Best matching candidate from rocr-runtime sources: `AqlQueue::pm4_ib_buf_` (4 KB, AllocateExecutable via `system_allocator()`) — but `HSA_ALLOCATE_QUEUE_DEV_MEM=1` did not change behavior, so it's either not pm4_ib_buf_ or that env var is not honored in either of the userspace builds tested. CWSR is documented as a related setup region but **disabling CWSR at the kernel level (`amdgpu.cwsr_enable=0`) does not fix the crash**, so the CWSR teardown is correlation, not causation.

## What's been ruled out (so we don't have to round-trip)

**Kernels** (all crash):
- 6.18.3-200.fc43 (last known-good per pytorch#173367)
- 6.18.5-200.fc43 (ChristianKniep's working baseline on his Framework)
- 6.19.12-200.fc43
- **7.0.1-262.vanilla.fc43 (KFD ABI 1.22)** — the libhsakmt warning `gfx1151 requires KFD ABI ≥ 1.20` is silenced; same crash

**Kernel cmdline** (none change behavior):
- `amdgpu.cwsr_enable=0`
- `amdgpu.sched_policy=2` (no MES HWS)
- `amdgpu.vm_fragment_size=9`
- `amdgpu.gttsize=126976`
- `amdttm.pages_limit=32768000` + `amdttm.page_pool_size=32768000` + `ttm.page_pool_size=32768000`
- `amd_iommu=off` (and conversely `iommu=pt` alone)

**HSA env vars** (none change behavior; tested via `kyuz0/amd-strix-halo-comfyui` on kernel 7.0.1 — `AMD_LOG_LEVEL=4` IS honored so at least some env vars reach the runtime):
- `HSA_ALLOCATE_QUEUE_DEV_MEM=1`
- `HSA_DISABLE_FRAGMENT_ALLOCATOR=1`
- `HSA_ENABLE_INTERRUPT=0`
- `HSA_ENABLE_SCRATCH_ASYNC_RECLAIM=0` + `HSA_NO_SCRATCH_RECLAIM=1`
- `HSA_MAX_QUEUES=1`
- `HSA_USE_SVM=0` + `HSA_ENABLE_SDMA=0`
- `HSA_OVERRIDE_GFX_VERSION=11.5.1` (and unset)
- `HSA_XNACK=1`
- `PYTORCH_HIP_ALLOC_CONF=backend:native,expandable_segments:True,garbage_collection_threshold:0.9,max_split_size_mb:512`

**Container privilege** (no change):
- rootless podman with `--device=/dev/kfd --device=/dev/dri --group-add 39 --group-add 105`
- `--security-opt seccomp=unconfined --security-opt label=disable`
- **`--privileged`** (falsifies the sdnext#4652 IOMMU/DMABUF hypothesis)

**Firmware**: 20260110 vs 20260309 — same crash on both.
**BIOS UMA**: 0.5 GB vs 64 GB — same crash on both.

## Negative / non-trigger

- The crash does **not** show "Memory access fault by GPU agent on address X / Page not present" — that's the #6118/#6146 class which the kernel-side fixes addressed. We are not in that class.
- `dmesg` is **clean** during the crash — no GPU VM faults, no ring resets, no KFD errors. Failure is entirely userspace-visible from the HSA runtime.
- Synthetic `torch.zeros(...)` and the 15-line `hipMalloc/Free` pure C reproducer pass on kernel 7.0.1. The crash is gated on the specific HSA queue/scratch setup pattern that PyTorch + ComfyUI's `model_management.load_models_gpu()` triggers when uploading a transformer text encoder or UNet.
- This is the same hardware that ChristianKniep ran WAN 2.2 T2V-A14B on successfully on 2026-01-16 with kernel 6.18.5 — BUT his hardware was a different OEM (Framework). Filing supports a board/BIOS-class delta hypothesis.

## Closely related but distinct tickets (please correlate, not duplicate)

| Ticket | Status | Why it's not this |
|---|---|---|
| ROCm/ROCm#6118 (`hsa_queue_create causes GPU page fault on gfx1151`) | closed | Different signature ("Page not present"), fixed by kernel `cwsr_size`/`ctl_stack_size` export which IS in this kernel |
| ROCm/ROCm#6146 (`Page Fault on hipMemcpy() in ROCm 7.2.1`) | closed 2026-04-16 | Same fix as #6118, doesn't cover this signature |
| ROCm/ROCm#5824 (`gfx1151 segfault`) | closed 2026-01-23 | Closed for inactivity; original reporter still saw issues post-FW upgrade |
| ROCm/TheRock#2991 (canonical gfx1151 VGPR fix summary) | closed 2026-02-23 | Userspace `hsakmt: Expose and use CWSR and Control stack sizes` shipped in TheRock Dec 19 2025+; we've tested that build; it fixes simple alloc but not this signature |
| sdnext#4652 (`Memory critical error by agent` on Bazzite Strix Halo) | open | Reporter fixed via `--privileged`; we tested `--privileged`, no effect — IOMMU/DMABUF hypothesis falsified for this hardware |
| pytorch/pytorch#173367 (`Strix Halo HSA crashes 6.18.4+`) | open since 2026-01-26 | Profile matches but the kernel-version differentiator they describe (6.18.3 vs 6.18.4) does not apply here — both crash |
| ROCm/rocm-systems#2200 (`hsakmt: Expose and use CWSR and Control stack sizes`) | merged | The userspace part of the fix that #2991 tracks; in the wheels we've tested |

## Questions / requests for triage

1. Is the failing 4 KB host-mapped node-1 page identifiable from the trace alone — pm4_ib_buf_ or something else? Does AMD have a known list of HSA queue setup objects that allocate `from host` on node 1 in this size?
2. Is `node-0` the CPU agent, or a separate GPU partition node? The error reports node-0 owns the in-use mapping while the alloc/unmap/free were on node 1.
3. Has any AMD engineer correlated bugs against AMI BIOS 1.07 / Bosgame M5 / Sixunited AXB35-02 specifically? GMKtec EVO-X2 (same physical board, BIOS 1.12) reports are absent from this signature in our search; if AMD has internal data showing this is BIOS-version-gated, that would close the case.
4. Is there a flag combination — kernel cmdline, HSA env, SMU/IOMMU policy — that we have NOT tried that's known to bypass the HSA queue setup pattern shown in the trace? Particularly anything that would change whether a 4 KB allocation lands `from host` vs `from device` on node 1.
5. Should we cross-flash GMK 1.12 BIOS as the recommended diagnostic, or RMA?

## Artifacts

All bundled in this gist: **https://gist.github.com/dkzv/bcc864bc91e1f35e3879ba06707f5bb0**

Files in the gist:
- `comfyui_extended_trace.log` — full extended HSA/KFD trace at the failing model load (~200 lines, captured with `AMD_LOG_LEVEL=4 AMD_LOG_MASK=0x60000 HSAKMT_DEBUG_LEVEL=7 HSA_XNACK=1`)
- `repro_hip.cpp` — 15-line C reproducer (passes on 7.0.1, crashed on 6.18.5)
- `repro_smoke.py` — synthetic torch alloc smoke (passes)
- `repro_matmul.py` — 200-iter matmul + free loop (passes)
- `comfyui_smoke_api.json` — exact `/prompt` POST body used (WAN 2.2 ti2v 5B Q5_K_M, 512×384×17, 20 steps, euler/simple)
- `rocminfo.txt`, `rocm-smi.txt`, `cmdline.txt`, `dmi.txt`, `kernel.txt`, `rpms.txt` — environment snapshots
- `test_hsa_levers.sh` — driver script used to test the 5 HSA env-var levers in sequence

`dmesg` is clean of GPU driver errors during the crash (no VM faults, ring resets, KFD errors); omitted to avoid attaching unrelated USB/Bluetooth host metadata. Available on request to triage.

Cross-link: pytorch/pytorch#173367, ROCm/TheRock#2991 closure, vladmandic/sdnext#4652, invoke-ai/InvokeAI#9053.

