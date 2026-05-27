# Ambiguous references to datatypes in ROCm

> **Issue #126**
> **状态**: closed
> **创建时间**: 2017-06-08T20:35:03Z
> **更新时间**: 2017-06-12T21:11:57Z
> **关闭时间**: 2017-06-12T21:11:57Z
> **作者**: acyeh
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/126

## 描述

Hello,

I'm running into a name conflict with many of the hip/hcc datatypes such as uchar1-uchar4, float2, char1-char3, etc.

The compilation errors are all along the same message of:

>
In file included from /server-home1/acyeh/relion/relion/src/gpu_utils/cuda_mem_utils.h:6:
In file included from /opt/rocm/hip/include/hip/hip_runtime.h:55:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_runtime.h:48:
In file included from /opt/rocm/hip/include/hip/hip_runtime_api.h:258:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_runtime_api.h:40:
In file included from /opt/rocm/hip/include/hip/hip_texture.h:27:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_texture.h:35: 
In file included from /opt/rocm/hip/include/hip/hcc_detail/channel_descriptor.h:27:
/opt/rocm/hip/include/hip/hcc_detail/hip_vector_types.h:1167:42: error: reference to 'uchar1' is ambiguous
DECLOP_MAKE_ONE_COMPONENT(unsigned char, uchar1);
                                         ^
/opt/rocm/hip/include/hip/hcc_detail/hip_vector_types.h:73:8: note: candidate found by name lookup is 'uchar1'
struct uchar1 {
       ^
/opt/rocm/hcc/include/hc_short_vector.inl:45:1: note: candidate found by name lookup is 'hc::short_vector::uchar1'
DECLARE_VECTOR_TYPE_CLASS(unsigned char, uchar);
^
/opt/rocm/hcc/include/hc_short_vector.inl:26:37: note: expanded from macro 'DECLARE_VECTOR_TYPE_CLASS'
typedef __vector<SCALAR_TYPE, 1>    CLASS_PREFIX ## 1; \
                                    ^
<scratch space>:131:1: note: expanded from here
uchar1

Here are the results of hipcc --version:

> HIP version: 1.0.17174
HCC clang version 5.0.0  (based on HCC 1.0.17172-ac6fc20-ae1d3ca-6d828a3 )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/hcc/bin

EDIT: added which files were included in the directory

---

## 评论 (7 条)

### 评论 #1 — scchan (2017-06-08T23:22:56Z)

HCC's short vector types and HIP's short vector types are different.
HCC's are C++ classes defined in the hc::short_vector namespace.
HIP's are defined in the global namespace and are implemented as a s struct to provide better portability.

Is there any chance that you have a "using namespace hc::short_vector" causing the collision between the HCC's vector types and HIP's vector types?

---

### 评论 #2 — acyeh (2017-06-08T23:54:35Z)

I haven't been using any namespaces from the HIP/HC directories so I don't think it's an issue with that.

I've grepped for "using namespace hc::short_vector" to confirm.

---

### 评论 #3 — pfultz2 (2017-06-09T00:39:36Z)

Do you have a short sample that demonstrates the problem?

---

### 评论 #4 — acyeh (2017-06-09T21:19:56Z)

As a note, this compilation notification began to arise after updating to the most recent ROCm.

Here is a small barebones sample that throws the same compilation error.

$HIP_DIR/bin/hipcc autopicker.cpp -I /opt/rocm/hcfft/include

Apologies in advance; not sure if it's possible to directly link .cpp and .h files, so I'll be copy and pasting it in.
**autopicker.cpp**

```cpp
#include "hcfft.h"
#include "autopicker.h"
```

**autopicker.h**

```cpp
#define CUDA
#ifdef CUDA
#include "cuda_mem_utils.h"
#endif
```

**cuda_mem_utils.h**

````cpp
#ifndef CUDA_DEVICE_MEM_UTILS_H_
#define CUDA_DEVICE_MEM_UTILS_H_
#define CUDA
#ifdef CUDA
#include <hip/hip_runtime.h>
#endif
````

Generates the following compilation error:

> $HIP_DIR/bin/hipcc autopicker.cpp -I /opt/rocm/hcfft/include
In file included from autopicker.cpp:2:
In file included from ./autopicker.h:3:
In file included from ./cuda_mem_utils.h:5:
In file included from /opt/rocm/hip/include/hip/hip_runtime.h:55:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_runtime.h:48:
In file included from /opt/rocm/hip/include/hip/hip_runtime_api.h:258:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_runtime_api.h:40:
In file included from /opt/rocm/hip/include/hip/hip_texture.h:27:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_texture.h:35:
In file included from /opt/rocm/hip/include/hip/hcc_detail/channel_descriptor.h:27:
/opt/rocm/hip/include/hip/hcc_detail/hip_vector_types.h:1167:42: error: reference to 'uchar1' is ambiguous
DECLOP_MAKE_ONE_COMPONENT(unsigned char, uchar1);
                                         ^
/opt/rocm/hip/include/hip/hcc_detail/hip_vector_types.h:73:8: note: candidate found by name lookup is 'uchar1'
struct uchar1 {
       ^
/opt/rocm/hcc/include/hc_short_vector.inl:45:1: note: candidate found by name lookup is 'hc::short_vector::uchar1'
DECLARE_VECTOR_TYPE_CLASS(unsigned char, uchar);
^
/opt/rocm/hcc/include/hc_short_vector.inl:26:37: note: expanded from macro 'DECLARE_VECTOR_TYPE_CLASS'
typedef __vector<SCALAR_TYPE, 1>    CLASS_PREFIX ## 1; \
                                    ^
<scratch space>:137:1: note: expanded from here
uchar1



---

### 评论 #5 — scchan (2017-06-11T20:42:02Z)

Note that cuda_mem_utils.h is missing another #endif at the end...

autopicker.cpp compiles fine for me.  Which version of hcfft are you using?  I was using the tip of the master branch.

---

### 评论 #6 — acyeh (2017-06-12T18:34:40Z)

Updating hcFFT seems to have resolved the issue! I was using the hcFFT library prior to the move to github (when it was on bitbucket).

---

### 评论 #7 — scchan (2017-06-12T21:11:57Z)

glad that it's working for you now :)

---
