# Missing cl_amd_device_attribute_query

- **Issue #:** 215
- **State:** closed
- **Created:** 2017-09-28T06:39:14Z
- **Updated:** 2018-04-23T17:38:48Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/215

A user of the CLBlast library [reported full output](https://github.com/CNugteren/CLBlast/issues/186#issuecomment-328012892) of running `/opt/rocm/opencl/bin/x86_64/clinfo` on a Fiji device with ROCm 1.6.

However, although it displays a value for  `CL_DEVICE_BOARD_NAME_AMD` which is part of the [AMD extension cl_amd_device_attribute_query](https://www.khronos.org/registry/OpenCL/extensions/amd/cl_amd_device_attribute_query.txt)), it does not list this extension when querying for the supported extensions.

Is `cl_amd_device_attribute_query` not officially supported by ROCm devices? How to reliably query for the `CL_DEVICE_BOARD_NAME_AMD` attribute?