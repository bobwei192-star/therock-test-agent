# OpenCL build log does not print error details

- **Issue #:** 817
- **State:** closed
- **Created:** 2019-06-09T12:11:10Z
- **Updated:** 2023-12-21T14:33:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/817

Hi,

I'm using ROCm 2.4 on linux.
When I compile a kernel with an error, the build log is always the same:
"Error: Failed to compile opencl source (from CL to LLVM IR)." 

Earlier, when I was using old proprietary AMD's OpenCL 2.0 driver provided by catalyst, the build log displayed the offending source in a usable compilation report.

Is there a way to get that sort of report with ROCm OpenCL?