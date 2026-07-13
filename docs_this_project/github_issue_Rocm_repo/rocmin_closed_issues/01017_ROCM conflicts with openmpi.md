# ROCM conflicts with openmpi

- **Issue #:** 1017
- **State:** closed
- **Created:** 2020-02-21T12:14:27Z
- **Updated:** 2021-04-19T12:53:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/1017

I'm not trying to use either of my GPUs, is there a simple way to prevent them being picked up via mpirun?

```
mpirun -np 2 echo "foo"
Memory access fault by GPU node-2 (Agent handle: 0x557153bfcf50) on address (nil). Reason: Unknown.
Aborted
```

