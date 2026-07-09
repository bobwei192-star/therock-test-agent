# Impact of OpenCL constant vs. global mem space on code generation.

- **Issue #:** 203
- **State:** closed
- **Created:** 2017-09-12T12:36:46Z
- **Updated:** 2018-05-24T04:28:22Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/203

This is a request for information, not a bug.

Using OpenCL with AMDGPU-pro 17.30 with RX Vega 64 on Linux (thus, with the ROCm compiler),
I see that the compiled code has different performance and different VGPR usage depending on a kernel argument being "constant" or "const global" pointer.

Maybe somebody could explain the reason for the difference, and what exactly is the difference.

(from my POV, if I only read from a buffer in the kernel I can mark it as either constant or global at my choice. Why wouldn't the compiler make the "better" choice instead of my trial-and-error? What is the impact on the compiler of marking the buffer constant. Thanks!)