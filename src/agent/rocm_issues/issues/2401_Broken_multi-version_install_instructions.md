# Broken multi-version install instructions

> **Issue #2401**
> **状态**: closed
> **创建时间**: 2023-08-23T19:27:09Z
> **更新时间**: 2023-09-20T13:29:21Z
> **关闭时间**: 2023-09-20T13:29:21Z
> **作者**: cgmb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2401

## 负责人

- Naraenda

## 描述

[The commands given to install multiple repositories](https://rocm.docs.amd.com/en/docs-5.5.1/deploy/linux/installer/install.html#add-required-repositories) are wrong:

```bash
for ver in 5.3.3 5.4.3; do
echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/$ver focal main" | sudo tee /etc/apt/sources.list.d/rocm.list
done
```
Each call to `echo <...> | sudo tee /etc/apt/sources.list.d/rocm.list` will truncate the file, so only the last version specified will be included in `rocm.list`.
