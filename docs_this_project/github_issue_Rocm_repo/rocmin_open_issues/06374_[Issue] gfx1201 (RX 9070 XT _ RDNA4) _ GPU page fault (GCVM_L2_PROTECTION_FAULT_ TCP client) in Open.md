# [Issue] gfx1201 (RX 9070 XT / RDNA4) — GPU page fault (GCVM_L2_PROTECTION_FAULT, TCP client) in OpenCL compute; identical workload runs fault-free on gfx1036

- **Issue #:** 6374
- **State:** open
- **Created:** 2026-06-22T17:38:28Z
- **Updated:** 2026-06-23T16:31:07Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6374

## Summary

On **gfx1201 (RX 9070 XT, Navi 48, RDNA4)**, real OpenCL compute workloads (DaVinci Resolve Studio's Neural Engine — UltraNR / Magic Mask / Super Scale) trigger a **GPU VM page fault** (`GCVM_L2_PROTECTION_FAULT`, UTCL2 client **TCP**, `PERMISSION_FAULTS: 0x3`) on a **host virtual address**. The HSA runtime then `abort()`s and the app dies (SIGABRT). The **exact same application/project/kernels run without any fault when compute is routed to the RDNA2 iGPU (gfx1036)** via `ROCR_VISIBLE_DEVICES=1`. This isolates the bug to the **gfx1201 OpenCL/ROCm path**, not the application.

Related (perf, not crash): #6124. Companion: Blackmagic forum thread t=235840.

## System

```
GPU (faulting): AMD Radeon RX 9070 XT — Navi 48, gfx1201, RDNA4, Chip 0x7550, 16 GB
iGPU (works):   AMD Radeon Graphics — Raphael, gfx1036, RDNA2 (APU, unified memory)
OS:             Arch Linux, kernel 7.0.12-arch1-1
ROCm/OpenCL:    ROCm 7.13.0 (gfx120x build) ; libhsa-runtime64 1.21.0
OpenCL driver:  3581.0 (HSA1.1, LC) ; Device Version OpenCL 2.0
Mesa:           26.1.3 (display only)
linux-firmware: 20260519 (downgrade to 20260410 tested — no change; see below)
App:            DaVinci Resolve Studio 21.0.0.0048 (native Linux), Neural Engine tools
```

## Symptom

During a Neural Engine op (AI UltraNR on a still is the most reliable), the dGPU takes a VM page fault and the HSA runtime aborts.

**Kernel log (`journalctl -k`):**
```
amdgpu 0000:03:00.0: [gfxhub] page fault (src_id:0 ring:24 vmid:8 pasid:NN)
amdgpu 0000:03:00.0:   Process GUI Thread ... thread resolve:cs0
amdgpu 0000:03:00.0:   in page starting at address 0x00007fXXXXXXXXXX from client 10
amdgpu 0000:03:00.0:   GCVM_L2_PROTECTION_FAULT_STATUS:0x00801031
amdgpu 0000:03:00.0:          Faulty UTCL2 client ID: TCP (0x8)
amdgpu 0000:03:00.0:          MORE_FAULTS: 0x1, WALKER_ERROR: 0x0, PERMISSION_FAULTS: 0x3,
                              MAPPING_ERROR: 0x0, RW: 0x0
```

**Application abort (HSA runtime):**
```
/usr/lib/libc.so.6(abort+0x26)
/opt/rocm/lib/libhsa-runtime64.so.1(+0x106917)
/opt/rocm/lib/libhsa-runtime64.so.1(+0x104201)
/opt/rocm/lib/libhsa-runtime64.so.1(+0x16d36a)
Signal Number = 6 (SIGABRT)
```

The faulting address is a **host VA (0x00007f…)**, client **TCP** (vector/L1 data), a **permission fault (0x3)** — i.e. a kernel accessing host memory that is not mapped/permitted in the dGPU's VM. Note `XNACK enabled: NO` and `Coherent Host Access: FALSE` on gfx1201 (per `rocminfo`).

## Decisive evidence — it's gfx1201-specific, not the application

Same machine, same Resolve install, same project, same kernels — only the compute device changes:

| `ROCR_VISIBLE_DEVICES` | Device | Result |
|---|---|---|
| `0` | **gfx1201** (RX 9070 XT, RDNA4) | **GPU page fault → HSA abort → crash** |
| `1` | **gfx1036** (iGPU, RDNA2) | **No fault. Runs correctly** (slow — 1 CU — but no page fault, app stays alive) |

Routing the identical OpenCL compute to the RDNA2 iGPU eliminates the fault entirely. The bug is in the gfx1201 path.

## What we ruled out (so it's narrowly scoped)

- **Not command-dispatch latency.** A minimal OpenCL microbenchmark (many small `clEnqueueNDRangeKernel` + per-dispatch `clWaitForEvents`) on gfx1201 is healthy: serialized ≈ 18 µs/dispatch, batched ≈ 3 µs/dispatch, and the old `rocvirtual: Host active wait for Signal ... 100000 ns` pattern is **absent** on this stack. So this is **not** the dispatch/queue-latency issue in #6124 — it is a correctness/memory fault.
- **Not linux-firmware.** Downgrading `linux-firmware-amdgpu` 20260519 → 20260410 (different `gc_12_0_0_mec` compute microcode) did **not** change the fault (`0x00801031` persists).
- **Not the application / project / silicon capability.** Runs fault-free on gfx1036 (above), and ROCm HIP/MIGraphX compute on gfx1201 is otherwise bit-exact for ONNX models.
- **Not host display/driver.** Display/OpenGL is Mesa radeonsi; the fault is purely in the ROCm/amdocl compute path.

## Suspected area

A kernel/runtime memory access to **host memory** (SVM / `CL_MEM_USE_HOST_PTR` / fine-grain pointer) that is valid on a unified-memory APU (gfx1036) but is **not correctly mapped into the gfx1201 dGPU VM** (XNACK off, non-coherent host access on RDNA4) → TCP permission fault. Either the amdocl/ROCr SVM/host-pointer mapping path is wrong for gfx1201, or LLVM codegen emits an out-of-range address for these kernels on gfx1201.

## Repro

1. gfx1201 (RDNA4) on ROCm 7.13.0, native DaVinci Resolve Studio 21.
2. Apply an AI Neural Engine op (AI UltraNR on a still is the most reliable).
3. dGPU: GPU page fault + SIGABRT (above). `ROCR_VISIBLE_DEVICES=1` (iGPU): no fault.

(Happy to provide a smaller standalone OpenCL repro that exercises host-pointer/SVM kernels on gfx1201 if useful.)

## Ask

1. Confirm/triage the gfx1201 GCVM TCP permission fault on host-VA access in the OpenCL/ROCr path (vs gfx1036 working).
2. Identify whether this is amdocl/ROCr SVM/host-pointer mapping or LLVM gfx1201 codegen.

## Offer

Can provide: full `dmesg`/`journalctl -k` fault dumps, the HSA abort backtrace with symbols, `rocprof`/`rocgdb` traces, the MIGraphX bit-exact correctness harness, the dispatch microbenchmark, and the `ROCR_VISIBLE_DEVICES` A/B logs.
