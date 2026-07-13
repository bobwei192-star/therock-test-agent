# [Issue]: ROCm Ubuntu 20.04 packages SHA256 changed

- **Issue #:** 4658
- **State:** closed
- **Created:** 2025-04-18T08:46:20Z
- **Updated:** 2025-04-22T07:16:59Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4658

### Problem Description

We use the ROCm Ubuntu 20.04 packages to build Nix derivations for ROCm. Since Nix requires that data fetched from the internet is a fixed-output, we store the SHA-256 of all packages:

https://github.com/huggingface/rocm-nix/blob/main/pkgs/rocm-packages/rocm-6.3.4-metadata.json

The sha256 checksums are retrieved directly from the package index (`Packages`) from the repository.

However, in the last few days, our builds started failing because the SHA256 hashes of a lot of ROCm 6.3.4 `-rpath` packages changed. Here is the diff:

https://gist.github.com/danieldk/2e75f947c2eaf0953d6f2a2377d96893

Were the packages updated in-place without bumping up the package revision or were they compromised? I inspected one of the packages and could not find anything suspect after a quick look, but wanted to check.

### Operating System

Ubuntu 20.04 (Focal Fossa)

### CPU

AMD EPYC 7R13 Processor

### GPU

None

### ROCm Version

6.3.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_