# [PyTorch] [ROCm 4.0.1] torch.pow produces incorrect results for the int8 dtype

> **Issue #1432**
> **状态**: closed
> **创建时间**: 2021-03-29T15:46:21Z
> **更新时间**: 2021-04-09T06:05:04Z
> **关闭时间**: 2021-04-09T06:05:04Z
> **作者**: imaginary-person
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1432

## 负责人

- ROCmSupport

## 描述

Hello,

PyTorch with ROCm 4.0.1 produces incorrect results for `torch.pow` for the `int8` dtype on MI25 or MI50.
This issue does not manifest with CUDA.

In [PyTorch PR 50999](https://github.com/pytorch/pytorch/pull/50999), [`test_int_and_float_pow_cuda`](https://github.com/pytorch/pytorch/blob/17bce70b569fa348e0b9d34c63c12c29a629d6f9/test/test_binary_ufuncs.py#L660-695) compares the results of `torch.pow` with `numpy.power`. For a 3-D tensor of shape `(5, 5, 5)` with dtype `torch.int8`, with elements in the range -2 to 2, the comparison fails with ROCm, when the exponent is (a scalar) 5.

Initially, I assumed the bug was related to overflow, so I changed the range of the elements in the tensor, but the comparison with `numpy.power` fails even if there's no overflow (elements in range -2 to 2, and the exponent is 5).
The corresponding Jenkins failure logs are [here](https://ci.pytorch.org/jenkins/job/pytorch-builds/job/pytorch-linux-bionic-rocm4.0.1-py3.6-test2/7404/console).

Please help fix this issue.
Thank you!

cc: @JeffDaily










---

## 评论 (12 条)

### 评论 #1 — ROCmSupport (2021-03-30T05:49:10Z)

Thanks @imaginary-person for reaching out.
Can you please share the exact steps(step by step procedure) to reproduce the problem, so that we will understand better and works on the issue.
Thank you.


---

### 评论 #2 — imaginary-person (2021-03-30T06:12:30Z)

Hello @ROCmSupport, can you please test [this function](https://github.com/pytorch/pytorch/blob/17bce70b569fa348e0b9d34c63c12c29a629d6f9/test/test_binary_ufuncs.py#L660-695) with your local ROCm PyTorch build with an Nvidia Tesla microarchitecture GPU? Please replace `test/test_binary_ufuncs.py` on your system with the one in the given link.

You can run this test with the command `python test_binary_ufuncs.py -v TestBinaryUfuncsCUDA.test_int_and_float_pow_cuda`.

`torch.pow(tensor_name, 5)` on a tensor of shape `(5, 5, 5)` of `int8` dtype would produce incorrect results for some elements.
For example, -31 instead of -32, so this test would fail. Please investigate as to why it produces an incorrect result.

Please let me know if you've any further questions. Thank you!

---

### 评论 #3 — ROCmSupport (2021-03-30T06:32:17Z)

Hi @imaginary-person 
I do not have NVidia GPU with me and ROCm is based on AMD GPUs.
Your point might be irrelevant here then.
Thank you

---

### 评论 #4 — imaginary-person (2021-03-30T06:44:54Z)

Hello @jeffdaily, is it possible for you to have this issue tested on an Nvidia Tesla microarchitecture GPU, since CircleCI only has Nvidia Tesla T4 GPUs? @ROCmSupport doesn't have access to one. Thank you!

---

### 评论 #5 — jeffdaily (2021-03-30T23:13:34Z)

Does torch.pow produce incorrect results for ROCm hardware, or just the Tesla T4 GPU?

---

### 评论 #6 — imaginary-person (2021-03-30T23:59:56Z)

> Does torch.pow produce incorrect results for ROCm hardware, or just the Tesla T4 GPU?

@jeffdaily, can you please confirm if you know whether the PyTorch CircleCI tests for ROCm run on AMD hardware?
Based on what I can see on CircleCI's website, it only seems to have Nvidia Tesla T4 GPUs.
So I assumed that that the test only fails on ROCm for Tesla T4 GPUs.
I don't have access to ROCm hardware, so I don't know if ROCm hardware produces correct results.

---

### 评论 #7 — jeffdaily (2021-03-31T00:01:05Z)

PyTorch CI for ROCm runs on MI25 or MI50.  It uses Jenkins CI, not CircleCI.  The test failure is from our Jenkins CI logs; so the failure you're seeing is for AMD GPUs.

---

### 评论 #8 — imaginary-person (2021-03-31T00:07:29Z)

Thanks for the info! That makes sense. I had been wondering why ROCm builds weren't tested on ROCm hardware,
as I had wrongly assumed that PyTorch Jenkins was also hosted by CircleCI.

So, I guess, debugging would be a breeze for @ROCmSupport now.

---

### 评论 #9 — imaginary-person (2021-03-31T16:28:10Z)

> I do not have NVidia GPU with me and ROCm is based on AMD GPUs.
> Your point might be irrelevant here then

@ROCmSupport, please use an AMD GPU to debug.
BTW, ROCm is supposed to be an open standard & does support Nvidia GPUs, but that's irrelevant now, as I was mistaken about what GPU the test failed on.

---

### 评论 #10 — jaglinux (2021-04-09T01:00:02Z)

@imaginary-person on ROCm 4.1 , I re-enabled the test and the output is pasted below.  There is a runtime warning.
Pytorch CI is moved to ROCm4.1 for AMD GPU's.  If the results are good, then you may want to submit PR with the tests enabled.

/home/pytorch-1/test# python test_binary_ufuncs.py -v TestBinaryUfuncsCUDA.test_int_and_float_pow_cuda
test_int_and_float_pow_cuda (__main__.TestBinaryUfuncsCUDA) ... test_binary_ufuncs.py:621: RuntimeWarning: invalid value encountered in power
  np_res = np.power(to_np(base), to_np(np_exponent))
ok

----------------------------------------------------------------------
Ran 1 test in 2.908s

OK



---

### 评论 #11 — imaginary-person (2021-04-09T01:05:56Z)

@jaglinux, thank you for the update!
IIRC, the warning is intended, so from your update, it seems that the issue has been fixed on ROCm 4.1.

---

### 评论 #12 — ROCmSupport (2021-04-09T05:33:34Z)

Thanks @imaginary-person for the update.
Am closing this now as the issue is fixed with 4.1.
Thank you.

---
