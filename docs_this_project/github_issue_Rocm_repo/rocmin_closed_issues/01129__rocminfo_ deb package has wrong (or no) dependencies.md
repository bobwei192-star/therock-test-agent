# `rocminfo` deb package has wrong (or no) dependencies

- **Issue #:** 1129
- **State:** closed
- **Created:** 2020-06-04T14:04:59Z
- **Updated:** 2024-08-14T15:26:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1129

```
$ apt show rocminfo
Package: rocminfo
Version: 1.30500.0
Priority: optional
Section: devel
Maintainer: Advanced Micro Devices Inc.
Installed-Size: 76.8 kB
Download-Size: 25.1 kB
APT-Manual-Installed: no
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime rocminfo tool
```

this is simply wrong.

You are missing dependency on `libstdc++6:amd64` and `hsa-rocr-dev`. It is also very unfortunate that the `/opt/rocm-3.5.0/lib/libhsa-runtime64.so.1` is in `hsa-rocr-dev` and not in the `libhsa1` with headers (and any potential static libraries in the future) in `libhsa-dev`.

