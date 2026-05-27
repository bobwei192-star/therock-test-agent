# files in /etc/ld.so.conf.d/ contain wrong paths

> **Issue #1156**
> **状态**: closed
> **创建时间**: 2020-06-21T18:06:21Z
> **更新时间**: 2020-06-24T23:47:55Z
> **关闭时间**: 2020-06-24T23:47:55Z
> **作者**: proailurus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1156

## 描述

System: openSUSE Tumbleweed, but should apply to SUSE too

During installation, ROCm packages will create files in /etc/ld.so.conf.d/, for example:
/etc/ld.so.conf.d/hsa-rocr-dev.conf

This file points to a nonexistent location:
```
$ cat hsa-rocr-dev.conf 
/opt/rocm/hsa/lib
```

/opt/rocm doesn't exist anymore, since all rocm stuff is in versioned folders like /opt/rocm-3.5.1 now.

---

## 评论 (2 条)

### 评论 #1 — ableeker (2020-06-23T17:40:03Z)

The installation guide tells us we can install the entire package, or a number of components, in a number of ways. If you install rocm-dkms, or rocm-dev, you're installing the complete package, and it will create the symlink /opt/rocm by itself. If you install some components, you can for instance just install rocm-opencl, it won't create /opt/rocm. In this case you'll have to create it yourself. You can install different versions of ROCM as well. If you do this, you'll also have to create /opt/rocm, and point it to the version you want to use.

In short, /opt/rocm should exist, or you'll have to create it yourself.

---

### 评论 #2 — proailurus (2020-06-24T23:47:55Z)

Thanks, I installed rocm-dev and it created the symlink.

---
