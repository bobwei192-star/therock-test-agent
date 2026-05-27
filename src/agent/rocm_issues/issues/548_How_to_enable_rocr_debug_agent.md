# How to enable rocr_debug_agent?

> **Issue #548**
> **状态**: closed
> **创建时间**: 2018-09-18T13:42:25Z
> **更新时间**: 2018-09-28T20:43:00Z
> **关闭时间**: 2018-09-28T20:42:50Z
> **作者**: misos1
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/548

## 标签

- **Question** (颜色: #cc317c)

## 描述

I have vega 10 and rocm 1.9 installed but I do not see state for wavefronts that report memory violation as is stated in readme.md. I have mentioned library at /opt/rocm/lib/librocr_debug_agent64.so. I am getting only same message as with older versions of rocm:
```
Memory access fault by GPU node-1 (Agent handle: 0x1e6d670) on address 0xa1a591000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```


---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-09-18T16:42:11Z)

Hi @misos1 

We're currently going through the last few steps to release the source code for the rocr_debug_agent. The repo will also contain directions on how to use the tool. Sorry for the delay, and thanks for your interest. I'll send a note once things are available.

---

### 评论 #2 — t-tye (2018-09-20T18:47:14Z)

Hi @misos1 
We just updated the documentation at https://rocm-documentation.readthedocs.io/en/latest/ROCm_Tools/ROCm-Tools.html#rocr-debug-agent . We will be open sourcing the source files shortly.

---

### 评论 #3 — jlgreathouse (2018-09-28T20:42:50Z)

In addition, the source code for the ROCm 1.9.0 release of the `rocr_debug_agent` [is now available](https://github.com/ROCm-Developer-Tools/rocr_debug_agent/tree/roc-1.9.x).

As such, I believe this issue is solved. Sorry about the delay, but I hope you find the tool useful! If you run into any problems, please create tickets in the debug agent's repo and we will try to solve them.

---
