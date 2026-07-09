# OpenCL: decreasing performance due to thermal throttling

- **Issue #:** 564
- **State:** closed
- **Created:** 2018-09-30T21:16:28Z
- **Updated:** 2018-10-11T16:34:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/564

Hi,
I have an up to date ubuntu 16.04.5 LTS running Rocm 1.9.
Hardware: Supermicro X10SRA-F, Xeon E5-2680V3, 3 x Radeon Pro Duo (polaris, gfx803). All GPUs are recognized.

I am running an OpenCL program that uses all 6 GPUs, the program is repeatedly executing a few kernels (without device side enqueue). At first, the performance of the program is good. After about 190 seconds, the performance starts to drop and never recovers. The only thing I noticed are messages in the output of dmesg that begin before the performance starts to drop.

The attached output of dmesg conatins messages like these:
[  483.147199] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  488.160470] enqueue_ih_ring_entry: 102777 callbacks suppressed
These messages worry me, because they are printed in red :)

The performance starts to drop at uptime 672 seconds.

What could cause these error messages? Should I look for a bug in my OpenCL kernels?

[dmesg.zip](https://github.com/RadeonOpenCompute/ROCm/files/2431980/dmesg.zip)
