# [Issue]: Can't install rocm 6.2.4

- **Issue #:** 4022
- **State:** closed
- **Created:** 2024-11-09T19:11:20Z
- **Updated:** 2024-11-12T18:31:15Z
- **Labels:** Under Investigation, ROCm 6.2.3, N/A
- **URL:** https://github.com/ROCm/ROCm/issues/4022

### Problem Description

The repository InRelease indices for ROCm 6.2.4 appear to be inconsistent with Release artifacts as of 2024-11-09 1900Z. This issue applies to "noble", "focal", and "jammy".

Note — I had to set the ROCm Version field to `ROCm 6.2.3` because there was no option for `ROCm 6.2.4`.

### Operating System

Ubuntu 24.04.1 LTS (Noble Numbat) 

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 6.2.3

### ROCm Component

_No response_

### Steps to Reproduce

```bash
$ echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/6.2.4 noble main"     | sudo tee --append /etc/apt/sources.list.d/rocm.list
$ sudo apt update
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

```bash
$ sudo apt update
...
Get:5 https://repo.radeon.com/rocm/apt/6.2.4 noble/main amd64 Packages [29.6 kB]
Err:5 https://repo.radeon.com/rocm/apt/6.2.4 noble/main amd64 Packages
  File has unexpected size (68560 != 29552). Mirror sync in progress? [IP: 69.192.139.240 443]
  Hashes of expected file:
   - Filesize:29552 [weak]
   - SHA256:5cba5765fe11410ac7a3679e5c8b2eab8c2e294971d8a9e4267c8784b746f21c
   - SHA1:53982ce2011f79dedaf8a5a69c361b8825fea447 [weak]
   - MD5Sum:d55fc8f653990ff0a080cdb20e55fc22 [weak]
  Release file created at: Wed, 06 Nov 2024 18:36:13 +0000
Hit:6 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:7 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Fetched 2617 B in 1s (3549 B/s)
Reading package lists... Done
E: Failed to fetch https://repo.radeon.com/rocm/apt/6.2.4/dists/noble/main/binary-amd64/Packages.gz  File has unexpected size (68560 != 29552). Mirror sync in progress? [IP: 69.192.139.240 443]
   Hashes of expected file:
    - Filesize:29552 [weak]
    - SHA256:5cba5765fe11410ac7a3679e5c8b2eab8c2e294971d8a9e4267c8784b746f21c
    - SHA1:53982ce2011f79dedaf8a5a69c361b8825fea447 [weak]
    - MD5Sum:d55fc8f653990ff0a080cdb20e55fc22 [weak]
   Release file created at: Wed, 06 Nov 2024 18:36:13 +0000
```

https://repo.radeon.com/rocm/apt/6.2.4/dists/noble/Release
```text
Origin: repo.radeon.com
Label: repo.radeon.com
Suite: noble
Codename: noble
Version: 6.2.4
Date: Fri, 08 Nov 2024 18:58:55 UTC
Architectures: amd64
Components: main proprietary
Description: ROCm APT Repository
MD5Sum:
 3e929ad7bef77ab769bdcc7cb2e921fe 351040 main/binary-amd64/Packages
 46d07f487bf91c2cb2ab321a7b96178a 68560 main/binary-amd64/Packages.gz
```

https://repo.radeon.com/rocm/apt/6.2.4/dists/noble/InRelease
```text
Origin: repo.radeon.com
Label: repo.radeon.com
Suite: noble
Codename: noble
Version: 6.2.4
Date: Wed, 06 Nov 2024 18:36:13 UTC
Architectures: amd64
Components: main proprietary
Description: ROCm APT Repository
MD5Sum:
 292daa54c9cacecd4d8915fbdee83897 111626 main/binary-amd64/Packages
 d55fc8f653990ff0a080cdb20e55fc22 29552 main/binary-amd64/Packages.gz
```

See also #3980 .