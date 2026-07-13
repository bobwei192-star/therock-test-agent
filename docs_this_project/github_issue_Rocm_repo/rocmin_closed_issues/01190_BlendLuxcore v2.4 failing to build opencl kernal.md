# BlendLuxcore v2.4 failing to build opencl kernal 

- **Issue #:** 1190
- **State:** closed
- **Created:** 2020-08-17T03:40:46Z
- **Updated:** 2021-03-01T08:55:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/1190

specs. 2x Vega 56, 3900x, 128gb ram, Ubuntu 20.04.1, rocm 3.5.1. 
in an attempt to diagnose a issue with blendluxcore, i installed rocm and it fails to build the opencl kernals, cycles is able to build kernals and render with my gpus. 
following error the addon spat out. 
OpenCL driver API error (code: -11, file:/home/vsts/work/1/s/LinuxCompile/LuxCore/src/luxrays/utils/ocl.cpp, line: 369): CL_BUILD_PROGRAM_FAILURE
it does build the kernal with the AMD PRO drivers. (however there is a issue with normal maps that i was trying to nail down by installing these drivers)

*UPDATE* Blendluxcore v2.3 doesnt compile either and just instantly crashes out
