# [Issue]: printf() call changing the behavior of the kernel? Compiler bug?

- **Issue #:** 5227
- **State:** closed
- **Created:** 2025-08-24T14:03:59Z
- **Updated:** 2025-09-11T06:32:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/5227

### Problem Description

My application started behaving unexpectedly so I started adding some printf() calls in the kernel to try and debug the values. Turns out that adding printf() calls changes the output of the application which isn't expected.

The same issue happens both on Linux 24 with ROCm 6.4 or on Window 11 with the [HIPSDK 6.42](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)

### Operating System

Ubuntu 24.04.2 LTS (Noble Numbat) & Windows 11

### CPU

13th Gen Intel(R) Core(TM) i5-13600KF

### GPU

Radeon RX 7900 XTX

### ROCm Version

ROCm 6.4.0.60400-47~24.04

### ROCm Component

HIP

### Steps to Reproduce

```
git clone --recursive https://github.com/TomClabault/HIPRT-Path-Tracer.git HIPRTPathTracer
cd HIPRTPathTracer
git checkout ROCMIssue
git update submodule update --recursive --init
mkdir build
cd build
cmake ..
<compile the application with the generator chosen>
./HIPRTPathTracer
```

Expected output in the console (the logging comes from a printf() in the kernel: [/HIPRT-Path-Tracer/src/Device/kernels/ReSTIR/ReGIR/GridFillTemporalReuse.h](https://github.com/TomClabault/HIPRT-Path-Tracer/blob/ROCMIssue/src/Device/kernels/ReSTIR/ReGIR/GridFillTemporalReuse.h)):
```
PDF: -nan
PDF: -nan
PDF: -nan
```
Application GUI:

<img width="3876" height="2072" alt="Image" src="https://github.com/user-attachments/assets/6d2b97cd-7e9a-440d-ba4c-efb888216d55" />

Un-commenting the printf() call line 57 & 58 of the same kernel [GridFillTemporalReuse.h:58](https://github.com/TomClabault/HIPRT-Path-Tracer/blob/ROCMIssue/src/Device/kernels/ReSTIR/ReGIR/GridFillTemporalReuse.h#L58) and restarting the application with `./HIPRTPathTracer` (no CPU recompilation needed) yields:
```
binPower: 40.000008
PDF: 0.250000
binPower: 40.000008
PDF: 0.250000
binPower: 40.000008
PDF: 0.250000
```
Application GUI:

<img width="3876" height="2072" alt="Image" src="https://github.com/user-attachments/assets/c793db23-f641-4fec-8ed6-b0a8146a1179" />

The second behavior is correct and I don't expect a single printf() call to change the behavior of the application like that?

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Running the application with `rocgdb` doesn't raise any exception so this probably isn't a memory access fault causing undefined beahvior?