# Cannot install on Ubuntu 22.04 with RC Kernel.

- **Issue #:** 1819
- **State:** closed
- **Created:** 2022-10-01T23:22:31Z
- **Updated:** 2024-02-08T16:37:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/1819

I get an error with `amdgpu-dkms` when trying to install with the linux RC kernel.

```
Hit:1 http://deb.debian.org/debian experimental InRelease
Hit:2 http://ca.archive.ubuntu.com/ubuntu jammy InRelease                                                                                                                                          
Hit:3 https://repo.steampowered.com/steam stable InRelease                                                                                                                                         
Get:4 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]                                                                                                           
Hit:5 https://repo.radeon.com/amdgpu/5.3/ubuntu jammy InRelease                                                                                                                      
Hit:6 https://repo.radeon.com/rocm/apt/5.3 jammy InRelease                                                                              
Get:7 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]                                                               
Get:8 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease [99.8 kB]                                               
Hit:9 https://ppa.launchpadcontent.net/cappelikan/ppa/ubuntu jammy InRelease                                                  
Hit:10 https://ppa.launchpadcontent.net/ubuntucinnamonremix/all/ubuntu jammy InRelease       
Fetched 324 kB in 1s (361 kB/s)                            
Reading package lists... Done
W: http://deb.debian.org/debian/dists/experimental/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
amdgpu-dkms is already the newest version (1:5.18.2.22.40.50300-1483871.22.04).
amdgpu-lib is already the newest version (1:5.3.50300-1483871.22.04).
linux-headers-6.0.0-rc7-amd64 is already the newest version (6.0~rc7-1~exp1).
rocm-hip-runtime is already the newest version (5.3.0.50300-63~22.04).
rocm-opencl-runtime is already the newest version (5.3.0.50300-63~22.04).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Setting up amdgpu-dkms (1:5.18.2.22.40.50300-1483871.22.04) ...
Removing old amdgpu-5.18.2.22.40-1483871.22.04 DKMS files...
Deleting module amdgpu-5.18.2.22.40-1483871.22.04 completely from the DKMS tree.
Loading new amdgpu-5.18.2.22.40-1483871.22.04 DKMS files...
Building for 6.0.0-rc7-amd64
Building for architecture x86_64
Building initial module for 6.0.0-rc7-amd64
ERROR (dkms apport): kernel package linux-headers-6.0.0-rc7-amd64 is not supported
Error! Bad return status for module build on kernel: 6.0.0-rc7-amd64 (x86_64)
Consult /var/lib/dkms/amdgpu/5.18.2.22.40-1483871.22.04/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

The RC kernel is the only one that supports bluetooth on the ASUS X670E board I am using.