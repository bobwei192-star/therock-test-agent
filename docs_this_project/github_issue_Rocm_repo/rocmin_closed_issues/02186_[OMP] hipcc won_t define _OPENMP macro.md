# [OMP] hipcc won't define _OPENMP macro

- **Issue #:** 2186
- **State:** closed
- **Created:** 2023-05-29T03:55:05Z
- **Updated:** 2024-11-01T03:39:54Z
- **Labels:** Under Investigation
- **Assignees:** david-salinas
- **URL:** https://github.com/ROCm/ROCm/issues/2186

Dear developers, the `hipcc` compiler driver won't define the `_OPENMP` macro when the `-fopenmp` option is specified. The macro will be defined only when GPU offloading is requested. This can cause issues during the CMake configuration step when testing for OpenMP availability.

ROCm versions: 5.0.2, 5.4.3

How to reproduce:

```
$ cat test.cpp 
#ifndef _OPENMP
#error NO OPENMP defined
#endif

int main () {}
$ hipcc -fopenmp test.cpp 
test.cpp:2:2: error: NO OPENMP defined
#error NO OPENMP defined
 ^
1 error generated when compiling for gfx90a.
$ clang -fopenmp test.cpp 
$ # success 
$ hipcc -fopenmp -target x86_64-pc-linux-gnu -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx90a test.cpp 
$ # success
```
Is this the intended behaviour?

Thank you