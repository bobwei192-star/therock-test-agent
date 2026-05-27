# ROCm Yum repository broken?

> **Issue #1178**
> **状态**: closed
> **创建时间**: 2020-07-10T07:17:32Z
> **更新时间**: 2020-12-16T12:09:16Z
> **关闭时间**: 2020-12-16T11:49:42Z
> **作者**: ekeever1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1178

## 描述

While attempting to update our ROCm installation, the update fails:

http://repo.radeon.com/rocm/yum/rpm/repodata/9a30f17a8ed8185a8b4308d64592e7fe40dd63943b4f4ef226ea63111f0639f3-filelists.sqlite.bz2: [Errno 14] HTTP Error 404 - Not Found
Trying other mirror.
To address this issue please refer to the below wiki article 
...     [generic output clipped]     ...
failure: repodata/9a30f17a8ed8185a8b4308d64592e7fe40dd63943b4f4ef226ea63111f0639f3-filelists.sqlite.bz2 from ROCm: [Errno 256] No more mirrors to try.
http://repo.radeon.com/rocm/yum/rpm/repodata/9a30f17a8ed8185a8b4308d64592e7fe40dd63943b4f4ef226ea63111f0639f3-filelists.sqlite.bz2: [Errno 14] HTTP Error 404 - Not Found

The error is not incorrect, as the actual filelists.sqlite.bz2 found on the repo URL http://repo.radeon.com/rocm/yum/rpm/repodata/ is
http://repo.radeon.com/rocm/yum/rpm/repodata/7428e729dfdff834c37a2c39f3e2f78d05105015dbb5307972b1c751864277e5-filelists.sqlite.bz2

Was the repomd.xml not updated perhaps?

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2020-12-16T11:49:42Z)

Thanks @ekeever1 for reaching us.
Issue is fixed and no more seen now. Recommend to try with the latest ROCm 3.10 packages.
Thank you.

---
