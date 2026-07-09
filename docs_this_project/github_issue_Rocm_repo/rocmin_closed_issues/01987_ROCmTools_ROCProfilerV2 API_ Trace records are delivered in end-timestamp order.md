# ROCmTools/ROCProfilerV2 API: Trace records are delivered in end-timestamp order

- **Issue #:** 1987
- **State:** closed
- **Created:** 2023-03-23T07:57:53Z
- **Updated:** 2024-08-12T19:52:00Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/1987

In the new ROCmTools/ROCProfilerV2 API (5.5 RC4) tracing records delivered via `rocprofiler_set_api_trace_sync_callback` are ordered by end-timestamp.

To simplify the output, I changed the `tracer/sample.cpp` from the `rocmprofv2-examples.zip` to something like this:

```c++
  int devId;
  hipGetDevice(&devId);

  // Activating Profiling Session to profile whatever kernel launches occurs up
  // till the next terminate session
  CHECK_ROCPROFILER(rocprofiler_start_session(session_id));

  hipDeviceProp_t devProp;
  HIP_CALL(hipGetDeviceProperties(&devProp, 0));
  HIP_CALL(hipMalloc((void **)&gpuMem, 1 * sizeof(int)));
  HIP_CALL(hipFree(gpuMem));

  // Deactivating session
  CHECK_ROCPROFILER(rocprofiler_terminate_session(session_id));
```

Output (`ROCTX ID` column dropped for clarity):

```
Record [1], Domain(HIP_API_DOMAIN), Begin(3021867580544991), End(3021867580615985), Correlation ID( 1), Function(hipGetDeviceProperties)
Record [3], Domain(HSA_API_DOMAIN), Begin(3021867580684354), End(3021867580849535), Correlation ID( 3), Function(hsa_amd_memory_pool_allocate)
Record [5], Domain(HIP_API_DOMAIN), Begin(3021867580675527), End(3021867580884592), Correlation ID( 2), Function(hipMalloc)
Record [7], Domain(HSA_API_DOMAIN), Begin(3021867580903968), End(3021867580909689), Correlation ID( 5), Function(hsa_amd_memory_pool_free)
Record [9], Domain(HIP_API_DOMAIN), Begin(3021867580892917), End(3021867580922513), Correlation ID( 4), Function(hipFree)
```

Duplicating the lines into individual begin and end lines and sort by timestamp, the (expected) order is as follows:

```
Record [1], Domain(HIP_API_DOMAIN), Begin(3021867580544991), Correlation ID( 1), Function(hipGetDeviceProperties)
Record [1], Domain(HIP_API_DOMAIN),   End(3021867580615985), Correlation ID( 1), Function(hipGetDeviceProperties)
Record [5], Domain(HIP_API_DOMAIN), Begin(3021867580675527), Correlation ID( 2), Function(hipMalloc)
Record [3], Domain(HSA_API_DOMAIN), Begin(3021867580684354), Correlation ID( 3), Function(hsa_amd_memory_pool_allocate)
Record [3], Domain(HSA_API_DOMAIN),   End(3021867580849535), Correlation ID( 3), Function(hsa_amd_memory_pool_allocate)
Record [5], Domain(HIP_API_DOMAIN),   End(3021867580884592), Correlation ID( 2), Function(hipMalloc)
Record [9], Domain(HIP_API_DOMAIN), Begin(3021867580892917), Correlation ID( 4), Function(hipFree)
Record [7], Domain(HSA_API_DOMAIN), Begin(3021867580903968), Correlation ID( 5), Function(hsa_amd_memory_pool_free)
Record [7], Domain(HSA_API_DOMAIN),   End(3021867580909689), Correlation ID( 5), Function(hsa_amd_memory_pool_free)
Record [9], Domain(HIP_API_DOMAIN),   End(3021867580922513), Correlation ID( 4), Function(hipFree)
```

`rocsight` shows the same behaviour. Putting the above HIP calls into a separate file and call `rocsight` on it:

```c++
#include <hip/hip_runtime_api.h>

int main()
{
    int devId;
    hipGetDevice(&devId);

    hipDeviceProp_t devProp;
    hipGetDeviceProperties(&devProp, 0);

    int *gpuMem;
    hipMalloc((void **)&gpuMem, 1 * sizeof(int));

    hipFree(gpuMem);

    return 0;    
}
```

```console
$ rocsight --sys-trace ./simple-hip
:
Record [149], Domain(HIP_API_DOMAIN), Begin(3022291145523111), End(3022291145538961), Correlation ID( 75), ROCTX ID(7312272752230166381), Function(hipGetDevice)
Record [151], Domain(HIP_API_DOMAIN), Begin(3022291145549180), End(3022291145572915), Correlation ID( 76), ROCTX ID(54), Function(hipGetDeviceProperties)
Record [153], Domain(HSA_API_DOMAIN), Begin(3022291145587813), End(3022291145636704), Correlation ID( 78), ROCTX ID(210453397508), Function(hsa_amd_memory_pool_allocate)
Record [155], Domain(HIP_API_DOMAIN), Begin(3022291145585228), End(3022291145648987), Correlation ID( 77), ROCTX ID(140580888654980), Function(hipMalloc)
Record [157], Domain(HSA_API_DOMAIN), Begin(3022291145660569), End(3022291145663094), Correlation ID( 80), ROCTX ID(140576863289344), Function(hsa_amd_memory_pool_free)
Record [159], Domain(HIP_API_DOMAIN), Begin(3022291145653776), End(3022291145669987), Correlation ID( 79), ROCTX ID(140580888654980), Function(hipFree)
```

Please note, that the `Correlation ID` corresponds to the expected order.

I was not able to find anything in the API or examples that it is possible to get a callback for begin and end individually. That was the case in roctracer, where the `hip_api_data_t` struct denoted with its `.phase` member which kind of event it was (`ACTIVITY_API_PHASE_ENTER` and `ACTIVITY_API_PHASE_EXIT`).

This renders the new ROCmTools/ROCProfilerV2 API broken when integrating it into performance tools like Score-P. All know and common tools interfaces deliver individual events for enter/begin and exit/end. This includes MPI, OMPT, OpenACC profiling interface, NVIDIA CUPTI, and also the (now) deprecated roctracer.