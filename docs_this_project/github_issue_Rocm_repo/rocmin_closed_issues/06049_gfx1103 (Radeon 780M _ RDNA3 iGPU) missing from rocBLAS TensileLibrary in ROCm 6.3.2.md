# gfx1103 (Radeon 780M / RDNA3 iGPU) missing from rocBLAS TensileLibrary in ROCm 6.3.2

- **Issue #:** 6049
- **State:** closed
- **Created:** 2026-03-20T17:11:47Z
- **Updated:** 2026-04-13T03:00:53Z
- **Labels:** status: assessed
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6049

## Hardware
- APU: AMD Ryzen 9 7940HS
- iGPU: AMD Radeon 780M (gfx1103, RDNA3)
- RAM: 24GB shared (UMA architecture)
- OS: Linux Mint 22.2 (Ubuntu 24.04 base)
- ROCm version: 6.3.2-66

## Summary
rocBLAS in ROCm 6.3.2 includes TensileLibrary files for every discrete RDNA3 GPU 
but is missing gfx1103 — the iGPU variant used in all Ryzen 7000 series APUs. 
This causes any application that calls rocBLAS matrix operations to crash at 
runtime on gfx1103 hardware.

## Exact Error
rocBLAS error: Cannot read /opt/rocm/lib/rocblas/library/TensileLibrary.dat: 
Illegal seek for GPU arch: gfx1103

List of available TensileLibrary Files:
"/opt/rocm/lib/rocblas/library/TensileLibrary_lazy_gfx1100.dat"
"/opt/rocm/lib/rocblas/library/TensileLibrary_lazy_gfx1101.dat"
"/opt/rocm/lib/rocblas/library/TensileLibrary_lazy_gfx1102.dat"
(gfx1103 absent from this list)

## What Is Present vs Missing

RDNA3 discrete GPUs — all supported:
- gfx1100 — RX 7900 XTX / 7900 XT
- gfx1101 — RX 7800 XT / 7700 XT
- gfx1102 — RX 7600

RDNA3 iGPU — not supported:
- gfx1103 — Radeon 780M / 760M (Ryzen 7000 series APU)

## Confirmed Working
- ROCm correctly detects gfx1103 via rocminfo
- Compiling HIP code with --offload-arch=gfx1103 succeeds
- Custom compiled HIP kernels run correctly on gfx1103
- The gap is specifically rocBLAS TensileLibrary runtime support

## Why This Matters
gfx1103 is not a niche or edge case chip. It ships in:
- Every AMD Ryzen 7000 series laptop (7940HS, 7840HS, 7640U etc)
- Popular mini PCs (GEEKOM A7, Minisforum UM780, etc)
- A large and growing segment of consumer AMD hardware

It is arguably the most widely deployed RDNA3 chip in existence. As AI inference 
on consumer hardware grows — local LLMs, image generation, etc — gfx1103 users 
represent a significant and underserved user base.

Applications like KoboldCPP, llama.cpp, and others can successfully compile and 
run GPU accelerated inference on gfx1103 using custom HIP kernels. The missing 
TensileLibrary support is the specific bottleneck preventing newer versions of 
these applications from working correctly.

## Request
Please add gfx1103 to the rocBLAS TensileLibrary build targets alongside the 
existing RDNA3 discrete GPU entries. Given the architectural similarity to 
gfx1100/1101/1102 this should be a relatively contained addition.

A fallback path or graceful degradation when TensileLibrary is missing for a 
given arch would also significantly improve the user experience for iGPU users.

## References
- KoboldCPP issue filed separately describing the application-level impact:
- https://github.com/LostRuins/koboldcpp/issues/2055
- gfx1103 HIP compilation confirmed working with LLAMA_HIPBLAS=1 and 
  GPU_TARGETS=gfx1103