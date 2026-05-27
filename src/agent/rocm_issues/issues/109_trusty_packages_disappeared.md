# trusty packages disappeared

> **Issue #109**
> **状态**: closed
> **创建时间**: 2017-05-02T08:35:34Z
> **更新时间**: 2017-05-04T07:00:12Z
> **关闭时间**: 2017-05-04T06:53:18Z
> **作者**: psteinb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/109

## 描述

Hi - 
I just noticed that the trusty packages disappeared. 

```
$ sudo aptitude update
#...
Ign http://packages.amd.com trusty/main Translation-en_US
Ign http://packages.amd.com trusty/main Translation-en
Err http://packages.amd.com trusty/main amd64 Packages
  404  Not Found
Fetched 72 B in 3s (22 B/s)  
W: Failed to fetch http://packages.amd.com/rocm/apt/debian/dists/trusty/main/binary-amd64/Packages: 404  Not Found
E: Some index files failed to download. They have been ignored, or old ones used instead.
E: Couldn't rebuild package cache
```
and indeed, I can see only xenial binaries (tagged 1.5 !!) on the server mentioned above. will trusty not be supported anymore for 1.5 and upwards?

---

## 评论 (4 条)

### 评论 #1 — jedwards-AMD (2017-05-02T14:15:32Z)

The trusty code will not be provided for 1.5. I am working to update the repository with the 1.4 binaries in *.gz format.

---

### 评论 #2 — psteinb (2017-05-02T14:26:50Z)

in other words, if I want to use 1.5, it's xenial then.



---

### 评论 #3 — jedwards-AMD (2017-05-02T16:29:27Z)

I have uploaded the ROCm 1.4 archives to the following location: http://packages.amd.com/rocm/archive/

The 1.5.0 release is also include.

---

### 评论 #4 — psteinb (2017-05-04T06:53:18Z)

ok, I ended up updating to xenial. rocm 1.5 is there and I am gradually cleaning the system from rocm 1.4

---
