# Possiblity of providing the source code of libhsa-amd-aqlprofile64, or binary on other achitecture

> **Issue #1781**
> **状态**: closed
> **创建时间**: 2022-08-07T04:48:21Z
> **更新时间**: 2025-06-12T14:12:13Z
> **关闭时间**: 2025-06-12T14:12:12Z
> **作者**: littlewu2508
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1781

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Hello, I am a member of Gentoo ROCm packaging team. There are a long history of discussing the closed-source libhsa-amd-aqlprofile64.so:

- https://bugs.gentoo.org/716948
- https://github.com/ROCm-Developer-Tools/rocprofiler/issues/38

Although not loading libhsa-amd-aqlprofile64.so does not affect running rocm, it does block rocprofiler's tracing, and the only source of libhsa-amd-aqlprofile64.so we can find is amd64 binary package. If ROCm is installed on arm or other arch, or compiled against musl, full featured profiling would be impossible.

So where can we find  the source code of libhsa-amd-aqlprofile64.so? It seems that it was previously open sourced in https://github.com/RadeonOpenCompute/HSA-AqlProfile-AMD-extension, but this is removed.

---

## 评论 (14 条)

### 评论 #1 — littlewu2508 (2022-08-07T08:07:54Z)

Well, I see the LICENSE.md, disclaimer and EULA in [hsa-amd-aqlprofile_1.0.0.50200-65_amd64.deb](http://repo.radeon.com/rocm/apt/5.2/pool/main/h/hsa-amd-aqlprofile/hsa-amd-aqlprofile_1.0.0.50200-65_amd64.deb). So is there a plan for open source, or providing binaries that compiles to other architectures?

---

### 评论 #2 — littlewu2508 (2022-08-07T10:44:24Z)

I patched hsa_rsrc_factory.cpp in rocprofiler and roctracer, removing the libhsa-amd-aqlprofile64.so loading code:

```diff
diff --git a/src/util/hsa_rsrc_factory.cpp b/src/util/hsa_rsrc_factory.cpp
index 643ff16..c08d98f 100644
--- a/src/util/hsa_rsrc_factory.cpp
+++ b/src/util/hsa_rsrc_factory.cpp
@@ -127,15 +127,6 @@ HsaRsrcFactory::HsaRsrcFactory(bool initialize_hsa) : initialize_hsa_(initialize
   if (cpu_pool_ == NULL) CHECK_STATUS("CPU memory pool is not found", HSA_STATUS_ERROR);
   if (kern_arg_pool_ == NULL) CHECK_STATUS("Kern-arg memory pool is not found", HSA_STATUS_ERROR);

-  // Get AqlProfile API table
-  aqlprofile_api_ = {0};
-#ifdef ROCP_LD_AQLPROFILE
-  status = LoadAqlProfileLib(&aqlprofile_api_);
-#else
-  status = hsa_api_.hsa_system_get_major_extension_table(HSA_EXTENSION_AMD_AQLPROFILE, hsa_ven_amd_aqlprofile_VERSION_MAJOR, sizeof(aqlprofile_api_), &aqlprofile_api_);
-#endif
-  CHECK_STATUS("aqlprofile API table load failed", status);
-
   // Get Loader API table
   loader_api_ = {0};
   status = hsa_api_.hsa_system_get_major_extension_table(HSA_EXTENSION_AMD_LOADER, 1, sizeof(loader_api_), &loader_api_);
```

And without libhsa-amd-aqlprofile64.so rocprofiler can run without issue. So what is libhsa-amd-aqlprofile64.so actually doing?

---

### 评论 #3 — tpkessler (2023-01-08T10:42:32Z)

Hi! I'm packaging ROCm for Arch Linux and we hit the same problem. The Debian folks also discuss this on their [mailing list](https://lists.debian.org/debian-ai/2022/05/msg00026.html). @cgmb @Maxzor

---

### 评论 #4 — littlewu2508 (2023-01-08T14:28:00Z)

> Hi! I'm packaging ROCm for Arch Linux and we hit the same problem. The Debian folks also discuss this on their [mailing list](https://lists.debian.org/debian-ai/2022/05/msg00026.html). @cgmb @Maxzor

I found a workaround to strip this lib and made ROCm profiling work as expected (maybe there is one day some profiling will use this proprietary lib, but I haven't encounter it yet).

There are three patches to strip it off (these are designed for ROCm-5.1.3, may need updates):

rocr-runtime: https://github.com/gentoo/gentoo/blob/78d327a366e02e8e9e0134961d36477a75f97797/dev-libs/rocr-runtime/files/rocr-runtime-4.3.0_no-aqlprofiler.patch

With rocr-runtime you are already free of runtime warnings when running ROCm programs normally. But profiler does not work as expected, unless applying the following patches:

roctracer: https://github.com/gentoo/gentoo/blob/78d327a366e02e8e9e0134961d36477a75f97797/dev-util/roctracer/files/roctracer-5.1.3-no-aqlprofile.patch

rocprofiler: https://github.com/gentoo/gentoo/blob/78d327a366e02e8e9e0134961d36477a75f97797/dev-util/rocprofiler/files/rocprofiler-4.3.0-no-aqlprofile.patch

---

### 评论 #5 — nartmada (2023-12-18T21:39:02Z)

Hi @littlewu2508, please check latest ROCm6.0.0 and see if your issue has been resolved.  Please close the ticket if your issue has been resolved.  Thanks.

---

### 评论 #6 — misos1 (2023-12-21T17:11:14Z)

@nartmada So is it already open-sourced?

---

### 评论 #7 — nartmada (2024-01-02T15:55:25Z)

Happy New Year @misos1, I am reaching out to the developers to find out if the source code is already "open sourced".  Thanks.

---

### 评论 #8 — nartmada (2024-01-02T17:41:29Z)

Hi @littlewu2508 and @misos1, unfortunately, aqlprofile code is NOT opensource and is NOT available on GitHub.

---

### 评论 #9 — misos1 (2024-01-03T04:01:29Z)

@nartmada 
> please check latest ROCm6.0.0 and see if your issue has been resolved. Please close the ticket if your issue has been resolved. Thanks.

So can you please specify how was this issue fixed? I think it was not only about providing source code - as title hints: "Possiblity of providing the source code of libhsa-amd-aqlprofile64, **or binary on other achitecture**"

---

### 评论 #10 — AphidGit (2024-07-07T17:14:50Z)

!! https://github.com/ROCm/rocprofiler/ _still_ now appears to depend on aqlprofile, which is blacklisted as closed source. The provided/linked patches by littlewu above no longer suffice to extirpate the connection.

I tried to remove this lib from its cmakelists and got the following compile error: 

```
/home/aphid/src/rocm/24_rocprofiler/rocprofiler/src/util/hsa_rsrc_factory.cpp: In static member function ‘static hsa_status_t rocprofiler::util::HsaRsrcFactory::LoadAqlProfileLib(aqlprofile_pfn_t*)’:
/home/aphid/src/rocm/24_rocprofiler/rocprofiler/src/util/hsa_rsrc_factory.cpp:322:8: error: ‘rocprofiler::util::HsaRsrcFactory::aqlprofile_pfn_t’ {aka ‘struct hsa_ven_amd_aqlprofile_1_00_pfn_s’} has no member named ‘hsa_ven_amd_aqlprofile_att_marker’; did you mean ‘hsa_ven_amd_aqlprofile_start’?
  322 |   api->hsa_ven_amd_aqlprofile_att_marker = (decltype(::hsa_ven_amd_aqlprofile_att_marker)*)
      |        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |        hsa_ven_amd_aqlprofile_start
/home/aphid/src/rocm/24_rocprofiler/rocprofiler/src/util/hsa_rsrc_factory.cpp:322:56: error: ‘::hsa_ven_amd_aqlprofile_att_marker’ has not been declared; did you mean ‘hsa_ven_amd_aqlprofile_start’?
  322 |   api->hsa_ven_amd_aqlprofile_att_marker = (decltype(::hsa_ven_amd_aqlprofile_att_marker)*)
      |                                                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                        hsa_ven_amd_aqlprofile_start
/home/aphid/src/rocm/24_rocprofiler/rocprofiler/src/util/hsa_rsrc_factory.cpp:322:56: error: ‘::hsa_ven_amd_aqlprofile_att_marker’ has not been declared; did you mean ‘hsa_ven_amd_aqlprofile_start’?
  322 |   api->hsa_ven_amd_aqlprofile_att_marker = (decltype(::hsa_ven_amd_aqlprofile_att_marker)*)
      |                                                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                        hsa_ven_amd_aqlprofile_start
/home/aphid/src/rocm/24_rocprofiler/rocprofiler/src/util/hsa_rsrc_factory.cpp:322:45: error: expected primary-expression before ‘decltype’
  322 |   api->hsa_ven_amd_aqlprofile_att_marker = (decltype(::hsa_ven_amd_aqlprofile_att_marker)*)
      |                                             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/aphid/src/rocm/24_rocprofiler/rocprofiler/src/util/hsa_rsrc_factory.cpp:322:45: error: expected ‘)’ before ‘decltype’
  322 |   api->hsa_ven_amd_aqlprofile_att_marker = (decltype(::hsa_ven_amd_aqlprofile_att_marker)*)
      |                                            ~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                             )
make[2]: *** [src/api/CMakeFiles/rocprofiler64.dir/build.make:174: src/api/CMakeFiles/rocprofiler64.dir/__/util/hsa_rsrc_factory.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1714: src/api/CMakeFiles/rocprofiler64.dir/all] Error 2
make: *** [Makefile:166: all] Error 2
```





---

### 评论 #11 — cgmb (2024-07-07T19:00:55Z)

Reopening, as this still a matter of ongoing discussion. The status quo is not acceptable.

---

### 评论 #12 — AphidGit (2024-07-08T06:10:36Z)

I wrote a new patch for rocprofiler; 

https://github.com/AphidGit/rocm_compile/blob/main/rocprofiler.patch 

This should compile the current git master version of rocprofiler. Note; the error above is due to a newly introduced dependency on ' rocprofiler-register', found at https://github.com/ROCm/rocprofiler-register 

---

### 评论 #13 — ppanchad-amd (2024-10-09T14:53:16Z)

Hi @littlewu2508. This is planned for future ROCm release. Thanks!

---

### 评论 #14 — tcgu-amd (2025-06-12T14:12:13Z)

Hi @littlewu2508, I will be closing this issue since aqlprofile is now opensource at  https://github.com/rocm/aqlprofile. Thanks! 

---
