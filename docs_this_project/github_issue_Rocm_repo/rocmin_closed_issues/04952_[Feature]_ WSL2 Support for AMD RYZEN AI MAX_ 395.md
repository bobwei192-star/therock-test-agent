# [Feature]: WSL2 Support for AMD RYZEN AI MAX+ 395

- **Issue #:** 4952
- **State:** closed
- **Created:** 2025-06-22T18:26:31Z
- **Updated:** 2026-02-06T13:30:36Z
- **Labels:** Feature Request, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4952

### Suggestion Description

Description:
After installing the AMD GPU driver for WSL2, the system fails to recognize the Radeon 8060S graphics card (gfx1151). The only hardware detected is the CPU, and there are no signs of the GPU functioning within the Windows Subsystem for Linux environment. Could add the support for AMD RYZEN AI MAX+ 395 w/ Radeon 8060S?

Steps to Reproduce:

Install WSL2 on Windows 11.
Update to the latest kernel and install the necessary dependencies for AMD GPU support.
Install the AMDGPU drivers following the official installation guide.
Launch the WSL2 terminal and run a command to list hardware details (e.g., lspci or glxinfo).
Expected Behavior:
The system should detect the Radeon 8060S and display relevant GPU information alongside the CPU.

Actual Behavior:
Only the CPU is detected, and there is no acknowledgment of the Radeon 8060S in the hardware listings.

Environment:

WSL2 version: 2.4.13.0
Windows version: Windows 11
AMDGPU driver version: 25.6.1
Radeon model: 8060S

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_