# Installation of DKMS failed on clean Ubuntu 18.04

- **Issue #:** 660
- **State:** closed
- **Created:** 2019-01-03T15:33:55Z
- **Updated:** 2019-01-08T00:03:08Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/660

I tried installing ROCm 2.0 following instructions here (https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository) and failed.

I have run upgrade to get latest packages and it is clean Ubuntu installation for the sole purpose of using ROCm (never tried it previously). I have kernel 4.15.0-43-generic and Radeon RX 580. 

Here is the terminal output: [https://pastebin.com/W7CLmfvE](url)

dkms status outputs this:
`amdgpu, 2.0-89, 4.15.0-43-generic, x86_64: built`

(after I run the install again & it failed with same output.. Before, dkms status showed this:
`amdgpu, 2.0-89: added`)