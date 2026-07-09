# OpenCL shared library overrides signal handling

- **Issue #:** 462
- **State:** closed
- **Created:** 2018-07-19T20:39:10Z
- **Updated:** 2018-10-16T13:51:36Z
- **Labels:** Under Investigation, Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/462

Hi,

we have a problem to use ROCm (1.8.151) OpenCL shared library (Ubuntu 16.04.4 LTS) in our own development environment where we make use of POSIX signal handlers. When calling clGetPlatformIDs function the signal handling of our application process gets overridden that causes problems for the application and finally makes it crashing. A simple CPP example below demonstrates the problem. Are there any specific reasons for the shared library to override the signal handling of the loading process? How can we avoid that?

Thanks for help.

```
// test.cpp
#include <dlfcn.h>
#include <signal.h>
#include <stdio.h>

int main()
{
    auto lib = dlopen("/opt/rocm/opencl/lib/x86_64/libOpenCL.so", RTLD_LAZY);
    auto function = reinterpret_cast<int (*)(unsigned, void *, unsigned *)>(dlsym(lib, "clGetPlatformIDs"));

    unsigned n = 0;
    auto result = function(0, 0, &n); // this function call overrides the current process signal handling

    printf("generating int3 trap\r\n");

    asm("int3"); // normally this induces a trap but here the process will exit silently
}

// compilation: g++ -std=c++11 -o test test.cpp -ldl
// execution: ./test
```