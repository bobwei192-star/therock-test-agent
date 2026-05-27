# Remove hardcoded values for NBIT and NBITSTR based on checks for x86_64 only in rocminfo

> **Issue #1223**
> **状态**: closed
> **创建时间**: 2020-09-17T21:55:32Z
> **更新时间**: 2021-01-28T11:05:57Z
> **关闭时间**: 2021-01-28T11:05:57Z
> **作者**: sameershende
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1223

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

rocminfo source code sets:

x86_64 specific!
## Extend Compiler flags based on Processor architecture
if ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86_64" )
  set ( NBIT 64 )
  set ( NBITSTR "64" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64  -msse -msse2" )
elseif ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86" )
  set ( NBIT 32 )
  set ( NBITSTR "" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32" )
endif ()

This makes it harder to port the tool to ppc64le which is 64bit but needs something like:

## Extend Compiler flags based on Processor architecture
if ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86_64" )
  set ( NBIT 64 )
  set ( NBITSTR "64" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64  -msse -msse2" )
elseif ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86" )
  set ( NBIT 32 )
  set ( NBITSTR "" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32" )
elseif ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "ppc64le" )
  set ( NBIT 64 )
  set ( NBITSTR "64" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64 " )
endif ()

Other architectures that are 64 bit wide (aarch64) may also be affected by this code that makes assumptions based on amd64 architecture. 

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2020-12-16T05:38:50Z)

Thanks @sameershende for reaching out.
I will talk to respective component owners and get back asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-01-28T11:05:57Z)

This requirement is already fulfilled and the latest HSA code has all the changes.
Request you to verify with the latest ROCm code.
Thank you.

---
