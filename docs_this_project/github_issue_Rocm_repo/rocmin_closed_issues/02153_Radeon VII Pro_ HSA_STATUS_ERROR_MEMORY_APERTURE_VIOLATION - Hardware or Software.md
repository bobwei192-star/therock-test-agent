# Radeon VII Pro: HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION - Hardware or Software

- **Issue #:** 2153
- **State:** closed
- **Created:** 2023-05-19T10:19:08Z
- **Updated:** 2023-11-11T19:38:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/2153

Hi,
Simulation code with embedded hip running on Radeon VII pro and ROCm 5.18.13. It  *always* fails with some memory error, most commonly with something like:

:0:rocdevice.cpp :2672: 0696142325 us: 5999 : [tid:0x7f676e4c7640] Device::callbackQueue aborting with error : HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION: The agent attempted to access memory beyond the largest legal address. code: 0x29
forrtl: error (76): Abort trap signal  + some backtrace.

but it *always* works on MI60, MI50 and Radeon VII (non-pro).

Is it possible to:
1) Say if this is hardware or driver error.
2) Any possible test for the card itself.
3) Say anything at all.

Thanks.
--





