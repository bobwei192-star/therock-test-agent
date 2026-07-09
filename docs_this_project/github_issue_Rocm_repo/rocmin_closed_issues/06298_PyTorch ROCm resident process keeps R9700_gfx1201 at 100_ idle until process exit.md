# PyTorch ROCm resident process keeps R9700/gfx1201 at 100% idle until process exit

- **Issue #:** 6298
- **State:** closed
- **Created:** 2026-05-25T00:32:50Z
- **Updated:** 2026-06-25T14:02:56Z
- **Labels:** status: assessed
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6298

### Problem

On a single Radeon AI PRO R9700 (`gfx1201`), a non-llama PyTorch ROCm resident process can keep the GPU pinned at `100%` use and elevated power while the process is idle. The GPU returns to low idle only after the ROCm process exits.

This is related to, but broader than, the closed llama.cpp thread #5706. In that thread, `GPU_MAX_HW_QUEUES=1` fixed my llama.cpp idle-busy case, but it did **not** fix this PyTorch ROCm resident-process case.

### Provenance from #5706

Prior comments from the same workstation:

- Initial llama.cpp R9700 idle-busy repro: https://github.com/ROCm/ROCm/issues/5706#issuecomment-4425963410
- `GPU_MAX_HW_QUEUES=1` fixed the llama.cpp idle-busy repro on this single R9700: https://github.com/ROCm/ROCm/issues/5706#issuecomment-4427687895
- Independent PyTorch ROCm resident-process repro, still failing with `GPU_MAX_HW_QUEUES=1`: https://github.com/ROCm/ROCm/issues/5706#issuecomment-4529952746
- Local DKMS backport retest of the GFX12 `oversubscription_timer` fix, still failing for PyTorch ROCm: https://github.com/ROCm/ROCm/issues/5706#issuecomment-4530597014

### Host / GPU

- OS: Ubuntu 24.04.4 LTS / noble
- Kernel during DKMS retest: `6.17.0-29-generic`
- GPU: AMD Radeon AI PRO R9700
- GFX: `gfx1201`
- Device ID: `0x7551`
- VBIOS: `113-R9700AT-F40`
- AMDGPU DKMS package: `amdgpu-dkms 1:6.16.13.30300000-2278356.24.04`
- ROCm package: `7.2.0.70200-43~24.04`
- HSA runtime package: `hsa-rocr 1.18.0.70200-43~24.04`
- PyTorch: `2.10.0+rocm7.0`
- Before daemon retest, GPU idle was about `3%` use and `16 W`

### Workload

A persistent PyTorch ROCm Kokoro TTS daemon. It loads a model on `cuda:0`, accepts socket commands, can synthesize audio, can move the model to CPU, drop pipeline references, run garbage collection, and call PyTorch CUDA/ROCm cache cleanup APIs while keeping the process alive.

Relevant environment:

```text
READSEL_TTS_DEVICE=cuda
GPU_MAX_HW_QUEUES=1
HIP_VISIBLE_DEVICES=0
ROCR_VISIBLE_DEVICES=0
MIOPEN_FIND_MODE=FAST
MIOPEN_USER_DB_PATH=/tmp/miopen-kokoro-cache
```

A separate resident Qwen `llama.cpp` process was healthy and idle at the same time. Its local GPU lock was free. The llama.cpp idle-busy issue on this machine had already been mitigated by `GPU_MAX_HW_QUEUES=1`.

### Observed behavior without the DKMS backport

With `GPU_MAX_HW_QUEUES=1`, the PyTorch ROCm daemon synthesized successfully on `cuda:0`, but idle behavior remained bad:

- Loaded resident idle: `100%` GPU use, about `84 W`
- Full in-process unload steps succeeded at the daemon/PyTorch level:
  - moved model off GPU
  - dropped resident pipeline refs
  - ran `gc.collect()`
  - ran `torch.cuda.empty_cache()`
  - allocator-visible memory dropped from `642,807,808` to `313,977,856` bytes allocated
  - reserved memory dropped from `698,351,616` to `356,515,840` bytes
- While the daemon process stayed alive, the R9700 stayed pinned:
  - immediately after unload: `100%`, `107 W`
  - unloaded soak: 30s `100% / 85 W`, 60s `100% / 87 W`, 120s `100% / 91 W`
- Reload and synthesis still worked in the same process
- Post-synth while the process stayed alive: 30s/60s/120s all `100%`, about `92-97 W`
- After terminating the PyTorch ROCm daemon process, GPU returned to low idle: about `3%`, `15-17 W`

### DKMS backport retest

I also tested a local backport of the GFX12 `oversubscription_timer` fix from commit `75575ad088dadd68d8f56361888d36edcd628024` onto the installed AMDGPU DKMS source:

- Base DKMS: `amdgpu/6.16.13-2278356.24.04`
- Local test DKMS version: `amdgpu/6.16.13-2278356.24.04+gfx12idlefix`
- Kernel: `6.17.0-29-generic`
- Patched behavior in `mes_v12_0.c`: `oversubscription_timer = mes_rev < 0x8b ? 0 : 50`
- Patch built, installed, and loaded after reboot
- Loaded module path: `/lib/modules/6.17.0-29-generic/updates/dkms/amdgpu.ko.zst`
- Loaded module srcversion during patched test: `EB8E7F83EBC8C4753F81E83`

The DKMS backport did **not** fix the PyTorch ROCm resident-process idle-busy case:

- Resident daemon loaded on `cuda:0`
- Loaded resident idle: `100%`, about `82 W`
- Full unload result: pipeline `unloaded`; allocator-visible memory dropped, but GPU stayed active
- 30s unloaded soak: `100%`, about `85 W`
- Reload and synthesis worked
- Post-synth idle: `100%`, about `85 W`
- After daemon process exit: GPU returned to about `3%`, `16 W`

### Expected behavior

If a PyTorch ROCm process has no active GPU work, and the model has been moved off GPU / unloaded from the resident daemon, the R9700 should return to a low idle state without requiring process exit.

### Actual behavior

The process lifetime itself appears sufficient to keep the R9700 in a high GPU-use / elevated-power state after PyTorch ROCm has loaded and used the device, even when allocator-visible memory drops and no synthesis is active.

### Why I am filing this separately

#5706 was titled and closed around llama.cpp HIP behavior. On this workstation, the llama.cpp case is mitigated by `GPU_MAX_HW_QUEUES=1`, but this PyTorch ROCm resident-process case is not. The DKMS `oversubscription_timer` fix also did not resolve it.

This looks like a broader PyTorch ROCm / HIP process-lifetime idle-busy behavior on R9700/RDNA4, distinct from llama.cpp warmup, mmap, context size, or queue-count configuration.

I can provide the daemon script, command logs, `rocm-smi` snapshots, `dkms status`, kernel logs, and a smaller repro if maintainers want a reduced test case.
