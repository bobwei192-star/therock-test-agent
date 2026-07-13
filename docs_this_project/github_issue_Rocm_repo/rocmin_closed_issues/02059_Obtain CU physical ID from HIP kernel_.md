# Obtain CU physical ID from HIP kernel?

- **Issue #:** 2059
- **State:** closed
- **Created:** 2023-04-18T05:25:38Z
- **Updated:** 2023-04-22T01:46:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/2059

Is there any approach for programmers to obtain the CU's physical ID like the way in CUDA:
```cpp
__device__ uint get_smid(void) {
   uint ret;
   asm("mov.u32 %0, %smid;" : "=r"(ret) );
}
```
