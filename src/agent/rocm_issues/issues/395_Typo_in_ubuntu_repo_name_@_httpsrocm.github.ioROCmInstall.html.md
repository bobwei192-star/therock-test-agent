# Typo in ubuntu repo name @  https://rocm.github.io/ROCmInstall.html

> **Issue #395**
> **状态**: closed
> **创建时间**: 2018-04-25T21:42:14Z
> **更新时间**: 2018-04-25T21:45:20Z
> **关闭时间**: 2018-04-25T21:45:20Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/395

## 描述

    wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
    sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'

should be

    wget -qO - http://repo.radeon.com/rocm/apt/debian/debian/rocm.gpg.key | sudo apt-key add -
    sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
