# [Error on PyTorch] Memory access fault by GPU node-4. Reason: Page not present or supervisor privilege.

- **Issue #:** 1262
- **State:** closed
- **Created:** 2020-10-18T17:20:23Z
- **Updated:** 2020-10-30T09:53:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/1262

I am implementing a incomplete gamma function in PyTorch in CPU and CUDA, but I always have a problem with a test with ROCm in PyTorch's CI.
The log can be found [here](https://ci.pytorch.org/jenkins/job/pytorch-builds/job/pytorch-linux-bionic-rocm3.8-py3.6-test2/1723/console) (search for `test_igamma_common_cuda_float64`) with some of the log:

    21:18:17 test_igamma_common_cuda_float32 (__main__.TestTorchDeviceTypeCUDA) ... ok
    21:18:18 test_igamma_common_cuda_float64 (__main__.TestTorchDeviceTypeCUDA) ... Memory exception on virtual address 0x7f32775e8000, node id 4 : Page not present
    21:18:18 Address does not belong to a known buffer
    21:18:18 Memory access fault by GPU node-4 (Agent handle: 0x55d2eee23120) on address 0x7f32775e8000. Reason: Page not present or supervisor privilege.

My pull request can be seen [here](https://github.com/pytorch/pytorch/pull/46183) with the CUDA implementation of the function can be seen [here](https://github.com/pytorch/pytorch/pull/46183/files?file-filters%5B%5D=.cpp&file-filters%5B%5D=.cu&file-filters%5B%5D=.cuh&file-filters%5B%5D=.h&file-filters%5B%5D=.py&file-filters%5B%5D=.rst&file-filters%5B%5D=.yaml#diff-279bf1f9943ed149363f7e7a5e2710fd50c913ac70ea7f29d54a095777fbb571).

I'm not sure why the error happens. Strangely, it works well with `float32`.