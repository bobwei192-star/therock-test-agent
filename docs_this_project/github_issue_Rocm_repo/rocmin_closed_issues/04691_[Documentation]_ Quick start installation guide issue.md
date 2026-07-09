# [Documentation]: Quick start installation guide issue

- **Issue #:** 4691
- **State:** closed
- **Created:** 2025-04-27T12:37:11Z
- **Updated:** 2025-04-29T13:52:35Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4691

### Description of errors

On the [quick installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) for ROCm with Ubuntu 22.04 

The script :
`wget https://repo.radeon.com/amdgpu-install/6.4/ubuntu/jammy/amdgpu-install_6.4.60400-1_all.deb
sudo apt install ./amdgpu-install_6.4.60400-1_all.deb
sudo apt update
sudo apt install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo apt install rocm`

Return an error :
`Err:7 https://repo.radeon.com/rocm/apt/6.4.0 jammy Release
  404  Not Found`


Had to edit : `/etc/apt/sources.list.d/rocm.list` 


Replaced:
`deb https://repo.radeon.com/rocm/apt/6.4.0 jammy main`

by:
`deb https://repo.radeon.com/rocm/apt/6.4 jammy main`

To get it to work





### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_