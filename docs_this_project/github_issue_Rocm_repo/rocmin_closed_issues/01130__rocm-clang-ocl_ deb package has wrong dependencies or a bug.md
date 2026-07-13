# `rocm-clang-ocl` deb package has wrong dependencies or a bug

- **Issue #:** 1130
- **State:** closed
- **Created:** 2020-06-04T14:08:42Z
- **Updated:** 2020-12-09T07:21:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/1130

```
$ /opt/rocm-3.5.0/bin/clang-ocl
/opt/rocm-3.5.0/bin/clang-ocl: line 37: /opt/rocm-3.5.0/llvm/bin/clang: No such file or directory
$
```

```
$ apt show rocm-clang-ocl
Package: rocm-clang-ocl
Version: 0.5.0.51-rocm-rel-3.5-30-74b3b81
Priority: optional
Section: devel
Maintainer: Paul Fultz II <paul.fultz@amd.com>
Installed-Size: 15.4 kB
Depends: rocm-opencl-dev
Download-Size: 1,616 B
APT-Manual-Installed: no
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: OpenCL compilation with clang compiler.
```

I don't know where, but no package provide `/opt/rocm-3.5.0/llvm/bin/clang` file.
