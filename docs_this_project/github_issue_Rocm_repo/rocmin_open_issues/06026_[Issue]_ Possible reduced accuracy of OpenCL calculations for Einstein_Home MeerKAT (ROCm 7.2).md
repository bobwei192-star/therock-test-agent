# [Issue]: Possible reduced accuracy of OpenCL calculations for Einstein@Home MeerKAT (ROCm 7.2)

- **Issue #:** 6026
- **State:** open
- **Created:** 2026-03-09T03:29:44Z
- **Updated:** 2026-04-06T21:56:18Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6026

### Problem Description

This is more of a 'red flag' than a concrete problem. With respect to the Einstein@Home BOINC project, I have been running their 'MeerKAT' BRP7 tasks for a long time now. The way E@H works is that it sends tasks to different users' computers for a given work-unit, at least two tasks per work-unit. If the results returned are aligned within some mathematical threshold, the results are deemed 'valid' and credit awarded. However, if the results don't match then further tasks are sent out until there is a matching pair of results and other results are deemed 'invalid'.

Since moving from ROCm 7.1.1 to 7.2, I noticed a sharp increase in results being marked as invalid, from 'occasional' to several dozens within a week. Since the only thing that had changed for me was the update in ROCm, I experimented with rolling back to ROCm 7.1.1 for a few days, and the invalid rate has since gone back to normal. **My concern is whether or not there is a known change to OpenCL that could be causing differences in rounding, for example.**

Unfortunately, public access to users' computer status reports are no longer available due to bot-abuse - only registered project users can view this information at present.

### Operating System

Ubuntu 24.04.4 LTS (Noble Numbat)

### CPU

AMD Ryzen Threadripper 3960X 24-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 7.2

### ROCm Component

_No response_

### Steps to Reproduce

I only have OpenCL components installed from ROCm: `amdgpu-install --opencl=rocr --usecase=opencl`

I accept it's not exactly reproducible due to the nature of the project's task validation, but I thought it would be good to report this in case there is a regression with OpenCL.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

While this is a problem for MeerKAT tasks, ROCm 7.2 has actually helped with excessive system memory usage on 'All-Sky' O4AS tasks. So it would be preferable not to be forced to choose between one version of ROCm over another.

@PorcelainMouse From your report #3575, I noticed you (used to) process MeerKAT tasks for E@H. If you happen to still be running them, have you noticed this issue?