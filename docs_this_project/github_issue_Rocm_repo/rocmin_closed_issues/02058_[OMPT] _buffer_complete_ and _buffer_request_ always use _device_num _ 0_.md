# [OMPT] `buffer_complete` and `buffer_request` always use `device_num = 0`

- **Issue #:** 2058
- **State:** closed
- **Created:** 2023-04-17T12:00:47Z
- **Updated:** 2023-09-21T16:14:12Z
- **Assignees:** ronlieb
- **URL:** https://github.com/ROCm/ROCm/issues/2058

**Description:**

The OMPT interface offers a way to enable actual tracing on a target device by utilizing the device tracing interface. Similar to the callbacks, callback functions can be registered for a device. Then, the interface can request buffers for each device and trigger a callback when the buffer has finished. 
The device tracing interface itself works fine in ROCm 5.4.x with [some important functions (see #1747)](https://github.com/RadeonOpenCompute/ROCm/issues/1747) still missing, mostly affecting the timestamps. However, while testing, I noticed that the `device_num` seemed off for both `buffer_request` and `buffer_complete` when utilizing multiple GPUs. 

**What is the issue?:**
The class `OmptTracingBufferMgr` contains the method `dispatchCallback` where the `buffer_complete` callback is invoked. Here, the device number of zero is [hard coded](https://github.com/RadeonOpenCompute/llvm-project/blob/amd-stg-open/openmp/libomptarget/src/ompt_buffer_mgr.cpp#L343). 
```C
ompt_device_callbacks.ompt_callback_buffer_complete(
    0 /* TODO device num */, buffer,
    /* bytes returned in this callback */
    (char *)getNextTR(last_cursor) - (char *)first_cursor,
    (ompt_buffer_cursor_t)first_cursor, false /* buffer_owned */);
```

This is the same case for requesting a buffer. Here, the number zero is [hard coded](https://github.com/RadeonOpenCompute/llvm-project/blob/amd-stg-open/openmp/libomptarget/src/ompt_buffer_mgr.cpp#L76) as well:
```C
  // TODO Move the buffer allocation to a helper thread
  ompt_device_callbacks.ompt_callback_buffer_request(0 /* device_num */,
                                                     &buffer, &total_bytes);
```

This issue affects the evaluation of the device tracing interface buffers significantly. We might be able to reconstruct the actual device using the invoked callbacks, but this is not ideal. Our current approach would be to support only one device until this issue (and #2057) is fixed.