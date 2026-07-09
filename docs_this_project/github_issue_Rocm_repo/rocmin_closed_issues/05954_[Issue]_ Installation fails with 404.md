# [Issue]: Installation fails with 404

- **Issue #:** 5954
- **State:** closed
- **Created:** 2026-02-11T16:39:32Z
- **Updated:** 2026-04-15T19:14:15Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5954

### Problem Description

I use Github actions to build packages for my software.  It runs inside a manylinux_2_34_x86_64 image.  I build versions for both ROCm 6 and 7.  Here are the steps that install it.

```yaml
- name: "Install HIP 6"
  if: matrix.hip-version == '6'
  run: |
    yum install -y epel-release
    yum install -y https://repo.radeon.com/amdgpu-install/6.4.4/el/9.6/amdgpu-install-6.4.60404-1.el9.noarch.rpm
    yum install -y rocm-device-libs hip-devel hip-runtime-amd hipcc

- name: "Install HIP 7"
  if: matrix.hip-version == '7'
  run: |
    yum install -y epel-release
    yum install -y https://repo.radeon.com/amdgpu-install/7.0.1/el/9.6/amdgpu-install-7.0.1.70001-1.el9.noarch.rpm
    yum install -y rocm-device-libs hip-devel hip-runtime-amd hipcc
```

This worked when I built my previous release 2.5 months ago, but now it fails.  Here is the complete output from that step.

```
Last metadata expiration check: 0:01:40 ago on Wed 11 Feb 2026 03:38:41 PM UTC.
Package epel-release-9-10.el9.noarch is already installed.
Dependencies resolved.
Nothing to do.
Complete!
Last metadata expiration check: 0:01:41 ago on Wed 11 Feb 2026 03:38:41 PM UTC.
amdgpu-install-6.4.60404-1.el9.noarch.rpm        84 kB/s |  25 kB     00:00    
Dependencies resolved.
================================================================================
 Package            Arch       Version                   Repository        Size
================================================================================
Installing:
 amdgpu-install     noarch     6.4.60404-2202139.el9     @commandline      25 k
Installing dependencies:
 rsync              x86_64     3.2.5-3.el9               baseos           404 k
Installing weak dependencies:
 dialog             x86_64     1.3-32.20210117.el9       appstream        239 k

Transaction Summary
================================================================================
Install  3 Packages

Total size: 668 k
Total download size: 643 k
Installed size: 1.4 M
Downloading Packages:
(1/2): dialog-1.3-32.20210117.el9.x86_64.rpm    2.5 MB/s | 239 kB     00:00    
(2/2): rsync-3.2.5-3.el9.x86_64.rpm             3.3 MB/s | 404 kB     00:00    
--------------------------------------------------------------------------------
Total                                           3.4 MB/s | 643 kB     00:00     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                        1/1 
  Installing       : rsync-3.2.5-3.el9.x86_64                               1/3 
  Installing       : dialog-1.3-32.20210117.el9.x86_64                      2/3 
  Installing       : amdgpu-install-6.4.60404-2202139.el9.noarch            3/3 
  Running scriptlet: amdgpu-install-6.4.60404-2202139.el9.noarch            3/3 
  Verifying        : dialog-1.3-32.20210117.el9.x86_64                      1/3 
  Verifying        : rsync-3.2.5-3.el9.x86_64                               2/3 
  Verifying        : amdgpu-install-6.4.60404-2202139.el9.noarch            3/3 

Installed:
  amdgpu-install-6.4.60404-2202139.el9.noarch dialog-1.3-32.20210117.el9.x86_64
  rsync-3.2.5-3.el9.x86_64                   

Complete!
ROCm 6.4.4 repository                           3.5 MB/s | 600 kB     00:00    
AMDGPU 6.4.4 repository                         5.7 kB/s | 562  B     00:00    
Errors during downloading metadata for repository 'amdgpu':
  - Status code: 404 for https://repo.radeon.com/amdgpu/6.4.4/el/9.7/main/x86_64/repodata/repomd.xml (IP: 23.218.216.204)
Error: Failed to download metadata for repo 'amdgpu': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
```

It successfully downloads the package I specify by URL, which comes from the directory `6.4.4/el/9.6`.  But it then tries to get additional packages from the nonexistent directory `6.4.4/el/9.7`.  The same thing happens with the ROCm 7 package with the error

```
   - Status code: 404 for https://repo.radeon.com/amdgpu/30.10.1/el/9.7/main/x86_64/repodata/repomd.xml (IP: 2.21.9.228)
```

### Operating System

manylinux_2_34_x86_64

### CPU

Unknown (Github actions runner)

### GPU

None

### ROCm Version

6.4.4 and 7.0.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_