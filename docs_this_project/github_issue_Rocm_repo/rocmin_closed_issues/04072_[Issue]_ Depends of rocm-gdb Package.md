# [Issue]: Depends of rocm-gdb Package

- **Issue #:** 4072
- **State:** closed
- **Created:** 2024-12-02T15:17:02Z
- **Updated:** 2025-01-16T15:46:30Z
- **Labels:** Under Investigation, ROCm 6.2.1, Radeon 7900 xtx
- **URL:** https://github.com/ROCm/ROCm/issues/4072

### Problem Description

I noticed a discrepancy between the Depends: field in the source code and the DEBIAN/control file in the package I downloaded.
From the source code [here](https://github.com/ROCm/ROCm/blob/cfdb6f2f089fe34232be5ddb7e180df7ceb3b0c9/tools/rocm-build/build_rocm-gdb.sh#L140), the Depends: field looks like this:
Depends: libexpat1, libtinfo5, libncurses5, rocm-dbgapi, libpython3.10 | libpython3.8, libbabeltrace-ctf1 (>= 1.2.1), libbabeltrace1 (>= 1.2.1), rocm-core
But from the DEBIAN/control file in the package downloaded from [https://repo.radeon.com/amdgpu/6.2.1/ubuntu noble InRelease](https://repo.radeon.com/amdgpu/6.2.1/ubuntu), the Depends: field looks like this:
Depends: libc6 (>= 2.38), libexpat1 (>= 2.0.1), libgcc-s1 (>= 4.2), libgmp10 (>= 2:6.3.0+dfsg), liblzma5 (>= 5.1.1alpha+20110809), libmpfr6 (>= 3.1.3), libncursesw6 (>= 6), libpython3.12t64 (>= 3.12.1), libstdc++6 (>= 12), libtinfo6 (>= 6), libzstd1 (>= 1.5.5), zlib1g (>= 1:1.2.0), rocm-dbgapi, rocm-core

Why is the DEBIAN/control file in the source code different from the one in the compiled DEB package?

### Operating System

ubuntu24.04

### CPU

AMD 9900

### GPU

Radeon 7900 xtx

### ROCm Version

ROCm 6.2.1

### ROCm Component

ROCgdb

### Steps to Reproduce

From the source code [here](https://github.com/ROCm/ROCm/blob/cfdb6f2f089fe34232be5ddb7e180df7ceb3b0c9/tools/rocm-build/build_rocm-gdb.sh#L140), the Depends: field looks like this:
Depends: libexpat1, libtinfo5, libncurses5, rocm-dbgapi, libpython3.10 | libpython3.8, libbabeltrace-ctf1 (>= 1.2.1), libbabeltrace1 (>= 1.2.1), rocm-core

From the DEB packge
https://repo.radeon.com/amdgpu/6.2.1/ubuntu 
sudo apt-get download rocm-gdb
sudo apt show ./rocm-gdb_14.2.60201-112~24.04_amd64.deb
Package: rocm-gdb
Version: 14.2.60201-112~24.04
Priority: optional
Essential: no
Section: utils
Maintainer: ROCm Debugger Support <rocm-gdb.support@amd.com>
Installed-Size: unknown
Depends: libc6 (>= 2.38), libexpat1 (>= 2.0.1), libgcc-s1 (>= 4.2), libgmp10 (>= 2:6.3.0+dfsg), liblzma5 (>= 5.1.1alpha+20110809), libmpfr6 (>= 3.1.3), libncursesw6 (>= 6), libpython3.12t64 (>= 3.12.1), libstdc++6 (>= 12), libtinfo6 (>= 6), libzstd1 (>= 1.5.5), zlib1g (>= 1:1.2.0), rocm-dbgapi, rocm-core
Download-Size: 85.0 MB
APT-Sources: https://repo.radeon.com/rocm/apt/6.2.1 noble/main amd64 Packages
Description: ROCgdb
 This is ROCgdb, the AMD ROCm source-level debugger for Linux,
 based on GDB, the GNU source-level debugger.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_