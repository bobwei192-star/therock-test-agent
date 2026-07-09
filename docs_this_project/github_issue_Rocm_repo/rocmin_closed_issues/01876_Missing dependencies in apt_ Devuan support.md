# Missing dependencies in apt, Devuan support

- **Issue #:** 1876
- **State:** closed
- **Created:** 2022-12-13T18:42:40Z
- **Updated:** 2024-05-23T18:22:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1876

I tried installing AMD's GPU drivers on Devuan 4 (chimaera)  Linux, only to be met with a few issues.

First and foremost, I would like to mention that Devuan is a version of Debian that doesn't use SystemD to boot. Now, on to the issue.

I first started by going to the AMD support website, and downloading the Ubuntu (x86_64) deb file. After running an `apt install` on it, it installed `amdgpu-install` just fine. However, after running it, I got an error stating that the OS was unrecognized. After changing the /etc/os-release to match Debian Bullseye, I ran it again. It got further, but failed when it had unmet dependencies: 
```
Hit:1 https://dl.google.com/linux/chrome/deb stable InRelease
Hit:2 https://repo.radeon.com/amdgpu/5.4.1/ubuntu focal InRelease
Hit:3 https://repo.radeon.com/rocm/apt/5.4.1 focal InRelease
Get:4 http://pkgmaster.devuan.org/merged chimaera-security InRelease [26.2 kB]
Get:5 http://deb.devuan.org/merged chimaera InRelease [33.5 kB]                
Get:6 http://deb.devuan.org/merged chimaera-updates InRelease [26.1 kB]        
Get:7 http://pkgmaster.devuan.org/merged chimaera-security/non-free Sources [648 B]
Get:8 http://deb.devuan.org/merged chimaera/non-free Sources [81.4 kB]
Get:9 http://pkgmaster.devuan.org/merged chimaera-security/main Sources [122 kB]
Get:10 http://deb.devuan.org/merged chimaera/contrib Sources [43.3 kB]
Get:11 http://deb.devuan.org/merged chimaera/main Sources [8,612 kB]
Get:12 http://pkgmaster.devuan.org/merged chimaera-security/main amd64 Packages [210 kB]
Get:13 http://pkgmaster.devuan.org/merged chimaera-security/main i386 Packages [209 kB]
Get:14 http://pkgmaster.devuan.org/merged chimaera-security/main Translation-en [3,924 B]
Get:15 http://pkgmaster.devuan.org/merged chimaera-security/non-free amd64 Packages [544 B]
Get:16 http://pkgmaster.devuan.org/merged chimaera-security/non-free i386 Packages [540 B]
Get:17 http://deb.devuan.org/merged chimaera/main amd64 Packages [8,313 kB]    
Get:18 http://deb.devuan.org/merged chimaera/main i386 Packages [8,251 kB]     
Get:19 http://deb.devuan.org/merged chimaera/main Translation-en [6,480 kB]    
Get:20 http://deb.devuan.org/merged chimaera/contrib amd64 Packages [50.7 kB]  
Get:21 http://deb.devuan.org/merged chimaera/contrib i386 Packages [45.5 kB]   
Get:22 http://deb.devuan.org/merged chimaera/contrib Translation-en [46.9 kB]  
Get:23 http://deb.devuan.org/merged chimaera/non-free amd64 Packages [98.1 kB] 
Get:24 http://deb.devuan.org/merged chimaera/non-free i386 Packages [79.6 kB]  
Get:25 http://deb.devuan.org/merged chimaera/non-free Translation-en [91.3 kB] 
Get:26 http://deb.devuan.org/merged chimaera-updates/main Sources [4,848 B]    
Get:27 http://deb.devuan.org/merged chimaera-updates/main i386 Packages [15.1 kB]
Get:28 http://deb.devuan.org/merged chimaera-updates/main amd64 Packages [14.7 kB]
Get:29 http://deb.devuan.org/merged chimaera-updates/main Translation-en [7,933 B]
Fetched 32.9 MB in 20s (1,651 kB/s)                                            
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
linux-headers-5.10.0-19-amd64 is already the newest version (5.10.149-2).
linux-headers-5.10.0-19-amd64 set to manually installed.
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-llvm : Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable or
                      libstdc++-11-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable or
                      libgcc-11-dev but it is not installable
             Recommends: gcc-multilib but it is not going to be installed
             Recommends: g++-multilib but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```
This is as far as I have been able to get on my own. I have been trying to install drivers for an AMD RX 550 to work with Hashcat. Help is appreciated, thank you.