# [Feature]: adaptive, hardware-aware multi-GPU work-splitting helper (prototype: hipsplit)

- **Issue #:** 6341
- **State:** open
- **Created:** 2026-06-09T12:23:44Z
- **Updated:** 2026-06-09T18:25:26Z
- **Labels:** Feature Request, status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6341

### Suggestion Description

**Motivation**

HIP exposes the building blocks for distributing work across GPUs — `hipGetDeviceProperties`, the occupancy API (`hipOccupancyMaxActiveBlocksPerMultiprocessor`, `hipOccupancyMaxPotentialBlockSize`), and multi-device control — but there is no built-in helper that, given a kernel and a 1-D workload, decides *how many items go to each device* and *what block/grid configuration to use*, weighted by each device's compute capability and achievable occupancy. Developers re-implement this ad hoc, and it gets harder with heterogeneous GPUs or multi-node setups.

**Question**

Does an occupancy-aware, hardware-weighted multi-GPU work-splitting helper fit within HIP/ROCm's scope, or is there an existing recommended approach I've missed?

**What I prototyped (for discussion)**

A small, permissively licensed library: https://github.com/fillay12321/hipsplit

- A HIP-free planning core (builds and unit-tests on any machine) that splits a workload across devices proportionally to a compute weight and picks block/grid sizes from a kernel profile.
- A HIP-backed layer that fills device weights from real `hipDeviceProp_t` data and the occupancy API.
- Optional multi-node tiling (level-1 split across nodes, level-2 across a node's devices) plus an opt-in MPI cluster-topology discovery helper.
- A small executor that launches each slice on its own device + stream and synchronizes at the end (cross-node transport is left to the caller's RCCL/MPI).
- A C ABI (`libhipsplit_c.so`) for driving it over FFI from any language.

**Questions for the maintainers**

1. Does this fit HIP/ROCm's scope, or is it intentionally left to higher-level libraries (rocPRIM/Thrust, RCCL, etc.)?
2. If there's interest, would you consider upstreaming something like this, and what would the right shape/location be?
3. Is there already a recommended pattern for occupancy-weighted multi-device splitting I should use instead?

**Notes**

The planning core has GPU-free unit tests; the executor smoke test and the `print_topology` example were verified on real gfx1151 hardware.

### Operating System

Ubuntu (gfx1151 / Ryzen AI Max 395 machine)

### GPU

AMD Radeon gfx1151 (Ryzen AI Max 395, 20 CU)

### ROCm Component

HIP