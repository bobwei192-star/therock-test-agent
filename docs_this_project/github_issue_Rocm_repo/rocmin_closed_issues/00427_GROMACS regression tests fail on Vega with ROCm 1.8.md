# GROMACS regression tests fail on Vega with ROCm 1.8

- **Issue #:** 427
- **State:** closed
- **Created:** 2018-05-31T18:12:21Z
- **Updated:** 2018-06-11T10:59:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/427

Multiple regressiontests fail on ROCm 1.8 while these do pass with AMDGPU-PRO.

To reproduce follow the "Quick and dirty" installation instructions and the `make check` stage should reveal the issues: http://manual.gromacs.org/documentation/2018/install-guide/index.html#quick-and-dirty-installation.