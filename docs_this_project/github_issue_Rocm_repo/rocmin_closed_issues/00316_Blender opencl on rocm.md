# Blender opencl on rocm

- **Issue #:** 316
- **State:** closed
- **Created:** 2018-01-29T07:58:27Z
- **Updated:** 2019-01-04T20:55:57Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/316

Hi

I tried using rocm driver on RX 480. The card can be selected in "system" menu as "opencl" device, but when choosing "cycles renderer" (in upper menu)  and "rendered" (in bottom menu), there is error with log.
System Ubuntu 16.04 + kernel 4.13 + rocm 1.7

I opened bug, since I could find anything on blender+rocm

```
Device init success
Compiling OpenCL kernel ...
Build flags:  -D__NODES_MAX_GROUP__=3 -D__NODES_FEATURES__=7 -D__MAX_CLOSURE__=64 -D__NO_HAIR__ -D__NO_OBJECT_MOTION__ -D__NO_CAMERA_MOTION__ -D__NO_BAKING__
/tmp/AMD_3689_19/t_3689_21.cl:2476:12: error: used type 'float' where floating point type is not allowed
        return (t)? a/t: a;
               ~~~^
1 error generated.
OpenCL kernel build output:
Error: Failed to compile opencl source (from CL to LLVM IR).

OpenCL build failed: errors in console
```
