# [Issue]: HIPRTC allocates unusually high amounts of LDS memory when compiling a kernel

- **Issue #:** 3806
- **State:** closed
- **Created:** 2024-09-24T18:52:23Z
- **Updated:** 2024-10-02T18:19:42Z
- **Labels:** Under Investigation, ROCm 5.7.1, AMD Radeon RX 7900 XTX, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3806

### Problem Description

HIPRTC allocates LDS memory on its own (isn't LDS allocation a programmer-only choice?) and in unreasonable amounts (~45k bytes) when compiling my kernels at runtime. This drastically reduces the occupancy of my kernels and kills performance.

The amount of LDS allocated is retrieved by calling `hipFuncGetAttribute()`. Radeon GPU Profiler also reports the same high-amount of LDS used when profiling my kernels.

I can reproduce this (although not on a minimal reproducer unfortunately) consistently on both Ubuntu 22.04 & Windows 11 with ROCm 6.2.0 and ROCm 5.7.1 respectively.

The only difference in my kernel between the version that allocates way too much LDS and the one that doesn't is the change from `int priority;` to `char priority;` ([link to Github diff](https://github.com/TomClabault/HIPRT-Path-Tracer/compare/d546340..ffe540a))

To begin with, is HIPCC "allowed" to allocate LDS on its own if it judges that this is going to benefit performance? Are there known issues with such automatic LDS allocation?

### Operating System

Windows 11 & Ubuntu 22.04

### CPU

Inte i5 13600KF

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.2.0, ROCm 5.7.1

### ROCm Component

HIP, HIPCC

### Steps to Reproduce

Not a minimal reproducer but I can reproduce it consistently on both Windows and Ubuntu 22.04 with ROCm 5.7.1 & ROCm 6.2.0 respectively:

Clone the repository of my project and build it with CMake:

```
git clone -b ROCmIssueLDSHighAmount https://github.com/TomClabault/HIPRT-Path-Tracer.git --recursive
cd HIPRT-Path-Tracer
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Debug ..
```

Compile with your build system and run (set HIPRTPathTracer as the startup project if using the Visual Studio generator on Windows).

The program outputs the following (on Windows):

```
hiprt ver.02004
Executing on 'AMD Radeon RX 7900 XTX'
Kernel "ReSTIR_DI_InitialCandidates" compiled in 2127ms.
        96 registers.
        59392 shared memory.
Kernel "ReSTIR_DI_SpatialReuse" compiled in 1467ms.
        96 registers.
        62464 shared memory.
Kernel "FullPathTracer" compiled in 4256ms.
        96 registers.
        53248 shared memory.
```
50k+ bytes of shared memory is way too high and I do not use shared memory in my kernels.

The expected amount is way lower than that.
Checking out the other branch that does not show the issue and building again:

```
git checkout ROCmIssueLDSFix
<Build with build system>

./HIPRTPathTracer
```

Run the program and it then outputs:
```
hiprt ver.02004
Executing on 'AMD Radeon RX 7900 XTX'
Kernel "ReSTIR_DI_InitialCandidates" compiled in 2077ms.
        96 registers.
        6144 shared memory.
Kernel "ReSTIR_DI_SpatialReuse" compiled in 1452ms.
        96 registers.
        9216 shared memory.
Kernel "FullPathTracer" compiled in 4224ms.
        96 registers.
        0 shared memory.
```

Which is way more reasonable, but even then, it should be 0. I am not using shared memory in any of my kernels.

The only difference between the two branches is a variable type change in a stack structure (which can be made manually, there's not even a need to checkout another branch actually).

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_