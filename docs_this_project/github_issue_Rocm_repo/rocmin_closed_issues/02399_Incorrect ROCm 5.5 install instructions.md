# Incorrect ROCm 5.5 install instructions

- **Issue #:** 2399
- **State:** closed
- **Created:** 2023-08-23T17:47:58Z
- **Updated:** 2023-08-24T17:35:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/2399

Following the [ROCm 5.5 install instructions](https://rocm.docs.amd.com/en/docs-5.5.1/deploy/linux/installer/install.html) will result in installing ROCm 5.6.

For example:

```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.6/ubuntu/focal/amdgpu-install_5.6.50600-1_all.deb
sudo apt install ./amdgpu-install_5.6.50600-1_all.deb
```