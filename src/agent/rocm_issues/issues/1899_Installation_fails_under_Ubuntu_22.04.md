# Installation fails under Ubuntu 22.04

> **Issue #1899**
> **状态**: closed
> **创建时间**: 2023-02-01T10:41:10Z
> **更新时间**: 2023-11-10T16:41:02Z
> **关闭时间**: 2023-11-10T16:41:02Z
> **作者**: upsj
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1899

## 描述

Running
```bash
echo "deb [arch=amd64] http://repo.radeon.com/rocm/apt/5.4 jammy main" > /etc/apt/sources.list.d/rocm.list
curl https://repo.radeon.com/rocm/rocm.gpg.key > /etc/apt/trusted.gpg.d/repo.radeon.com.asc
apt-get update
apt-get install -y rocm-hip-sdk
```
in a Ubuntu 22.04 docker image leads to the following error
```
The following packages have unmet dependencies:
 rocm-hip-runtime : Depends: rocminfo (= 1.0.0.50400-72~22.04) but 5.0.0-1 is to be installed
 rocm-hip-runtime-dev : Depends: rocm-device-libs (= 1.0.0.50400-72~22.04) but 5.0.0-1 is to be installed
                        Depends: rocm-cmake (= 0.8.0.50400-72~22.04) but 5.0.0-1 is to be installe
```

---

## 评论 (3 条)

### 评论 #1 — freechelmi (2023-03-02T14:47:54Z)

Had the same on 22.04.2 , just remove rocminfo first

---

### 评论 #2 — MSLaaf (2023-06-19T20:23:40Z)

Had the same on Linux Mint 21.1 Vera, remove rocminfo too


---

### 评论 #3 — kentrussell (2023-11-10T16:41:02Z)

Removing existing rocminfo should be sufficient. Also newer install scripts will help to mitigate this failuire.

---
