# Bump versions of Ubuntu deb packages with new ROCm versions

> **Issue #1354**
> **状态**: closed
> **创建时间**: 2020-12-30T14:06:50Z
> **更新时间**: 2021-01-05T05:53:37Z
> **关闭时间**: 2021-01-05T05:52:35Z
> **作者**: t-vi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1354

## 描述

The Ubuntu deb packages change while retaining the same version, e.g. for `llvm-amdgpu` for ROCm 4.0, which is unchanged at 12.0dev from ROCm 3.10 (at least).
Now, you officially instruct  to remove ROCm and reinstall but people *do* upgrade and then end with [seemingly missing bits](https://discuss.pytorch.org/t/setup-py-says-use-rocm-off-while-i-set-use-rocm-1/107141/2). These stem from llvm-amdgpu remaining at the 3.10 version when the rest is in 4.0. When one forces reinstallation through  `apt-get install --reinstall llvm-amdgpu`, things work again.
A proper fix would be if you could make sure that the libraries have strictly increasing version numbers from release to release (e.g. by adding `+rocm-4.0` to the version, e.g. `12.0dev+rocm-4.0`would be a very good way and very similar to what Debian does when they want to upgrade through rebuilds).
Thank you!


---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-01-04T12:26:27Z)

Thanks @t-vi for reaching out.
I will check and get back to you asap.

---

### 评论 #2 — ROCmSupport (2021-01-05T05:52:35Z)

Hi @t-vi 
The issue is with a few set of packages like llvm-amdgpu, hipify-clang etc. which are missing proper package versions, which we are already aware. Hence we requested to do a clean install instead of upgrade.
The naming for all other packages are perfect as per debian standards and also follows standard structure.

Now the conclusion is: we have unified the package naming for all packages now and the changes are integrated for our internal builds, which are going through some validation now.
The same will be available from next upcoming releases.
Please stay tuned for the changes/fix.
Thank you.

---
