# On AMD Ryzen CPU, OpenCL app runs faster when the CPU is not idle

- **Issue #:** 319
- **State:** closed
- **Created:** 2018-01-31T01:42:52Z
- **Updated:** 2018-06-03T14:45:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/319

System: Ubuntu 17.10, CPU Ryzen 1700x, Rx Vega64, ROCm 1.7.

case 1: the CPU is idle, save for the OpenCL app which is not using much CPU.
case 2: the CPU is busy, used by mprime https://www.mersenne.org/download/ , which runs with nice -20.

In case 2 (CPU busy), the measured performance of the OpenCL app is about 1.5% faster than in case 1 (CPU idle).
