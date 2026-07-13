# [Issue] ROCm 6.1 - Ubuntu package for hipblas-dev should run ldconfig after install

- **Issue #:** 3081
- **State:** closed
- **Created:** 2024-05-03T04:28:49Z
- **Updated:** 2025-04-22T19:15:38Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3081

### Problem Description

When installing hipblas-dev on Ubuntu using apt, the package installation should run ldconfig before completing.

We are testing building LocalAI using ROCm 6.1 based on an Ubuntu 22.04 image: rocm/dev-ubuntu-22.04:6.1.

Our build succeeds, but the execution fails with this error:

```
localai-1  | ./local-ai: error while loading shared libraries: libhipblas.so.2: cannot open shared object file: No such file or directory
```

We worked around the issue in our Dockerfile by manually calling ldconfig after the package installations, and were able to get everything running successfully.

This is due to the hipblas-dev package installation not running ldconfig, which is the [standard policy](https://www.debian.org/doc/debian-policy/ch-sharedlibs.html#ldconfig) when installing shared libraries.  Any AMD built deb package for Debian/Ubuntu should follow this policy:

```
Any such package must have the line activate-noawait ldconfig in its triggers control file (i.e. DEBIAN/triggers).
```
* /opt/rocm-6.1.0/lib isn't listed in /etc/ld.so.conf, it's in /etc/ld.so.conf.d.  However:
* If a file is added to  /etc/ld.so.conf.d/ and that location is included from /etc/ld.so.conf, it should follow this policy.
* /etc/ld.so.conf only has one line, and that is include /etc/ld.so.conf.d/*.conf, so anything in /etc/ld.so.conf.d/ is in /etc/ld.so.conf.
* If this is done as part of the package installation, it may not be needed as part of [post-installation instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/native-install/post-install.html).

### Operating System

Ubuntu 22.04 Jammy

### CPU

AMD Ryzen 7 7800X3D 8-Core Processor

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.1.0

### ROCm Component

hipBLAS

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_