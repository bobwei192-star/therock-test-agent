# hcc and friends not in path

> **Issue #11**
> **状态**: closed
> **创建时间**: 2016-05-17T11:30:50Z
> **更新时间**: 2016-08-20T18:49:01Z
> **关闭时间**: 2016-08-20T18:49:01Z
> **作者**: psteinb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/11

## 描述

Hi -

I just installed ROCm 1.1 on an ubuntu 14.04.04 box successfully, but the paths to hcc/clang++/hipify are not in PATH/LD_LIBRARY_PATH after boot. I am not sure what the rational behind this is, but I suggest to add /opt/rocm/\* to the respective PATHs so that after a fresh boot, I can use these tools right away.

Also, I couldn't find any manpages or other terminal-based documentation bundled under `/opt/rocm`. I only saw `/opt/rocm/hip/docs/html`. Are there any plans to provide further documentation?

Just 2 suggestions/questions -
P


---

## 评论 (3 条)

### 评论 #1 — psteinb (2016-06-20T11:18:23Z)

anyone on this?


---

### 评论 #2 — jedwards-AMD (2016-06-20T14:52:12Z)

Hi,

The PATH environment variable is not being explicitly set on install of hcc/hip because other versions of LLVM may be installed, and the user should be conscious of which version they are using. The installation of a package should never set LD_LIBRARY_PATH; this variable is reserved for developers. A more appropriate action would be to use ld config and a proper configuration file to add /opt/rocm/(hip|hcc)/lib to the linker/loader search path. I will contact both development teams about this.
.
Man page documentation is not currently available, but that would be a welcome addition. This may be something added in a future release.


---

### 评论 #3 — psteinb (2016-06-20T17:47:22Z)

from a system point of view that is OK. many HPC installations use non-standard paths anyway and then adapt the environment through modulefiles, but in this arena having /opt/rocm hardcoded in the deb/rpm is not desirable as copying libraries/binaries to shared network volumes may result in broken libraries/binaries (depends on your build setup). 

I personally would hope that you guys would merge up to llvm/clang quickly, so that upon installation of rocm, I get a llvm/clang stack which is feature complete in comparison to the stock llvm/clang of the distribution and thus replacing clang++/clang is not a big deal. I know that this is easier said than done, but it would solve many problems.   


---
