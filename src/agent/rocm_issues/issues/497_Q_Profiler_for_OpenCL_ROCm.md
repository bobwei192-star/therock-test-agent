# Q: Profiler for OpenCL / ROCm ?

> **Issue #497**
> **状态**: closed
> **创建时间**: 2018-08-10T14:55:54Z
> **更新时间**: 2019-02-08T17:16:52Z
> **关闭时间**: 2019-02-08T17:16:52Z
> **作者**: preda
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/497

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I would like to obtain insight into the performance of an OpenCL app running on ROCm. Is there a GPU profiler that I could use? (that works with ROCm 1.8.2, and OpenCL).

I'm thinking about information such as:
- occupancy problems
- slow or stalled instructions
- cache L1/L2 hit rate etc
- bank conflicts (global or LDS)
etc

---

## 评论 (12 条)

### 评论 #1 — jlgreathouse (2018-08-10T20:03:11Z)

Hi @preda 

We are planning on releasing a ROCm profiling utility as part of the ROCm 1.9 release.

---

### 评论 #2 — jlgreathouse (2018-08-22T16:46:55Z)

Hi @preda 

We have released the source code for rocprofiler, a library and tool that will allow you to get access to the hardware performance counters in AMD GPUs. This should be included as part of ROCm 1.9, but if you would like to try it out on your current installation, you can get it from https://github.com/ROCmSoftwarePlatform/rocprofiler

To build it on ROCm 1.8.x, you will need to add in an environment variable change. So change `cmake -DCMAKE_PREFIX_PATH=/opt/rocm/lib:/opt/rocm/include/hsa ..` to `CMAKE_CURR_API=1 CMAKE_PREFIX_PATH=/opt/rocm/lib:/opt/rocm/include/hsa cmake ..`

