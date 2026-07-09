# [Issue]: Extraneous spaces in some varaible names in hip runtime include files causing compiler faults

- **Issue #:** 3221
- **State:** closed
- **Created:** 2024-06-03T21:01:51Z
- **Updated:** 2024-08-26T15:21:28Z
- **Labels:** AMD Instinct MI300X, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3221

### Problem Description

I'm currently trying to port an NVIDIA code to ROCM/HIP using amdclang++
While compiling I've noticed that I'm getting some errors caused by extra space in some hip runtime include files, specifically 
Currently using amdclang++ 17.0.0

_In amd_hip_runtime_pt_api.h_
In file included from /opt/rocm-6.1.0/include/hip/hip_runtime_api.h:8915:
/opt/rocm-6.1.0/include/hip/amd_detail/amd_hip_runtime_pt_api.h:94:48: error: expected ')'
   94 |                                  size_t **offset __dparm(**0),
      |                                                ^
/


_In hip_runtime_api.h_
DEPRECATED(DEPRECATED_MSG)
hipError_t hipBindTexture(
    size_t* offset,
    const textureReference* tex,
    const void* devPtr,
    const hipChannelFormatDesc* desc,
    size_t **size __dparm(**UINT_MAX));

You'll note that there are variable names here, offset_dparm and size_dparm, that have an extraneous space in the middle of the variable name and this is causing compiler faults. I've grepped through these files for other examples and have noticed a couple of more.I am a new employee and am working on a home computer that does not currently have an AMD gpu in it but that's of little matter as I'm just trying to do a lot of porting now.

### Operating System

Ubuntu 20.04.6 LTS 

### CPU

Intel Core i7-6700K

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.1.0

### ROCm Component

HIPCC

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_