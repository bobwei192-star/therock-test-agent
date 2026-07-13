# [Issue]: `/opt/rocm/bin/hipcc` and `/opt/rocm/bin/hipconfig` have the same sha256 checksum

- **Issue #:** 5054
- **State:** closed
- **Created:** 2025-07-16T15:38:51Z
- **Updated:** 2025-08-28T13:47:33Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5054

### Problem Description

Hi,

As per tile.

Repro: `docker run -it --rm --device /dev/kfd --device /dev/dri --security-opt seccomp=unconfined --shm-size=64g --net host rocm/dev-ubuntu-22.04:6.4.1 /bin/bash`

And:

```bash
sha256sum /opt/rocm/bin/hipconfig
sha256sum /opt/rocm/bin/hipcc
```

yielding the same:
```
a2e73caf4d75e85960ea4fd6cac9012eb91d2a60facb26d4ec8b23921ca1add1  /opt/rocm/bin/hipconfig
a2e73caf4d75e85960ea4fd6cac9012eb91d2a60facb26d4ec8b23921ca1add1  /opt/rocm/bin/hipcc
```

although these two binaries should be different, and e.g. `hipcc --version` and `hipconfig --version` produce a different output.

`ls -la /opt/rocm/bin` shows that these two are not symlinks or hard links.

### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 9554 64-Core Processor

### GPU

AMD Instinct MI300X

### ROCm Version

6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_