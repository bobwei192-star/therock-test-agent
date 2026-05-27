# Incorrect ROCm 5.5 install instructions

> **Issue #2399**
> **状态**: closed
> **创建时间**: 2023-08-23T17:47:58Z
> **更新时间**: 2023-08-24T17:35:28Z
> **关闭时间**: 2023-08-24T14:13:05Z
> **作者**: cgmb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2399

## 描述

Following the [ROCm 5.5 install instructions](https://rocm.docs.amd.com/en/docs-5.5.1/deploy/linux/installer/install.html) will result in installing ROCm 5.6.

For example:

```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.6/ubuntu/focal/amdgpu-install_5.6.50600-1_all.deb
sudo apt install ./amdgpu-install_5.6.50600-1_all.deb
```
