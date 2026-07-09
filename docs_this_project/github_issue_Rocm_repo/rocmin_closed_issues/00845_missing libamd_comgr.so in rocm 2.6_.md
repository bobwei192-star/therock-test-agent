# missing libamd_comgr.so in rocm 2.6?

- **Issue #:** 845
- **State:** closed
- **Created:** 2019-07-14T03:45:58Z
- **Updated:** 2019-07-14T03:58:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/845

Hello,

Just upgraded rocm 2.6 yesterday and tried running TVM using [this script](https://gist.github.com/masahi/460223846b142b7fc01897143eb732df) ([related discussions](https://discuss.tvm.ai/t/rocm-apps-benchmark-gpu-imagenet-py-failures-loading-kernel/3218/4))

It was fine with rocm 2.5 (or 2.4 maybe..), but now I hit following error:

```
  File "/usr/lib/python3.6/ctypes/__init__.py", line 348, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libamd_comgr.so: cannot open shared object file: No such file or directory
```

It appears `libamd_comgr.so` no longer exists in `/opt/rocm/lib` on my host.
With docker image, since the .so file is still there, the script can work (or error out as expected...)

What package should I install for that? Or I should just compile [RadeonOpenCompute/ROCm-CompilerSupport](https://github.com/RadeonOpenCompute/ROCm-CompilerSupport) for myself? (is it the right repo?)

BTW, I have gfx900 vega56 on my host.

Thanks!