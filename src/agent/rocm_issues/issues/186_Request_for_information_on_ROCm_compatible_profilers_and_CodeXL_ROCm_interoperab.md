# Request for information on ROCm compatible profilers and CodeXL / ROCm interoperability

> **Issue #186**
> **状态**: closed
> **创建时间**: 2017-08-24T04:44:00Z
> **更新时间**: 2017-10-17T14:01:58Z
> **关闭时间**: 2017-10-17T14:01:58Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/186

## 描述

Just wanting to check in on how to optimize for AMD cards these days.

Last time I tried CodeXL out on a system without an AMD card, I couldn't get the main window to appear (IIRC I had this issue in various forms ~ 4 years ago on completely different computers/laptops).  It did work when using on a machine offering firegl drivers + opengl (which is where I think the problem happened...)

Just checked in here:
http://rocm-documentation.readthedocs.io/en/latest/ROCm_GPU_Tunning_Guides/ROCm-GPU-Tunning-Guides.html#vega-tuning-guide
and
http://rocm-documentation.readthedocs.io/en/latest/ROCm_Tools/ROCm-Tools.html

https://github.com/GPUOpen-Tools/GPA/blob/master/GPUPerfAPI/doc/GPUPerfAPI-UserGuide.pdf [dead]
https://github.com/RadeonOpenCompute/ROCm-Profiler/blob/master/README.md (looks like this is a branch of codexl, but hasn't been touched since november 2016)

Which listed but did not inform to the status of tools/apis such as CodeXL, ROCm-Profiler / profiling apis.  Have these been shown to work seamlessly with HIP?

Also, it sounded like no build was available that worked with rocm per that ROCm-Profiler readme - is that still the case with the select distro packages the ROCm project makes available?


---

## 评论 (4 条)

### 评论 #1 — chesik-amd (2017-08-24T12:38:38Z)

Where did you get that link to the GPA documentation?  The correct link is:

https://github.com/GPUOpen-Tools/GPA/blob/master/Doc/GPUPerfAPI-UserGuide.pdf

Also, the ROCm-Profiler repository you linked to is obsolete.  The correct place to get the profiler is:

https://github.com/GPUOpen-Tools/RCP

The profiler is also installed by default if you install ROCm.  After a sucessful install, the profiler appears in /opt/rocm/profiler/ and can be run using /opt/rocm/bin/rocm-profiler

---

### 评论 #2 — gstoner (2017-08-24T17:02:22Z)

@nevion. I will ping you.   Chris is the right guy to talk to about these tools, his group owns them. 

---

### 评论 #3 — nevion (2017-08-24T20:44:00Z)

@chesik-amd https://rocm.github.io/documentation.html under 
Development Tools -> GPU Performance API (GPUPerfAPI), including access to performance counters

Please delete obsolete things or mark as appropriately (on every page?) with a link to the new stuff... probably a good idea to an automated tool scrub that checks and makes sure all your links are active as well... lots of cruft building up; I know you guys are aware of it and preparing new documentation... Just for mention, take a look at how boost does old docs: http://www.boost.org/doc/libs/1_63_0 - the header has a easy to spot banner with a link to the current stuff if it exists or a redirect to the top level new doc.

From RCP's readme:
https://github.com/GPUOpen-Tools/RCP/blob/master/Src/GPUPerfAPI ...also dead 

Can one programmatically control profiling such as with cuda profiling api and nvtk / [vtune](https://software.intel.com/en-us/node/544204)?

---

### 评论 #4 — gstoner (2017-08-24T20:47:15Z)

For ROCm we are working on a new foundation for tracing and accessing perf counters, please be patient to replace GPUPerfAPI.   The first phase of the project is in place now.  GPUperfcounter we dead when they moved to the new Linux kernel driver. 

---
