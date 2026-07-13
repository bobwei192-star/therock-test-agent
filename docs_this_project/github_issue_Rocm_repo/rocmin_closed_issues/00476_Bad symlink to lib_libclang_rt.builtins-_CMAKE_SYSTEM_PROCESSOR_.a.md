# Bad symlink to lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a

- **Issue #:** 476
- **State:** closed
- **Created:** 2018-07-27T22:51:29Z
- **Updated:** 2018-08-02T20:01:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/476

ROCm 1.8.2

There's a bad symlink on lib/libclang_rt.builtins-* that incorrectly expands `CMAKE_SYSTEM_PROCESSOR` using `@x@` instead of `${x}`.