# Compatibility of opencl binaries with Windows open CL AMD drivers.

- **Issue #:** 332
- **State:** closed
- **Created:** 2018-02-12T13:27:52Z
- **Updated:** 2018-06-03T14:42:34Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/332

It's not clear if a compiled, then exported OpenCL binary in ROCm enviroment  is compatible with the latest OpenCL AMD Windows drivers. (the windows OpenCl program will load it using the OPenCL clCreateProgramWithBinary function).