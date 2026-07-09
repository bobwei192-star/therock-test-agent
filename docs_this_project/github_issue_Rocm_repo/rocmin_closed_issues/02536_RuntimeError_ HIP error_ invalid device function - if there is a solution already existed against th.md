# RuntimeError: HIP error: invalid device function - if there is a solution already existed against this issue.

- **Issue #:** 2536
- **State:** closed
- **Created:** 2023-10-10T15:15:29Z
- **Updated:** 2025-11-26T23:13:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/2536

Server： (Inspur NF5280A6) + (2 x Milan7453) + (16Dimm * 32GB-3200) 
GPU：    83:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] (rev c1)
OS：      Centos Steam9.2， kernel：5.14.0-373.el9.x86_64
ROCm：5.7
Pytorch installation cmd：pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.7

[root@6700xt ~]# dkms status
amdgpu/6.2.4-1652687.el9, 5.14.0-373.el9.x86_64, x86_64: installed (original_module exists)
[root@6700xt ~]#

_ipython interaction_
```
In [1]: import torch

In [2]: torch.__version__
Out[2]: '2.2.0.dev20231010+rocm5.7'

In [3]: torch.cuda.is_available()
Out[3]: True

In [4]: torch.cuda.device_count()
Out[4]: 1

In [5]: torch.cuda.current_device()
Out[5]: 0

In [6]: torch.cuda.get_device_name(torch.cuda.current_device())
Out[6]: 'AMD Radeon RX 6700 XT'

In [7]: device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

In [8]: device
Out[8]: device(type='cuda')

In [9]: torch.rand(3, 3).to(device)
Out[9]: ---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
File /usr/local/lib/python3.9/site-packages/IPython/core/formatters.py:708, in PlainTextFormatter.__call__(self, obj)
    701 stream = StringIO()
    702 printer = pretty.RepresentationPrinter(stream, self.verbose,
    703     self.max_width, self.newline,
    704     max_seq_length=self.max_seq_length,
    705     singleton_pprinters=self.singleton_printers,
    706     type_pprinters=self.type_printers,
    707     deferred_pprinters=self.deferred_printers)
--> 708 printer.pretty(obj)
    709 printer.flush()
    710 return stream.getvalue()

File /usr/local/lib/python3.9/site-packages/IPython/lib/pretty.py:410, in RepresentationPrinter.pretty(self, obj)
    407                         return meth(obj, self, cycle)
    408                 if cls is not object \
    409                         and callable(cls.__dict__.get('__repr__')):
--> 410                     return _repr_pprint(obj, self, cycle)
    412     return _default_pprint(obj, self, cycle)
    413 finally:

File /usr/local/lib/python3.9/site-packages/IPython/lib/pretty.py:778, in _repr_pprint(obj, p, cycle)
    776 """A pprint that just redirects to the normal repr function."""
    777 # Find newlines and replace them with p.break_()
--> 778 output = repr(obj)
    779 lines = output.splitlines()
    780 with p.group():

File /usr/local/lib64/python3.9/site-packages/torch/_tensor.py:442, in Tensor.__repr__(self, tensor_contents)
    438     return handle_torch_function(
    439         Tensor.__repr__, (self,), self, tensor_contents=tensor_contents
    440     )
    441 # All strings are unicode in Python 3.
--> 442 return torch._tensor_str._str(self, tensor_contents=tensor_contents)

File /usr/local/lib64/python3.9/site-packages/torch/_tensor_str.py:664, in _str(self, tensor_contents)
    662 with torch.no_grad(), torch.utils._python_dispatch._disable_current_modes():
    663     guard = torch._C._DisableFuncTorch()
--> 664     return _str_intern(self, tensor_contents=tensor_contents)

File /usr/local/lib64/python3.9/site-packages/torch/_tensor_str.py:595, in _str_intern(inp, tensor_contents)
    593                     tensor_str = _tensor_str(self.to_dense(), indent)
    594                 else:
--> 595                     tensor_str = _tensor_str(self, indent)
    597 if self.layout != torch.strided:
    598     suffixes.append("layout=" + str(self.layout))

File /usr/local/lib64/python3.9/site-packages/torch/_tensor_str.py:347, in _tensor_str(self, indent)
    343     return _tensor_str_with_formatter(
    344         self, indent, summarize, real_formatter, imag_formatter
    345     )
    346 else:
--> 347     formatter = _Formatter(get_summarized_data(self) if summarize else self)
    348     return _tensor_str_with_formatter(self, indent, summarize, formatter)

File /usr/local/lib64/python3.9/site-packages/torch/_tensor_str.py:138, in _Formatter.__init__(self, tensor)
    134         self.max_width = max(self.max_width, len(value_str))
    136 else:
    137     nonzero_finite_vals = torch.masked_select(
--> 138         tensor_view, torch.isfinite(tensor_view) & tensor_view.ne(0)
    139     )
    141     if nonzero_finite_vals.numel() == 0:
    142         # no valid number, do nothing
    143         return

**RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing HIP_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.**


In [10]:
```