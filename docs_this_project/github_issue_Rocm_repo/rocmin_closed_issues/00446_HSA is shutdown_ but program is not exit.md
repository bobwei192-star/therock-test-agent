# HSA is shutdown, but program is not exit.

- **Issue #:** 446
- **State:** closed
- **Created:** 2018-06-28T02:36:17Z
- **Updated:** 2018-08-14T15:11:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/446

OMEN-by-HP-Laptop
Model: 15-ax211TX
OS: Ubuntu 16.04.4 LTS (Xenial Xerus)
CPU: Intel Core i5-7300HQ
Graphics Card:AMD Radeon RX 460

wei@OMEN-by-HP-Laptop:~$ cd /opt/rocm/hsa/sample/
wei@OMEN-by-HP-Laptop:/opt/rocm/hsa/sample$ ./vector_copy
...
Shutting down the runtime succeeded.
But program isn't exit.
As shown, when press Enter or Control C, even if no new command prompt appeared.
 rocminfo and opencl programs also have the same situation.
![2018-06-27 15-49-18](https://user-images.githubusercontent.com/22558386/42009832-9b350142-7abe-11e8-86a2-ab22abd7ae5d.png)
