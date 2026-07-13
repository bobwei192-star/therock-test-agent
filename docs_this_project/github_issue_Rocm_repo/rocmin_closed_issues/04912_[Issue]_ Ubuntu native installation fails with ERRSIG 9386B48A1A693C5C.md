# [Issue]: Ubuntu native installation fails with ERRSIG 9386B48A1A693C5C

- **Issue #:** 4912
- **State:** closed
- **Created:** 2025-06-10T20:27:50Z
- **Updated:** 2025-06-17T17:25:22Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4912

### Problem Description

I am trying to install the ROCm via [the following guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager/package-manager-ubuntu.html).

```
OS:
NAME="Ubuntu"
VERSION="25.10 (Questing Quokka)"
```

```
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null
sha1sum /etc/apt/keyrings/rocm.gpg
```
> ececf5eea22ced391975f46ba3e11ad58a12c794

```
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/6.4.1 noble main" | sudo tee /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt update
```
> Get:4 https://repo.radeon.com/rocm/apt/6.4.1 noble InRelease [2,605 B]                                                                  
> Err:4 https://repo.radeon.com/rocm/apt/6.4.1 noble InRelease                                                                           
>   The following signatures were invalid: ERRSIG 9386B48A1A693C5C

I've tried `sudo gpg --keyserver keyserver.ubuntu.com --recv-keys 9386B48A1A693C5C`, but nothing changed.

### Operating System

Ubuntu 25.10 (Questing Quokka)

### CPU

AMD Ryzen 7 5700G with Radeon Graphics

### GPU

AMD RX 7600 XT

### ROCm Version

ROCM 6.4.1
