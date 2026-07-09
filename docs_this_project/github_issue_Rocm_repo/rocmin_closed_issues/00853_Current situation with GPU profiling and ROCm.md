# Current situation with GPU profiling and ROCm

- **Issue #:** 853
- **State:** closed
- **Created:** 2019-07-30T11:20:40Z
- **Updated:** 2019-09-11T19:55:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/853

According to the [ROCm Tools Docs](https://rocm-documentation.readthedocs.io/en/latest/ROCm_Tools/ROCm-Tools.html) there seem to be 2 different GPU performance profilers, [Radeon Compute Profiler (RCP)](https://github.com/GPUOpen-Tools/RCP) and [ROC Profiler (rocprof)](https://github.com/ROCm-Developer-Tools/rocprofiler). There is also the [ROCm Tracer (roctracer)](https://github.com/ROCm-Developer-Tools/roctracer) which is used by rocprof (`rocprof --hip-trace`) to get results broadly similar to Nvidia's nvprof. [CodeXL](https://github.com/GPUOpen-Tools/CodeXL) is also mentioned as the GUI tool suite for GPU profiling.
A [closer look indicates](https://github.com/RadeonOpenCompute/ROCm/issues/414#issuecomment-449507062) that rocprof is the actual profiler and rcprof (RCP) is integrated into it?

However there appear to be a bunch of other tools on the [GPUOpen-Tools repo](https://github.com/GPUOpen-Tools/) that are not mentioned in the documentation. Such as [RGA (Radeon GPU Analyzer)](https://github.com/GPUOpen-Tools/RGA), [Radeon GPU Profiler (RGP)](https://github.com/GPUOpen-Tools/Radeon-GPUProfiler) and [GPU Performance API (GPA)](https://github.com/GPUOpen-Tools/GPA). These appear to be for graphics profiling/analysis, but otherwise it's not totally clear why there are so many tools for seemingly similar purposes.

The main approach for analyzing performance of GPU compute programs appears to be to use CodeXL. But the last release was in October 2018 and [had to be tweaked to support gfx906](https://github.com/GPUOpen-Tools/CodeXL/issues/239). Since then there has been a regression somewhere which has broken rcprof ([RCP #25](https://github.com/GPUOpen-Tools/RCP/issues/25)) therefore CodeXL can't be used anymore and the only working profiling tool is rocprof.

The documentation on "readthedocs" for all of these tools consists of nothing more than a copy+paste of the repo readme for each tool, or a link to that readme. There are no examples and most of the space is taken up with build instructions which aren't needed for most people. It could really do with a high level overview explaining which tools do what and when to use them. Looks like [this is an old problem](https://github.com/RadeonOpenCompute/ROCm/issues/186) and unfortunately not a priority?

**What is current situation/future plans for profiling/performance analysis on ROCm HIP/HCC?**

Compared to Nvidia, it seems that `rocprof` is the equivalent of `nvprof`, but it doesn't output results in the same way. A script could be built (hipprof?) to generate reports similar to those created by `nvprof`. CodeXL looks like a good equivalent to Nvidia's Visual Profiler but it doesn't appear to be getting much use, has few updates and the rcprof tool it relies on has been broken for a while.

The ROCm Tools Documentation looks like it could do with some work.
@jlgreathouse you previously said that [ideas for wiki updates were welcome](https://github.com/RadeonOpenCompute/ROCm/issues/726#issuecomment-475421159), it looks like these would be best submitted as PRs in the [ROCm documentation repository](https://github.com/RadeonOpenCompute/ROCm_Documentation/pulls)?
