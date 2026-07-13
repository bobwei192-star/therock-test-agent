# How to enable rocr_debug_agent?

- **Issue #:** 548
- **State:** closed
- **Created:** 2018-09-18T13:42:25Z
- **Updated:** 2018-09-28T20:43:00Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/548

I have vega 10 and rocm 1.9 installed but I do not see state for wavefronts that report memory violation as is stated in readme.md. I have mentioned library at /opt/rocm/lib/librocr_debug_agent64.so. I am getting only same message as with older versions of rocm:
```
Memory access fault by GPU node-1 (Agent handle: 0x1e6d670) on address 0xa1a591000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```
