# __shfl_sync: case of false advertising?

- **Issue #:** 5852
- **State:** closed
- **Created:** 2026-01-14T23:16:45Z
- **Updated:** 2026-02-23T19:41:33Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5852

Since ROCm aims to align with CUDA, a case can be made that recently introduced __shfl_sync primitives are inadequate reflections of their CUDA counterparts. Let's compare. ROCm performs an elaborate dance that effectively boils down to:
```
heavily_over_engineered_assert(mask == __activemask());
__shfl(...);
```
To illuminate the difference with CUDA let's consider the following snippet:
```
__global__ void kernel(long *p)
{
    long m;

    if (threadIdx.x & 1) {
        m = __activemask();
        m = __shfl_xor_sync(~0L, m, 1);
    } else {
        m = __activemask();
        m = __shfl_xor_sync(~0L, m, 1);
    }
    p[threadIdx.x] = m;
}
```
Does it work on AMD? No, it crashes due to heavily_over_engineered_assert. Does it work on CUDA? Yes! Well, it's kind of a tricky question in the sense that it works differently on pre-Volta and post-Volta, but at the very least it doesn't crash and produces predictable result.

Hardware-wise AMD GPUs are equivalent to pre-Volta with respect to shuffle operation. So given the initial assessment what does ROCm try to achieve? If to simply reflect hardware capabilities and align with pre-Volta, then it fails. And if it attempts to align with with post-Volta, then it fails again...

For reference. On pre-Volta __shfl_sync-s are compiled as simple __shfl-s. That's it. One can argue that it can be confusing to the programmer, but that's how it is, and therefore is supposed to be recognized/known. For post-Volta let's consider more generalized
```
if (condition) {
    // pre-true
    __shfl_sync(mask, ...);
    // post-true
} else {
    // pre-false
    __shfl_sync(mask, ...);
    // post-false
}
```
It's "**executed**" as
```
if (condition) {
    // pre-true
} else {
    // pre-false
}
__shlf(...);
if (condtion) {
    // post-true
} else {
    // post-false
}
```
I've put "executed" in quotes to denote the fact that it's not how the binary code will look like. But it's a valid way for us to **think** about it. There are nuances, but overall the point is that this is the minimum a compiler would have to do **if** it aimed to align with post-Volta on pre-Volta hardware.
