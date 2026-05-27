# fatal error: 'limits' file not found

> **Issue #2054**
> **状态**: closed
> **创建时间**: 2023-04-16T00:23:08Z
> **更新时间**: 2023-04-16T00:40:28Z
> **关闭时间**: 2023-04-16T00:40:11Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2054

## 描述

When trying to run a PyTorch application on ROCm 5.4, I get this error:

```
MIOpen(HIP): Error [Compile] 'hiprtcCompileProgram(prog.get(), c_options.size(), c_options.data())' naive_conv.cpp: HIPRTC_ERROR_COMPILATION (6)
MIOpen(HIP): Error [BuildHip] HIPRTC status = HIPRTC_ERROR_COMPILATION (6), source file: naive_conv.cpp
MIOpen(HIP): Warning [BuildHip] /tmp/comgr-ededb1/input/naive_conv.cpp:39:10: fatal error: 'limits' file not found
#include <limits> // std::numeric_limits
         ^~~~~~~~
1 error generated when compiling for gfx900.
terminate called after throwing an instance of 'miopen::Exception'
  what():  /long_pathname_so_that_rpms_can_package_the_debug_info/data/driver/MLOpen/src/hipoc/hipoc_program.cpp:304: Code object build failed. Source: naive_conv.cpp
```

---

## 评论 (2 条)

### 评论 #1 — Bengt (2023-04-16T00:40:11Z)

Installing the development headers for the c++ 12 standard library resolved this issue for me under Ubuntu 22.04:

```bash
sudo apt install --yes libstdc++-12-dev
```

---

### 评论 #2 — Bengt (2023-04-16T00:40:28Z)

Via: https://github.com/RadeonOpenCompute/ROCm/issues/1889

---
