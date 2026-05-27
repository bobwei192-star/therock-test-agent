# MIOpen(HIP): Warning [SQLiteBase] Unable to read system database file:/opt/rocm/miopen/share/miopen/db/gfx906_60.kdb Performance may degrade terminate called after throwing an instance of 'boost::filesystem::filesystem_error'

> **Issue #1677**
> **状态**: closed
> **创建时间**: 2022-02-15T05:53:50Z
> **更新时间**: 2024-01-20T01:54:03Z
> **关闭时间**: 2024-01-20T01:54:02Z
> **作者**: Griffintaur
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1677

## 描述

Full error message when I am trying to train a deep learning model.
```
MIOpen(HIP): Warning [SQLiteBase] Unable to read system database file:/opt/rocm/miopen/share/miopen/db/gfx906_60.kdb Performance may degrade
terminate called after throwing an instance of 'boost::filesystem::filesystem_error'`  
what():  boost::filesystem::permissions: No such file or directory: "/home/ssml/singh/.config/miopen//gfx906_60.HIP.2_11_0_993628deb.ufdb.txt"
```

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2022-02-21T08:21:16Z)

Hi @Griffintaur 
Thanks for reaching us.
Can you please share the exact steps to reproduce the problem locally.
And also request to share few details like GPU, OS, outputs of /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo.
Thank you.

---

### 评论 #2 — ROCmSupport (2022-05-09T05:15:41Z)

I am going to close it as there is no update on this ticket for the last 4 months.
Request user to file new issues, if any, for quick resolutions.
Thank you.

---

### 评论 #3 — nartmada (2024-01-20T01:54:02Z)

Closing this ticket as there is no update.  @Griffintaur, please file a new ticket for any issues you have encountered.  Thanks.

---
