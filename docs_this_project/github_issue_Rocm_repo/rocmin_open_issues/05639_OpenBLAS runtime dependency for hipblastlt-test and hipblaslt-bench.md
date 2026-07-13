# OpenBLAS runtime dependency for hipblastlt-test and hipblaslt-bench

- **Issue #:** 5639
- **State:** open
- **Created:** 2025-11-07T23:39:12Z
- **Updated:** 2025-11-08T00:10:51Z
- **Labels:** Verified Issue, ROCm 7.1.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5639

Running `hipblaslt-test` or `hipblaslt-bench` without installing the OpenBLAS development package results in the following error:
```
libopenblas.so.0: cannot open shared object file: No such file or directory
```
As a workaround, first install `libopenblas-dev` or `libopenblas-deve`, depending on the package manager used. The issue will be fixed in a future ROCm release. 