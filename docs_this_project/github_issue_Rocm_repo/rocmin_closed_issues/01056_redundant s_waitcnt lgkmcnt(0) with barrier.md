# redundant s_waitcnt lgkmcnt(0) with barrier

- **Issue #:** 1056
- **State:** closed
- **Created:** 2020-03-23T10:15:05Z
- **Updated:** 2024-08-18T16:41:44Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/1056

ROCm 3.1, Radeon VII,
looking at the generated code I often see this block:
```
s_waitcnt lgkmcnt(0)
s_barrier
s_waitcnt lgkmcnt(0)
```
It seems that the second s_waitcnt is not needed, right?