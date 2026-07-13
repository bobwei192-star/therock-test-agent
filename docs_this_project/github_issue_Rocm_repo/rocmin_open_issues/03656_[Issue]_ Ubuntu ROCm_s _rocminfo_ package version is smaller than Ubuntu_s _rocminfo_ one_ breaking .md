# [Issue]: Ubuntu ROCm's `rocminfo` package version is smaller than Ubuntu's `rocminfo` one, breaking `rocm-hip-runtime` installation

- **Issue #:** 3656
- **State:** open
- **Created:** 2024-08-29T13:41:24Z
- **Updated:** 2026-04-29T20:10:49Z
- **Labels:** Under Investigation, ROCm 6.2.0, AMD Radeon Pro W7800
- **URL:** https://github.com/ROCm/ROCm/issues/3656

### Problem Description

I'm running ROCm 6.2.0 on Ubuntu 24.4 Noble. The GPU is an `AMD Radeon PRO W7600` but it doesn't matter because the issue is a packaging issue affecting packages provided by [repo.radeon.com](https://repo.radeon.com).

Ubuntu provides a `rocminfo` package with version 5.7.1:

```
Get:1 http://archive.ubuntu.com/ubuntu noble/universe amd64 rocminfo amd64 5.7.1-3build1 [25.6 kB]
```

The AMD APT repository for ROCm 6.2 provides a `rocminfo` package with version 1.0.0:

```
Get:1 https://repo.radeon.com/rocm/apt/6.2 noble/main amd64 rocminfo amd64 1.0.0.60200-66~24.04 [29.3 kB]
```

The workstation was running Ubuntu 23.10 Jammy Jellyfish with ROCm 6.1.3 and was then updated to Ubuntu 24.04 Noble Numbat and then ROCm was updated to ROCm 6.2. It means the update from Ubuntu 23.10 to Ubuntu 24.04 was done before uptating ROCm from 6.1.3 to 6.2.

While updating Ubuntu from 23.10 to 24.04, the `rocminfo` package was upgraded with Ubuntu one with version `5.7`, meaning the system received a package older than the one from ROCm 6.2 but with an higher version and taking priority over.

Later, when upgrading to ROCm 6.2, it brokes the installation of `rocm-hip-runtime` as it depends on `rocminfo=1.0.0.60200-66~24.04` but an older package with a higher version number (`5.7.1-3build1`) is already installed:

```
# apt-get install rocm-hip-runtime
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-hip-runtime : Depends: rocminfo (= 1.0.0.60200-66~24.04) but 5.7.1-3build1 is to be installed
```


### Operating System

Ubuntu 24.04 Noble Numbat

### CPU

AMD Ryzen Threadripper PRO 3955WX 16-Cores

### GPU

AMD Radeon Pro W7800

### ROCm Version

ROCm 6.2.0

### ROCm Component

rocminfo

### Steps to Reproduce

1. Install Ubuntu 23.10
2. Install `rocm-hip-runtime` from ROCm 6.1.3
3. Upgrade to Ubuntu 24.04
4. Attempt to install `rocm-hip-runtime` from ROCm 6.2

Alternatively (untested):

1. Install Ubuntu 24.04
2. Install `rocm-hip-runtime` from Ubuntu repositories
3. Attempt to install `rocm-hip-runtime` from ROCm 6.2

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_