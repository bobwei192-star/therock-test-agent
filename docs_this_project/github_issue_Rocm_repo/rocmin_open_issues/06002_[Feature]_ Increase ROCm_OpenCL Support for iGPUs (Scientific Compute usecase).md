# [Feature]: Increase ROCm/OpenCL Support for iGPUs (Scientific Compute usecase)

- **Issue #:** 6002
- **State:** open
- **Created:** 2026-02-26T03:40:50Z
- **Updated:** 2026-04-06T18:48:03Z
- **Labels:** Feature Request, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6002

### Suggestion Description

AMD is a leader in efficiency-per-watt, but the lack of official, out-of-the-box support for iGPU compute in projects like Folding@Home and BOINC is allowing competitors to close the gap.

While the community has attempted to use ROCm on some APUs, it remains fragmented. In contrast, I have spent the last month in a dedicated thread with Qualcomm developers. They have confirmed they are officially reviewing the implementation of OpenCL 3.0, SYCL, and high-precision math pathways for the Snapdragon X2 specifically to support the scientific community.

If Qualcomm enables their Adreno iGPU for research while AMD's Radeon iGPUs remain difficult to configure, AMD will lose its competitive edge in the "Pro" mobile workstation market.

I urge AMD to provide first-party collaboration with FAH and BOINC to ensure RDNA 3 and 4 iGPUs are whitelisted and optimized. High-precision scientific compute should be accessible on every efficient AMD-powered laptop.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_