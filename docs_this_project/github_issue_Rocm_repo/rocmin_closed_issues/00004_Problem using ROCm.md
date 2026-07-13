# Problem using ROCm

- **Issue #:** 4
- **State:** closed
- **Created:** 2016-04-21T03:43:00Z
- **Updated:** 2016-08-20T18:49:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/4

Hi,
I have been following the development of hcc and ROCm for a while. I have used most of previous versions and had them running on my Kaveri APU system. However, since I updated to ROCm-1.0 release, none of the executable I compile runs.
When I try to run executable compiled with hcc, I get 

`### Error: HSA_STATUS_ERROR_INCOMPATIBLE_ARGUMENTS (4109) at line:1757`

Funny thing is, my code is not very long. They are toy examples and are well less than a thousand lines of code.

I can run /opt/rocm/hsa/sample/vector_copy and it prints out success messages. But that's the only thing I can run right now.

Also, configuring hcc compilation environment does not find hsa installation any more. Before installing ROCm, cmake would find everything without any issues. Now, I get

`=============================================`
`HCC version: 0.10.16163-caab0f1-7e4cd9e`
`=============================================`
`CMake Error at CMakeLists.txt:261 (MESSAGE):`
`Neither OpenCL nor HSA is available on the system!`

What did I do wrong?
