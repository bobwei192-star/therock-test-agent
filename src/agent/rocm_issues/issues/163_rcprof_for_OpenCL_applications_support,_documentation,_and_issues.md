# rcprof for OpenCL applications: support, documentation, and issues

> **Issue #163**
> **状态**: closed
> **创建时间**: 2017-07-17T15:08:24Z
> **更新时间**: 2018-06-03T14:47:28Z
> **关闭时间**: 2018-06-03T14:47:28Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/163

## 描述

rcprof seems to be missing explicit OpenCL support; I'm aware that the runtimes are changing/merging, but it's not immediately obvious (nor seems to be documented) why the options `-t`  `-p` `-O` don't work and throw errors like the following:
```
libRCPCLOccupancyAgent.so is missing
Make sure you have libRCPCLOccupancyAgent.so under /opt/rocm/profiler/bin/
No profile mode specified. Nothing will be done.
```

Now, the HSA profiling modes do generate some data, but:
- `rcprof -A` often hangs and never finishes
- `rcprof -a foo.atp -T` generates some data, but a lot of it is HSA api data or related memory leak warnings that I never asked for nor do I know how to interpret
- `rcprof -C` keeps throwing the errors below (possibly for every kernel invocation)

I've attached some output from GROMACS test runs which illustrate both the hanging, dump of HSA API trace: https://goo.gl/oT52xL

---

## 评论 (6 条)

### 评论 #1 — chesik-amd (2017-07-19T18:48:05Z)

Hi pszi1ard,

Yes, the version of rcprof that is installed with ROCm does not have OpenCL support.  Admittedly, it should give better user feedback in this situation; however, since it was viewed as a short-term problem, we never got around to improving the user feedback in this case.

If you want, you can grab a full build of RCP from the [RCP Github repo](https://github.com/GPUOpen-Tools/RCP).  With that build, there is experimental support for profiling OpenCL running on top of ROCm. Tracing (--apitrace or -t) mode should mostly work.  Collecting perf counters (--perfcounter or -p) and occupancy (--occupancy or -O) is not yet supported (we need additional support from the OpenCL runtime for perf counter mode)

However, the supported mechanism for profiling OpenCL on top of ROCm is to use the HSA profiling modes (--hsatrace or -A, --hsapmc or -C).  There are some known issues for this since the OpenCL runtime never calls hsa_shut_down (see the [Known Issues](https://github.com/GPUOpen-Tools/RCP#known-issues) list in the RCP repo).  It sounds like you've tried that and are running into some issues.

We've had some previous reports of rcprof hangs occurring for applications that perform lots of data transfers.  These should be fixed in future versions of the ROCm runtime.  I'm not sure if what you're seeing is related to these issues or if it is an unrelated issue,  Would it be possible for you to share the application you are running so we can run some tests against it here?

Thanks,
Chris

---

### 评论 #2 — chesik-amd (2017-07-19T18:50:52Z)

I should point out, too, that we are planning to have full OCL profiler support in future versions of ROCm and RCP.

Chris

---

### 评论 #3 — pszi1ard (2017-07-20T01:17:25Z)

Hi Chris,

Thanks for the detailed feedback. It's a bit disappointing to see that not only the new platform does not extend the limited range of performance counters, but it takes a step back in terms of OpenCL support. However, I understand that the tools are still under development and it'd good to hear that there are plans for support  -- though "future versions of ROCm and RCP" are note too encouraging.

I'll try to squeeze out the time to compile RPC from source and give feedback, but to be honest, it's performance counters (and more of them exposed) what I'm hoping to see soon.

A related question: in what way is profiling/tracing different with AMDGPU-PRO? Should CodeXL 2.3 be compatible with with ROCm (1.6)? Could I at least collect some traces with RCP, perhaps combined with with manual instrumentation and visualize it all along API calls, GPU tasks with CodeXL?

Cheers,
Szilárd

---

### 评论 #4 — gstoner (2017-07-20T04:24:26Z)

Wow, you're interpreting the wrong way what going on.  We are building out a new foundation, which means we have are we need to still build out in stages.  

 We are building new foundations in the core driver for exposing debugging, profiling &  tracing.  We had few place where we want to improve how we exposing run control, doing capture which better support AQL UserMode Queues in the base driver.    We also wanted to put in place new foundation made it easier for third party tools to interface with ROCm stack.   

For tools developers, we are close to rolling out new helper library provides methods for instantiation of the profile context object and for populating of the start and stop AQL packets. The profile object contains a profiling events list and needed for profiling buffers descriptors, a command buffer and an output data buffer. To check if there was an error the library methods return a status code. Also, the library provides methods for querying required buffers attributes, to validate the event attributes and to get profiling output data.

On perf counters we working on adding more counter to the foundation, there are more counter with even new streaming counter which is in the GFX9 GPU architecture  coming in future releases  

Here is  more info on where to see more info in the source code 
- https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/master/src/perfctr.c
- https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/master/src/pmc_table.c
- https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/master/src/pmc_table.h
-https://github.com/GPUOpen-Tools/GPA/tree/master/Src/GPUPerfAPIHSA 

We giving full source code to peek deep into what really going on 

As they say, you can not Build Rome in a Day, nor a week. 

---

### 评论 #5 — gstoner (2017-07-20T04:24:59Z)

RCP is used to capture the trace,  CodeXL is how you view it. 

---

### 评论 #6 — chesik-amd (2017-07-20T14:40:09Z)

Hi Szilárd,

A couple more points of clarification.

1) You don't need to clone and build RCP yourself.  You can simply grab the 5.1 release from the Releases page:  https://github.com/GPUOpen-Tools/RCP/releases/download/v5.1/RadeonComputeProfiler-v5.1.6396.tgz.
2) CodeXL 2.3 is not compatible with ROCm 1.6.  CodeXL 2.4 is:  https://github.com/GPUOpen-Tools/CodeXL/releases/tag/v2.4.  CodeXL 2.4 includes RCP 5.1
3) OpenCL profiling is supported on amdgpu-pro, just not when OpenCL is running on ROCm. 
4) Do you have a list of additional perf counters you are looking for?

Tanks,
Chris

---
