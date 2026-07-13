# Question: how is SQ_INSTS_VALU incremented?

- **Issue #:** 1723
- **State:** closed
- **Created:** 2022-04-11T22:05:57Z
- **Updated:** 2024-05-09T15:59:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/1723

Hello, colleagues!
I noticed that SQ_INSTS_VALU is incremented once per warp by an instruction. It's right?
Then to count the total number of executed vector instructions on the grid, I have to multiply this value by the size of a warp?
