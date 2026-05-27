# GPG issue on ubuntu

> **Issue #2362**
> **状态**: closed
> **创建时间**: 2023-08-02T21:40:21Z
> **更新时间**: 2023-12-11T22:39:32Z
> **关闭时间**: 2023-12-11T22:39:32Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2362

## 负责人

- Naraenda

## 描述

I followed https://rocm.docs.amd.com/en/latest/deploy/linux/os-native/install.html to re-add key but I keep getting
```
The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
```
I tried to verify the key and got
```
sha1sum /etc/apt/keyrings/rocm.gpg 
ececf5eea22ced391975f46ba3e11ad58a12c794  /etc/apt/keyrings/rocm.gpg
```
which is different from 73f5d8100de6048aa38a8b84cd9a87f05177d208 mentioned in https://rocm.docs.amd.com/en/latest/deploy/linux/os-native/install.html

How to fix this?

