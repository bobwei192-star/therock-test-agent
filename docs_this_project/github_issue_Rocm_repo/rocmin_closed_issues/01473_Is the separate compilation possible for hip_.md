# Is the separate compilation possible for hip?

- **Issue #:** 1473
- **State:** closed
- **Created:** 2021-05-18T00:43:37Z
- **Updated:** 2021-05-18T16:31:09Z
- **URL:** https://github.com/ROCm/ROCm/issues/1473

Hi all,

I did not find it in the HIP programming guide but is the separate compilation possible for hip?

And is that possible for link-time optimization?

For example, we have a function file a.c and main file main.c:
--a.c
extern __device__ foo() {
...
}

---a.h
extern __device__ foo();

--main.c
#include "a.h"

__global__ kernel() {
...
fool();
...
}

I tried to compile:
>hipcc -flto -c a.c -o a.o
>hipcc -c main -o main.o
>hipcc a.o main.o -o main

The command line will give me "lld: error: undefined hidden symbol:foo()".
P.S.: I compiled llvm to use for hipcc and compile the LLVMgold.so to use lto.
