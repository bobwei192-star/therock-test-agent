# Examples in hip-samples don't work out of the box

> **Issue #1137**
> **状态**: closed
> **创建时间**: 2020-06-06T19:13:45Z
> **更新时间**: 2021-02-15T10:36:03Z
> **关闭时间**: 2021-02-15T10:33:55Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1137

## 描述

```
root@debian:/opt/rocm-3.5.0/hip/samples/0_Intro/square# make
../../../bin/hipify-perl square.cu > square.cpp
../../../bin/hipcc  square.cpp -o square.out
Can't exec "/opt/rocm/hcc/bin/hcc": No such file or directory at ../../../bin/hipcc line 245.
Use of uninitialized value $HCC_VERSION in pattern match (m//) at ../../../bin/hipcc line 246.
Use of uninitialized value $HCC_VERSION_MAJOR in substitution (s///) at ../../../bin/hipcc line 249.
Can't exec "/opt/rocm/hcc/bin/hcc-config": No such file or directory at ../../../bin/hipcc line 258.
Use of uninitialized value $HCC_VERSION_MAJOR in string eq at ../../../bin/hipcc line 263.
Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at ../../../bin/hipcc line 686.
Use of uninitialized value $targetsStr in substitution (s///) at ../../../bin/hipcc line 687.
Use of uninitialized value $targetsStr in split at ../../../bin/hipcc line 693.
Can't exec "/opt/rocm/hcc/bin/hcc": No such file or directory at ../../../bin/hipcc line 857.
failed to execute: No such file or directory
make: *** [Makefile:21: square.out] Error 255
$
```



---

## 评论 (3 条)

### 评论 #1 — baryluk (2020-06-06T19:25:32Z)

`/opt/rocm-3.5.0/hip/bin/hipcc` in the perl source code comment, mentions this:

```perl
# Other environment variable controls:
...
# HCC_HOME       : Path to HCC SDK (defaults to ../../hcc relative to this
#                  script's abs_path). Used on AMD platforms only.
```

But that doesn't look to be the case, and the ../../hcc doesn't exist either. (There is no `/opt/rocm-3.5.0/hcc/` directory).


---

### 评论 #2 — ROCmSupport (2021-02-15T05:38:27Z)

@baryluk ,
  
    Sorry for extremely late response. I think this problem has been resolved right?
    I am able to build /  execute without any issue. 
    Are you still facing the problem?


---

### 评论 #3 — ROCmSupport (2021-02-15T10:34:21Z)

HCC is removed and now the primary compiler is clang.
Not reproduced with ROCm 4.0.
Request you to open a new issue, if any.
Thank you.

---
