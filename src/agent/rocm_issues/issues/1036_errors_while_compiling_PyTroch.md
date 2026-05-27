# errors while compiling PyTroch

> **Issue #1036**
> **状态**: closed
> **创建时间**: 2020-03-07T12:37:43Z
> **更新时间**: 2020-09-02T12:24:53Z
> **关闭时间**: 2020-09-02T12:24:53Z
> **作者**: Roalkege
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1036

## 描述

Hello I tried to compile ROCm/PyTorch for my RX580 but I get everytime this error and I dont know hat I have to do.
I use [this Doc ](https://rocm-documentation.readthedocs.io/en/latest/Deep_learning/Deep-learning.html#pytorch) to compile it.
![image](https://user-images.githubusercontent.com/44238399/76143531-72684700-6078-11ea-98af-2583cda06985.png)

I hope someone can help me. Or is there a precompiled image for my RX580?

---

## 评论 (3 条)

### 评论 #1 — MichaelEssich (2020-03-08T14:07:07Z)

Perhaps you have to apply this patch (not sure if it is already fixed in current version, but the last time I built PyTorch I had to apply it): https://github.com/pytorch/pytorch/commit/3a7ecd32eb7418e18146fe09dc9301076b5f0f17
If that's not the issues, maybe this guide can help: https://github.com/ROCmSoftwarePlatform/pytorch/issues/581

---

### 评论 #2 — Roalkege (2020-03-09T15:07:29Z)

[pytorch/pytorch@3a7ecd3](https://github.com/pytorch/pytorch/commit/3a7ecd32eb7418e18146fe09dc9301076b5f0f17) worked for me but now I tried to check if everything is working with `PYTORCH_TEST_WITH_ROCM=1 python test/run_test.py --verbose` but I get this.
After the the compile process the script also copied a lot of files.
I also replaced `python` with `python3`
![grafik](https://user-images.githubusercontent.com/44238399/76227573-cf523180-621f-11ea-922d-be9b5097b4b4.png)


---

### 评论 #3 — JavascriptAddict (2020-04-22T11:15:49Z)

Try using python3.6 instead of python3

---
