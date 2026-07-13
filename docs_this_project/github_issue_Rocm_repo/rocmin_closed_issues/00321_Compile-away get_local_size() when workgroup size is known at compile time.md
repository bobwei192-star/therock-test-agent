# Compile-away get_local_size() when workgroup size is known at compile time.

- **Issue #:** 321
- **State:** closed
- **Created:** 2018-02-01T21:23:18Z
- **Updated:** 2018-06-03T15:34:14Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/321

(OpenCL, ROCm 1.7)

The workgroup size can be fixed at compile-time using: ```__attribute__((reqd_work_group_size(x, y, z)))```

The workgroup size can be queried at runtime using get_local_size().

Expected: for a kernel with compile-time fixed workgroup size, the get_local_size() should be compiled-away to the compile-time constant.

Observed: get_local_size() is kept, reading the size from SGPR values passed to the kernel at runtime.
