# roctracer headers do not follow include rules

> **Issue #1830**
> **状态**: closed
> **创建时间**: 2022-10-11T15:32:56Z
> **更新时间**: 2024-02-19T12:20:00Z
> **关闭时间**: 2024-02-19T12:20:00Z
> **作者**: bertwesarg
> **标签**: Verified Issue, 5.3.0, 5.3.1, 5.2.0, 5.4.0, 5.3.2
> **URL**: https://github.com/ROCm/ROCm/issues/1830

## 标签

- **Verified Issue** (颜色: #0052cc)
- **5.3.0** (颜色: #fbca04)
- **5.3.1** (颜色: #4FE5CF)
- **5.2.0** (颜色: #6A0DD4)
- **5.4.0** (颜色: #224B70)
- **5.3.2** (颜色: #503B15)

## 负责人

- nunnikri
- frepaul
- raramakr

## 描述

Starting with [ROCm 5.2](https://docs.amd.com/bundle/ROCm-Release-Notes-v5.2/page/Deprecations_and_Warnings.html), the headers advertise to use `/opt/rocm-ver/include/` as the `-I`-flag and prefix the headers with the component `roctracer`. But the headers from roctracers are not usable this way:

An example when including `<roctracer/roctracer.h>:

```
/opt/rocm-5.2.3/include/roctracer/roctracer.h:45:10: error: 'ext/prof_protocol.h' file not found with <angled> include; use "quotes" instead
#include <ext/prof_protocol.h>  
         ^~~~~~~~~~~~~~~~~~~~~  
         "ext/prof_protocol.h"  
1 error generated.
```

Here is a script to check all headers:


```sh
find /opt/rocm-5.2.3/include/roctracer -maxdepth 1 -type f -printf '%f\n' |
    while read header
    do
        cat >includetest.cc <<EOF
#include <roctracer/$header>
EOF
        echo $header
        amdclang++ \
            -D__HIP_PLATFORM_AMD__ \
            -E includetest.cc \
            -o includetest.i \
            -I/opt/rocm-5.2.3/include 2>&1 | head -n 23
    done


---

## 评论 (3 条)

### 评论 #1 — bertwesarg (2022-11-21T09:32:20Z)

With ROCm 5.3.2 I'm down to an error in `<roctracer/roctracer_hsa.h>`:

```console
$ cat includetest.cc
#include <roctracer/roctracer_hsa.h>
$ amdclang++ -D__HIP_PLATFORM_AMD__ -E includetest.cc -o includetest.i -I/opt/rocm-5.3.2/include
In file included from includetest.cc:1:
/opt/rocm-5.3.2/include/roctracer/hsa_prof_str.h:1212:10: error: 'hsa_ostream_ops.h' file not found with <angled> include; use "quotes" instead
#include <hsa_ostream_ops.h>
         ^~~~~~~~~~~~~~~~~~~
         "hsa_ostream_ops.h"
1 error generated.
```

Will try 5.4 build 67 next.

---

### 评论 #2 — nunnikri (2022-11-22T00:21:31Z)

Thanks @bertwesarg  for the report. 
We had corrected all the #includes in the roctracer in ROCm 5.3 release. But looks like  hsa_prof_str.h is a generated file and got missed the changes.  We will get the changes asp to 5.4 new builds

---

### 评论 #3 — nartmada (2024-02-17T03:12:45Z)

Hi @bertwesarg, please close the ticket if the issue has been fixed.  Thank you.

---
