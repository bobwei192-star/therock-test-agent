# Will Vega 64/56 support be dropped like Instinct MI25?

> **Issue #1669**
> **状态**: closed
> **创建时间**: 2022-02-09T00:20:57Z
> **更新时间**: 2024-05-07T21:08:05Z
> **关闭时间**: 2024-05-07T21:08:04Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1669

## 描述

Hi,

I was just wondering if support for the Vega 56 and Vega 64 consumer GPUs will be dropped after ROCm 4.5 like with the Radeon Instinct MI25 server/workstation GPU. Both have the same GFX9 ISA, so I guess the vast majority of issues will affect both or neither.

Cheers,
Bengt

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2022-02-18T10:18:47Z)

Hi @Bengt 
Thanks for reaching out.
AFAIK, Vega10 is also under EOL, anyhow I will double check with my product and documentation team and update asap.
Thank you.

---

### 评论 #2 — martinschwinzerl (2022-04-03T12:41:38Z)

Are there any updates regarding this issue? I think there is a broader issue with respect to hardware support and (at least to me) the unclear situation which versions of the ROCm stack do support which hardware and/or features (i.e., only OpenCL or HIP / ML stacks, etc.), cf. #1714 .

Thanks in advance!

Cheers,
Martin

---

### 评论 #3 — DaveScream (2022-10-22T22:47:31Z)

No answer were given, sad

---

### 评论 #4 — ppanchad-amd (2024-05-07T21:08:04Z)

@Bengt Sorry for the lack of response. Vega64/56 is no longer supported.  Please check (https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html) for supported GPU's.  Thanks!

---
