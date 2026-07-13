# [Issue]: OpenCL crash (0xC0000005) when iGPU runtime creates command queue for discrete GPU (iGPU+dGPU systems)

- **Issue #:** 6328
- **State:** closed
- **Created:** 2026-06-03T17:57:59Z
- **Updated:** 2026-06-04T19:49:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/6328

### Problem Description

On Windows systems with both an integrated GPU (e.g., gfx1036) and a discrete GPU (e.g., RX 9070 XT / gfx1201), the Adrenalin driver installs two separate OpenCL ICD packages with mismatched runtime versions:

- **Platform 0** (amdocl64.dll v10.0.3679.0) — dGPU runtime, has RDNA4 support
- **Platform 1** (amdocl64.dll v10.0.3652.0) — iGPU runtime, lacks RDNA4 PAL support

Both platforms enumerate both GPUs through the KMD. When an application creates a command queue for gfx1201 (dGPU) on Platform 1 (iGPU runtime), the PAL layer crashes with `0xC0000005` (access violation) because it lacks RDNA4 device tables.

This affects any OpenCL application that auto-selects platforms, including Folding@home, Blender Cycles, and others reported in [this Reddit thread](https://www.reddit.com/r/Amd/comments/1t9w7ir/blender_cycles_has_issues_with_amd_adrenalin_2651/). Related to the F@H portion of #6227.

**Crash matrix (all 4 platform/device combinations):**

| Platform | Device | Result |
|---|---|---|
| P0 (v3679.0, dGPU runtime) | gfx1201 (dGPU) | OK |
| P0 (v3679.0, dGPU runtime) | gfx1036 (iGPU) | OK |
| P1 (v3652.0, iGPU runtime) | gfx1036 (iGPU) | OK |
| **P1 (v3652.0, iGPU runtime)** | **gfx1201 (dGPU)** | **SEGFAULT** |

**Crash stack trace:**
```
Exception Code: 0xC0000005
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x20F186, clSetKernelExecInfo() + 0x1D17D6
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x1A0C96, clSetKernelExecInfo() + 0x1632E6
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x20C8CB, clSetKernelExecInfo() + 0x1CEF1B
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x1AAABB, clSetKernelExecInfo() + 0x16D10B
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x1A1E7C, clSetKernelExecInfo() + 0x1644CC
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x1AD3DD, clSetKernelExecInfo() + 0x16FA2D
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0xCD650, clSetKernelExecInfo() + 0x8FCA0
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0xCA84F, clSetKernelExecInfo() + 0x8CE9F
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x51991, clSetKernelExecInfo() + 0x13FE1
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x49A7B, clSetKernelExecInfo() + 0xC0CB
amdocl.inf_amd64_b385e7dbfacd37b3\amdocl64.dll + 0x70B4F, clSetKernelExecInfo() + 0x3319F
KERNEL32.DLL + 0x2E957, BaseThreadInitThunk() + 0x17
ntdll.dll + 0x427C, RtlUserThreadStart() + 0x2C
```

**Suggested fix:** The iGPU's OpenCL runtime should either not enumerate devices it cannot support, or return `CL_DEVICE_NOT_AVAILABLE` instead of segfaulting.

### Operating System

Windows 11 Pro 10.0.26200

### CPU

AMD Ryzen 9 7950X 16-Core Processor (integrated graphics enabled in bios)

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

amdhip64_7.dll v10.0.3679.0 (Adrenalin 26.6.1)

### ROCm Component

OpenCL, drivers

### Steps to Reproduce

**Prerequisite:** iGPU must be enabled.

**Minimal reproducer (Python):**
```bash
pip install pyopencl
```
```python
import pyopencl as cl
platforms = cl.get_platforms()
# Platform 1 = iGPU runtime (v3652.0), Device 0 = gfx1201 (dGPU)
ctx = cl.Context([platforms[1].get_devices()[0]])
cl.CommandQueue(ctx, platforms[1].get_devices()[0])  # SEGFAULT here
```

**Verify your system has 2 OpenCL platforms first:**
```bash
clinfo | grep "Platform Version"
# Should show two lines with different versions (e.g., 3679.0 and 3652.0)
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

N/A

### Additional Information

- The HIP runtime is not affected on 26.6.1 as the KMD no longer exposes the iGPU to HIP
- The crash was first reported with Adrenalin 26.5.1 and persists on 26.6.1
- Corroborating evidence: Platform 1 reports `local_mem_size=65536` for gfx1201 while Platform 0 correctly reports `32768`, indicating the iGPU runtime's hardware tables are wrong for RDNA4
- Current Workaround: disable iGPU in BIOS per the [documentation](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/prerequisites/prerequisitesrad.html#disable-igpu)
