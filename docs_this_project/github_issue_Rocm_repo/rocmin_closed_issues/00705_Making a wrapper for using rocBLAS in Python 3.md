# Making a wrapper for using rocBLAS in Python 3

- **Issue #:** 705
- **State:** closed
- **Created:** 2019-02-13T22:07:12Z
- **Updated:** 2019-02-13T22:08:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/705

It will be highly beneficial to end users if rocBLAS can be integrated into Python 3 in a form of a wrapper using PyopenCL.

For now I am using CLBlast as they do have a Python 3 package pyclblast, but for some reasons the SGEMM performance was sub-optimal on Vega where I obtained only ~3.5 TFLOPs at best. It may just be better if the AMD optimized rocBLAS can be utilized in Python.

Update: Sorry, I meant to submit this under rocBLAS.