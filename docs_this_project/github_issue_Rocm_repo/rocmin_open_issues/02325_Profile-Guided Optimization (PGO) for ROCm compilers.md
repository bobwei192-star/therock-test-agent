# Profile-Guided Optimization (PGO) for ROCm compilers

- **Issue #:** 2325
- **State:** open
- **Created:** 2023-07-18T22:35:12Z
- **Updated:** 2023-07-19T01:42:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/2325

Hi!

Recently I checked Profile-Guided Optimization (PGO) improvements on multiple projects. The results are [here](https://github.com/zamazan4ik/awesome-pgo/).

Since PGO showed measurable improvements in compiler-like loads (Clang, Clangd, clang-format, GCC, Rustc, etc.) I think it could be useful to check PGO on ROCm compilers (https://rocm.docs.amd.com/en/latest/reference/rocmcc/rocmcc.html) as well.

We need to perform PGO benchmarks on ROCm. And if it shows improvements - add a note about possible improvements ROCm performance with PGO. Providing an easier way (e.g. a build option) to build scripts with PGO can be useful for the end-users too.

Also, I think would be better if AMD will distribute already PGO-optimized binaries for the end-users. It will reduce users' compilation time (it's important for CI workloads and local development cycles).