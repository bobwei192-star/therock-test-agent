# Unable to complete pytorch tests using recommended installation guide.

- **Issue #:** 1395
- **State:** closed
- **Created:** 2021-02-28T21:57:44Z
- **Updated:** 2021-03-01T06:01:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/1395

Hello, I'm trying to set up an environment for training some models using pytorch using my AMD GPU. 

OS: ubuntu 20.04
gpu: rx 570
cpu / mobo: MSI B450 + Ryzen 5 1600

I'm simply attempting to set up using the official guide. I'm able to install ROCm itself to see the device in clinfo, however, I next try to follow: https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#recommended-install-using-published-pytorch-rocm-docker-image

I get the the step of running the pytorch tests: 
`PYTORCH_TEST_WITH_ROCM=1 python3.6 test/run_test.py –-verbose`

This runs for a long while before getting to a few similar errors like the following:

```
ERROR: test_context_manager_test (test_jit_cuda_fuser.TestPassManagerCudaFuser)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/root/.local/lib/python3.6/site-packages/torch/testing/_internal/common_utils.py", line 815, in wrapper
    method(*args, **kwargs)
  File "/var/lib/jenkins/pytorch/test/test_jit_cuda_fuser.py", line 518, in test_context_manager_test
    t_jit(x, y)
  File "/root/.local/lib/python3.6/site-packages/torch/testing/_internal/common_utils.py", line 118, in prof_func_call
    return prof_callable(func_call, *args, **kwargs)
  File "/root/.local/lib/python3.6/site-packages/torch/testing/_internal/common_utils.py", line 115, in prof_callable
    return callable(*args, **kwargs)
RuntimeError: Running the CUDA fuser requires a CUDA build.

----------------------------------------------------------------------
Ran 18 tests in 1.112s

FAILED (errors=11, skipped=6)
Traceback (most recent call last):
  File "test/run_test.py", line 718, in <module>
    main()
  File "test/run_test.py", line 707, in main
    raise RuntimeError(err)
RuntimeError: test_jit_cuda_fuser_legacy failed!

```

I've not been able to find any more information about this error. Can anyone provide some pointers so I could start to look into solving it?