# How to represent NaN compatible with ROCm?

- **Issue #:** 1004
- **State:** closed
- **Created:** 2020-01-22T13:34:51Z
- **Updated:** 2020-01-23T17:37:55Z
- **Assignees:** b-sumner
- **URL:** https://github.com/ROCm/ROCm/issues/1004

I tried to use std::nan("") and std::nanf("") but got this:

error:  'nan':  no overloaded function has restriction specifiers that are compatible with the ambient context ...