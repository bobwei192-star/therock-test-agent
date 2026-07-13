# Charge amdgpu GTT allocations to the memory cgroup (memcg) for OOM/Kubernetes accounting on RDNA3.5 APUs

- **Issue #:** 6370
- **State:** open
- **Created:** 2026-06-19T16:52:22Z
- **Updated:** 2026-06-19T21:12:16Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6370

## Summary

On RDNA3.5 APUs (Strix Halo / Ryzen AI Max), GPU memory is accessed through **GTT** — system RAM mapped into GPU virtual address spaces. GTT allocations are dynamic and not permanently reserved (by design, for flexibility), but as a result the **Linux memory cgroup (memcg) subsystem does not account for them as process memory**.

This request is to have the `amdgpu`/`amdttm` driver stack **charge GTT allocations to the allocating process's memory cgroup** (e.g. via `mem_cgroup_charge()` or equivalent when GTT pages are pinned), so that the kernel's per-cgroup memory accounting reflects real GTT usage.

> **Attribution note:** the problem analysis, the survey of existing mechanisms, and the short-term mitigations below were largely provided by the ROCm AI Assistant in the AMD Discord in response to this exact question. I'm filing it here as the assistant recommended, and adding measured data from my own Kubernetes cluster. Where something is the assistant's assessment (rather than my own observation) I've attributed it.

## The problem

Because GTT host pages are not charged to any memory cgroup:

- The **OOM killer** sees a GPU-heavy process consuming very little "memory" from the kernel's perspective, and **kills innocent bystanders** instead of the actual GPU memory hog.
- For **Kubernetes**, this compounds:
  - **kubelet cannot set meaningful cgroup memory limits** that cover GTT usage — a pod `memory` limit does not bound GTT and will not cause the cgroup OOM-killer to target the offending pod.
  - The **scheduler over-packs the node** because it sizes the node from cgroup requests/working-set, which exclude GTT, leading to node-level OOM.

### Measured example (my environment: Kubernetes, Strix Halo / Ryzen AI Max, 780M, ROCm)

On a node running ROCm GPU workloads under Kubernetes, I measured:

- `node_drm_memory_gtt_used_bytes` ≈ **50.6 GB** of GTT in use.
- Sum of **all** container cgroup working-sets on the node ≈ **37.0 GB**.
- Node memory actually used ≈ **101.8 GB / 134 GB**.

The ~50 GB of GTT is real host RAM pressure that is invisible to cgroup accounting (and therefore to the Kubernetes scheduler and to kubelet's memory limits/eviction victim-selection). The kernel OOM-killer, ranking by cgroup RSS, does not pick the GPU process as the victim.

## Existing mechanisms and why they don't close the gap

(This survey is from the ROCm AI Assistant's analysis.)

- **TTM page-limit tuning** (`/sys/module/ttm/parameters/pages_limit`, or the `amdgpu.gttsize` ceiling): a **global** cap on GTT-accessible memory. Useful as a blast-radius backstop, but it is **not per-process accounting** and does not solve the cgroup-visibility problem.
- **AMD GPU DRA Driver (beta)**: exposes GPU memory as a structured capacity field in `ResourceSlice`, giving the **Kubernetes scheduler** visibility for placement decisions. Valuable, but it is a Kubernetes-layer solution — **kubelet cgroup memory limits still do not enforce GTT usage**, and the kernel OOM-killer still mis-selects victims.
- **`GPU_MAX_ALLOC_PERCENT` / `GPU_SINGLE_ALLOC_PERCENT`**: cap how much a process can allocate via the GPU runtime — a useful per-process safety valve, but runtime-side soft fencing, not kernel cgroup accounting.

The gap that none of these close: **reporting GTT allocations to the memory resource controller** (`memory.current` / `memory.max`) so the kernel's accounting, the OOM-killer, and kubelet all see GTT as the allocating process's memory.

## Feature request

Have the `amdgpu`/`amdttm` driver **charge GTT-backing host pages to the allocating process's memory cgroup** when they are pinned (and uncharge on release), so that:

- `memory.current` for the cgroup reflects GTT usage,
- the cgroup OOM-killer targets the actual GPU memory consumer,
- kubelet memory limits and eviction behave correctly for GPU workloads,
- the Kubernetes scheduler's node accounting is accurate.

This is a kernel-level change in the driver stack. Per the ROCm AI Assistant, this does not appear to be implemented upstream as of ROCm 7.2.4, and it was not able to point to documentation indicating it is on a near-term roadmap — hence this request, which the assistant suggested filing here against the amdgpu/KFD driver team. (Separately: the `dmem` cgroup controller in Linux 6.14 accounts discrete **VRAM** regions a DRM driver registers, but does **not** cover amdgpu GTT host-backed memory, so it does not address this case.)

## Use case

Running ROCm inference/serving workloads (LLM serving, image generation/diffusion, embeddings, TTS) on Strix Halo / Ryzen AI Max nodes in a **Kubernetes** cluster, where unaccounted GTT causes node OOM and wrong-victim kills that can take down unrelated (including control-plane) workloads.

## Short-term mitigations (suggested by the ROCm AI Assistant)

- Set an `amdgpu.gttsize` / TTM `pages_limit` ceiling so the GPU cannot allocate unbounded host RAM (turns node-OOM into a clean in-job ROCm allocation failure).
- Reserve node memory at the kubelet level (`--system-reserved` / `--kube-reserved`) so the scheduler does not hand out RAM that GTT will later claim.
- Use the **AMD GPU DRA Driver** for scheduler-aware placement.
- `GPU_MAX_ALLOC_PERCENT` as a per-process safety valve.

These mitigate but do not fix the root cause. Charging GTT to the memory cgroup is the long-term fix that needs to land in the kernel driver.

## Environment

- Hardware: AMD Ryzen AI Max / Strix Halo (RDNA3.5 APU, Radeon 780M-class iGPU), unified memory / GTT.
- Software: ROCm 7.2.x; Kubernetes (kubelet cgroup v2); upstream `amdgpu`/TTM.
