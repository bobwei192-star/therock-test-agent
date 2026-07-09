# I can't install ROCm v4.3 on Kali Linux Kernel 5.10.0-kali9-amd64

- **Issue #:** 1582
- **State:** closed
- **Created:** 2021-10-05T12:38:37Z
- **Updated:** 2021-10-05T13:34:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/1582

I want to install ROCm for my AMD GPU (5700XT) and use Hashcat on Kali Linux.
Hashcat requirements: AMD GPU ROCm v3.3 and above.

I followed this guide that show you how to do it on Ubuntu (Debian). I failed to install ROCm after all the gpg.key and the sudo update. I used the v4.3 Ubuntu release.

    ──(kali㉿kali)-[~]
    └─$ sudo apt-get update
    Hit:1 http://kali.cs.nctu.edu.tw/kali kali-rolling InRelease          
    Hit:2 https://repo.radeon.com/rocm/apt/4.3 ubuntu InRelease
    Reading package lists... Done
    
    ┌──(kali㉿kali)-[~]
    └─$ sudo apt install rocm-dkms               
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    Some packages could not be installed. This may mean that you have
    requested an impossible situation or if you are using the unstable
    distribution that some required packages have not yet been created
    or been moved out of Incoming.
    The following information may help to resolve the situation:
    
    The following packages have unmet dependencies:
     llvm-amdgpu : Depends: libstdc++-5-dev but it is not installable or
                            libstdc++-7-dev but it is not installable
                   Depends: libgcc-5-dev but it is not installable or
                            libgcc-7-dev but it is not installable
                   Recommends: gcc-multilib but it is not going to be installed
                   Recommends: g++-multilib but it is not going to be installed
     openmp-extras : Depends: libstdc++-5-dev but it is not installable or
                              libstdc++-7-dev but it is not installable
                     Depends: libgcc-5-dev but it is not installable or
                              libgcc-7-dev but it is not installable
     rocm-gdb : Depends: libpython3.8 but it is not installable
    E: Unable to correct problems, you have held broken packages.

Sources: 
Guide 
https://rocmdocs.amd.com/en/latest/Archived_Documentation/4_1_Installation_Guide.html