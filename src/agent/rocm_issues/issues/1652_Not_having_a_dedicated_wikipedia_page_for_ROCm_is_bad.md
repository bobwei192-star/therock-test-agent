# Not having a dedicated wikipedia page for ROCm is bad

> **Issue #1652**
> **状态**: closed
> **创建时间**: 2021-12-30T18:45:38Z
> **更新时间**: 2023-02-24T22:00:24Z
> **关闭时间**: 2023-02-24T22:00:23Z
> **作者**: Maxzor
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1652

## 描述

https://en.wikipedia.org/wiki/GPUOpen#Radeon_Open_Compute_(ROCm)
NVidia Cuda and Intel OneAPI have their obviously.

P.S. There is an overall blatant lack of entry & medium level documentation about the stack, about what each component does, and how the components interact with one another. Specifically talking about the device driver, the system runtime and low-level libraries, such as the roct-thunk, the rocr-runtime, hipamd and hipcc compiler, the common language runtime...

I don't understand how an AMD executive in charge of the ROCm stack cannot realize that throwing a few hundred k$ towards good documentation is an urgent matter in the race for GPU APIs.

At least there is no wall-of-text. I mean, come on. https://i.imgur.com/Mel05t9.png

---

## 评论 (5 条)

### 评论 #1 — Maxzor (2022-01-17T22:22:06Z)

This is not my job, so I made a skeleton and turned it into a game: fix the inaccuracies and mistakes, inspired by [Cunningham's Law](https://meta.wikimedia.org/wiki/Cunningham%27s_Law) :smile: .

https://en.wikipedia.org/wiki/Rocm

---

### 评论 #2 — ROCmSupport (2022-01-28T11:42:32Z)

Thanks @Maxzor for making this point.
We have much documentation defined at different places but can not comment on wiki part.
Let me talk to my management/ business unit team and get some update asap.
Thank you.

---

### 评论 #3 — keryell (2022-04-05T19:01:09Z)

@Maxzor thank you for doing this.
The problem with Wikipedia is that AMD cannot contribute massively to this page without creating a conflict of interest. https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest
So external contributors are welcome. :-)


---

### 评论 #4 — keryell (2022-04-14T18:34:24Z)

@Maxzor so I guess this can be closed?

---

### 评论 #5 — kentrussell (2023-02-24T22:00:23Z)

Closing thanks to the great work of the open-source community. https://en.wikipedia.org/wiki/ROCm is still being updated.

---
