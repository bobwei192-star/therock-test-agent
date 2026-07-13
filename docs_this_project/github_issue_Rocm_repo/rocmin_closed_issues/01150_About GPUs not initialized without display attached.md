# About GPUs not initialized without display attached

- **Issue #:** 1150
- **State:** closed
- **Created:** 2020-06-16T09:31:38Z
- **Updated:** 2021-01-12T08:12:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/1150

A number of users have been complaining about GPUs and OpenCL non initialized if no display is attached to the GPU.
This behavior only happens on some systems, on other systems (like computing RIGs) I have never encountered this bug.
Thus the bug must be system-configuration dependent or package-dependent, but it does not happen on all systems.
Do you have any idea why this happens only on some systems?
