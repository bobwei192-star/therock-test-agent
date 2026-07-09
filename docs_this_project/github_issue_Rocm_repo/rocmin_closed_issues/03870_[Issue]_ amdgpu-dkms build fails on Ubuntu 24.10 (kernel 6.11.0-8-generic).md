# [Issue]: amdgpu-dkms build fails on Ubuntu 24.10 (kernel 6.11.0-8-generic)

- **Issue #:** 3870
- **State:** closed
- **Created:** 2024-10-06T22:54:36Z
- **Updated:** 2025-02-13T09:43:10Z
- **Labels:** AMD Radeon RX 7900 XT, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3870

### Problem Description

amdgpu-dkms build fails:

```
Performing actions...
(Reading database ... 316051 files and directories currently installed.)
Removing qtchooser (66-2build2) ...
Setting up amdgpu-dkms (1:6.8.5.60202-2041575.24.04) ...
Removing old amdgpu-6.8.5-2041575.24.04 DKMS files...
Deleting module amdgpu-6.8.5-2041575.24.04 completely from the DKMS tree.
Loading new amdgpu-6.8.5-2041575.24.04 DKMS files...
Building for 6.11.0-8-generic
Building for architecture x86_64
Building initial module for 6.11.0-8-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms.0.crash'
Error! Bad return status for module build on kernel: 6.11.0-8-generic (x86_64)
Consult /var/lib/dkms/amdgpu/6.8.5-2041575.24.04/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Processing triggers for man-db (2.12.1-3) ...
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
Setting up amdgpu-dkms (1:6.8.5.60202-2041575.24.04) ...
Removing old amdgpu-6.8.5-2041575.24.04 DKMS files...
Deleting module amdgpu-6.8.5-2041575.24.04 completely from the DKMS tree.
Loading new amdgpu-6.8.5-2041575.24.04 DKMS files...
Building for 6.11.0-8-generic
Building for architecture x86_64
Building initial module for 6.11.0-8-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms.0.crash'
Error! Bad return status for module build on kernel: 6.11.0-8-generic (x86_64)
Consult /var/lib/dkms/amdgpu/6.8.5-2041575.24.04/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
```

From the `make.log` we can find various errors such as:

```
/tmp/amd.0wFA7BzU/scheduler/./gpu_scheduler_trace.h:60:1: error: macro "__assign_str" passed 2 arguments, but takes just 1
```

The root cause seems to be https://github.com/torvalds/linux/commit/2c92ca849fcc, which changed the arguments for the macro on kernel 6.10, so bulid fails (isn't `__` prefix for internal stuff that shouldn't be used anyway?).

### Operating System

Ubuntu 24.10 (Oracular Oriole)

### CPU

AMD Ryzen 7 3700X 8-Core Processor

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

Just try to install the package & bulid it on 6.11.0-8-generic.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Ubuntu 24.10 is still in development, but [is set to be released in 4 days](https://www.omgubuntu.co.uk/2024/05/ubuntu-24-10-release-date#:~:text=Canonical%20has%20published%20a%20draft,on%20Thursday%20October%2010%2C%202024.).