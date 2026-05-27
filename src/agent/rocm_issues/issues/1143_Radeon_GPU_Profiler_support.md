# Radeon GPU Profiler support?

> **Issue #1143**
> **状态**: closed
> **创建时间**: 2020-06-09T09:30:32Z
> **更新时间**: 2020-06-25T13:45:39Z
> **关闭时间**: 2020-06-25T13:45:39Z
> **作者**: thesleort
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1143

## 描述

I was trying to profile some OpenCL code using the Radeon GPU Profiler (RGP), while using ROCm and had no success doing so. In the end I assumed, that it might have been because I am not using the closed source AMD driver on Linux.

I know there is the `rocprof`, however, compared to RGP, it can be cumbersome to display the data in a similar fashion to the built in GUI of RGP. 

If RGP should work with ROCm, then I have a problem seeing the "Active Processes" after connecting successfully. 
If RGP is not currently supposed to work with ROCm, are there then any plans to "integrate" the two? Maybe get RGP to understand the .csv files that rocprof outputs.
Or could ROCm rocprof get its own GUI similar to RGP or the now deprecated CodeXL?

---

## 评论 (3 条)

### 评论 #1 — eshcherb (2020-06-09T15:39:16Z)

'rocprof' is generating traces in JSON format compatible with Chrome Tracing.
Could you try to open it with with Chrome Tracing, which is an internal trace visualization tool in Google Chrome?
Chrome tracing review can be found by the link: https://aras-p.info/blog/2017/01/23/Chrome-Tracing-as-Profiler-Frontend/

---

### 评论 #2 — thesleort (2020-06-12T12:07:06Z)

Ahh I see that, yes. 

I don't know if there is a problem in ROCm 3.5, because whenever I have either `--timestamp on`, `--stats` and `--hsa-trace` or all of them, I get the following:
```
error(4096) "Complete(), Tracker::Complete bad signal value"
Aborted (core dumped)
Data extracting error:  /tmp/results.txt'
```
Doing `cat /tmp/results.txt` returns nothing.

The whole output:
```
rocprof -i input.xml --basenames on --stats --timestamp on --hsa-trace -o output.csv 'gst-launch-1.0 videotestsrc ! video/x-raw,framerate=40/1,width=3840,height=2160,format=RGBA ! webkitoverlay url="https://google.com" opencl=TRUE ! decodebin ! videoconvert ! fpsdisplaysink'   
RPL: on '200612_140024' from '/usr/local/rocprofiler' in '/home/troels/Documents/git/gst-webkitoverlay/analysis'
RPL: profiling 'gst-launch-1.0 videotestsrc ! video/x-raw,framerate=40/1,width=3840,height=2160,format=RGBA ! webkitoverlay url="https://google.com" opencl=TRUE ! decodebin ! videoconvert ! fpsdisplaysink'
RPL: input file 'input.xml'
RPL: result dir '/tmp'
symbol: for_each_buffer
***** Warning: You are currently running a development build! *****
*****   Please use devmode=false in production environment.   *****

Nproc CPUS: 16
webkit dimensions: 0x0
function: allocate_buffer
function return: allocate_buffer: 0
/usr/local/lib/x86_64-linux-gnu/gstreamer-1.0/gstwebkitoverlay_alpha.cl
Setting pipeline to PAUSED ...
Pipeline is PREROLLING ...
Pipeline is PREROLLED ...
Setting pipeline to PLAYING ...
New clock: GstSystemClock
error(4096) "Complete(), Tracker::Complete bad signal value"
Aborted (core dumped)
Data extracting error:  /tmp/results.txt'
```

---

### 评论 #3 — thesleort (2020-06-25T13:45:39Z)

I think I will put the issue up on the rocprof github page instead, since this issue seems more related to that.

---
