# Missing header. <CXLActivityLogger.h>

> **Issue #327**
> **状态**: closed
> **创建时间**: 2018-02-04T13:48:38Z
> **更新时间**: 2018-04-16T01:43:42Z
> **关闭时间**: 2018-02-04T18:33:57Z
> **作者**: Mandrewoid
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/327

## 描述

After a clean install of Ubuntu and the ROCm stack, I moved towards install hipCaffe. 
I got an error because /opt/rocm/include/hip/hip_profile.h calls for CXLActivityLogger.h. 

I'm posting this here rather than in the Caffe issues or user group because hip_profile.h is part of the ROCm install. 
Did I miss something? I found the missing header in https://github.com/GPUOpen-Tools/common-src-AMDTActivityLogger Is that supposed to be part of the ROCm install as well, or is it a separate post-install step? 

---

## 评论 (3 条)

### 评论 #1 — Mandrewoid (2018-02-04T17:15:35Z)

I have dug a little deeper, and it appears it expects /opt/rocm/profiler/CXLActivityLogger/include
I have /opt/rocm/profiler but inside I only have 3 subdirs:
 bin  counterfiles  docs  jqPlot

It appears to me that CXLActivityLogger has been superseded by AMDTActivityLogger. Trying a workaround

---

### 评论 #2 — Mandrewoid (2018-02-04T18:33:57Z)

fixed by sudo apt-get install cxlactivitylogger

---

### 评论 #3 — davclark (2018-04-16T01:43:41Z)

I got hit with this, and was running the AMDGPU-PRO drivers, which doesn't make the above available. I had to go back and install the open drivers per the rocm project webpage (not via the AMD driver install package). I'm pragmatic at this point, and with other things, the pro drivers are still quite a bit faster... is there no way to work around this issue with the official AMD packages? (i.e., is there a way to get cxlactivitylogger along with the official AMD packages?)

---
