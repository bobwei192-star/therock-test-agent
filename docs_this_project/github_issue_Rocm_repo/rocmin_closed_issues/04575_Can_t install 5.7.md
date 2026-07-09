# Can't install 5.7

- **Issue #:** 4575
- **State:** closed
- **Created:** 2025-04-08T17:30:27Z
- **Updated:** 2025-04-10T16:04:07Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4575

So I am trying to do a multi install on Ubuntu 22.04 (Jammy).

6.3.3 will install fine, but if I use `sudo apt install rocm5.7` then it can't find the package.

The following doesn't work either;
```
for ver in 6.3.3 5.7; do
    sudo apt install rocm$ver
done
```
If I remove the 6.3.3 from above, it still won't find 5.7

Here's my rocm.list file
```
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/6.3.3 jammy main
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/5.7 jammy main
```


Here is what I see if I type in `sudo apt update`
```
Hit:1 https://repo.radeon.com/amdgpu/6.3.3/ubuntu jammy InRelease
Hit:2 http://gb.archive.ubuntu.com/ubuntu jammy InRelease           
Hit:3 http://gb.archive.ubuntu.com/ubuntu jammy-updates InRelease                                                
Hit:4 https://esm.ubuntu.com/apps/ubuntu jammy-apps-security InRelease                                           
Hit:5 http://gb.archive.ubuntu.com/ubuntu jammy-backports InRelease                                              
Hit:6 https://esm.ubuntu.com/apps/ubuntu jammy-apps-updates InRelease                                            
Hit:7 https://esm.ubuntu.com/infra/ubuntu jammy-infra-security InRelease
Hit:8 http://security.ubuntu.com/ubuntu jammy-security InRelease    
Hit:9 https://esm.ubuntu.com/infra/ubuntu jammy-infra-updates InRelease
Hit:10 https://repo.radeon.com/rocm/apt/6.3.3 jammy InRelease
Hit:11 https://repo.radeon.com/rocm/apt/5.7 jammy InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
3 packages can be upgraded. Run 'apt list --upgradable' to see them.
```