# MIGraphX Python API will fail when running on Python 3.13

- **Issue #:** 5500
- **State:** open
- **Created:** 2025-10-10T22:46:38Z
- **Updated:** 2025-12-02T12:56:04Z
- **Labels:** Verified Issue, ROCm 7.0.2, ROCm 7.1.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5500

Applications using the MIGraphX Python API will fail when running on Python 3.13 and return the error message `AttributeError: module 'migraphx' has no attribute 'parse_onnx'`. The issue does not occur when you manually build MIGraphX. For detailed instructions, see [Building from source](https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/install/install-migraphx.html#build-migraphx-from-source). As a workaround, change the Python version to the one found in the installed location:

```
ls -l /opt/rocm-7.0.0/lib/libmigraphx_py_*.so
```
The issue will be resolved in a future ROCm release.