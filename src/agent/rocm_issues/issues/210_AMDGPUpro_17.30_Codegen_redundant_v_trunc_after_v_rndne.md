# AMDGPUpro 17.30 Codegen: redundant v_trunc after v_rndne ?

> **Issue #210**
> **状态**: closed
> **创建时间**: 2017-09-15T11:33:05Z
> **更新时间**: 2018-02-16T02:08:19Z
> **关闭时间**: 2018-02-16T02:08:19Z
> **作者**: preda
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/210

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

On Ubuntu 17.04, AMDGPU-pro 17.30, Vega64.

I see this sequence generated:
```
v_rndne_f64_e32 v[10:11], v[10:11]                   // 00000001041C: 7E14330A
v_trunc_f64_e32 v[10:11], v[10:11]                   // 000000010420: 7E142F0A
```
Corresponding to *rint(double)* in the context of:
```
long toLong(double x) { return rint(x); }
```

My understanding is that *rndne* (round-to-nearest-even) already produces an integral value. So why is the *trunc* needed afterwards?


---

## 评论 (12 条)

### 评论 #1 — gstoner (2017-09-24T13:25:55Z)

@preda We are looking at this.   

---

### 评论 #2 — gstoner (2017-10-19T13:49:40Z)

Please look at 17.40 beta build  http://support.amd.com/en-us/kb-articles/Pages/AMDGPU-Pro-Beta-Mining-Driver-for-Linux-Release-Notes.aspx

---

### 评论 #3 — preda (2017-10-26T08:28:17Z)

This is still present with ROCm 1.6-180, see e.g.
```
	v_rndne_f64_e32 v[10:11], v[10:11]                         // 0000000087F0: 7E14330A
	v_rndne_f64_e32 v[12:13], v[12:13]                         // 0000000087F4: 7E18330C
	v_trunc_f64_e32 v[10:11], v[10:11]                         // 0000000087F8: 7E142F0A
	v_trunc_f64_e32 v[12:13], v[12:13]                         // 0000000087FC: 7E182F0C
```

---

### 评论 #4 — preda (2017-10-30T08:41:15Z)

Well, not very hard to repro:

```
KERNEL(256) test(global double *in, global ulong *out) {
  uint p = get_global_id(0);
  out[p] = rint(in[p]);
}
```


---

### 评论 #5 — preda (2017-10-30T08:46:19Z)

And let me also hint to a possible cause:
there is a pre-packaged code block that does the conversion double -> long. That block starts with a v_trunc_f64.

The rint() already just did a v_rndne_f64, but the compiler fails to optimize away the v_trunc at the beginning of the pre-packaged conversion block.


---

### 评论 #6 — preda (2017-10-30T10:29:05Z)

I attach ISA for the example kernel above.
[foo.txt](https://github.com/RadeonOpenCompute/ROCm/files/1426806/foo.txt)


---

### 评论 #7 — Srinivasuluch (2017-10-30T10:47:13Z)

Thank you Mihai for the details.

---

### 评论 #8 — Srinivasuluch (2017-10-30T15:04:16Z)

Hi Mihai - The issue has been fixed with latest compiler changes, the fix would be available in next ROCm release.
Thank you for posting us the details for the bug.

---

### 评论 #9 — preda (2017-11-08T21:57:19Z)

Thanks. How can I try the fix out?

---

### 评论 #10 — gstoner (2017-11-09T04:48:42Z)

It will be  it ROCm 1.7,    One thing I talking to the the team about is have a binary train of  GA( Stable) , Beta( Dev-Stable), Alpha( Canary) via our repo server. 
 

---

### 评论 #11 — acmeman925 (2018-02-15T23:31:00Z)

Hi @preda could this issue be closed?

---

### 评论 #12 — preda (2018-02-16T02:08:19Z)

Yes, seems fixed in 1.7.

---
