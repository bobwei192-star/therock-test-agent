# shows too much vram

- **Issue #:** 1915
- **State:** closed
- **Created:** 2023-03-03T17:02:10Z
- **Updated:** 2023-03-07T11:46:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/1915

I've just spotted an issue with the `AMD` driver.

When I'm running machine learning applications with `OpenCL`, the whole system or just the program eventually crahes.
`rocm-smi` shows me `40GB` of RAM, however the graphics card only has `20GB` of RAM as shown by Windows and on the package.
The total RAM usage never exceeds 5GB, however there are invalid address ranges accessed, which means the AMD driver does not recognize the correct range.

Some relevant information:
GPU: AMD RADEON RX 7900 XT
RESIZABLE_BAR: on
CPU: AMD RYZEN 7 5950SomeThing
SYSTEM_RAM: 32GB


Please redirect me to the correct repository. I believe this is not the correct place to report.