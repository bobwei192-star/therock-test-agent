# Flags used for building ROCm packages for Ubuntu/CentOS?

- **Issue #:** 1348
- **State:** closed
- **Created:** 2020-12-23T00:16:18Z
- **Updated:** 2021-03-09T08:13:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/1348

As I can't find source packages on http://repo.radeon.com/rocm, could you disclose which flags you use for building ROCm packages for Ubuntu/CentOS.

Given the hardware requirements being essentially AMD Zen and newer or Intel Haswell and newer, I'd expect something like
```-march=haswell``` or ```-march=core-avx2``` which are both compatible with AMD Zen.
Most importantly the ```-march``` flag as well as the ```-O``` optimization level used for the repo packages would be of interest.
Any more flags that are used would be appreciated as well.

I'd propose to the package maintainers for Arch Linux over at https://github.com/rocm-arch/rocm-arch to use these flags to be in line with the upstream built packages so they achieve comparable CPU features and performance.
