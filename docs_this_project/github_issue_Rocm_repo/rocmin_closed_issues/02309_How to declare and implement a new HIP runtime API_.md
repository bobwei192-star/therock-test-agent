# How to declare and implement a new HIP runtime API?

- **Issue #:** 2309
- **State:** closed
- **Created:** 2023-06-30T09:05:52Z
- **Updated:** 2023-07-01T03:55:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/2309

Suppose I want to declare and implement a new HIP runtime API related to HIP stream named `hipStreamXXX`. I declare it in [hip_runtime_api.h](https://github.com/ROCm-Developer-Tools/HIP/blob/develop/include/hip/hip_runtime_api.h) and implement it in [hip_stream.cpp](https://github.com/ROCm-Developer-Tools/hipamd/blob/develop/src/hip_stream.cpp) like this:

```cpp
hipError_t hipStreamXXX(hipStream_t stream) {
  HIP_INIT_API(hipStreamXXX, stream);
  std::printf("This is a newly added HIP runtime API\n");
  HIP_RETURN(hipSuccess);
}
```

The compiler reports errors from the `HIP_INIT_API` macro, saying that `HIP_CB_SPAWNER_OBJECT` needs a `operation_id` for this runtime API.
After inspecting the [`CMakeLists.txt`](https://github.com/ROCm-Developer-Tools/hipamd/blob/develop/src/CMakeLists.txt#L233-L236), I know that the include header is generated from a Python script [`hip_prof_gen.py`](https://github.com/ROCm-Developer-Tools/hipamd/blob/develop/src/hip_prof_gen.py), but I can't figure out how the `operation_id` is defined. Is there any file I missed to define and implement a newly added HIP runtime API?