# rocm-validation-suite3.8.0 ./conf/deviceid.sh doesn't work. Wrong paths.

> **Issue #1233**
> **状态**: closed
> **创建时间**: 2020-09-22T21:44:03Z
> **更新时间**: 2024-01-19T20:15:10Z
> **关闭时间**: 2024-01-19T20:15:10Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1233

## 描述

rocm-validation-suite3.8.0 3.4.30800

```
root@debian:/opt/rocm-3.8.0/rvs# ./conf/deviceid.sh 
./conf/deviceid.sh: line 99: /opt/rocm/rvs/rvs: No such file or directory
```

Providing `ROCM_PATH` environment variable doesn't help.

`RVS_EXE_PATH=/opt/rocm-3.8.0/rvs/rvs` appears to resolve the issue, but the script does nothing.

My suggestion:

1) Use proper paths by default.
2) Respect `ROCM_PATH`
3) Terminate script early (with error message and how to fix it) if the provided or computed `RVS_EXE_PATH` doesn't point to executable file that exists.


---

## 评论 (7 条)

### 评论 #1 — pramenku (2020-10-30T19:53:48Z)

Can you please try with latest release 3.9.

---

### 评论 #2 — baryluk (2020-11-02T06:33:07Z)

> Can you please try with latest release 3.9.

Same issue with `rocm-validation-suite3.9.0`

---

### 评论 #3 — rkothako (2020-11-04T08:43:44Z)

Thanks @baryluk 
This issue is known to us and we are working on the fix.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-02-15T08:39:01Z)

Hi @baryluk 
Issue is fixed and changes are pushed.
Request you to verify with ROCm 4.1 or 4.2.
Thank you.

---

### 评论 #5 — baryluk (2021-02-16T09:19:19Z)

I will test when, 4.1 or 4.2 is out, packaged and available for testing.

---

### 评论 #6 — rkothako (2021-06-23T07:21:49Z)

Hi @baryluk 
Hope the issue is resolved.
Please confirm.


---

### 评论 #7 — nartmada (2024-01-19T20:15:10Z)

Closing the ticket as no response @baryluk.  Please re-open the ticket if issue still exists with latest ROCm6.0.0.  Thanks.

---
