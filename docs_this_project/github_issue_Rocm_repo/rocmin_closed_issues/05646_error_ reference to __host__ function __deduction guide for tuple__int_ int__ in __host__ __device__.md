# error: reference to __host__ function '<deduction guide for tuple><int, int>' in __host__ __device__ function

- **Issue #:** 5646
- **State:** closed
- **Created:** 2025-11-09T17:02:55Z
- **Updated:** 2025-12-02T15:34:50Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5646

Seems like deduction guides are treated as actual functions. They should probably not. Much like `constexpr` functions do not need to be annotated with `__host__`/`__device__`.

``` c++
#include <tuple>
#include <hip/hip_runtime.h>

__host__ __device__ void func()
{
	std::tuple<int, int> t = std::tuple(1, 1);
}
```
```
> hipcc -std=c++23 a.cpp
a.cpp:6:27: error: reference to __host__ function '<deduction guide for tuple><int, int>' in __host__ __device__ function
    6 |         std::tuple<int, int> t = std::tuple(1, 1);
      |                                  ^
/usr/lib/gcc/x86_64-linux-gnu/13/../../../../include/c++/13/tuple:1203:5: note: '<deduction guide for tuple><int, int>' declared here
 1203 |     tuple(_UTypes...) -> tuple<_UTypes...>;
      |     ^
```
