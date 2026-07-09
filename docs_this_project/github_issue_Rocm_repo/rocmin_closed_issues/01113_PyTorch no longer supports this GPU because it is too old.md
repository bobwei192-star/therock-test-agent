# PyTorch no longer supports this GPU because it is too old.

- **Issue #:** 1113
- **State:** closed
- **Created:** 2020-05-20T00:56:43Z
- **Updated:** 2021-06-02T12:25:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/1113

Dear all
The environment is :
CPU : ryzen 1800x
GPU : RX570 or VEGA-56
ROCm : 3.3
Pytorch : 1.4
OS : unbuntu 18.04

Each time I run the code in Pytorch with GPU, it will show the following warning message:
/home/datakey/.local/lib/python3.7/site-packages/torch/cuda/__init__.py:87: UserWarning: 
    Found GPU0 Vega 10 XT [Radeon RX Vega 64] which is of cuda capability 3.0.
    PyTorch no longer supports this GPU because it is too old.
    The minimum cuda capability that we support is 3.5.

No matter which GPU that I used, RX570 or VEGA-56.

And the command :　
torch._C._cuda_getCompiledVersion()
Out[2]: 303

Is there any one encounter same situation as me ?
Will it affect the computing efficient of Pytorch with such situation?
Thanks


 