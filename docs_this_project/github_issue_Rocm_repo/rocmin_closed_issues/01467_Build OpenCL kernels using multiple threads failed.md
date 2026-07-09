# Build OpenCL kernels using multiple threads failed

- **Issue #:** 1467
- **State:** closed
- **Created:** 2021-05-10T08:00:51Z
- **Updated:** 2021-05-13T06:13:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1467

I'm trying to read multiple *.cl files and write pre-built *.bin files with multiple threads.
So I made a simple compiler and it works like this `./my_opencl_compiler foo.cl -o foo.bin`
It just create `clContext` with 1 AMD GPU and call `clBuildProgram()`, `clGetProgramInfo(..., CL_PROGRAM_BINARIES, ...)` to get the byte sequences.

But when I put compile command in Makefile and do `make -j`, it fails like this
```
Error: AMD HSA Code Object loading failed: HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed 
to allocate the necessary resources. This error may also occur when the core runtime library needs to
spawn threads or create internal OS-specific events.
```

Any suggestions?

ROCm : 4.0.0
OS : ubuntu 20.04.1 LTS
GPU : rx5700