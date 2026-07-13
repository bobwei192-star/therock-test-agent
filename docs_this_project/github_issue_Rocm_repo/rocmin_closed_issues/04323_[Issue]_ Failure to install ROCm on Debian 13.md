# [Issue]: Failure to install ROCm on Debian 13

- **Issue #:** 4323
- **State:** closed
- **Created:** 2025-01-31T20:19:54Z
- **Updated:** 2025-10-18T17:39:46Z
- **Labels:** 6.3.1, AMD Radeon RX 7800 XT
- **URL:** https://github.com/ROCm/ROCm/issues/4323

### Problem Description

I was a Debian 12 user who recently bought an RX 7800 XT. Version 6.1 of the kernel was too old for this, so I decided to upgrade to Debian 13 (trixie). 

I was hoping to install ROCm. I tried to go through the instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.3.1/install/quick-start.html) (hoping they'd work for 13 as well as they presumably work for 12) but I was scuppered by this:

```
$ sudo apt install amdgpu-dkms rocm
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

Unsatisfied dependencies:
 rocm-llvm : Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable or
                      libstdc++-11-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable or
                      libgcc-11-dev but it is not installable
             Recommends: gcc-multilib but it is not going to be installed
             Recommends: g++-multilib but it is not going to be installed
```

This is related to https://github.com/ROCm/ROCm/issues/4272, but approached differently.

### Operating System

Debian 13 (trixie)

### CPU

AMD Ryzen 9 5950X

### GPU

AMD Radeon RX 7800 XT

### ROCm Version

6.3.1

### ROCm Component

_No response_

### Steps to Reproduce

On Debian 13:

```
sudo apt update
sudo apt install "linux-headers-$(uname -r)"
sudo apt install -y python3-setuptools python3-wheel libpython3.11
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
wget https://repo.radeon.com/amdgpu-install/6.3.1/ubuntu/jammy/amdgpu-install_6.3.60301-1_all.deb
sudo apt install ./amdgpu-install_6.3.60301-1_all.deb
sudo apt update
sudo apt install amdgpu-dkms rocm
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_