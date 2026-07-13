# WSL2 not detect Radeon 8060S

- **Issue #:** 4809
- **State:** closed
- **Created:** 2025-05-27T13:15:57Z
- **Updated:** 2026-02-03T18:42:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/4809

**Description:**
After installing the AMD GPU driver for WSL2, the system fails to recognize the Radeon 8060S graphics card. The only hardware detected is the CPU, and there are no signs of the GPU functioning within the Windows Subsystem for Linux environment.

**Steps to Reproduce:**
1. Install WSL2 on Windows 11.
2. Update to the latest kernel and install the necessary dependencies for AMD GPU support.
3. Install the AMDGPU drivers following the official installation guide.
4. Launch the WSL2 terminal and run a command to list hardware details (e.g., `lspci` or `glxinfo`).

**Expected Behavior:**
The system should detect the Radeon 8060S and display relevant GPU information alongside the CPU.

**Actual Behavior:**
Only the CPU is detected, and there is no acknowledgment of the Radeon 8060S in the hardware listings.

**Environment:**
- WSL2 version: 2.4.13.0
- Windows version: Windows 11
- AMDGPU driver version: 25.5.1
- Radeon model: 8060S
