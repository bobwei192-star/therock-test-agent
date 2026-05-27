# Multiple issues with rocprof

> **Issue #909**
> **状态**: closed
> **创建时间**: 2019-10-14T03:17:24Z
> **更新时间**: 2020-01-08T15:09:50Z
> **关闭时间**: 2019-12-24T08:11:35Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/909

## 描述

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

---

## 评论 (11 条)

### 评论 #1 — ye-luo (2019-11-27T07:07:57Z)

[2] still persist with 2.10. A big dig into the log I found librocprofiler64.so is causing problems.
```
Nov 27 01:04:47 ryzen-box kernel: [13115.668002] check_spo_batch[18207]: segfault at 3b ip 00007fd9e3f1ecd9 sp 00007fffba2d8630 error 4 in librocprofiler64.so.1.0.0[7fd9e3f04000+37000]
Nov 27 01:04:47 ryzen-box kernel: [13115.668008] Code: f8 fe ff ff ff 90 e8 00 00 00 85 c0 0f 84 3f 05 00 00 48 8b 85 08 ff ff ff 4c 8b 50 e8 4d 8b 42 78 4d 85 c0 0f 84 3f 05 00 00 <4d> 8b 48 10 4d 85 c9 0f 84 32 05 00 00 48 8b 8d d8 fe ff ff 48 8b
Nov 27 01:04:47 ryzen-box kernel: [13115.765316] Started evicting pasid 32770
Nov 27 01:04:47 ryzen-box kernel: [13115.765318] Evicting PASID 32770 queues
Nov 27 01:04:47 ryzen-box kernel: [13115.765465] Finished evicting pasid 32770
```
My system is ubuntu 18.04 + Radeon VII. Both 4.15 and 5.0.0 kernels hit segfault.

---

### 评论 #2 — josemonsalve2 (2019-11-27T23:12:06Z)

Same behavior here with gfx900 Vega 10 XTX [Radeon Vega Frontier Edition]. Ubuntu 18.04 and ROCm 2.9.6

---

### 评论 #3 — eshcherb (2019-12-03T02:39:51Z)

Hi Ye-luo,

According to the issue 1. Could you clarify what do you mean under "The rocprofiler-dev package list version 1.0.0. Totally irrelevant."?

According to the issue 2. I'll try to reproduce it on Ubuntu 18.04. Could you share what application are you profiling?

---

### 评论 #4 — ye-luo (2019-12-03T03:01:09Z)

[1] It seems that rocprofiler-dev version is listed constantly 1.0.0 even it gets updated as ROCm releases. The issue was when I upgraded to ROCm 2.9 the rocprofiler-dev contents were not consistent with https://github.com/ROCm-Developer-Tools/rocprofiler 2.9 tag.
[3] There is an dependency issue. roctracer-dev need to be required by rocprofiler-dev
I would say the above two are mostly packaging issue.

[2] is the major problem I had. You need to build https://github.com/QMCPACK/miniqmc using the OMP_offload branch. See AOMP [instructions](https://github.com/QMCPACK/miniqmc/wiki/OpenMP-offload). ~~You will need aomp 0.7-4 because I hit big problems with 0.7-5 https://github.com/ROCm-Developer-Tools/aomp/issues/45. When using 0.7-4, you will only be able to build part of miniQMC but you only need to succeed in `make -j8 check_spo_batched`.~~
Then just run rocprof ./bin/check_spo_batched and hit Segmentation fault.

---

### 评论 #5 — eshcherb (2019-12-03T22:59:42Z)

Hi Ye-luo,

Thank you for providing the details.
I'll check your application ant try to reproduce your issue.

---

### 评论 #6 — ye-luo (2019-12-04T02:29:02Z)

The AOMP 0.7-5 issue I hit was related to my machine. After fixing that, [2] still remains.

---

### 评论 #7 — ye-luo (2019-12-21T04:33:07Z)

With rocm 3.0, the error becomes "Error: V3 code object detected - code objects tracking should be enabled"

---

### 评论 #8 — eshcherb (2019-12-23T17:00:25Z)

There is a rocprof option to enable support for V3 code object '--obj-tracking on'.

---

### 评论 #9 — ye-luo (2019-12-24T08:11:35Z)

After adding "--obj-tracking on", rocprof from rocm 3.0 works well with my application built with AOMP. Hopefully users don't need to specify this option in the future.

---

### 评论 #10 — eshcherb (2020-01-07T22:42:05Z)

You can set "obj-tracking=on" by default in the profiler rc file 'rpl_rc.xml'.

Configuration file:
  You can set your parameters defaults preferences in the configuration file 'rpl_rc.xml'. The search path sequence: .:$HOME
  First the configuration file is looking in the current directory, then in your home.
  Configurable options: 'basenames', 'timestamp', 'ctx-limit', 'heartbeat', 'obj-tracking'.
  An example of 'rpl_rc.xml':
    \<defaults
        basenames=off
        timestamp=off
        ctx-limit=0
        heartbeat=0
        obj-tracking=off
    \>\</defaults>

---

### 评论 #11 — dmcdougall (2020-01-08T15:09:50Z)

@eshcherb The error message currently says

```
Error: V3 code object detected - code objects tracking should be enabled
```

But it could be updated to instead say

```
Error: V3 code object detected - code objects tracking should be enabled by passing '--obj-tracking=on'
```

Just a thought.  This would make it easier for the user to address the problem if there is a good reason code object tracking is not on by default.

---
