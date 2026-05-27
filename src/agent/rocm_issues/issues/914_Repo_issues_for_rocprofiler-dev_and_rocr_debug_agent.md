# Repo issues for rocprofiler-dev and rocr_debug_agent

> **Issue #914**
> **状态**: closed
> **创建时间**: 2019-10-21T07:50:08Z
> **更新时间**: 2023-12-18T17:10:14Z
> **关闭时间**: 2023-12-18T17:10:14Z
> **作者**: VincentSC
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/914

## 描述

This is the output
```Get:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0 [217 kB]
Err:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0
  Hash Sum mismatch
Get:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocr_debug_agent amd64 1.0.0 [890 kB]
Err:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocr_debug_agent amd64 1.0.0
  Writing more data than expected (890180 > 890176)
Fetched 216 kB in 0s (2032 kB/s)         
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocprofiler-dev/rocprofiler-dev_1.0.0_amd64.deb  Hash Sum mismatch

E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocr_debug_agent/rocr_debug_agent_1.0.0_amd64.deb  Writing more data than expected (890180 > 890176)
```
The update of the deb-database is not done (correctly)?

---

## 评论 (4 条)

### 评论 #1 — zhang2amd (2019-12-06T00:14:52Z)

I tested the repo again. Didn't see this issue. The current release is 2.10. I also tried 2.9 release which was the latest in October and no issue too.
Did you clear apt cache before install? Are you behind a firewall or using proxy servers? These are possible reasons from your side to see this error.

---

### 评论 #2 — VincentSC (2020-03-04T11:13:59Z)

Missed your reply. Cache cleared, no proxy, all other repos work. I solved it by manually downloading rocprofiler-dev, removing rocprofiler-dev, manually installing rocprofiler-dev with dpkg -i, and then reinstalling "hipblas rocblas rocm-dev rocprofiler-dev rocrand".

Is the repo hosted on a server that has FAT or any other MS filesystem? It seems that the more data is sent than advertised. When I download the file on Windows, the file-size and size-on-disk are equal to what is printed. I think it would be solved by or updating the filesize to size-on-disk, or by not sending the trailing zeroes.

---

### 评论 #3 — nartmada (2023-12-12T23:17:51Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #4 — nartmada (2023-12-18T17:10:14Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
