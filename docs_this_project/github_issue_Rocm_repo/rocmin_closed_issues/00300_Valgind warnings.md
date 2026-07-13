# Valgind warnings

- **Issue #:** 300
- **State:** closed
- **Created:** 2018-01-17T00:44:02Z
- **Updated:** 2018-05-05T14:48:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/300

I ran my opencl program against valgrind, and I get a number of 
`== Conditional jump or move depends on uninitialised value(s)`
warnings triggered  by `clEnqueueNDRangeKernel` and `clEnqueueWriteBuffer`


