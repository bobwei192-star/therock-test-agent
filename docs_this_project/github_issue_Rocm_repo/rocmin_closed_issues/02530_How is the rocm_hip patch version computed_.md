# How is the rocm/hip patch version computed?

- **Issue #:** 2530
- **State:** closed
- **Created:** 2023-10-06T14:37:28Z
- **Updated:** 2024-04-07T21:45:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/2530

By hip version, I mean 5.4.6, 5.5.2, 5.6.0, 5.6.1 etc.  In `/opt/rocm-5.6.0/include/hip/hip_version.h`, I see

```
      #define HIP_VERSION_MAJOR 5
      #define HIP_VERSION_MINOR 6
      #define HIP_VERSION_PATCH 31061
      #define HIP_VERSION    (HIP_VERSION_MAJOR * 10000000 + HIP_VERSION_MINOR * 100000 + HIP_VERSION_PATCH)
```

But how is the `HIP_VERSION_PATCH` mapped to the `z` in `rocm-x.y.z`?

