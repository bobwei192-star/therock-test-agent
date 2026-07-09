# [Issue]: ROCm build version 6.3.0 

- **Issue #:** 4205
- **State:** closed
- **Created:** 2024-12-29T23:11:01Z
- **Updated:** 2025-01-17T18:33:27Z
- **Labels:** Under Investigation, ROCm 6.3.0, GPU_ARCHS=gfx90a
- **URL:** https://github.com/ROCm/ROCm/issues/4205

### Problem Description

Build issue found:   /src/out/ubuntu-22.04/22.04/logs/opencl_on_rocclr.errors on version 6.3.0

prerequisites script finished successfully but still having the error below.
Any ideas what this might be ???

```
-- Found AMD_OPENCL: /src/clr/opencl/khronos/headers/opencl2.2/CL
-- Found NUMA: /usr/lib/x86_64-linux-gnu/libnuma.so
-- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so
--
ICD not found. Build may succeed if OpenCL ICD is installed in the system (missing: AMD_ICD_LIBRARY_DIR)
-- Found GLEW: /usr/include (found version "2.2.0")
--
ICD not found. Build may succeed if OpenCL ICD is installed in the system (missing: AMD_ICD_LIBRARY_DIR)
--
ICD not found. Build may succeed if OpenCL ICD is installed in the system (missing: AMD_ICD_LIBRARY_DIR)
--
ICD not found. Build may succeed if OpenCL ICD is installed in the system (missing: AMD_ICD_LIBRARY_DIR)
--
ICD not found. Build may succeed if OpenCL ICD is installed in the system (missing: AMD_ICD_LIBRARY_DIR)
^[[0mUsing CPACK_PACKAGE_VERSION 2.0.0.60300^[[0m
-- ROCM Installation path(ROCM_PATH): /opt/rocm-6.3.0
^[[0mUsing CPACK_DEBIAN_PACKAGE_RELEASE local.9999~22.04^[[0m
^[[0mUsing CPACK_RPM_PACKAGE_RELEASE local.9999^[[0m
^[[0mRESULT_VARIABLE 0 OUTPUT_VARIABLE: ^[[0m
-- Configuring done
^[[0mCMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
```

### Operating System

Ubuntu 22.04.5 LTS 

### CPU

AMD EPYC 7742 64-Core Processor

### GPU

GPU_ARCHS=gfx90a  

### ROCm Version

ROCm 6.3.0

### ROCm Component

clr

### Steps to Reproduce

Installed on AMD Server, with Ubuntu 22.04.5 LTS
Linux msl-ssg-dgx2.msl.lab 5.15.0-127-generic #137-Ubuntu SMP Fri Nov 8 15:21:01 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
Followed the ROCm install instructions.
Using docker instructions to build the source code.

Note: I do not have a AMD GPU in this server right now.  This is a test environment to try to build the code.
The AMD GPU is in another server which is being brought up now and will be available shortly.
Not sure if AMD GPU presence is required for this software build ?

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is NOT loaded, possibly no GPU devices



### Additional Information

Let me know if more debug information is needed.