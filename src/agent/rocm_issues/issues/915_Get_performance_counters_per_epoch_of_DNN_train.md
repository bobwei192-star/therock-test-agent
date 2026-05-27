# Get performance counters per epoch of DNN train

> **Issue #915**
> **状态**: closed
> **创建时间**: 2019-10-21T19:42:15Z
> **更新时间**: 2023-12-18T17:13:51Z
> **关闭时间**: 2023-12-18T17:13:51Z
> **作者**: theRTLmaker
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/915

## 描述

I would like to get some help regarding the use of the Library public API of rocprofiler. 
I am currently using the AMD Radeon Vega Frontier Edition to train machine learning models using the PyTorch framework. As part of my task, I need to get the output of the performance counters between each epoch of the train and get it while the model is training.
The pseudocode of the application is something like:

Init Program;
for epoch in range(1,10): {
    Reset performance counters;
    Train(); //Train one epoch of the model;
    Output Performance counters value of epoch to file;
}

What is the best way to accomplish this? Since my framework is in python, I was thinking of creating a .so file with the API methods written in C++. Can I invocate APIs calls in my PyTorch script that interacts with the rocprof command-line tool?

Thank you for your help.

Setup:
- ROCM 2.8
- CentOS 7.5
- Python 3.6
- PyTorch 1.3

---

## 评论 (4 条)

### 评论 #1 — eshcherb (2019-12-04T20:51:57Z)

We don't provide Python wrapper for rocProfiler C API.
You can make a C library callable from Python by wrapping it with Cython https://medium.com/@shamir.stav_83310/making-your-c-library-callable-from-python-by-wrapping-it-with-cython-b09db35012a3
So you can try to use Cython to call rocProfiler or your helper library which will use rocProfiler.

---

### 评论 #2 — iotamudelta (2019-12-20T21:31:17Z)

@TheEmbbededCoder seconding what @eshcherb said here from the PyTorch perspective. You can use both the event-based autograd profiler and the rocTX / `emit_nvtx()` functionality with PyTorch on ROCm. So while you can trace and get overall performance counters, per iteration counters are not currently supported.

---

### 评论 #3 — nartmada (2023-12-12T23:19:19Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #4 — nartmada (2023-12-18T17:13:51Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
