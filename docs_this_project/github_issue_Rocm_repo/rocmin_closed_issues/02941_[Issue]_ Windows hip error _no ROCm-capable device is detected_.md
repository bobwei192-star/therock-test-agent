# [Issue]: Windows hip error 'no ROCm-capable device is detected'

- **Issue #:** 2941
- **State:** closed
- **Created:** 2024-03-04T15:27:54Z
- **Updated:** 2025-10-12T10:23:37Z
- **Labels:** ROCm 5.7.1, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/2941

### Problem Description

After installing all HIP SDK with all its options successfully and setting up the system environment variables,
I get hipErrorNoDevice when running the `hipinfo` command or when trying to use hip:

```
:4:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\rocclr\platform\runtime.cpp:83  : 1256747841 us: [pid:20784 tid:0x9b0] init
:3:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\hipamd\src\hip_context.cpp:48  : 1256747970 us: [pid:20784 tid:0x9b0] Direct Dispatch: 0
:3:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\hipamd\src\hip_device_runtime.cpp:546 : 1256748073 us: [pid:20784 tid:0x9b0]  hipGetDeviceCount ( 0000000801EFFA3C )
:3:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\hipamd\src\hip_device_runtime.cpp:548 : 1256748170 us: [pid:20784 tid:0x9b0] hipGetDeviceCount: Returned hipErrorNoDevice :
:3:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\hipamd\src\hip_device_runtime.cpp:546 : 1256748258 us: [pid:20784 tid:0x9b0]  hipGetDeviceCount ( 0000000801EFFA3C )
:3:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\hipamd\src\hip_device_runtime.cpp:548 : 1256748345 us: [pid:20784 tid:0x9b0] hipGetDeviceCount: Returned hipErrorNoDevice :
:3:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\hipamd\src\hip_device_runtime.cpp:546 : 1256748410 us: [pid:20784 tid:0x9b0]  hipGetDeviceCount ( 0000000801EFFA3C )
:3:C:\constructicon\builds\gfx\two\23.30\drivers\compute\clr\hipamd\src\hip_device_runtime.cpp:548 : 1256748470 us: [pid:20784 tid:0x9b0] hipGetDeviceCount: Returned hipErrorNoDevice :
error: 'no ROCm-capable device is detected'(100) at C:\constructicon\builds\gfx\two\23.30\drivers\compute\hip-tests\samples\1_Utils\hipInfo\hipInfo.cpp:205
error: API returned error code.
error: TEST FAILED
```

The GPU is recognized by the system and usually works.

### Operating System

Windows 11 Pro 10.0.22621 (22H2)

### CPU

Intel(R) Core(TM) i7-8086K CPU @ 4.00GHz

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 5.7.1

### ROCm Component

HIP

### Steps to Reproduce

I uninstalled all existing HIP and AMD drivers and downgraded from windows 23H2 to 22H2 (attempting to fix this). 
Downloaded HIP SDK 5.7.1 for Windows 10 & 11 and installed it.
Then I set up the system environment variables to be `HIP_PATH=C:\Program Files\AMD\ROCm\5.7\`, `HIP_PATH_57=C:\Program Files\AMD\ROCm\5.7\`, `HIP_VISIBLE_DEVICES=1` and in the Path variable I added `C:\Program Files\AMD\ROCm\5.7\bin` and `%HIP_PATH%bin`.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_