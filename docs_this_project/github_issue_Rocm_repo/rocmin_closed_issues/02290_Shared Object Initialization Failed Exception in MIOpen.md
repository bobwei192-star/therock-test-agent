# Shared Object Initialization Failed Exception in MIOpen

- **Issue #:** 2290
- **State:** closed
- **Created:** 2023-06-28T22:03:32Z
- **Updated:** 2024-04-22T13:53:32Z
- **Labels:** Verified Issue, 5.6.0
- **URL:** https://github.com/ROCm/ROCm/issues/2290

MIOpen throws a shared object initialization failed exception in MI250x products due to a known HIP issue,

```
Memory leak when code object files are loaded/unloaded via hipModuleLoad/hipModuleUnload APIs

```

Therefore, online exhaustive tuning via the MIOpen environment variable is discouraged. Users are encouraged to use the default setting, report any tuning requirements, or process online tuning in smaller batches. This issue will be fixed in a future release.