# Multiple issues with rocprof

- **Issue #:** 909
- **State:** closed
- **Created:** 2019-10-14T03:17:24Z
- **Updated:** 2020-01-08T15:09:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/909

[1] rocprof shipped with rocm 2.9 is not consistent with https://github.com/ROCm-Developer-Tools/rocprofiler/releases/tag/roc-2.9.0
The rocprofiler-dev package list version 1.0.0. Totally irrelevant.
[2] Segmentation fault
```
$ rocprof ./a.out 
RPL: on '191013_220730' from '/opt/rocm/rocprofiler' in '/home/yeluo/opt/miniqmc/build_ryzen_aomp_MP'
RPL: profiling './a.out'
RPL: input file ''
RPL: output dir '/tmp/rpl_data_191013_220730_8233'
RPL: result dir '/tmp/rpl_data_191013_220730_8233/input_results_191013_220730'
ROCProfiler: input from "/tmp/rpl_data_191013_220730_8233/input.xml"
  0 metrics
  0 traces
Segmentation fault (core dumped)
RPL: '/home/yeluo/opt/miniqmc/build_ryzen_aomp_MP/results.csv' is generated
```
[3] ~~try to load non-exist dynamic library.~~ Just need to install roctracer-dev package which is not installed by default.
```
$ rocprof --hsa-trace ./a.out
...
Tool lib "/opt/rocm/roctracer/tool/libtracer_tool.so" failed to load.
```