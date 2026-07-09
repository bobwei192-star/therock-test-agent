# [Issue]: ROCm apt repo (noble) out of sync: Packages.gz size/hash mismatch for multiple days (again)

- **Issue #:** 6070
- **State:** closed
- **Created:** 2026-03-26T15:12:46Z
- **Updated:** 2026-03-26T18:42:17Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6070

### Problem Description

```
E: Failed to fetch https://repo.radeon.com/rocm/apt/debian/dists/noble/main/binary-amd64/Packages.gz  File has unexpected size (61330 != 60911). Mirror sync in progress? [IP: 2a02:26f0:fd00:15::213:a1a8 443]
   Hashes of expected file:
    - Filesize:60911 [weak]
    - SHA256:a21e883477e4f1b79c31c9334e86c88ab3db5811922331fddd81e493666e0406
    - SHA1:f5468913de65867b9181d16ce56a5dad84272f4b [weak]
    - MD5Sum:5c1137d1ebf2fa64c71ad64904f4ce61 [weak]
   Release file created at: Tue, 13 Jan 2026 02:19:55 +0000
E: Some index files failed to download. They have been ignored, or old ones used instead.
```


### Operating System

Ubuntu 26.04

### CPU

Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz

### GPU

Advanced Micro Devices, Inc. [AMD/ATI] Navi 33 [Radeon Pro W7500]

### ROCm Version

7.2.1

### ROCm Component

_No response_

### Steps to Reproduce

Attempt to "apt update" with repo source set to:

URIs: https://repo.radeon.com/rocm/apt/debian
Suites: noble
Architectures: amd64
Components: main proprietary



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

This seems to pop up regularly. There are past tickets opened for the same Packages.gz size mismatch issue across various directories

Perhaps an automated check would be a good idea?
