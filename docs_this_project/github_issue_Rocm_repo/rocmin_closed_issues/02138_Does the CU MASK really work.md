# Does the CU MASK really work

- **Issue #:** 2138
- **State:** closed
- **Created:** 2023-05-14T15:06:12Z
- **Updated:** 2024-08-01T15:12:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/2138

Hi, I am learning CU_MASK mechanism, my experiment scenario is like this:
I used two separate sets of masks

unsigned int cuMaskAll[2] = {0xFFFFFFFF, 0xFFFFFFF0};
unsigned int cuMaskBE[2] = {0x11111111, 0x0000000};
They are used to create two streams, which are used to carry out a bert model inferrence
There is little difference in the infer latency between the two of them. cuMaskBE is supposed to enable only 8 CUS. Why wouldn't it ？
Thank you in advance.
