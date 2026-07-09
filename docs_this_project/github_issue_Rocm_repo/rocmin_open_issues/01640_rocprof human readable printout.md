# rocprof human readable printout

- **Issue #:** 1640
- **State:** open
- **Created:** 2021-12-15T01:04:42Z
- **Updated:** 2024-08-13T20:42:55Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/1640

I drive rocprof mostly via command line with "--stats". A csv file is friendly to excel but not really to human who just want to take a quick look by `cat`. So could you provide an option to output human readable tables?

The ugly look now
```
$ cat results.hsa_stats.csv
"Name","Calls","TotalDurationNs","AverageNs","Percentage"
hsa_signal_wait_scacquire,1220,177633790,145601,53.91378585000949
hsa_amd_memory_lock_to_pool,36,41889377,1163593,12.713881187629408
hsa_amd_memory_lock,803,41304882,51438,12.536480602637097
hsa_amd_memory_unlock,838,23449281,27982,7.1171116383357935
hsa_queue_create,2,13847256,6923628,4.202792692731822
hsa_system_get_info,10612,7117219,670,2.1601533188793565
hsa_signal_create,875,6695317,7651,2.0321014765035863
hsa_amd_memory_pool_allocate,114,5350743,46936,1.6240086542117764
hsa_signal_store_relaxed,834,2302478,2760,0.69882709712132
hsa_amd_signal_async_handler,803,1409572,1755,0.4278204217123869
hsa_amd_memory_async_copy,803,1404153,1748,0.4261756963168346
hsa_signal_store_screlease,1606,1153983,718,0.35024638238339395
hsa_queue_destroy,1,942742,942742,0.2861324430436892
hsa_amd_memory_pool_free,108,700081,6482,0.21248219222063827
hsa_amd_agents_allow_access,11,615481,55952,0.186805172758796
hsa_amd_profiling_get_async_copy_time,803,486070,605,0.14752752777562259
```