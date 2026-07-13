# ROCm installation breaks CUDA on dual-GPU system (NVIDIA + AMD)

- **Issue #:** 6354
- **State:** open
- **Created:** 2026-06-11T18:10:45Z
- **Updated:** 2026-06-16T15:49:42Z
- **Labels:** status: triage
- **Assignees:** nkulshre-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6354

I have a system with both RTX 3060 and RX 7800 XT. After installing ROCm 5.7, CUDA stopped working on the NVIDIA card.

```
nvidia-smi: Failed to initialize NVML
```

Is there a way to have both CUDA and ROCm coexist? The ROCm installer seems to modify some shared system libraries.

Workaround: Uninstalling ROCm and reinstalling NVIDIA drivers fixes it, but then I lose AMD support.

Ubuntu 22.04, kernel 6.5.0