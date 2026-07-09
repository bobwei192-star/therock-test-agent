# Blender 2.80 Cycles testing, compiling kernel hangs, ROCm 1.8.0

- **Issue #:** 402
- **State:** closed
- **Created:** 2018-05-05T21:10:50Z
- **Updated:** 2020-12-17T03:38:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/402

Hi all,

I'm just testing Blender Cycles from the bleeding edge branch as well as 2.79b with ROCm 1.8.0 OpenCL on a Vega10 Frontier Edition, running on a HP z620 Workstation (2x E5-2680v2's, 64GB RAM, Quadro k2000 for display). Currently this is the debug I get from the command line using --debug-cycles:

```I0505 14:02:50.856982  5927 session.cpp:701] Requested features:
Experimental features: Off
Max nodes group: 3
Nodes features: 6
Use Hair: True
Use Object Motion: False
Use Camera Motion: True
Use Baking: False
Use Subsurface: True
Use Volume: True
Use Branched Integrator: True
Use Patch Evaluation: False
Use Transparent Shadows: True
Use Principled BSDF: False
Use Denoising: False
I0505 14:02:50.857064  5927 opencl_base.cpp:216] Loading kernels for platform AMD Accelerated Parallel Processing, device Vega 10 XTX [Radeon Vega Frontier Edition].
I0505 14:02:50.857336  5927 opencl_util.cpp:288] OpenCL program split not found in cache.
I0505 14:02:50.897501  5927 opencl_util.cpp:288] Kernel file /home/alex/.cache/cycles/kernels/cycles_kernel_split_33D08D521DA35BC482B41E5979556C99_DBB1D123AFA735A3DDBE5D0BD2C271B9.clbin either doesn't exist or failed to be loaded by driver.
Compiling OpenCL program split
I0505 14:02:50.926681  5927 opencl_util.cpp:288] Build flags: -D__SPLIT_KERNEL__ -D__NODES_MAX_GROUP__=3 -D__NODES_FEATURES__=6 -D__NO_OBJECT_MOTION__ -D__NO_BAKING__ -D__NO_PATCH_EVAL__ -D__NO_SHADOW_TRICKS__ -D__NO_PRINCIPLED__ -D__NO_DENOISING__ -D__NO_SHADER_RAYTRACE__ -D__COMPUTE_DEVICE_GPU__
I0505 14:02:50.926702  5927 opencl_util.cpp:315] Build options passed to clBuildProgram: '-cl-no-signed-zeros -cl-mad-enable -D__KERNEL_OPENCL_AMD__ -D__SPLIT_KERNEL__ -D__NODES_MAX_GROUP__=3 -D__NODES_FEATURES__=6 -D__NO_OBJECT_MOTION__ -D__NO_BAKING__ -D__NO_PATCH_EVAL__ -D__NO_SHADOW_TRICKS__ -D__NO_PRINCIPLED__ -D__NO_DENOISING__ -D__NO_SHADER_RAYTRACE__ -D__COMPUTE_DEVICE_GPU__'.
```

Currently it looks like the compiler just hangs here for quite some time, I can let it run for awhile and see if it eventually compiles, but it seems like something to look into. I can try to help test here as best as I can to assist the ROCm developers.

Cheers!