# OpenCL miscompilation

- **Issue #:** 1817
- **State:** closed
- **Created:** 2022-09-30T22:51:51Z
- **Updated:** 2024-05-09T16:34:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/1817

I've encountered a scenario where the ROCm OpenCL codegen miscompiles a kernel and it returns the wrong result. Here is a collection of files which replicate the issue and verifies it's not just undefined behavior in the kernel code: https://gist.github.com/PlasmaPower/c8a650b3268dc5cd8a54755431427350

`kernel.cl` is the kernel in question. `run-kernel.c` is a program to execute the kernel on the first OpenCL device and print the result, and `host.c` is `kernel.cl` which a short preamble containing a main function that allows the same code to run on the host instead of the GPU, which has a different result.

To execute the program on the host, and enable sanitizers showing that it doesn't have undefined behavior:
```sh
$ clang host.c -Wall -fsanitize=memory,undefined,unsigned-integer-overflow,implicit-conversion -o host && ./host
Host result: 369c71
```

To execute the program on the GPU:
```sh
$ clang run-kernel.c -lOpenCL -o run-kernel && ./run-kernel
Running on GPU: gfx1010:xnack-
GPU result: 26c8c71
```

This issue has been replicated on a 5700 XT and a 6900 XT. I've reduced the test case as much as I could. You'll note that parts of it are entirely unused, but are needed to trick the optimizer into thinking they're used, which is necessary to replicate the issue. That's the reason for the `zero` argument, which is always set to zero.