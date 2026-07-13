# memory order in single thread

- **Issue #:** 500
- **State:** closed
- **Created:** 2018-08-15T00:20:34Z
- **Updated:** 2023-08-05T16:47:24Z
- **Labels:** Under Investigation, Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/500

```
KERNEL(1024) testA(global uint *bufN, global ulong *sumN) {
  if (get_global_id(0) == 0) {
    uint n = bufN[0];
    bufN[0] = 0;
    sumN[0] += n;
  }
}

KERNEL(1024) testB(global uint *bufN, global ulong *sumN) {
  if (get_global_id(0) == 0) {
    uint n = bufN[0];
    sumN[0] += n;
    bufN[0] = 0;
  }
}
```
ROCm 1.8.2, Vega64, Ubuntu 18.04, OpenCL 2.x.

Consider the two kernels above. The second one, testB(), works as expected. But the first one, testA(), behaves as if the value "n" is always zero. As if the write bufN[0]=0 takes place before the read n=bufN[0].
