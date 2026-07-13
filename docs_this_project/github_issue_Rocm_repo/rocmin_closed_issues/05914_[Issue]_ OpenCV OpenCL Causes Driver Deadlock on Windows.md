# [Issue]: OpenCV OpenCL Causes Driver Deadlock on Windows

- **Issue #:** 5914
- **State:** closed
- **Created:** 2026-01-29T16:22:57Z
- **Updated:** 2026-02-25T16:15:05Z
- **Labels:** Windows, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5914

### Problem Description

When using OpenCV (Python or C++) in a Windows environment to initialize OpenCL devices (specifically AMD Radeon RX 7000 series GPUs), the application enters an indefinite deadlock state, failing to create the OpenCL context.

### Operating System

Windows 24H2 26100.7623

### CPU

AMD Ryzen 9 7950X 16-Core Processor

### GPU

AMD Radeon RX 7900 XTX [Driver 26.1.1]

### ROCm Version

7.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Reproduction Steps
Execute standard OpenCV OpenCL detection code (e.g., cv.ocl.haveOpenCL() or cv::ocl::getPlatfomsInfo()).
The program hangs indefinitely while attempting to interface with the AMD OpenCL ICD loader.
Expected Result
The program should successfully enumerate all OpenCL platforms and devices and return control.
Actual Result/Issue
The program deadlocks and becomes unresponsive, requiring a forced termination. Internal OpenCV logs stop during the context creation phase, as the driver function call does not return.
Attempted Solutions
The following methods were attempted without success:
No OPENCV_OPENCL_DEVICE environment variable set: Program deadlocks.
Setting OPENCV_OPENCL_DEVICE=DISABLED: Program runs without deadlocking (but with OpenCL disabled), confirming the issue is specific to the OpenCL initialization phase.
Attempting to specify a specific device (AMD:GPU:0): Program deadlocks.
Clearing OpenCV cache files: No effect.
Reproduced in both Python and C++ bindings: Both environments trigger the same issue.
Stack Trace
According to C++ debugger analysis, the deadlock consistently occurs within the following driver module and function (the function call does not return):
amdocl64.dll!clSetKernelExecInfo+0x503279 (0x7ffdf4f0c6d9)
C:\Windows\System32\DriverStore\FileRepository\amdocl.inf_amd64_71fdb5a0a9dd7076\amdocl64.dll
... (other memory addresses omitted) ...
The issue appears to be a deadlock within the AMD OpenCL driver when processing multi-platform/device enumeration requests.
Would you like me to draft the reproduction code snippet in C++ to include with this report?