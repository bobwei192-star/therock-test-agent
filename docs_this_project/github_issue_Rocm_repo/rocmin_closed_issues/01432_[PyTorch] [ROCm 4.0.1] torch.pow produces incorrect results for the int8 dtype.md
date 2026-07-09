# [PyTorch] [ROCm 4.0.1] torch.pow produces incorrect results for the int8 dtype

- **Issue #:** 1432
- **State:** closed
- **Created:** 2021-03-29T15:46:21Z
- **Updated:** 2021-04-09T06:05:04Z
- **Assignees:** ROCmSupport
- **URL:** https://github.com/ROCm/ROCm/issues/1432

Hello,

PyTorch with ROCm 4.0.1 produces incorrect results for `torch.pow` for the `int8` dtype on MI25 or MI50.
This issue does not manifest with CUDA.

In [PyTorch PR 50999](https://github.com/pytorch/pytorch/pull/50999), [`test_int_and_float_pow_cuda`](https://github.com/pytorch/pytorch/blob/17bce70b569fa348e0b9d34c63c12c29a629d6f9/test/test_binary_ufuncs.py#L660-695) compares the results of `torch.pow` with `numpy.power`. For a 3-D tensor of shape `(5, 5, 5)` with dtype `torch.int8`, with elements in the range -2 to 2, the comparison fails with ROCm, when the exponent is (a scalar) 5.

Initially, I assumed the bug was related to overflow, so I changed the range of the elements in the tensor, but the comparison with `numpy.power` fails even if there's no overflow (elements in range -2 to 2, and the exponent is 5).
The corresponding Jenkins failure logs are [here](https://ci.pytorch.org/jenkins/job/pytorch-builds/job/pytorch-linux-bionic-rocm4.0.1-py3.6-test2/7404/console).

Please help fix this issue.
Thank you!

cc: @JeffDaily








