# [Issue]: build script breaks the host system

- **Issue #:** 4752
- **State:** closed
- **Created:** 2025-05-19T05:36:58Z
- **Updated:** 2025-06-10T03:37:26Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4752

### Problem Description

The build makefile `make -f ROCm/tools/rocm-build/ROCm.mk ...` and the individual makefiles launched form it make various assumptions that break the host system:

1. the build makes frequent use of `sudo` to alter the system.
This _might_ be fine in a throw-away container, though it is a bad approach and a symptom of lack of separation between the preparation of the environment, the build process, and the install process.
It is a _terrible_ approach when used on a non-containerised system:
  - if the user does not have `sudo` rights, the process will fail
  - worse, if the user _does have_ `sudo` rights, it will alter the host system; see for example the use of `sudo chown ... /opt`.
The build system should decouple the "build" part, that should happen by a non-`root` process in a non-`root` owned directory, and the "install" process, that _may_ be invoked by a `root` user to install under `/opt`. In any case it should not try to call `sudo` itself.

2. (some of) the build ignores the `$CCACHE_DIR` environment variable and overrides it with `$HOME/.ccache`.
This leads to much worse performance (and possible other issues) on a system where the `$HOME` is on a network filesystem.

3. the build does not let the user specify the install directory. Instead, it assumes that the installation will always be in `/opt/rocm-6.4.0` (or other version).
This breaks many uses cases where a user would install ROCm in a user-specified, non -system directory.
One example is the utilisation on the LUMI supercomputer.

### Operating System

any

### CPU

any

### GPU

any

### ROCm Version

6.4.0

### ROCm Component

_No response_

### Steps to Reproduce

Follow the instructions at https://github.com/ROCm/ROCm/blob/rocm-6.4.0/README.md#build-rocm-from-source , in particular the "Option 2" to use the host system.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_