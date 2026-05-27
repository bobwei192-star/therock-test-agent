# Incomplete implementation of OMPT runtime entry points (ROCm 5.1)

> **Issue #1747**
> **状态**: closed
> **创建时间**: 2022-06-02T10:05:09Z
> **更新时间**: 2023-12-22T19:46:35Z
> **关闭时间**: 2023-12-22T19:46:35Z
> **作者**: wrwilliams
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1747

## 描述

In my work on OMPT target support, I've found a number of runtime entry points that are not yet implemented (and correctly return `NULL` when queried). This issue is to help prioritize the ongoing implementation effort.

**High importance for tools**

`translate_time`
`get_device_time`

At least one of these two entry points is necessary in order to map trace record timestamps into any other time stream in a portable way. `translate_time` has the advantage of compatibility with host-side queries of the OpenMP runtime but `wtime_t` is a less useful format than a `uint64_t` nanosecond-resolution timestamp.

**Not sure of importance, but surprised by the omission**

`get_device_num_procs`

This seems like low-hanging fruit. I don't think I need it in the near term though.

`pause_trace`

Isn't stop just a pause/flush?

**Important for clean code that we don't have to fix later**

`get_record_type`

Presently only OMPT type records are supported, not native records, which is fine. We should still be able to write tool code that checks the record type rather than blindly assuming OMPT formats via `static_cast`.

**Not important to us right now**

`get_record_native`
`get_record_abstract`
`set_trace_native`

Only supporting the OMPT format is fine for now.

---

## 评论 (3 条)

### 评论 #1 — Thyre (2023-04-17T12:54:36Z)

As of aomp 17.0-x, the following functions seem to be implemented

**High importance for tools**
- [x] `translate_time`
- [x] `get_device_time`

**Not sure of importance, but surprised by the omission**
- [ ] `get_device_num_procs`
- [ ] `pause_trace`

**Important for clean code that we don't have to fix later**
- [x] `get_record_type`
---

I haven't tested the last three ones as I'm focusing on the standard record type.

As aomp can be quite ahead of ROCm, not all of those functions are available in ROCm 5.4.x yet (I think only `get_record_type`?). However, it is nice to see that there is progress and we can continue implementing OMPT in our tools. 

I guess `pause_trace` and `get_device_num_procs` are the most interesting of the missing functions. `pause_trace` would be useful for us as long as `stop_trace` is (somewhat) broken. `get_device_num_procs` could be used to present the user a bit more information, but is not that important. 

---

### 评论 #2 — nartmada (2023-12-19T04:19:03Z)

Hi @wrwilliams, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.


---

### 评论 #3 — nartmada (2023-12-22T19:46:35Z)

Closing the issue for now.  @wrwilliams, if you still see the issue with ROCm 6.0.0, please re-open the ticket.  Thanks.

---