At that point, when you set the environment variables [here](https://github.com/ROCmSoftwarePlatform/rocprofiler#to-run-the-test), you can run HIP, HCC, or OpenCL applications and rocprofiler will gather the performance counters requested in your `input.xml` (set with `ROCP_INPUT`). The metrics that you can add into this XML file are defined in the `metrics.xml` (set with `ROCP_METRICS`). You'll note that our default `metrics.xml` is a series of formulae that calculate higher-level performance metrics based off hardware counters defined in `gfx_metrics.xml`.

`gfx_metrics.xml` uses the same numbering (which hardware block and which event in that block) as described in the various "PublicCounterNames" files in GPUPerfAPI. For example, [this file for gfx9](https://github.com/GPUOpen-Tools/GPA/blob/v3.2/Src/PublicCounterCompilerInputFiles/PublicCounterNamesHSAGfx9.txt) shows all of the hardware blocks and their counter numbers. Only some of these counters have been "made public" by naming them. and I believe most of the named counters in rocprofiler are the same as GPA.

There is also a helper scripts [described here](https://github.com/ROCmSoftwarePlatform/rocprofiler#profiling-utility-usage) that should make it easier to run all of this.

---

### 评论 #3 — masahi (2018-08-23T04:32:54Z)

@jlgreathouse what is the difference between the new profiler and the existing [rcprof](https://github.com/GPUOpen-Tools/RCP)?

---

### 评论 #4 — preda (2018-08-23T09:42:55Z)

@jlgreathouse  thanks for making available rocprofiler.
I could build it successfully. I tried to use it, but it seems a bit too low-level for me.
For running, I tried with rpl_run.sh, but I couldn't get the log with it (my error, for sure).
I could run with build/run.sh. This produced a file RESULTS/results.txt, which seems correct, but too low-level for me to interpret.

Some suggestions, maybe somebody knowledgeable could write an article about the perf counters, enumerating the most notable counters with examples. Maybe provide some default .xml lists of counters, and a way to post-process results.txt into meaningful aggregates. Maybe some "common issues", such as: how to diagnose LDS bank conflicts. How to diagnose global mem bank conflicts. How to diagnose low occupancy caused by X. etc.

And a walk-through realistic example of using the profiler to find some non-obvious (new) information about an OpenCL kernel, and maybe using that to fix the performance problem, would be nice.

Thank you, and keep up the good work!


---

### 评论 #5 — preda (2018-08-23T09:53:13Z)

(In particular, my use case is this: I have some OpenCL code which is very well tuned already. I know how much time every kernel takes, I measured and optimized "to death" (but without a profiler). I would like to use a tool (the profiler) that would allow me to identify if there's anything that I missed in my optimization, some approach that would allow me to improve perf a bit more.)


---

### 评论 #6 — jlgreathouse (2018-08-23T15:27:07Z)

Hi @masahi 

rcprof is a higher-level tool that an gather hardware performance counters, API traces, kernel occupancy information, etc. on AMD GPUs. At its heard, rcprof was the "gathering data about GPU workloads" heard of AMD's CodeXL tool. It was originally called `sprofile` back in the day (in case you ever worked with CodeXL from the command line). You can take the outputs from rcprof and put them into the CodeXL visualization engine, for example, which may help you find bottlenecks in your application in a visual manner. The outputs are all plaintext as well (e.g. CSV files for performance counters, ATP files for API traces).

rcprof can be used to gather this information from OpenCL applications and HSA-style applications on top of ROCm. If you tried rcprof on ROCm in before 2018, OpenCL counters were not available -- they work now, so have it. :)  The support for HSA-style programming languages (HIP, HCC) uses a somewhat older profiling path (there may be a few bugs), but it should also work.

rocprofiler is a lower-level mechanism specifically built for ROCm to get access to performance counters (activity tracing can be done with [roctracer](https://github.com/ROCmSoftwarePlatform/roctracer)). It is at a lower level than rcprof, but its goal is to replace some of the underlying plumbing that tools like rcprof use to gather performance counter data on the ROCm platform. (For instance, I noted above that HSA-style languages use an older profiling path; rocprofiler is meant to replace this).

In the medium term, we are looking to update rcprof to interface with rocprofiler to increase the robustness of our performance monitoring solutions on the ROCm software stack. As it stands, you might try using both to see which works better for your needs.

---

### 评论 #7 — jlgreathouse (2018-08-23T16:09:16Z)

Hi @preda

Thank you for testing rocprofiler and for your feedback. If you could show me the rpl_run.sh line that you ran, I could see if the problem is on our end. :)

I agree that we could do with some better documentation about what these counters actually signify and how to use them to optimize your application. I will posit, however, that if you already have well-tuned kernels, then you're going to have to learn about more low-level details to be able to fix your problems. :)

Towards this end, we are currentyl working to put together an updated tutorial on the deep innards of AMD GPUs. We will be presenting this first at this year's Internatinoal Symposium on Microarchitecture. My goal is to cover our GCN microarchitecture over the course of a few hours. Later in the tutorial, I'd like to walk through how you can use this knowledge to optimize some machine learning kernels.

Hopefully this tutorial (and the slides from it)would be a good starting point for later writing a deeper description of what our hardware performance counters mean, how they relate to the microarchitecture, and how you can use that knowledge to optimize your own kernels.

As for looking into your kernel, we are also exploring some hardware performance monitoring mechanisms that may help you dig into your kernel's performance pain points. Stay tuned. :)

---

### 评论 #8 — masahi (2018-08-24T01:33:27Z)

@jlgreathouse Thanks very much for the detailed answer. I have used rcprof and CodeXL on rocm environment before. It worked, but I wanted a workflow where everything can be done on command line (like nvprof). I'll definitely try the new profiler with my kernels. (I use rocm and llvm's AMDGPU backend directly to generate and run HSA code. I am one of the authors of [this blog](https://tvm.ai/2017/10/30/Bringing-AMDGPUs-to-TVM-Stack-and-NNVM-Compiler-with-ROCm.html).

I'm very much looking forward to your GCN tutorial!

---

### 评论 #9 — jlgreathouse (2018-12-21T21:49:47Z)

Hi @masahi @preda and anyone else who is following this thread,

With the release of ROCm 2.0 and [RCP 5.6](https://github.com/GPUOpen-Tools/RCP/tree/v5.6), we have now integrated RCP (a.k.a. `rcprof` discussed earlier in this thread) to work by using `rocprofiler`. This integration should have cleared up a number of the previous issues you may have had with profiling GPU kernels on the ROCm software stack. You should be able to install it by installing the `rocm-profiler` package on Ubuntu, CentOS, and RHEL.

Its outputs can be visualized using CodeXL, but you can do basically all of the `rcprof` profiling command-line only. (To be honest, I personally have done almost all my `sprofile`/`rcprof` work command-line only. :)  )

---

### 评论 #10 — masahi (2018-12-22T12:00:41Z)

@jlgreathouse Can I view kernel-by-kernel breakdown of execution time using command line tool only? I have used CodeXL before, but I want workflows similar to nvprof with --print-gpu-summary option (without using GUI app). 

---

### 评论 #11 — jlgreathouse (2018-12-22T16:16:04Z)

Hi @masahi 

[This part of the RCP documentation](https://radeon-compute-profiler-rcp.readthedocs.io/en/latest/commandline.html#example-command-lines) may cover what you're looking for. In particular, the following command will take an OpenCL API trace and generate a summary of all of those calls:
```bash
rcprof ---apitrace --tracesummary "/path/to/app.exe" --device gpu
```

If you're using an HSA-based application (e.g. an application programmed in HCC, HIP, ATMI, ROCm-Numba), you would use:
```bash
rcprof --hsatrace --tracesummary "/path/to/app.exe" rcprof --hsaaqlpackettrace --tracesummary "/path/to/app.exe"
```

Collecting these API traces will produce `.atp` files, and RCP can create summaries of them with:
```bash
rcprof --atpfile "/path/to/output.atp" --tracesummary
```

That said, IIRC (I'm at home and don't have a test system on hand), these will be HTML summaries. If you would like to generate your own custom summary of the .atp files, you can do this by parsing the file with any of your own favorite command line utilities. The `.atp` file format is documented here:
https://radeon-compute-profiler-rcp.readthedocs.io/en/latest/outputfiles.html#application-trace-output-session-name-atp

---

### 评论 #12 — masahi (2018-12-22T23:59:28Z)

@jlgreathouse thanks, I'll try rolling my own parser.

---
