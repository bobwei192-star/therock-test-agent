# AddressSanitizer instrumentation incorrect for device global variables

- **Issue #:** 2551
- **State:** closed
- **Created:** 2023-10-13T21:38:20Z
- **Updated:** 2024-04-17T20:19:40Z
- **Labels:** Under Investigation, Verified Issue, Resolved, 5.7.1, 6.0.0
- **URL:** https://github.com/ROCm/ROCm/issues/2551

The AddressSanitizer instrumentation results in incorrect information about the size of device global variables, which causes,

- the function *hipModuleGetGlobal* to return an incorrect size, resulting in the generation of a buffer overflow report if used in a hipMemcpy operation

- failures reported by calls to the function *hipModuleGetTexRef*

This issue is under investigation and will be fixed in a future release.
