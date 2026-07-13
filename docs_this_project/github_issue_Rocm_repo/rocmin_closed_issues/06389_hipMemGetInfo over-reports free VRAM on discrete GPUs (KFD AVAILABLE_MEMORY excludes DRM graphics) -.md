# hipMemGetInfo over-reports free VRAM on discrete GPUs (KFD AVAILABLE_MEMORY excludes DRM graphics) -> downstream OOM

- **Issue #:** 6389
- **State:** closed
- **Created:** 2026-06-30T03:20:47Z
- **Updated:** 2026-06-30T06:22:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/6389

### Summary
On discrete AMD GPUs, `hipMemGetInfo` / `hsa_agent_get_info(HSA_AMD_AGENT_INFO_MEMORY_AVAIL)` reports more free VRAM than is actually available. It is backed by KFD `AMDKFD_IOC_AVAILABLE_MEMORY`, which counts only ROCm/KFD allocations and ignores DRM graphics allocations (Vulkan/GL/desktop compositor). With a graphics session holding VRAM the gap can be multiple GiB, and frameworks that size GPU offload from this value over-commit and OOM at load.

- Downstream report: https://github.com/ggml-org/llama.cpp/issues/24906 (a llama.cpp-side workaround https://github.com/ggml-org/llama.cpp/pull/25123 was closed in favor of fixing this in ROCm).
- Prior discrepancy report: #1909 (2023), closed as a metric-difference note for a small idle delta; the actionable problem here is the multi-GiB over-report under graphics load causing OOM.

### Root cause
`HSA_AMD_AGENT_INFO_MEMORY_AVAIL` -> `KfdDriver::AvailableMemory` -> `hsaKmtAvailableMemory` -> `AMDKFD_IOC_AVAILABLE_MEMORY` (KFD compute-available; excludes DRM graphics). `rocm-smi` reads amdgpu `mem_info_vram_used` (graphics-inclusive).

### Reproduce (gfx1100 RX 7900 GRE, ROCm 7.2.1)
| state | hipMemGetInfo free | rocm-smi / amdgpu |
|---|---|---|
| idle | 16332 MiB | 16170 MiB |
| ~11 GiB resident | 5696 MiB | 5420 MiB |

### Fix
In ROCR `GpuAgent::GetInfo` (`HSA_AMD_AGENT_INFO_MEMORY_AVAIL`, projects/rocr-runtime in the rocm-systems super-repo), on discrete GPUs cross-check amdgpu's graphics-inclusive VRAM usage via the agent's existing libdrm handle and take the conservative value; APUs keep the KFD UMA value.

Fix PR: ROCm/rocm-systems#7990
