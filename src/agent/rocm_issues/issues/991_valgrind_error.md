# valgrind error

> **Issue #991**
> **状态**: closed
> **创建时间**: 2020-01-03T13:45:26Z
> **更新时间**: 2023-12-18T17:21:23Z
> **关闭时间**: 2023-12-18T17:21:22Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/991

## 描述

Reproducer can be found [here](https://github.com/GrokImageCompression/latke)

```
==5442== Mismatched free() / delete / delete []
==5442==    at 0x4C3123B: operator delete(void*) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==5442==    by 0x5DB9D4A: amd::hsa::loader::AmdHsaCodeLoader::DestroyExecutable(amd::hsa::loader::Executable*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x5D9901E: HSA::hsa_executable_destroy(hsa_executable_s) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x4F93173: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==    by 0x10FD2CBF: ???
==5442==    by 0x4F942E6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==    by 0x11E507BF: ???
==5442==    by 0x4F442D2: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==  Address 0x10949d10 is 0 bytes inside a block of size 51 alloc'd
==5442==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==5442==    by 0x5A0B9B9: strdup (strdup.c:42)
==5442==    by 0x5DC26FE: amd::hsa::loader::ExecutableImpl::Freeze(char const*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x5DB9C05: amd::hsa::loader::AmdHsaCodeLoader::FreezeExecutable(amd::hsa::loader::Executable*, char const*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x5D99311: HSA::hsa_executable_freeze(hsa_executable_s, char const*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x4F93FAD: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==    by 0x100000000001101: ???
==5442==    by 0x76D5C3F: ???
==5442==    by 0x7C2AE3F: ???
==5442==    by 0x10907CEF: ???
==5442==    by 0x30: ???
==5442==    by 0x18: ???
==5442== 
```

---

## 评论 (5 条)

### 评论 #1 — ehoffman2 (2020-06-26T19:52:00Z)

I can confirm it's still there with version 3.5.1-34

String allocated with strdup(), freed with delete()

In src/loader/executable.cpp

Created:
```
hsa_status_t ExecutableImpl::Freeze(const char *options) {
   ...
   lco->r_debug_info.l_name = strdup(ss.str().c_str());
   ...
}
```

Deleted:
```
static void RemoveCodeObjectInfoFromDebugMap(link_map* map) {
   ...
   delete map->l_name;
   ...
}
```

---

### 评论 #2 — boxerab (2021-11-13T00:50:07Z)

Still getting valgrind errors in 4.3

```
==45551== Syscall param sched_setaffinity(mask) points to uninitialised byte(s)
==45551==    at 0x4EC8326: create_thread (createthread.c:124)
==45551==    by 0x4EC9E0F: pthread_create@@GLIBC_2.2.5 (pthread_create.c:817)
==45551==    by 0x9D7A745: rocr::os::CreateThread(void (*)(void*), void*, unsigned int) (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DCEC0C: rocr::core::Runtime::SetAsyncSignalHandler(hsa_signal_s, hsa_signal_condition_t, long, bool (*)(long, void*), void*) (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DD3FE6: rocr::core::Runtime::Load() (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DD42D4: rocr::core::Runtime::Acquire() (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DACF39: rocr::HSA::hsa_init() (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9ADE014: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
==45551==    by 0x9A92ABE: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
==45551==    by 0x9A9D5B5: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
==45551==    by 0x9A8C604: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
==45551==    by 0x4ED247E: __pthread_once_slow (pthread_once.c:116)
==45551==  Address 0x5643561 is 1 bytes inside a block of size 8 alloc'd
==45551==    at 0x483B723: malloc (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
==45551==    by 0x483E017: realloc (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
==45551==    by 0x4ED5839: pthread_attr_setaffinity_np@@GLIBC_2.3.4 (pthread_attr_setaffinity.c:45)
==45551==    by 0x9D7A728: rocr::os::CreateThread(void (*)(void*), void*, unsigned int) (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DCEC0C: rocr::core::Runtime::SetAsyncSignalHandler(hsa_signal_s, hsa_signal_condition_t, long, bool (*)(long, void*), void*) (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DD3FE6: rocr::core::Runtime::Load() (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DD42D4: rocr::core::Runtime::Acquire() (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9DACF39: rocr::HSA::hsa_init() (in /opt/rocm-4.3.1/lib/libhsa-runtime64.so.1.3.40301)
==45551==    by 0x9ADE014: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
==45551==    by 0x9A92ABE: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
==45551==    by 0x9A9D5B5: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
==45551==    by 0x9A8C604: ??? (in /opt/rocm-4.3.1/opencl/lib/libamdocl64.so)
```

---

### 评论 #3 — keryell (2022-04-05T20:56:32Z)

More efficient to send a PR for this if not fixed already.

---

### 评论 #4 — nartmada (2023-12-14T03:02:32Z)

Hi @boxerab, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #5 — nartmada (2023-12-18T17:21:23Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
