# Q: are these dmesg messages expected?

- **Issue #:** 343
- **State:** closed
- **Created:** 2018-02-21T04:14:13Z
- **Updated:** 2019-08-07T09:40:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/343

Ubuntu 17.10, ROCm 1.7, Vega64

When I run my OpenCL app, I see plenty of such entries appearing in dmesg. Are these normal/expected and nothing to worry about, or do they signal some problem?

```
[ 2258.451590] Evicting PASID 1 queues
[ 2258.459225] Restoring PASID 1 queues
[ 2261.663077] Evicting PASID 1 queues
[ 2261.671167] Restoring PASID 1 queues
[ 2270.003068] Evicting PASID 1 queues
[ 2270.011013] Restoring PASID 1 queues
[ 2273.263280] Evicting PASID 1 queues
[ 2273.271263] Restoring PASID 1 queues
[ 2276.529269] Evicting PASID 1 queues
[ 2276.535340] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[ 2276.535357] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[ 2276.535433] Restoring PASID 1 queues
[ 2279.792647] Evicting PASID 1 queues
[ 2279.799514] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[ 2279.799570] Restoring PASID 1 queues
[ 2283.091064] Evicting PASID 1 queues
[ 2283.099425] Restoring PASID 1 queues
```