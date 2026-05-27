# ROCm libraries install test binaries, which is not desired for distribution packaging

> **Issue #1905**
> **状态**: closed
> **创建时间**: 2023-02-12T04:00:03Z
> **更新时间**: 2024-02-23T23:04:38Z
> **关闭时间**: 2024-02-23T23:04:38Z
> **作者**: littlewu2508
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1905

## 负责人

- cgmb
- TorreZuk

## 描述

Take rocBLAS as example

https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/56c25c239782ce09b0445d794d183323af3ce963/clients/gtest/CMakeLists.txt#L220-L221

installs rocblas-test and test data into `<prefix>/bin`. Usually testing is executed after build and before install, and test binaries are not installed to the final location. Please consider adding an cmake option to turn off installing testing files. This also applies to other packages under https://github.com/ROCmSoftwarePlatform

---

## 评论 (6 条)

### 评论 #1 — saadrahim (2023-03-01T00:03:56Z)

The option to turn off testing files should exist already. I've added a few developers from this team to confirm.

---

### 评论 #2 — TorreZuk (2023-03-01T00:19:02Z)

Yes the cmake options are likely all there but not standardized across all libraries.  
option( BUILD_CLIENTS_TESTS "Build rocBLAS unit tests" OFF ) along with BUILD_CLIENTS_SAMPLES and BUILD_CLIENTS_BENCHMARKS are found in clients/cmake/client-build-options.cmake
If you provide your cmake buiild command we can analyze further, but I think you are saying you want the option to build clients like the rocblas-test client (to verify with) but want the option to choose not to install them?  


---

### 评论 #3 — cgmb (2023-03-01T01:10:12Z)

The behaviour of installing the test binaries is indeed a bit unusual. The code that installs the test binaries was added in ROCm 5.2 as part of a feature to generate CPack packages for the test binaries across all libraries (SWDEV-320749).

> you are saying you want the option to build clients like the rocblas-test client (to verify with) but want the option to choose not to install them?

That's my interpretation. I'm not familiar with Gentoo's package system, but it's a (very minor) annoyance for Debian packaging. We have to add them to the `not-installed` list to ignore the tests. This behaviour is also a little weird for ROCm Spack packages, because it means that enabling the build-time tests for a package will actually change what is installed.

---

### 评论 #4 — littlewu2508 (2023-03-01T01:25:54Z)

> I think you are saying you want the option to build clients like the rocblas-test client (to verify with) but want the option to choose not to install them?

Exactly. Build clients like the rocblas-test, execute it before installation for testing purpose, and then install the rocblas libraries but without rocblas-test.

---

### 评论 #5 — nartmada (2024-02-16T19:53:25Z)

Hi @littlewu2508, please close the ticket if the issue has been resolved.  Thanks.

---

### 评论 #6 — nartmada (2024-02-23T23:04:38Z)

Closing the ticket as reported issue has been fixed.  Thanks.

---
