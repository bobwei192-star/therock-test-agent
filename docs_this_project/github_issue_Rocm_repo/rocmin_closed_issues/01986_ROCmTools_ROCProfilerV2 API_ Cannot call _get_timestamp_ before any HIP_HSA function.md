# ROCmTools/ROCProfilerV2 API: Cannot call `get_timestamp` before any HIP/HSA function

- **Issue #:** 1986
- **State:** closed
- **Created:** 2023-03-23T07:37:07Z
- **Updated:** 2025-03-21T18:35:05Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/1986

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
