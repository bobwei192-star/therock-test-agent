# [Issue]: amdgpu-dkms configure script broken when `libpam-tmpdir` installed on Ubuntu

- **Issue #:** 4204
- **State:** closed
- **Created:** 2024-12-28T00:05:00Z
- **Updated:** 2025-03-05T15:32:03Z
- **Labels:** Under Investigation, ROCm 6.3.0, AMD Radeon RX 6600
- **URL:** https://github.com/ROCm/ROCm/issues/4204

### Problem Description

Basically, I was encountering the same compile errors as #4164 (except on Ubuntu 24.04 LTS) and I was pulling my hair out. 

See below for details

### Operating System

Ubuntu 24.04.1 LTS (Noble Numbat)

### CPU

AMD Ryzen Threadripper 2950X 16-Core Processor

### GPU

AMD Radeon RX 6600

### ROCm Version

ROCm 6.3.0

### ROCm Component

_No response_

### Steps to Reproduce

1. Install `libpam-tmpdir` package
2. Run `pam-auth-update` and enable "per-user temp directories" (if not already enabled)
3. Log out, or reboot to ensure the `TMPDIR` env var is set.
4. Follow instructions at https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

Not applicable

### Additional Information

Following a deep dive into `amdgpu-dkms`, it seems there is a incompatibility (bug?) in DKMS module's `amd/dkms/configure` script, which (when `libpam-tmpdir` is active) generates an incorrect `amd/dkms/config/config.h` file that won't compile.

In particular, when the `configure` script runs test compilations, it creates a temporary build directory a la:

```bash
build_dir=$(mktemp -d -t build_XXXXXXXX -p $build_dir_root)
```
.. where `$build_dir_root` is `/var/lib/dkms/amdgpu/6.10.5-2095006.24.04/build` (or similar, depending on your system).

The problem is that, according to `mktemp --help`, the presence of the `-d` switch in the call to `mktemp` means that the `-p $build_dir_root` argument is ignored in favor of the `TMPDIR` environment variable, if it exists.  Setting `TMPDIR`, meanwhile, is the entire purpose of the `libpam-tmpdir` pam module. 

In some test compilations, however, the `./configure` script adds `-I../tiny_wrapper/include` to `CFLAGS`, meaning correct results are contingent on `$build_dir` being a subdirectory of `$build_dir_root`. 

False negatives in these test compilations lead to several macros not being defined in `config.h`, which causes the inclusion of code that won't compile, leading to the errors seen in #4164.

As a temporary workaround, I was able to get the module to build by adding `unset TMPDIR` right after the shebang in the `./configure` script. 

Potential permanent fixes include: 

1) setting `TMPDIR` to `$build_dir_root` in the `./configure` script (or in `pre-build.sh`), 
2) unsetting `TMPDIR` in the `./configure` script (or in `pre-build.sh`),
3) replacing all usages of relative paths (e.g. `-I../tiny_wrapper/include` and similar) in test compiles with their respective absolute paths,
4) if this is a 'wontfix', `libpam-tmpdir` should at least be added as a conflicting package in `amdgpu-dkms`'s `debian/control` file