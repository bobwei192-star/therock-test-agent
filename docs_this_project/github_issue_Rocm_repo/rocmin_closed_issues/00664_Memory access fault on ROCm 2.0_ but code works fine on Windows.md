# Memory access fault on ROCm 2.0, but code works fine on Windows

- **Issue #:** 664
- **State:** closed
- **Created:** 2019-01-06T14:20:33Z
- **Updated:** 2019-01-07T23:02:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/664

My platform:
Ubuntu 18.04
ROCm 2.0
Radeon RX 580

Error message:
Memory access fault by GPU node-1 (Agent handle: 0x561756df8460) on address 0x501006000. Reason: Page not present or supervisor privilege.

Code:
[rocm_crash.zip](https://github.com/RadeonOpenCompute/ROCm/files/2730523/rocm_crash.zip)

Description:
Same code works fine on Windows 10, Visual Studio 2017 and this SDK [https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/releases](url).

I am not sure what to do next to determine cause of this error or what it even means. Perhaps it's problem in ROCm itself, which is why I post it here - feel free to try the code or instruct me what to do to debug this.

Note:
Tried running it as root without change.