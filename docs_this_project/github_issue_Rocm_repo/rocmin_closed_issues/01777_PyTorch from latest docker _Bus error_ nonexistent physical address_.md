# PyTorch from latest docker "Bus error: nonexistent physical address"

- **Issue #:** 1777
- **State:** closed
- **Created:** 2022-08-04T10:09:07Z
- **Updated:** 2024-04-08T10:53:39Z
- **Assignees:** sunway513
- **URL:** https://github.com/ROCm/ROCm/issues/1777

Hello,

I pulled the latest PyTorch container from https://hub.docker.com/r/rocm/pytorch

I can get some PyTorch code working 30% of the time. The rest of the time, I get these sorts of bus error randomly. I am running distributed code on 4 AMD MI250x. 

```
[nid005060:78213:0:78213] Caught signal 7 (Bus error: nonexistent physical address)
==== backtrace (tid:  78213) ====
 0  /lib/libucs.so.0(ucs_handle_error+0x2a4) [0x147c3982f8f4]
 1  /lib/libucs.so.0(+0x2bacf) [0x147c3982facf]
 2  /lib/libucs.so.0(+0x2bdb6) [0x147c3982fdb6]
 3  /lib/x86_64-linux-gnu/libpthread.so.0(+0x14420) [0x147e20af9420]
 4  /opt/rocm/lib/libhsa-runtime64.so.1(+0x4d42d) [0x147d6d00542d]
 5  /opt/rocm/lib/libhsa-runtime64.so.1(+0x4d2ea) [0x147d6d0052ea]
 6  /opt/rocm/lib/libhsa-runtime64.so.1(+0x40fd9) [0x147d6cff8fd9]
 7  /opt/rocm/lib/libamdhip64.so.5(+0x28fc3b) [0x147d96f57c3b]
 8  /opt/rocm/lib/libamdhip64.so.5(+0x27e88a) [0x147d96f4688a]
 9  /opt/rocm/lib/libamdhip64.so.5(hipDeviceSynchronize+0xfd) [0x147d96d4e54d]
10  /opt/conda/lib/python3.7/site-packages/torch/lib/libtorch_hip.so(_ZN4c10d16ProcessGroupNCCL8WorkNCCL19synchronizeInternalENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x199) [0x147dae7f9299]
11  /opt/conda/lib/python3.7/site-packages/torch/lib/libtorch_hip.so(_ZN4c10d16ProcessGroupNCCL8WorkNCCL4waitENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE+0x254) [0x147dae806254]
12  /opt/conda/lib/python3.7/site-packages/torch/lib/libtorch_python.so(+0xa36330) [0x147ddca94330]
13  /opt/conda/lib/python3.7/site-packages/torch/lib/libtorch_python.so(+0x34cb48) [0x147ddc3aab48]
14  /opt/conda/bin/python(_PyMethodDef_RawFastCallKeywords+0x254) [0x55db8e0e47a4]
15  /opt/conda/bin/python(_PyObject_FastCallKeywords+0x130) [0x55db8e11a140]
16  /opt/conda/bin/python(+0x17fbd1) [0x55db8e11abd1]
17  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x4762) [0x55db8e162702]
18  /opt/conda/bin/python(+0x137b47) [0x55db8e0d2b47]
19  /opt/conda/bin/python(+0x17f9c5) [0x55db8e11a9c5]
20  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x4762) [0x55db8e162702]
21  /opt/conda/bin/python(_PyFunction_FastCallKeywords+0x187) [0x55db8e0d38d7]
22  /opt/conda/bin/python(+0x17f9c5) [0x55db8e11a9c5]
23  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x4762) [0x55db8e162702]
24  /opt/conda/bin/python(_PyObject_FastCallDict+0x1b6) [0x55db8e0b5436]
25  /opt/conda/bin/python(+0x1864bc) [0x55db8e1214bc]
26  /opt/conda/bin/python(PyObject_Call+0xb4) [0x55db8e0b5b94]
27  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x1cb8) [0x55db8e15fc58]
28  /opt/conda/bin/python(_PyFunction_FastCallKeywords+0x187) [0x55db8e0d38d7]
29  /opt/conda/bin/python(+0x17f9c5) [0x55db8e11a9c5]
30  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x661) [0x55db8e15e601]
31  /opt/conda/bin/python(_PyFunction_FastCallKeywords+0x187) [0x55db8e0d38d7]
32  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x3f5) [0x55db8e15e395]
33  /opt/conda/bin/python(_PyFunction_FastCallKeywords+0x187) [0x55db8e0d38d7]
34  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x3f5) [0x55db8e15e395]
35  /opt/conda/bin/python(_PyEval_EvalCodeWithName+0x255) [0x55db8e0b3e85]
36  /opt/conda/bin/python(+0x1d7d8e) [0x55db8e172d8e]
37  /opt/conda/bin/python(_PyMethodDef_RawFastCallKeywords+0xe9) [0x55db8e0e4639]
38  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x4428) [0x55db8e1623c8]
39  /opt/conda/bin/python(_PyEval_EvalCodeWithName+0x255) [0x55db8e0b3e85]
40  /opt/conda/bin/python(_PyFunction_FastCallKeywords+0x521) [0x55db8e0d3c71]
41  /opt/conda/bin/python(_PyEval_EvalFrameDefault+0x3f5) [0x55db8e15e395]
42  /opt/conda/bin/python(_PyEval_EvalCodeWithName+0x255) [0x55db8e0b3e85]
43  /opt/conda/bin/python(_PyFunction_FastCallDict+0x1e6) [0x55db8e0d2dc6]
44  /opt/conda/bin/python(+0x221b82) [0x55db8e1bcb82]
45  /opt/conda/bin/python(+0x232feb) [0x55db8e1cdfeb]
46  /opt/conda/bin/python(_Py_UnixMain+0x3c) [0x55db8e1ce18c]
47  /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf3) [0x147e20917083]
48  /opt/conda/bin/python(+0x1d803a) [0x55db8e17303a]
=================================
```
Is there a way this can be solved?

Thanks!