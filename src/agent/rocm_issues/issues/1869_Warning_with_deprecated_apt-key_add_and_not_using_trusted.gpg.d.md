# Warning with deprecated apt-key add and not using trusted.gpg.d

> **Issue #1869**
> **状态**: closed
> **创建时间**: 2022-11-29T16:36:49Z
> **更新时间**: 2024-02-01T20:59:42Z
> **关闭时间**: 2024-02-01T20:59:42Z
> **作者**: danielzgtg
> **标签**: Verified Issue, 5.3.0, Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1869

## 标签

- **Verified Issue** (颜色: #0052cc)
- **5.3.0** (颜色: #fbca04)
- **Documentation** (颜色: #5319e7)

## 负责人

- frepaul

## 描述

`apt-key add` is deprecated.

# Expected Behavior

The documentation should not suggest `wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -` at https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.3/page/How_to_Install_ROCm.html . I should not see any warning when adding or when running `apt update`. The key should be in `trusted.gpg.d` not `trusted.gpg`. This improves security by ensuring the key is not accidentally used for other repositories.

Something new like whatever `add-apt-repository` does should be used.

# Actual Behavior

```
# apt update
Hit:1 [...]
Fetched 48.9 kB in 1s (33.5 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
7 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: https://repo.radeon.com/amdgpu/22.10/ubuntu/dists/focal/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
W: https://repo.radeon.com/rocm/apt/5.3/dists/focal/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
```

---

## 评论 (1 条)

### 评论 #1 — abhimeda (2024-01-30T04:06:28Z)

@danielzgtg  Hi, can we close this ticket?

---
