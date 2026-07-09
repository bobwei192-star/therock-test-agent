# Why does `flang` predefine `__PGLLVM__`?

- **Issue #:** 1811
- **State:** closed
- **Created:** 2022-09-21T14:34:45Z
- **Updated:** 2024-05-09T16:18:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/1811

This was pre-defined for the "classic" flang implementation. The new `flang` (based on `f18`, i.e., upstream) does not define it anymore.