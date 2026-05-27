# rocprof human readable printout

> **Issue #1640**
> **状态**: open
> **创建时间**: 2021-12-15T01:04:42Z
> **更新时间**: 2024-08-13T20:42:55Z
> **作者**: ye-luo
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1640

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

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

---

## 评论 (7 条)

### 评论 #1 — JonChesterfield (2021-12-17T17:10:00Z)

`cat results.hsa_stats.csv | trace ',' '\t'` or similar might be a workaround for now. Outputting a percentage as  53.91378585000949 doesn't seem ideal though.

---

### 评论 #2 — ROCmSupport (2021-12-20T11:09:45Z)

Thanks @ye-luo for reaching us out.
I will pass this information to developer and will share update once I get it.
Thank you.

---

### 评论 #3 — ex-rzr (2021-12-20T12:34:17Z)

`column -t -s, results.hip_stats.csv` or even `column -t -s, -R 2,3,4 results.hip_stats.csv` can be used for better formatting, but I agree that human-readable output of rocprof would be great.

---

### 评论 #4 — nartmada (2024-01-27T04:27:41Z)

Hi @ye-luo, has your issue been addressed?  Do we still need to keep this ticket opened?  Thanks.

---

### 评论 #5 — ye-luo (2024-01-29T02:02:00Z)

Don’t make a joke. It is as bad as it was.

---

### 评论 #6 — nartmada (2024-01-29T04:42:04Z)

Sorry @ye-luo, it was not meant as a joke.  I am trying to sort out which issues have been fixed and which ones still need AMD's attention.  I will forward your concerns regarding readable printout to the rocprof team.  Thanks.

---

### 评论 #7 — harkgill-amd (2024-08-13T20:42:32Z)

Hi @ye-luo, wanted to provide a quick update on this issue. The rocprof team is aware of it and they have added it to their queue of features to implement. In the meantime, there are a few different options to make the csv output more readable such as the `column` command mentioned by @ex-rzr or third party tools like `csvkit`. 

The latter outputs the following
```
csvlook results.hsa_stats.csv
| Name                                      | Calls | TotalDurationNs |  AverageNs | Percentage |
| ----------------------------------------- | ----- | --------------- | ---------- | ---------- |
| hsa_queue_create                          |     1 |      12,849,342 | 12,849,342 |    40.420… |
| hsa_amd_memory_pool_free                  |     3 |       4,338,947 |  1,446,315 |    13.649… |
| hsa_amd_memory_lock_to_pool               |     3 |       2,776,793 |    925,597 |     8.735… |
| hsa_amd_agents_allow_access               |     6 |       2,759,904 |    459,984 |     8.682… |
| hsa_executable_load_agent_code_object     |     2 |       2,526,944 |  1,263,472 |     7.949… |
| hsa_amd_memory_pool_allocate              |     9 |       1,878,322 |    208,702 |     5.909… |
| hsa_amd_memory_async_copy_on_engine       |     3 |       1,504,926 |    501,642 |     4.734… |
| hsa_signal_wait_scacquire                 |     6 |       1,406,483 |    234,413 |     4.424… |
| hsa_executable_freeze                     |     2 |       1,203,226 |    601,613 |     3.785… |
| hsa_agent_get_info                        |   103 |         149,403 |      1,450 |     0.470… |
| hsa_signal_store_screlease                |     2 |          90,994 |     45,497 |     0.286… |
| hsa_signal_create                         |    72 |          83,309 |      1,157 |     0.262… |
| hsa_executable_iterate_symbols            |    15 |          69,871 |      4,658 |     0.220… |
| hsa_isa_get_info_alt                      |     4 |          59,300 |     14,825 |     0.187… |
| hsa_code_object_reader_create_from_memory |     2 |          32,541 |     16,270 |     0.102… |
| hsa_executable_symbol_get_info            |   229 |          12,600 |         55 |     0.040… |
| hsa_executable_create_alt                 |     2 |           9,105 |      4,552 |     0.029… |
| hsa_amd_agent_iterate_memory_pools        |     4 |           8,649 |      2,162 |     0.027… |
| hsa_iterate_agents                        |     1 |           8,321 |      8,321 |     0.026… |
| hsa_amd_pointer_info                      |    12 |           4,535 |        377 |     0.014… |
| hsa_executable_get_symbol_by_name         |    15 |           3,577 |        238 |     0.011… |
| hsa_signal_load_relaxed                   |    26 |           2,074 |         79 |     0.007… |
| hsa_amd_memory_unlock                     |     3 |           1,923 |        641 |     0.006… |
| hsa_amd_memory_pool_get_info              |    24 |           1,691 |         70 |     0.005… |
| hsa_amd_agent_memory_pool_get_info        |    16 |           1,561 |         97 |     0.005… |
| hsa_amd_memory_copy_engine_status         |     4 |           1,448 |        362 |     0.005… |
| hsa_signal_destroy                        |     2 |             834 |        417 |     0.003… |
| hsa_system_get_info                       |     7 |             666 |         95 |     0.002… |
| hsa_agent_iterate_isas                    |     2 |             625 |        312 |     0.002… |
| hsa_system_get_major_extension_table      |     1 |             433 |        433 |     0.001… |
| hsa_signal_silent_store_relaxed           |     4 |             395 |         98 |     0.001… |
| hsa_queue_add_write_index_screlease       |     2 |             306 |        153 |     0.001… |
| hsa_queue_load_read_index_scacquire       |     2 |             225 |        112 |     0.001… |
| hsa_queue_load_read_index_relaxed         |     2 |             201 |        100 |     0.001… |
| hsa_amd_profiling_set_profiler_enabled    |     1 |             127 |        127 |     0.000… |
| hsa_dispatch                              |     1 |               0 |          0 |     0.000… |
```

---
