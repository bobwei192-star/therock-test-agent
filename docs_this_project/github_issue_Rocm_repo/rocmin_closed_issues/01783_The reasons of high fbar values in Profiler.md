# The reasons of high fbar values in Profiler

- **Issue #:** 1783
- **State:** closed
- **Created:** 2022-08-09T06:56:25Z
- **Updated:** 2024-05-09T15:53:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/1783

Hello, dear colleagues!
I have two kernels which implement the same algorithm, but the first kernel does its work in the LDS, and the second kernel distributes the data between the LDS and registers in half. The performance of the second kernel is ~2.5 times low as the first kernel. I've found that the **fbar** counter of the second kernel is more _higher_. 
Please, if anybody knows, how can I understand _the reasons_ for the higher value of **fbar**?
Thanks!