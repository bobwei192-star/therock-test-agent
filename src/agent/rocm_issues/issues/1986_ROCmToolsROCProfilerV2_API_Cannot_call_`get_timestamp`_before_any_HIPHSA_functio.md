# ROCmTools/ROCProfilerV2 API: Cannot call `get_timestamp` before any HIP/HSA function

> **Issue #1986**
> **状态**: closed
> **创建时间**: 2023-03-23T07:37:07Z
> **更新时间**: 2025-03-21T18:35:05Z
> **关闭时间**: 2025-03-21T18:35:04Z
> **作者**: bertwesarg
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1986

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

In the new ROCm Tools API (5.5 RC4) I see the following error when calling `get_timestamp` before any HIP/HSA call:

```c++
/* setting up session */
rocprofiler_start_session(session_id);
rocprofiler_timestamp_t ts;
rocprofiler_get_timestamp(&ts);
```

Gives me this as output:
```
rocprofiler_get_timestamp(), Timestamps can't be collected
```

The value of the timestamp is `0`.

If I add a HIP/HSA call it works:

```c++
int devId;
hipGetDevice(&devId);
/* setting up session */
rocprofiler_start_session(session_id);
rocprofiler_timestamp_t ts;
rocprofiler_get_timestamp(&ts);
```


---

## 评论 (6 条)

### 评论 #1 — bertwesarg (2023-03-23T09:36:53Z)

probably the same issue I reported here:

https://github.com/ROCm-Developer-Tools/roctracer/issues/65

---

### 评论 #2 — nartmada (2024-02-16T17:00:53Z)

Hi @bertwesarg, thanks for the work-around in https://github.com/ROCm/roctracer/issues/65.  Please close this ticket if it is no longer needed.  Thanks.

---

### 评论 #3 — bertwesarg (2024-02-19T12:24:56Z)

but this workaround is not documented and it should actually be not needed. so I do not consider this solved but I haven't tested if anything has changed in the past

---

### 评论 #4 — nartmada (2024-03-17T14:24:54Z)

Thanks @bertwesarg.  I have asked the internal team to take a look.  

---

### 评论 #5 — schung-amd (2024-07-24T17:57:15Z)

Hi @bertwesarg, can you provide more of the code you used when encounting this issue? Specifically, I assume you are calling rocprofiler_create_session() to get session_id, but are you also calling rocprofiler_initialize()?

I can reproduce a similar issue (but not the exact issue) on ROCm 6.1.3 with the following code:
```
int main (int argc, char ** argv){

// Initialize the tools
// Without this step, the timestamp is not written
//   rocprofiler_initialize();

// Create the session with no replay mode
   rocprofiler_session_id_t session_id;
   rocprofiler_create_session(ROCPROFILER_NONE_REPLAY_MODE, &session_id);

// Start Session
   rocprofiler_start_session(session_id);

// try to get timestamp
    rocprofiler_timestamp_t ts;
    ts.value = 0;
    rocprofiler_get_timestamp(&ts);
    std::cout << ts.value << std::endl;

// Deactivating session
   rocprofiler_terminate_session(session_id);

// Destroy sessions
   rocprofiler_destroy_session(session_id);

// Destroy all profiling related objects
   rocprofiler_finalize();
  
}
```
and compiling with hipcc.

Without calling rocprofiler_initialize(), rocprofiler_get_timestamp() does not complain but also does not write a timestamp. This can be confirmed by running the generated executable multiple times in a row, which produces monotonically increasing results as expected with rocprofiler_initialize() and 0 always without calling it.

Digging into the internal code, I suspect the issue is that rocprofiler_get_timestamp() queries the HIP runtime which has not been initialized yet. As you observed, calling any HIP function will fix the issue as internally the HIP functions will initialize the runtime if it has not been initialized.

Can you test your code on an updated version of ROCm? Hopefully your issue has been resolved by recent versions. If not I will investigate further. Thanks!

---

### 评论 #6 — schung-amd (2025-03-21T18:35:04Z)

Closing due to lack of response. If you're still experiencing this on recent ROCm versions and have verified that you're calling rocprofiler_initialize(), feel free to comment and we can reopen this.

---
