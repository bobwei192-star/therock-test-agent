# [Issue]: ROCm apt repo (noble) out of sync: Packages.gz size/hash

- **Issue #:** 6317
- **State:** closed
- **Created:** 2026-05-30T16:09:25Z
- **Updated:** 2026-06-01T20:00:18Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6317

### Problem Description

Reading package lists... Done
N: Repository 'https://repo.radeon.com/rocm/apt/latest noble InRelease' changed its 'Version' value from '7.2.3' to '7.2.4'
N: Repository 'https://repo.radeon.com/graphics/latest/ubuntu noble InRelease' changed its 'Version' value from '7.2.3' to '7.2.4'
E: Failed to fetch https://repo.radeon.com/rocm/apt/latest/dists/noble/main/binary-amd64/Packages.gz  File has unexpected size (61315 != 61300). Mirror sync in progress? [IP: 2600:1408:c400:e::17cd:6a0c 443]
   Hashes of expected file:
    - Filesize:61300 [weak]
    - SHA256:ca9ce1e681e736592a8dc8a7309a2ef5e0a71b7152da450de4dc672a3ce62e6e
    - SHA1:cdb95b9ddb892133dfa5eeb8d7e7d3044da9e81a [weak]
    - MD5Sum:0f88be93cc8847d24dbdbcb64c174684 [weak]
   Release file created at: Tue, 26 May 2026 01:25:03 +0000
E: Failed to fetch https://repo.radeon.com/graphics/latest/ubuntu/dists/noble/main/binary-amd64/Packages.gz  File has unexpected size (10341 != 10344). Mirror sync in progress? [IP: 2600:1408:c400:e::17cd:6a0c 443]
   Hashes of expected file:
    - Filesize:10344 [weak]
    - SHA256:278eb2c2518b925fb4200a14c455ef033a719657fabd61d14cbb03a2b6fc7475
    - SHA1:c454242eb7f143c1138a4a72dccf4e4d19287b2c [weak]
    - MD5Sum:344412491dda851b621faf6dd058dfd8 [weak]
   Release file created at: Tue, 26 May 2026 07:58:35 +0000
E: Some index files failed to download. They have been ignored, or old ones used instead.

### Operating System

Linux Mint 22.3

### CPU

AMD Ryzen 7 7700X

### GPU

AMD Radeon RX 7800 XT

### ROCm Version

7.2.3

### ROCm Component

_No response_

### Steps to Reproduce

Running apt update with repository sources set to:

deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/latest noble main
deb [arch=amd64,i386 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/graphics/latest/ubuntu noble main

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Repo update hash errors occurring since 5/29