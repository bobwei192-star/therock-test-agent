# ROCm on a Steam Deck would be appreciated

> **Issue #1815**
> **状态**: closed
> **创建时间**: 2022-09-29T18:48:24Z
> **更新时间**: 2025-03-07T23:10:47Z
> **关闭时间**: 2024-04-21T16:12:52Z
> **作者**: peardox
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1815

## 描述

Got my Steam Deck todsay and the first thing I did with it was this

> Python 3.10.2 (main, Jan 15 2022, 19:56:27) [GCC 11.1.0] on linux
> Type "help", "copyright", "credits" or "license" for more information.
> >>> import torch
> >>> if torch.cuda.is_available() and torch.version.hip:
> ...     print('We have ROCm')
> ... else:
> ...     print('CPU Only')
> ...
> "hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
> Aborted (core dumped)
> (134)(deck@steamdeck ~)$

Are we going to get HIP / ROCm for the Steam Deck?

CC https://github.com/pytorch/pytorch/issues/85909



---

## 评论 (5 条)

### 评论 #1 — kyflores (2022-09-29T22:38:14Z)

The `HSA_OVERRIDE_GFX_VERSION=10.3.0` hack mentioned several times in issues here (see https://github.com/RadeonOpenCompute/ROCm/issues/1797) appears to work on the steam deck, at least to the point of creating tensors and `matmul` on gpu completing successfully. However mine locked up while trying to run the torch testsuite. Also, I was limited to the dedicated VRAM carved out for graphics, which is 1G on the steamdeck by default, and can be raised to 4G. 

Personally I'm interested in trying the various APUs for inference workloads too but from comments on other issues it seems unlikely that official support is coming anytime soon.

---

### 评论 #2 — saadrahim (2022-10-13T21:53:07Z)

This is not an issue. I am encouraging users to use https://github.com/RadeonOpenCompute/ROCm/discussions/1836 instead. Please migrate the discussion to the forums.

---

### 评论 #3 — Ma5onic (2024-01-16T12:37:58Z)

@kyflores, do you mind sharing how you were able to increase the VRAM to 4G (or point me towards the resources that you used to figure it out)?
Was it by changing the UMA frame buffer size?



---

### 评论 #4 — nartmada (2024-04-21T16:12:52Z)

Closing this ticket.  As saadrahim indicated, "This is not an issue. I am encouraging users to use https://github.com/ROCm/ROCm/discussions/1836 instead. Please migrate the discussion to the forums."

---

### 评论 #5 — deftdawg (2025-03-07T23:10:46Z)

> [@kyflores](https://github.com/kyflores), do you mind sharing how you were able to increase the VRAM to 4G (or point me towards the resources that you used to figure it out)? Was it by changing the UMA frame buffer size?

Allocation of RAM to VRAM can be set in the Steam Deck's BIOS before boot-up.

---
