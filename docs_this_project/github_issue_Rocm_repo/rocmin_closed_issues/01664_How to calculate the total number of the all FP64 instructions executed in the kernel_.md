# How to calculate the total number of the all FP64 instructions executed in the kernel?

- **Issue #:** 1664
- **State:** closed
- **Created:** 2022-02-03T08:43:18Z
- **Updated:** 2024-03-22T23:32:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/1664

Hello!
I analyzing the performance of a several scientific libraries. And, I'd like to understand an actual arithmetic complexity of each. Which metrics of rocproof  I should use for this goal? 

I guess SQ_INSTS_VALU, then _the total number_ will be equal: 
`CU_NUM * SIMD_NUM * SQ_INSTS_VALU`.  Where, for AI100: `CU_NUM` is 120 CU, `SIMD_NUM` is 4. It's correct?

Thanks!