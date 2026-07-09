# [Issue]: INT64 _very_slow with rocm-opencl versions >= 5.5.7 on Fedora (39 + 40)

- **Issue #:** 3273
- **State:** closed
- **Created:** 2024-06-10T01:22:35Z
- **Updated:** 2024-09-13T20:58:51Z
- **Labels:** Under Investigation, ROCm 6.0.0, ROCm 5.7.1, AMD Radeon RX 7900 XTX, ROCm 5.6.0, ROCm 5.7.0, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3273

### Problem Description

When comparing INT64 in very large arrays I have a significant slow down when using rocm-opencl since 5.5.7 onwards.

I copy the very large array to global memory prior to commencement of the comparison check.
My kernel compares 15,000 INT64 values against an 14Gb array of INT64 values, using a VERY basic kernel that essentially says if (myBigArray[get_global_id()] == targetValue) atomic_inc a pointer.

When using rocm-opencl-5.5.1 on Fedora 39 or 40 (currently using FC40) I can perform approximately 1.7 Trillion comparisons per second on a 7900XTX or 1.2 Trillion comparisons per second of a 6900XT. 
When using rocm-opencl-5.7.1, this crashed to 450 and 350 billion comparisons / sec respectively. Using rocm-opencl-6.0.2, the system freezes.

- Downgrading the version of rocm-opencl to 5.5.1 on any version of Fedora resolves the issue with speed of comparison returned to normal.
- There is no issue running the same opencl on a machine with RTX308ti's using the Nvidia libOpenCL.so.
- When using a known test value - the comparison succeeds the pointer is incremented and returned correctly by the kernel.
- There is no difference switching between LLVM and GCC, although I use GCC by default.

### Operating System

Fedora 40

### CPU

AMD Ryzen 5950x

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.0, ROCm 6.0.0, ROCm 5.7.1, ROCm 5.7.0, ROCm 5.6.0

### ROCm Component

ROCm

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_