# Add HIP-Language support to "Using CMake" page

> **Issue #1957**
> **状态**: closed
> **创建时间**: 2023-03-16T14:26:37Z
> **更新时间**: 2023-05-17T13:07:24Z
> **关闭时间**: 2023-05-17T13:07:24Z
> **作者**: skyreflectedinmirrors
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1957

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- pfultz2
- cgmb
- skyreflectedinmirrors
- lawruble13
- MathiasMagnus
- nunnikri

## 描述

Main points are:

- Requires CMake >= 3.21
- CMAKE_HIP_COMPILER=clang++ (in place of CMAKE_CXX_COMPILER=hipcc)
- Suffix of HIP files is '.hip', or use `source_files_properties` + `LANGUAGE hip` (https://cmake.org/cmake/help/latest/command/set_source_files_properties.html)
- Brief discussion of hip-lang:: targets

I can help contribute here, @saadrahim 

---

## 评论 (9 条)

### 评论 #1 — saadrahim (2023-03-16T15:11:58Z)

Assigned this issue to a few people who may have opinions on this matter. Let's work on a expanding this topic. It would be great if @arghdos you can take the lead on this.

---

### 评论 #2 — cgmb (2023-03-16T18:22:04Z)

> Requires CMake >= 3.21

Requires CMake 3.21.3. While HIP language support was added in 3.21.0, it worked a bit differently. The versions 3.21.0, 3.21.1 and 3.21.2 had a lot of gotchas and should be avoided.

> CMAKE_HIP_COMPILER=clang++ (in place of CMAKE_CXX_COMPILER=hipcc)

Yup. Or, the environment variable `HIPCXX=clang++` in place of `CXX=hipcc`.

> Suffix of HIP files is '.hip', or use source_files_properties + LANGUAGE hip (https://cmake.org/cmake/help/latest/command/set_source_files_properties.html)

Yup.

> Brief discussion of hip-lang:: targets

That would be good. I don't know anything about them.

---

### 评论 #3 — pfultz2 (2023-03-16T18:28:45Z)

> Brief discussion of hip-lang:: targets

The hip-lang:: targets aren't meant to be used directly by users. Its only for kitware to get the flags needed for hip compilation.

---

### 评论 #4 — skyreflectedinmirrors (2023-03-16T21:15:52Z)

>The hip-lang:: targets aren't meant to be used directly by users. Its only for kitware to get the flags needed for hip compilation.

We actually had a user ask about that recently (specifically, hip-lang::host on anything that isn't considered 'HIP' language gets ignored), so it would be great to write that down!

---

### 评论 #5 — ye-luo (2023-03-16T21:24:30Z)

Also point user to do `find_package(hip CONFIG)` if hip runtime library is used in non-HIP host code.

---

### 评论 #6 — cgmb (2023-03-17T21:52:12Z)

It's a bit tangential to this topic, but the HIP Language support in CMake does not yet work for distro-provided packages. That may surprise people. For anyone interested, the bug is https://gitlab.kitware.com/cmake/cmake/-/issues/24562.

---

### 评论 #7 — cgmb (2023-03-22T23:53:52Z)

I've opened a PR on CMake that will slightly change how hip-lang-config.cmake is found. If you have any comments, please let me know. https://gitlab.kitware.com/cmake/cmake/-/merge_requests/8356

---

### 评论 #8 — cgmb (2023-03-23T23:35:24Z)

I think the conclusion of my discussion with Brad King is that users should enable the C or CXX languages before enabling the HIP language. We should probably recommend using `project(myproj LANGUAGES CXX HIP)`. Users need to have a C++ toolchain installed anyway, since clang++ automatically includes some C++ standard library headers when compiling for HIP.

---

### 评论 #9 — skyreflectedinmirrors (2023-03-29T20:41:55Z)

> I think the conclusion of my discussion with Brad King is that users should enable the C or CXX languages before enabling the HIP language. We should probably recommend using `project(myproj LANGUAGES CXX HIP)`. Users need to have a C++ toolchain installed anyway, since clang++ automatically includes some C++ standard library headers when compiling for HIP.

This makes sense to me, I have never thought of trying it otherwise (but probably worth calling it out explicitly on the eventual docs)

---
