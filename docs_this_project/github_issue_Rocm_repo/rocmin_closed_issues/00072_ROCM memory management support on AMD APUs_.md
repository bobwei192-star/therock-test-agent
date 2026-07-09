# ROCM memory management support on AMD APUs? 

- **Issue #:** 72
- **State:** closed
- **Created:** 2017-01-09T04:34:23Z
- **Updated:** 2017-02-24T20:51:24Z
- **Assignees:** hthangirala
- **URL:** https://github.com/ROCm/ROCm/issues/72

Is it possible to reserve few addresses of DRAM as config registers during boot up ? I need to access the same physical address on each boot up . These will be a device config registers for my application research.
Can we modify the MMU for this requirement in ROCM platform ? 