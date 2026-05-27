# Potential rocm 1.7  performance issue in HCC 

> **Issue #279**
> **状态**: closed
> **创建时间**: 2017-12-21T16:15:29Z
> **更新时间**: 2018-01-05T16:30:32Z
> **关闭时间**: 2018-01-05T16:30:31Z
> **作者**: JiniusDnn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/279

## 描述

*(无描述)*

---

## 评论 (4 条)

### 评论 #1 — JiniusDnn (2017-12-21T16:17:35Z)

**Phenomenon:**
Rocm 1.7   regression bug  with performance down 20% on some mem heavy algorithm.


**How I found:**
After I upgrade to 1.7,    my app recompiled  and found performance lower to 80% of original rocm1.6 system.

**Suggestion:**
There are some upgrade on hcc compiler,    I am pretty sure the regression lower performance is from some of the commits. 



---

### 评论 #2 — gstoner (2017-12-23T15:20:51Z)

Can you isolate it little more than this,  we have nothing to go on to looking into this do you have sample kerne aka test case to show the issue.    We have not observed performance drops on the  AMD EPYC and Intel Xeon system with MI25 we work on. 

---

### 评论 #3 — gstoner (2017-12-23T15:21:23Z)

Also what hardware are you on Processor, GPU etc.  

---

### 评论 #4 — JiniusDnn (2018-01-05T16:30:31Z)

Sorry for the delayed reply due to this holiday season.  

The hardware is vega 64.

The kernel I use have more than 8K LOC,  I 'll try to simplify it to a test case to demo this regression issue if I can.

---
