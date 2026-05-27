# Error: close failed in file object destructor: sys.excepthook is missing

> **Issue #885**
> **状态**: closed
> **创建时间**: 2019-09-12T08:58:31Z
> **更新时间**: 2019-09-12T10:42:39Z
> **关闭时间**: 2019-09-12T10:42:39Z
> **作者**: smithakihide
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/885

## 描述

Hello, thank you for developing ROCm.

I am testing new environment on ROCm 2.4 September 12th, Ubuntu 18.04.3 LTS, Vega VII these days, and now testing to compile a simple program using HIP compiler that I can find in /opt/rocm/hip/bin/. 

The problem is that I cannot compile the below source using hipcc, with a command hipcc test.cpp where test.cpp denotes the file name of the source.

```
#include <iostream>

int main(){
    std::cout << "test is also a test\n";
}

```
After launching hipcc, it stops and does not reply to console. The error message I could obtain sending an exit signal using "Ctl + C" is as following,

```
close failed in file object destructor:
sys.excepthook is missing
lost sys.stderr
```

How can I solve this problem? please help me.

---

## 评论 (1 条)

### 评论 #1 — smithakihide (2019-09-12T10:42:39Z)

I solved this problem, by rebooting.
If any one encountered to the same issue, I would be glad this information helps you.

---
