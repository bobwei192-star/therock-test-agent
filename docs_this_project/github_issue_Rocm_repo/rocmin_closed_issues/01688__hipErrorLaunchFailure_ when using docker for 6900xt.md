# 'hipErrorLaunchFailure' when using docker for 6900xt

- **Issue #:** 1688
- **State:** closed
- **Created:** 2022-02-20T16:34:46Z
- **Updated:** 2022-04-16T17:02:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/1688

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