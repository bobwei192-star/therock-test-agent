# OpenCL clBuildProgram terminates on invalid -save-temps

- **Issue #:** 779
- **State:** closed
- **Created:** 2019-04-22T06:29:41Z
- **Updated:** 2019-04-22T16:25:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/779

ROCm 2.2 OpenCL:

when clBuildProgram() is invoked with an invalid path in -save-temps , it terminates the process abruptly after displaying the message:
LLVM ERROR: IO failure on output stream: Bad file descriptor

The expected behavior of clBuildProgram is to return an error code != CL_SUCCESS on error, not to terminate the process.
