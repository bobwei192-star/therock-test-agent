# ROCgdb unable to properly debug OpenCL GPU kernels on MI300X (ROCm 6.2.2) — breakpoint hits but stepping fails

- **Issue #:** 6303
- **State:** closed
- **Created:** 2026-05-26T13:03:46Z
- **Updated:** 2026-06-01T18:22:46Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6303

I am trying to debug an OpenCL kernel running on an AMD GPU using roc-gdb and want to understand whether this workflow is officially supported or if I am missing some required debug setup.

Environment
GPU: AMD Instinct MI300X (gfx942)
CPU: AMD EPYC 9534
ROCm version: 6.2.2
Debugger: roc-gdb
OpenCL runtime: ROCm OpenCL
OS: Linux

Test setup :-
I have a simple OpenCL vector addition example:
Kernel:

__kernel void vecadd(__global const float *a,
__global const float *b,
__global float *c)
{
int gid = get_global_id(0);
c[gid] = a[gid] + b[gid];
}

Host code:

creates OpenCL context
selects GPU device
creates queue with:
clCreateCommandQueueWithProperties(...)
(not deprecated clCreateCommandQueue())
builds program with:
clBuildProgram(program,
1,
&device,
"-g -cl-opt-disable",
NULL,
NULL);

launches kernel with:
clEnqueueNDRangeKernel(...)

What works
Host-side debugging works fine:

break main
break clBuildProgram
break clEnqueueNDRangeKernel

Kernel execution works correctly.

I can also set a breakpoint on the kernel symbol:

break vecadd

and roc-gdb does stop at kernel entry.

So kernel dispatch is definitely happening.

Problem

When I try to step inside the OpenCL GPU kernel:

step

roc-gdb fails with:
fatal error:
Per-queue memory reserved for the debugger is missing.
amd_dbgapi_displaced_stepping_start failed

Additional investigation

I extracted the generated OpenCL program binary using:
clGetProgramInfo(program, CL_PROGRAM_BINARIES, ...)
and inspected it:
llvm-readelf -S kernel.bin

The binary contains:

.text
.symtab
.dynsym

but no debug sections, e.g. no:

.debug_info
.debug_line
.debug_abbrev
.debug_str

So although I pass:

-g -cl-opt-disable

to clBuildProgram(), the generated GPU kernel binary does not appear to contain DWARF debug information.

Questions
-Is source-level OpenCL GPU kernel debugging with roc-gdb officially supported on ROCm 6.2.2?
-Does ROCm OpenCL actually support generating debug info for kernels via:
clBuildProgram(..., "-g")
or is this ignored / unsupported?

-What causes:
Per-queue memory reserved for the debugger is missing
amd_dbgapi_displaced_stepping_start failed
Is this an OpenCL runtime limitation?

-Is the OpenCL runtime expected to create debugger-compatible GPU queues automatically when launched under roc-gdb?
-Is roc-gdb intended primarily for HIP kernels, with OpenCL support being partial / limited?