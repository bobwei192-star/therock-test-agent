# Paths convention within /opt/rocm/ 

> **Issue #647**
> **状态**: closed
> **创建时间**: 2018-12-24T12:31:20Z
> **更新时间**: 2019-10-22T15:42:09Z
> **关闭时间**: 2019-10-22T15:42:09Z
> **作者**: ubombi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/647

## 描述

Can someone fix paths within a framework. 
There are a lot of mess like:
`/opt/rocm/[something]/include` and `/opt/rocm/include/[something]/`
`/opt/rocm/[something]/bin` and `/opt/rocm/bin/[something]/`
They differ per project and always are hardcoded.

It's strange to see [below] in TensorFlow code.
```
   # Add MIOpen headers
   inc_dirs.append("/opt/rocm/miopen/include")	  
    # Add rtg headers
   inc_dirs.append("/opt/rocm/include/migraph")
``` 

Same with build scripts.  

---

## 评论 (1 条)

### 评论 #1 — kentrussell (2019-10-22T15:42:09Z)

We've managed to get this normalized starting in 2.7. I think the final projects finally got this aligned in 2.9. Please re-open the issue if this is not the case for any of the projects that you see.

---
