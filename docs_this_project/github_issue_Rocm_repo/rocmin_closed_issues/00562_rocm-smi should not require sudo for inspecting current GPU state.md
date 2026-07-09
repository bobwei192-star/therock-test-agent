# rocm-smi should not require sudo for inspecting current GPU state

- **Issue #:** 562
- **State:** closed
- **Created:** 2018-09-27T13:17:59Z
- **Updated:** 2018-12-24T22:48:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/562

The `rocm-smi` tool currently tries to relaunch itself with sudo privileges, even when only trying to display the current GPU state.  Looking at the code, it seems that write access to `/sys` is only needed to modify power profiles, clocks, etc, but the script attempts to relaunch itself with sudo regardless of whether read or write operations need to be performed.  This prevents rocm-smi from being used by normal users who can run GPU code, but also want to monitor the GPU load, temperature, etc.