# SYCL program fails to link with ROCm 3.3.0 + Ubuntu 20.04

> **Issue #1108**
> **状态**: closed
> **创建时间**: 2020-05-10T13:10:28Z
> **更新时间**: 2021-06-03T09:36:10Z
> **关闭时间**: 2021-06-03T09:36:10Z
> **作者**: c0d3st0rm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1108

## 描述

First of all, I understand that my setup is wholly unsupported by the ROCm stack (Ubuntu 20.04 + ROCm 3.3.0 including dkms + Intel's DPC++ LLVM compiler). I'm trying to run a sycl-based program using one of Intel's daily DPC++ releases (from https://github.com/intel/llvm/releases), and I can successfully run this application on both the host target (without OpenCL) and on the CPU (with OpenCL) using Intel's compute runtime. However, when it comes to executing it on a Vega 56, the program ends up failing to execute with

```
OpenCL API failed. OpenCL API returns: -17 (CL_LINK_PROGRAM_FAILURE) -17 (CL_LINK_PROGRAM_FAILURE)
```

How can I go about debugging this on the ROCm side of things? Is there a `DEBUG_ENABLE` sort of environment variable?

(the chosen device is a gfx900, so I'm pretty sure it's choosing the Vega as a target)

---

## 评论 (5 条)

### 评论 #1 — preda (2020-05-10T23:38:58Z)

You can try the debug environment variables described here:
https://github.com/RadeonOpenCompute/ROCm-CompilerSupport/tree/master/lib/comgr#debug-the-code-object-manager

---

### 评论 #2 — c0d3st0rm (2020-05-10T23:46:10Z)

```
<other output all succeeds>

amd_comgr_do_action:
	  ActionKind: AMD_COMGR_ACTION_LINK_RELOCATABLE_TO_EXECUTABLE
	     IsaName: amdgcn-amd-amdhsa--gfx900
	     Options: ""
	        Path: 
	    Language: AMD_COMGR_LANGUAGE_NONE
COMGR::InProcessDriver::Execute argv: lld "/tmp/comgr-3efff3/input/linked.bc.o" "-shared" "-o" "/tmp/comgr-3efff3/output/a.so"
	ReturnStatus: AMD_COMGR_STATUS_SUCCESS

<comgr output above, dpc++ output below>

OpenCL API failed. OpenCL API returns: -17 (CL_LINK_PROGRAM_FAILURE) -17 (CL_LINK_PROGRAM_FAILURE)
```

Looks like this might be a problem with dpc++ as all comgr calls succeed - could it be further down the pipeline, or is `a.so` the final output?

---

### 评论 #3 — c0d3st0rm (2020-05-11T18:21:02Z)

So given sycl works fine with other OpenCL runtimes, I'm not sure what is the issue. How would I go about debugging this further?

---

### 评论 #4 — ROCmSupport (2021-03-03T11:11:13Z)

Hi @c0d3st0rm 
Thanks for reaching out.
Request to try with the latest ROCm 4.0 and share an update asap.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-06-03T09:36:10Z)

I am closing this as there is no response for more than 2 months.
Feel free to open a new issue, if any.
Thank you.

---
