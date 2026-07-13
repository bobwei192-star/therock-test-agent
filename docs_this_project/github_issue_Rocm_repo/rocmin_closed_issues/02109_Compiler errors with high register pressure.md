# Compiler errors with high register pressure

- **Issue #:** 2109
- **State:** closed
- **Created:** 2023-05-04T09:14:47Z
- **Updated:** 2023-05-04T09:14:55Z
- **Labels:** Verified Issue, 5.4.2
- **URL:** https://github.com/ROCm/ROCm/issues/2109

This issue is ported from the release notes.

Under certain circumstances typified by high register pressure, users may encounter a compiler abort with one of the following error messages:

- `error: unhandled SGPR spill to memory`
- `cannot scavenge register without an emergency spill slot!`
- `error: ran out of registers during register allocation`