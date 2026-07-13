# [Issue]: Ubuntu `rocm-opencl-runtime` package upgrade doesn't upgrade `rocprofiler-register` one

- **Issue #:** 3654
- **State:** closed
- **Created:** 2024-08-29T10:45:01Z
- **Updated:** 2024-09-11T13:46:36Z
- **Labels:** Under Investigation, ROCm 6.1.0, ROCm 6.2.0, AMD Radeon Pro W7800
- **URL:** https://github.com/ROCm/ROCm/issues/3654

### Problem Description

I'm running ROCm 6.2.0 on Ubuntu 24.4 Noble. The GPU is an `AMD Radeon PRO W7600` but it doesn't matter because the issue is a packaging issue affecting packages provided by [repo.radeon.com](https://repo.radeon.com).

On Ubuntu, when an existing ROCm OpenCL is installed, upgrading the `rocm-opencl-runtime` package upgrade doesn't upgrade the required `rocprofiler-register` one.

By doing `apt-get install rocm-opencl-runtime`, this updates `rocm-opencl-runtime` and `comgr hip-runtime-amd hsa-rocr openmp-extras-runtime rocm-core rocm-hip-runtime rocm-language-runtime rocm-opencl rocm-opencl-icd-loader rocminfo`.

But not everything is updated in a way it can work:

```
$ LD_PRELOAD=/opt/rocm-6.2.0/lib/libamdocl64.so.2 clinfo --list
clinfo: error while loading shared libraries: librocprofiler-register.so.0: cannot open shared object file: No such file or directory
```

Doing `apt-get dist-upgrade` will upgrade `hsa-rocr-dev hsakmt-roct-dev rocm-dbgapi rocm-gdb rocm-llvm rocprofiler-register`:

```
The following packages will be upgraded:
   hsa-rocr-dev (1.13.0.60103-122~22.04 => 1.14.0.60200-66~24.04)
   hsakmt-roct-dev (20240125.5.08.60103-122~22.04 => 20240607.3.8.60200-66~24.04)
   rocm-dbgapi (0.71.0.60103-122~22.04 => 0.76.0.60200-66~24.04)
   rocm-gdb (14.1.60103-122~22.04 => 14.2.60200-66~24.04)
   rocm-llvm (17.0.0.24193.60103-122~22.04 => 18.0.0.24292.60200-66~24.04)
   rocprofiler-register (0.3.0.60103-122~22.04 => 0.4.0.60200-66~24.04)
```

Just doing `apt-get install rocprofiler-register` is enough to make OpenCL working again:

```
$ LD_PRELOAD=/opt/rocm-6.2.0/lib/libamdocl64.so.2 clinfo --list
Platform #0: AMD Accelerated Parallel Processing
 `-- Device #0: gfx1102
```

This library mismatch happens on every ROCm update, for example I previously got this when upgrading from 6.1.2 to 6.1.3:

```
$ LD_PRELOAD=/opt/rocm-6.1.3/lib/libamdocl64.so clinfo --list
clinfo: error while loading shared libraries: librocprofiler-register.so.0: cannot open shared object file: No such file or directory
```

And I remember having got the same error before when upgrading from 6.1.1 to 6.1.2, etc.

This affects both Ubuntu Jammy Jellyfish 22.04 and Ubuntu Noble Numbat 24.04, and this affects both ROCm 6.1 and ROCm 6.2.

A solution would be to make the dependency version of `rocprofiler-register` more strict in the `rocm-opencl-runtime` package.

It happens that `rocm-opencl-runtime` only depends on `rocm-core=6.2.0.60200-66~24.04 rocm-language-runtime=6.2.0.60200-66~24.04 rocm-opencl=2.0.0.60200-66~24.04 rocm-opencl-icd-loader=1.2.60200-66~24.04`

The dependency tree is: `rocm-opencl-runtime=2.0.0.60200-66~24.04 → rocm-opencl=2.0.0.60200-66~24.04 → hsa-rocr → rocprofiler-register`. As we see no version is enforced below the `rocm-opencl` package.

### Operating System

Ubuntu 24.04 Noble Numbat

### CPU

AMD Ryzen Threadripper PRO 3955WX 16-Cores

### GPU

AMD Radeon Pro W7800

### ROCm Version

ROCm 6.2.0, ROCm 6.1.0

### ROCm Component

rocprofiler

### Steps to Reproduce

```sh
apt-get install --yes 'gdebi-core'

wget 'https://repo.radeon.com/amdgpu-install/6.1.3/ubuntu/jammy/amdgpu-install_6.1.60103-1_all.deb'
gdebi --non-interactive 'amdgpu-install_6.1.60103-1_all.deb'
apt-get update
apt-get install --yes --verbose-versions 'rocm-opencl-runtime'

wget 'https://repo.radeon.com/amdgpu-install/6.2/ubuntu/noble/amdgpu-install_6.2.60200-1_all.deb'
gdebi --non-interactive 'amdgpu-install_6.2.60200-1_all.deb'
apt-get update
apt-get install --yes --verbose-versions 'rocm-opencl-runtime'

apt-get install --yes --verbose-versions 'clinfo'

LD_PRELOAD='/opt/rocm-6.2.0/lib/libamdocl64.so.2' clinfo --list
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_