# memory order in single thread

> **Issue #500**
> **状态**: closed
> **创建时间**: 2018-08-15T00:20:34Z
> **更新时间**: 2023-08-05T16:47:24Z
> **关闭时间**: 2023-08-05T16:47:23Z
> **作者**: preda
> **标签**: Under Investigation, Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/500

## 标签

- **Under Investigation** (颜色: #0052cc)
- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

```
KERNEL(1024) testA(global uint *bufN, global ulong *sumN) {
  if (get_global_id(0) == 0) {
    uint n = bufN[0];
    bufN[0] = 0;
    sumN[0] += n;
  }
}

KERNEL(1024) testB(global uint *bufN, global ulong *sumN) {
  if (get_global_id(0) == 0) {
    uint n = bufN[0];
    sumN[0] += n;
    bufN[0] = 0;
  }
}
```
ROCm 1.8.2, Vega64, Ubuntu 18.04, OpenCL 2.x.

Consider the two kernels above. The second one, testB(), works as expected. But the first one, testA(), behaves as if the value "n" is always zero. As if the write bufN[0]=0 takes place before the read n=bufN[0].


---

## 评论 (9 条)

### 评论 #1 — preda (2018-08-15T00:42:22Z)

In the "bad" case, such ISA is generated, where we see an s_load and global_store to the same location, not separated by any sync.

```
	v_mov_b32_e32 v0, s0                                       // 000000005A54: 7E000200
	v_mov_b32_e32 v2, s2                                       // 000000005A58: 7E040202
	v_mov_b32_e32 v1, s1                                       // 000000005A5C: 7E020201
	s_load_dword s4, s[0:1], 0x0                               // 000000005A60: C0020100 00000000
	v_mov_b32_e32 v3, s3                                       // 000000005A68: 7E060203
	global_store_dword v[0:1], v4, off
```


---

### 评论 #2 — b-sumner (2018-08-15T02:06:51Z)

We'll take a look.  Thanks for the report.

---

### 评论 #3 — preda (2019-01-04T00:13:21Z)

Is this fixed in ROCm 2.0?


---

### 评论 #4 — b-sumner (2019-02-08T21:48:45Z)

We do intend to fix this, but haven't yet.

---

### 评论 #5 — preda (2019-11-26T13:35:29Z)

Still open more than 1y later?

---

### 评论 #6 — b-sumner (2019-11-26T16:03:30Z)

Ugh.  This apparently fell through the cracks.  I'll try to get this back into focus.

---

### 评论 #7 — ROCmSupport (2021-02-10T04:45:30Z)

Hi @preda 
As this is logged long back, recommend you to try with the latest ROCm 4.0 and update us so that we will move it next level based on your updates.
Thank you.

---

### 评论 #8 — preda (2021-02-10T07:09:34Z)

I'm not planning to check repro of this bug on ROCm 4.0 myself. If you are confortable with potentially having this corecteness bug and don't care to look deeper to establish either way, that's fine from my side, you can ignore and close the issue.


---

### 评论 #9 — jlgreathouse (2023-08-05T16:47:23Z)

I just tested the provided reproducer on a ROCm 5.4.3 system running Vega 10, and it appears to produce correct code now. 

---
