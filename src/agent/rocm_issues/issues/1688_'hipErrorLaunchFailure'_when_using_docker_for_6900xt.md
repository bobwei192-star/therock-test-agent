# 'hipErrorLaunchFailure' when using docker for 6900xt

> **Issue #1688**
> **状态**: closed
> **创建时间**: 2022-02-20T16:34:46Z
> **更新时间**: 2022-04-16T17:02:25Z
> **关闭时间**: 2022-02-22T01:32:01Z
> **作者**: slbln
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1688

## 描述

Hello, I'm using ubuntu20.04 and 6900xt. I'm using the docker container 'rocm/pytorch:latest' and 'torch.cuda.is_available()' will return true. However, when I try to do any calculation with my gpu, it prints 'RuntimeError: Hip error: hipErrorLaunchFailure'. The following code falis: `import torch; x=torch.tensor([2.]); x.to(torch.device('cuda'))` And when I run the same code with 'HIP_LAUNCH_BOLACKING=1', the output will be like this:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/conda/lib/python3.8/site-packages/torch/_tensor.py", line 249, in __repr__
    return torch._tensor_str._str(self)
  File "/opt/conda/lib/python3.8/site-packages/torch/_tensor_str.py", line 415, in _str
    return _str_intern(self)
  File "/opt/conda/lib/python3.8/site-packages/torch/_tensor_str.py", line 390, in _str_intern
    tensor_str = _tensor_str(self, indent)
  File "/opt/conda/lib/python3.8/site-packages/torch/_tensor_str.py", line 251, in _tensor_str
    formatter = _Formatter(get_summarized_data(self) if summarize else self)
  File "/opt/conda/lib/python3.8/site-packages/torch/_tensor_str.py", line 90, in __init__
    nonzero_finite_vals = torch.masked_select(tensor_view, torch.isfinite(tensor_view) & tensor_view.ne(0))
```
I also try the docker for rocm4.5.2 and I get the same error. Thanks for your help.

---

## 评论 (3 条)

### 评论 #1 — jithunnair-amd (2022-02-21T22:04:19Z)

6900xt is a Navi21 card.

`rocm/pytorch:latest` uses the PT1.10 branch, which doesn't have support for Navi21 yet. You can try the `rocm/pytorch:rocm5.0_ubuntu18.04_py3.7_pytorch_staging` docker image for Navi21 support.

---

### 评论 #2 — slbln (2022-02-22T01:31:31Z)

@jithunnair-amd Thank you very much for your help, it solved my problem perfectly. I've spent days trying to figure this problem out. Thank you again. 

---

### 评论 #3 — march-o (2022-04-16T17:02:25Z)

@jithunnair-amd Maybe this is a redundant question, but how do I actually install this PyTorch into for example Conda? I have searched on how to do this but nothing helpful pops up. Could you maybe elaborate on this? I have a 6600XT so it probably won't work anyway because Navi 23 is not supported, at least that is what I read. Maybe any solutions for that? Thanks

---
