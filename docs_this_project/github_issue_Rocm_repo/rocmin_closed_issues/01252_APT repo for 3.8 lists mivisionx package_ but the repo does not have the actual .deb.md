# APT repo for 3.8 lists mivisionx package, but the repo does not have the actual .deb

- **Issue #:** 1252
- **State:** closed
- **Created:** 2020-10-05T13:07:16Z
- **Updated:** 2020-10-07T17:47:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1252

From http://repo.radeon.com/rocm/apt/3.8/dists/xenial/main/binary-amd64/Packages:

```
Package: mivisionx
Architecture: amd64
Priority: optional
Section: devel
Filename: pool/main/m/mivisionx/mivisionx_1.9.1_amd64.deb
Size: 48924254
SHA256: cd439e3fe8fe945a7e3c8771bc4752d4a355a59440c6a7df9eed2cafb2264072
SHA1: 42437b53121087525778a61fd1e89a9f63b7a43c
MD5sum: 81e820bc77e0547fca32a62e07dfc73d
Description: AMD MIVisionX toolkit is a comprehensive computer vision and machine intelligence libraries, utilities and applications bundled into one.
Maintainer: Kiriti Gowda <Kiriti.NageshGowda@amd.com>
Version: 1.9.1
Installed-Size: 70098
```

But http://repo.radeon.com/rocm/apt/3.8/pool/main/m/ does not contain said package.

I suspect the entry in `Packages` is obsolete. The 3.7.0 `Packages` file lists the same version (and it's in that repo).